#file = open('x86_nopae_xubuntu12_1.mem', 'rb')
file = open('../qemu_vm/x86_nopse_nopae_winxp_prosp3/xxx.memdump', 'rb')
bytes = file.read()
#cr3 = 0xfba7000
cr3 = 0x00039000
pdes = []
va = 0x00000000

# 67 0110 0111
# e3 1110 0011
#    0111 1011
#    7    b
#    0110 0011
#    6    3

def getEntry(addr):
	global bytes
	_4bytes = bytes[addr : addr + 4]
	# little endian
	pde = _4bytes[3] << 24
	pde = pde | (_4bytes[2] << 16)
	pde = pde | (_4bytes[1] << 8)
	pde = pde | (_4bytes[0])
	return pde

def va2pa(va):
	global cr3
	pde = getEntry((cr3 & 0xfffff000) | (va >> 20) & 0x00000ffc)
	pte = getEntry((pde & 0xfffff000) | (va >> 20) & 0x00000ffc)
	pa  = getEntry((pte & 0xfffff000) | (va & 0x00000fff))
	return pa

for i in range(1024):
	pde = getEntry((cr3 & 0xfffff000) + 4*i)
	if ((pde & 0x7b) == 0x63):
		print(hex(pde) + '===========================================')
		for j in range(1024):
			pte = getEntry((pde & 0xfffff000) + 4*j)
			print(hex(pte), end=' ')
			if (j % 4 == 3): print('')
			
	pdes.append(pde)



# print(hex(va2pa(va)))

'''
for i in range(len(pdes)):
	#print(hex2Bin(pdes[i]))
	if ((pdes[i] & 0x1) == 1):
		print(hex(pdes[i]))'''

