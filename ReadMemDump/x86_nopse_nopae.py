from scan_mem import *

cr3_list = []
w_cr3 = []

# Check pte function
def check_pt_func_nopse_nopae(pde, pte):
    if (bitAt(pte, 0) == 0): return 0
    if (bitAt(pte, 6) == 1):
        if (bitAt(pte, 5) == 0): return -1
    if (bitAt(pte, 2) == 1):
        if (bitAt(pde, 2) == 0): return -1
    return 1

# Check pde function
def check_pd_func_nopse_nopae(pde):
    if (bitAt(pde, 0) == 0): return 0
    if (bitAt(pde, 7) == 1): return -1
    return 1

# Scan memdump with 2 process name
def scan_pd_nopse_nopae(pname1, pname2):
    global mem_size, b, file_mem_path, mem_size
    page_indexs_1 = find4KBPageIndex(pname1, b)
    page_indexs_2 = find4KBPageIndex(pname2, b)
    
    for i0 in range(0, mem_size, 4096):
        if (i0 > mem_size - 1024): break
        
        # print log to console
        if ( i0 > 0x100000 and (i0 & 0x000fffff) == 0):
            print(hex(i0))
        
        w = scanPageDirectory(i0, check_pd_func_nopse_nopae, check_pt_func_nopse_nopae, i0, page_indexs_1, page_indexs_2, mem_size)
        if(w > 0):
            cr3_list.append(i0)
            w_cr3.append(w)
    
    f = open(file_mem_path + '/' + pname1.replace('/', '') + '_' + pname2.replace('/', '') + '.txt', 'w')
    for i in range(len(cr3_list)):
        f.write(hex(cr3_list[i]) + ' ' + hex(w_cr3[i]) + '\n')
    f.close()
    
    cr3_list.clear()
    w_cr3.clear()


