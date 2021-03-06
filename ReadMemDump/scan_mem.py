from log_func import *
import math

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
def getEntry(addr, mem, i0, i1, i2, num_of_bytes):
    _nbyte = mem[addr : addr + num_of_bytes]
    if (len(_nbyte) != num_of_bytes):
        print_err(hex(addr) + ' ' + str(i0) + ' ' + str(i1) + ' ' + str(i2) + '\n')
        return 0
    
    # little endian
    entry = 0
    for i in range(num_of_bytes):
        entry = entry | (_nbyte[i] << (8*i))
    return entry

# Get address of next page from an entry
def getAddrFromEntry(entry, page_size, mem_size, num_of_bytes):
    bits_need_present_addr = math.ceil(math.log(mem_size, 2))
    mask = pow(2,bits_need_present_addr) - 1
    zero_bits_end = math.ceil(math.log(page_size, 2))
    mask = ((mask >> zero_bits_end) << zero_bits_end)
    return entry & mask

# Find all 4KB page contain process name
def find4KBPageIndex(pname, mem):
    page_indexs = []

    process_name = bytes(pname, 'ascii') + b'\x00'
    string_index = [mem.find(process_name)]

    while (string_index[-1] != -1):
        if(len(page_indexs) == 0 or page_indexs[-1] != (string_index[-1] & 0xfffffffffffff000)):
            page_indexs.append(string_index[-1] & 0xfffffffffffff000)
        string_index.append(mem.find(process_name, string_index[-1] + 1))    # get last element of array: array_name[-1]

    return page_indexs

# Find all 4MB page contain process name
def find4MBPageIndex(pname, mem):
    page_indexs = []

    process_name = bytes(pname, 'ascii') + b'\x00'
    string_index = [mem.find(process_name)]

    while (string_index[-1] != -1):
        if(len(page_indexs) == 0 or page_indexs[-1] != (string_index[-1] & 0xffffffffffc00000)):
            page_indexs.append(string_index[-1] & 0xffffffffffc00000)
        string_index.append(mem.find(process_name, string_index[-1] + 1))    # get last element of array: array_name[-1]

    return page_indexs

# Find all 2MB page contain process name
def find2MBPageIndex(pname, mem):
    page_indexs = []

    process_name = bytes(pname, 'ascii') + b'\x00'
    string_index = [mem.find(process_name)]

    while (string_index[-1] != -1):
        if(len(page_indexs) == 0 or page_indexs[-1] != (string_index[-1] & 0xffffffffffe00000)):
            page_indexs.append(string_index[-1] & 0xffffffffffe00000)
        string_index.append(mem.find(process_name, string_index[-1] + 1))    # get last element of array: array_name[-1]

    return page_indexs

# Scan page table with pt_con_func is function check condition
def scanPageTable(pde, pt_addr, pt_con_func, mem, i0, i1, page_indexs_1, page_indexs_2, byte_per_entry):
    w = 0
    for i2 in range(0, 4096, byte_per_entry):
        pte_addr = pt_addr + i2
        pte = getEntry(pte_addr, mem, i0, i1, i2, byte_per_entry)
        
        check_pte = pt_con_func(pde, pte, len(mem), byte_per_entry)
        if (check_pte == 0): continue
        if (check_pte == -1):
          print_err(hex(pde) + '-' + hex(pte) + ' ' + hex(pte_addr) + ' ' + str(i0) + ' ' + str(i1) + ' ' + str(i2) + '\n')
          return -1
        
        page_addr = getAddrFromEntry(pte, 4096, len(mem), byte_per_entry)
        if (page_addr in page_indexs_1 or page_addr in page_indexs_2):
            w += 1
    return w

# Check is a page directory also a page table 
def check_loop_pd(pd_addr, mem, i0, byte_per_entry):
    for i1 in range(0, 4096, byte_per_entry):
        pde_addr = pd_addr + i1
        pde = getEntry(pde_addr, mem, i0, i1, 0, byte_per_entry)
        pt_addr = getAddrFromEntry(pde, 4096, len(mem), byte_per_entry)
        if (pd_addr == pt_addr): return True
    return False

# Scan page directory with pd_con_func is function check condition
def scanPageDirectory(pd_addr, pd_con_func, pt_con_func, mem, i0, page_indexs_1, page_indexs_2, mem_size, page_indexs_3 = [], page_indexs_4 = [], byte_per_entry = 4):
    w = 0
    isLoop = check_loop_pd(pd_addr, mem, i0, byte_per_entry)

    for i1 in range(0, 4096, byte_per_entry):
        pde_addr = pd_addr + i1
        pde = getEntry(pde_addr, mem, i0, i1, 0, byte_per_entry)

        check_pde = pd_con_func(pde, mem_size)
        if (check_pde == 0): continue
        if (check_pde == -1):
            #if(isLoop):
            #    continue
            #else:
            #    print_err(hex(pde_addr) + ' ' + str(i0) + ' ' + str(i1) + ' ' + '01' + '\n')
            #    return -1
            return -1

        if (bitAt(pde, 7) == 1):
            page_addr = 0
            if (byte_per_entry == 4):
                page_addr = getAddrFromEntry(pde, 4194304, len(mem), byte_per_entry) # 4*1024*1024 = 4194304
            else:
                page_addr = getAddrFromEntry(pde, 2097152, len(mem), byte_per_entry) # 2*1024*1024 = 2097152
            
            if (page_addr in page_indexs_3 or page_addr in page_indexs_4):
                w += 1
        else:
            pt_addr = getAddrFromEntry(pde, 4096, len(mem), byte_per_entry)
            
            #if (pt_addr > mem_size - 1024): continue
            
            w_pte = scanPageTable(pde, pt_addr, pt_con_func, mem, i0, i1, page_indexs_1, page_indexs_2, byte_per_entry)
            
            if (w_pte == -1):
                if (isLoop):
                    continue
                else:
                    print_err(hex(pde_addr) + ' ' + str(i0) + ' ' + str(i1) + ' ' + '02' + '\n')
                    return -1
                #return -1
            
            w += w_pte
    
    return w
