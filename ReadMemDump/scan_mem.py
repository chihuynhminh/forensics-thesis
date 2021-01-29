from log_func import *

i0=0
i1=0
i2=0

# Get bit at specific location
def bitAt(a, i):
    return (a >> i) & 1

# Get bit from i_from to i_to (i_from < i_to)
def bitFromTo(a, i_from, i_to):
    return (a >> i_from) & (pow(2, i_to - i_from + 1) - 1)

# Get entry of paging table at an specific address (4 b)
def getEntry(addr, b, i0, i1, i2):
    _4b = b[addr : addr + 4]
    if (len(_4b) != 4):
        print_err(hex(addr) + ' ' + str(i0) + ' ' + str(i1) + ' ' + str(i2) + '\n')
        return 0
  
    # little endian
    pde = _4b[3] << 24
    pde = pde | (_4b[2] << 16)
    pde = pde | (_4b[1] << 8)
    pde = pde | (_4b[0])
    return pde

# Find all 4KB page contain process name
def find4KBPageIndex(pname, b):
    page_indexs = []

    process_name = bytes(pname, 'ascii') + b'\x00'
    string_index = [b.find(process_name)]

    while (string_index[-1] != -1):
        if(len(page_indexs) == 0 or page_indexs[-1] != (string_index[-1] & 0xfffff000)):
            page_indexs.append(string_index[-1] & 0xfffff000)
        string_index.append(b.find(process_name, string_index[-1] + 1))    # get last element of array: array_name[-1]

    return page_indexs

#scan page table with pt_con_func is function check condition
def scanPageTable(pde, pt_addr, pt_con_func, b, i0, i1, page_indexs_1, page_indexs_2):
    w = 0
    for i2 in range(1024):
        pte_addr = pt_addr + 4*i2
        pte = getEntry(pte_addr, b, i0, i1, i2)
        
        check_pte = pt_con_func(pde, pte)
        if (check_pte == 0): continue
        if (check_pte == -1): return -1
        
        page_addr = pte & 0xfffff000
        if (page_addr in page_indexs_1 or page_addr in page_indexs_2):
            w += 1
    return w

#scan page directory with pd_con_func is function check condition
def scanPageDirectory(pd_addr, pd_con_func, pt_con_func, b, i0, page_indexs_1, page_indexs_2, mem_size, page_indexs_1_4MB = [], page_indexs_2_4MB = []):
    w = 0
    for i1 in range(1024):
        pde_addr = pd_addr + i1 * 4
        pde = getEntry(pde_addr, b, i0, i1, 0)

        check_pde = pd_con_func(pde, mem_size)
        if (check_pde == 0): continue
        if (check_pde == -1): return -1

        if (bitAt(pde, 7) == 1):
            page_addr = pde &0xffc00000
            if (page_addr in page_indexs_1_4MB or page_addr in page_indexs_2_4MB):
                w += 1
        else:
            pt_addr = pde & 0xfffff000
            if (pt_addr > mem_size - 1024): continue
            w_pte = scanPageTable(pde, pt_addr, pt_con_func, b, i0, i1, page_indexs_1, page_indexs_2)
            if (w_pte == -1): return -1
            w += w_pte

    return w

# Find all 4MB page contain process name
def find4MBPageIndex(pname, b):
    page_indexs = []

    process_name = bytes(pname, 'ascii') + b'\x00'
    string_index = [b.find(process_name)]

    while (string_index[-1] != -1):
        if(len(page_indexs) == 0 or page_indexs[-1] != (string_index[-1] & 0xffc00000)):
            page_indexs.append(string_index[-1] & 0xffc00000)
        string_index.append(b.find(process_name, string_index[-1] + 1))    # get last element of array: array_name[-1]

    return page_indexs

