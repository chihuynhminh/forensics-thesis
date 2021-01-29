#from x86_nopse_nopae import *
from x86_pse_nopae import *

import time
start_time = time.time()

#file_mem_path = '../qemu_vm/x86/nopse_nopae/haikuOS/1'
file_mem_path = '/media/n30/Data/qemu_vm/x86/nopae/haikuOS/memdumps/1'

file = open(file_mem_path + '.memdump', 'rb')
b = file.read()
mem_size = len(b)

# haiku
process_list = ['/boot/system/servers/input_server', '/boot/system/servers/app_server',
                'kernel_team', '/boot/system/data/deskbar/menu/Applications/Terminal',
                '/boot/system/servers/package_daemon', '/boot/system/Tracker']

#winxp
#process_list = ['sass.exe', 'lsass.exe', 'csrss.exe', 'winlogon.exe', 'System',
#                'services.exe', 'alg.exe', 'explorer.exe', 'cmd.exe', 'spoolsv.exe']

#freebsd
#process_list = ['/sbin/devd', '/usr/sbin/syslogd-s', '/usr/sbin/sshd', '/usr/sbin/moused-p/de',
#                '-csh(csh)', 'sleep60']

for i_process_list in range(0, int(len(process_list)), 2):
  print(process_list[i_process_list] + ' ' + process_list[i_process_list + 1])
  scan_pd_pse_nopae(process_list[i_process_list], process_list[i_process_list + 1], mem_size, b, file_mem_path)


print("Running time: %s seconds -----------------------" % (time.time() - start_time))

