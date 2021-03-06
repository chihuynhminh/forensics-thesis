from x86_pse_pae import *

import time
start_time = time.time()
import os

#file_mem_path = 'x86/nopse_nopae/haikuOS/1'
#file_mem_path = 'x86/pse_nopae/haikuOS/1'
#file_mem_path = 'x86/pse_nopae/winxp/3'
#file_mem_path = 'x86/pse_nopae/xubuntu_10/1'
#file_mem_path = 'x86/pse_nopae/win_vista/4'
#file_mem_path = 'memdump_pae/1'
file_mem_path = '../../../Data/qemu_vm/x86/winxp/memdump/pse_pae/2'


if (not os.path.exists(file_mem_path)): os.mkdir(file_mem_path)

file = open(file_mem_path + '.dump', 'rb')
mem = file.read()
mem_size = len(mem)

# haiku
#process_list = ['/boot/system/servers/input_server', '/boot/system/servers/app_server',
#                'kernel_team', '/boot/system/data/deskbar/menu/Applications/Terminal',
#                '/boot/system/servers/package_daemon', '/boot/system/Tracker']

# winxp
#process_list = ['sass.exe', 'lsass.exe', 'csrss.exe', 'winlogon.exe', 'System',
#                'services.exe', 'alg.exe', 'explorer.exe', 'cmd.exe', 'spoolsv.exe']

#process_list = ['sass.exe', 'lsass.exe', 'csrss.exe', 'winlogon.exe', 'System',
#                'services.exe', 'alg.exe', 'explorer.exe', 'cmd.exe', 'spoolsv.exe',
#                'notepad.exe', 'svchost.exe']

#process_list = ['sass.exe', 'lsass.exe', 'csrss.exe', 'winlogon.exe', 'System',
#                'services.exe', 'alg.exe', 'explorer.exe', 'cmd.exe', 'spoolsv.exe',
#                'notepad.exe', 'svchost.exe', 'wmplayer.exe', 'wpabaln.exe']

# winvista
process_list = ['smss.exe', 'lsass.exe', 'csrss.exe', 'winlogon.exe', 'System',
                'services.exe', 'svchost.exe', 'explorer.exe', 'cmd.exe', 'spoolsv.exe']

#process_list = ['smss.exe', 'lsass.exe', 'csrss.exe', 'winlogon.exe', 'System',
#                'services.exe', 'alg.exe', 'explorer.exe', 'cmd.exe', 'spoolsv.exe',
#                'notepad.exe', 'svchost.exe', 'taskeng.exe', 'MSASCui.exe']

#process_list = ['smss.exe', 'lsass.exe', 'csrss.exe', 'winlogon.exe', 'System',
#                'services.exe', 'alg.exe', 'explorer.exe', 'cmd.exe', 'spoolsv.exe',
#                'notepad.exe', 'svchost.exe', 'taskeng.exe', 'wmpnetwk.exe']

#process_list = ['smss.exe', 'lsass.exe', 'csrss.exe', 'winlogon.exe', 'System',
#               'services.exe', 'alg.exe', 'explorer.exe', 'cmd.exe', 'spoolsv.exe',
#                'notepad.exe', 'svchost.exe', 'MineSweeper.exe', 'wmpnetwk.exe']

# freebsd
#process_list = ['/sbin/devd', '/usr/sbin/syslogd-s', '/usr/sbin/sshd', '/usr/sbin/moused-p/de',
#                '-csh(csh)', 'sleep60']

# ubuntu 8
#process_list = ['hald-runner', '-bash', '/usr/sbin/cupsd', '/usr/sbin/cron',
#                '/usr/lib/bluetooth/bluetoothd-service-input', '/usr/bin/system-tools-backends']

# xubuntu 10
#process_list = ['hald-runner', '/usr/bin/xfce4-volumed', 'update-notifier', '/usr/lib/gvfs/gvfsd',
#                '/usr/lib/gamin/gam_server', 'xfsettingsd']

#process_list = ['hald-runner', '/usr/bin/xfce4-volumed', 'update-notifier', '/usr/lib/gvfs/gvfsd',
#                '/usr/lib/gamin/gam_server', 'xfsettingsd', 'mousepad', '/usr/lib/udisks/udisks-daemon']

#process_list = ['hald-runner', '/usr/bin/xfce4-volumed', 'update-notifier', '/usr/lib/gvfs/gvfsd',
#                '/usr/lib/gamin/gam_server', 'nm-applet--sm-disable', 'mousepad', '/usr/lib/udisks/udisks-daemon',
#                '/usr/games/gnomine', 'xfsettingsd']

#process_list = ['hald-runner', '/usr/bin/xfce4-volumed', 'update-notifier', '/usr/lib/gvfs/gvfsd',
#                '/usr/lib/gamin/gam_server', 'xfsettingsd', 'mousepad', '/usr/lib/udisks/udisks-daemon',
#                '/usr/games/gnomine', '/usr/lib/firefox-3.6.3/firefox-bin', 
#                '/bin/sh /usr/lib/firefox-3.6.3/run-mozilla.sh', '/bin/sh /usr/lib/firefox-3.6.3/firefox']


for i_process_list in range(0, int(len(process_list)), 2):
    pname1 = process_list[i_process_list]
    pname2 = process_list[i_process_list + 1]
    print(pname1 + ' ' + pname2)

    cr3_list, w_cr3, pd_list = list_pdpt_pse_pae(pname1, pname2, mem_size, mem)
    
    f = open(file_mem_path + '/' + pname1.replace('/', '') + '_' + pname2.replace('/', '') + 'pdpt.txt', 'w')
    for i in range(len(cr3_list)):
        f.write(hex(cr3_list[i]) + ' ' + hex(w_cr3[i]) + '\n')
    f.close()

    f = open(file_mem_path + '/' + pname1.replace('/', '') + '_' + pname2.replace('/', '') + 'pd.txt', 'w')
    for i in range(len(pd_list)):
        f.write(hex(pd_list[i]) + ' ' + '\n')
    f.close()



print("Scaning time: %s seconds -----------------------" % (time.time() - start_time))

