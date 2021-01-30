from scan_mem import *

# Check pte function
def check_pt_func_nopse_nopae(pde, pte):
    if (bitAt(pte, 0) == 0): return 0
    if (bitAt(pte, 6) == 1):
        if (bitAt(pte, 5) == 0): return -1
    if (bitAt(pte, 2) == 1):
        if (bitAt(pde, 2) == 0): return -1
    return 1

# Check pde function
def check_pd_func_nopse_nopae(pde, memsize):
    if (bitAt(pde, 0) == 0): return 0
    if (bitAt(pde, 7) == 1): return -1
    return 1

# List page directory with 2 process name
def list_pd_nopse_nopae(pname1, pname2, mem_size, mem, file_mem_path):
    page_indexs_1 = find4KBPageIndex(pname1, mem)
    page_indexs_2 = find4KBPageIndex(pname2, mem)
    
    cr3_list = []
    w_cr3 = []

    for i0 in range(0, mem_size, 4096):
        if (i0 > mem_size - 1024): break
        
        # print log to console
        if ( i0 > 0x100000 and (i0 & 0x000fffff) == 0):
            print(hex(i0))
        
        w = scanPageDirectory(i0, check_pd_func_nopse_nopae, check_pt_func_nopse_nopae, mem, i0, page_indexs_1, page_indexs_2, mem_size)
        if(w > 0):
            cr3_list.append(i0)
            w_cr3.append(w)
    
    return cr3_list, w_cr3

