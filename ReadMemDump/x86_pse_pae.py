from x86_pse_nopae import *

# Check pte function
def check_pt_func_pse_pae(pde, pte, memsize, byte_per_entry):
    if (bitAt(pte, 0) == 0): return 0
    if (bitAt(pte, 6) == 1):
        if (bitAt(pte, 5) == 0): return -1
    if (bitAt(pte, 2) == 1):
        if (bitAt(pde, 2) == 0): return -1
    MAXPHYADDR = math.ceil(math.log(memsize, 2))
    if (bitFromTo(pte, MAXPHYADDR, 62) != 0): return -1
    return 1

# Check pde function
def check_pd_func_pse_pae(pde, memsize):
    if (bitAt(pde, 0) == 0): return 0
    if (bitAt(pde, 7) == 1):
        if(bitFromTo(pde, 13, 20) != 0): return -1
    MAXPHYADDR = math.ceil(math.log(memsize, 2))
    if (bitFromTo(pde, MAXPHYADDR, 62) != 0): return -1
    return 1

# List page directory with 2 process name
def list_pd_pse_pae(pname1, pname2, mem_size, mem):
    page_indexs_1 = find4KBPageIndex(pname1, mem)
    page_indexs_2 = find4KBPageIndex(pname2, mem)
    page_indexs_1_2MB = find2MBPageIndex(pname1, mem)
    page_indexs_2_2MB = find2MBPageIndex(pname2, mem)
    
    cr3_list = []
    w_cr3 = []

    for i0 in range(0, mem_size, 4096):
        if (i0 > mem_size - 1024): break
        
        # print log to console
        if ( i0 > 0x100000 and (i0 & 0x000fffff) == 0):
            print(hex(i0))
        
        w = scanPageDirectory(i0, check_pd_func_pse_pae, check_pt_func_pse_pae, mem, i0, page_indexs_1, page_indexs_2, mem_size, page_indexs_1_2MB, page_indexs_2_2MB, 8)
        if(w > 0):
            cr3_list.append(i0)
            w_cr3.append(w)

    return cr3_list, w_cr3    

# Check pde function
def check_pdpt_func_pse_pae(pdpte, memsize):
    if (bitAt(pdpte, 0) == 0): return 0
    MAXPHYADDR = math.ceil(math.log(memsize, 2))
    if (bitFromTo(pdpte, 1, 2) != 0 or bitFromTo(pdpte, 5, 8) != 0 or bitFromTo(pdpte, MAXPHYADDR, 63) != 0):
        return -1
    return 1

# List Page-Directory-Pointer-Table with 2 process name
def list_pdpt_pse_pae(pname1, pname2, mem_size, mem):
    pdpt_list = []
    w_list = []
    pd_list, a = list_pd_pse_pae(pname1, pname2, mem_size, mem)
    for i0 in range(0, mem_size, 32):
        count = 0
        for i1 in range(4):
            pdpte = getEntry(i0 + i1 * 8, mem, i0, i1, 0, 8)
            
            check_pdpte = check_pdpt_func_pse_pae(pdpte, mem_size)
            if (check_pdpte == -1):
                count = 0
                break
            if (check_pdpte == 0): continue

            pd_addr = getAddrFromEntry(pdpte, 4096, mem_size, 8)
            if (pd_addr in pd_list): count += 1
        if (count > 0):
            pdpt_list.append(i0)
            w_list.append(count)

    return pdpt_list, w_list, pd_list
