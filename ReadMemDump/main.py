from x86_nopse_nopae import *
from x86_pse_nopae import *

import time
start_time = time.time()

#file_mem_path = '../qemu_vm/x86/nopse_nopae/haikuOS/1'
#file_mem_path = '/media/n30/Data/qemu_vm/x86/nopae/haikuOS/memdumps/1'
#file_mem_path = '/media/n30/Data/qemu_vm/x86/nopae/winxp/memdump/1'
file_mem_path = '/media/n30/Data/qemu_vm/x86/nopae/ubuntu_8/memdump/1'

file = open(file_mem_path + '.memdump', 'rb')
mem = file.read()
mem_size = len(mem)

# haiku
#process_list = ['/boot/system/servers/input_server', '/boot/system/servers/app_server',
#                'kernel_team', '/boot/system/data/deskbar/menu/Applications/Terminal',
#                '/boot/system/servers/package_daemon', '/boot/system/Tracker']

# winxp
#process_list = ['sass.exe', 'lsass.exe', 'csrss.exe', 'winlogon.exe', 'System',
#                'services.exe', 'alg.exe', 'explorer.exe', 'cmd.exe', 'spoolsv.exe']

# freebsd
#process_list = ['/sbin/devd', '/usr/sbin/syslogd-s', '/usr/sbin/sshd', '/usr/sbin/moused-p/de',
#                '-csh(csh)', 'sleep60']

# ubuntu 8
process_list = ['hald-runner', '-bash', '/usr/sbin/cupsd', '/usr/sbin/cron',
                '/usr/lib/bluetooth/bluetoothd-service-input', '/usr/bin/system-tools-backends']

for i_process_list in range(0, int(len(process_list)), 2):
    pname1 = process_list[i_process_list]
    pname2 = process_list[i_process_list + 1]
    print(pname1 + ' ' + pname2)
    cr3_list, w_cr3 = list_pd_pse_nopae(pname1, pname2, mem_size, mem, file_mem_path)
    
    f = open(file_mem_path + '/' + pname1.replace('/', '') + '_' + pname2.replace('/', '') + '.txt', 'w')
    for i in range(len(cr3_list)):
        f.write(hex(cr3_list[i]) + ' ' + hex(w_cr3[i]) + '\n')
    f.close()

print("Running time: %s seconds -----------------------" % (time.time() - start_time))

