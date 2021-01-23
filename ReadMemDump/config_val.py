#file_mem_path = '../qemu_vm/x86/nopse_nopae/haikuOS/1'
file_mem_path = '../qemu_vm/x86/nopae/haikuOS/memdumps/1'

file = open(file_mem_path + '.memdump', 'rb')
b = file.read()
mem_size = len(b)

