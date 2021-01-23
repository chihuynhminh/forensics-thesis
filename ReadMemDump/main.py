#from x86_nopse_nopae import *
from x86_nopae import *

import time
start_time = time.time()


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
  scan_pd_nopae(process_list[i_process_list], process_list[i_process_list + 1])


print("Running time: %s seconds -----------------------" % (time.time() - start_time))

