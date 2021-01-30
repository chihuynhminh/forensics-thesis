from x86_nopse_nopae import *
import math

# Check pde function
def check_pd_func_pse_nopae(pde, memsize):
    if (bitAt(pde, 0) == 0): return 0
    if (bitAt(pde, 7) == 1):
        MAXPHYADDR = math.ceil(math.log(memsize, 2))
        if(MAXPHYADDR <= 32):
            if(bitFromTo(pde, 13, 21) != 0): return -1
        else:
            M = min(40, MAXPHYADDR)
            if(bitFromTo(pde, M - 19, 21) != 0): return -1
    return 1

# List page directory with 2 process name
def list_pd_pse_nopae(pname1, pname2, mem_size, mem, file_mem_path):
    page_indexs_1 = find4KBPageIndex(pname1, mem)
    page_indexs_2 = find4KBPageIndex(pname2, mem)
    page_indexs_1_4MB = find4MBPageIndex(pname1, mem)
    page_indexs_2_4MB = find4MBPageIndex(pname2, mem)
    
    cr3_list = []
    w_cr3 = []

    for i0 in range(0, mem_size, 4096):
        if (i0 > mem_size - 1024): break
        
        # print log to console
        if ( i0 > 0x100000 and (i0 & 0x000fffff) == 0):
            print(hex(i0))
        
        w = scanPageDirectory(i0, check_pd_func_pse_nopae, check_pt_func_nopse_nopae, mem, i0, page_indexs_1, page_indexs_2, mem_size, page_indexs_1_4MB, page_indexs_2_4MB)
        if(w > 0):
            cr3_list.append(i0)
            w_cr3.append(w)

    return cr3_list, w_cr3    
    
    

