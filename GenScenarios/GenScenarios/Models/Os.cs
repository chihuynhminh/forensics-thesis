using System;
using System.Collections.Generic;

namespace GenScenarios.Models
{
    public partial class Os
    {
        public static int count = 0;

        public int Id { get; set; }
        public string OsName { get; set; }
        public string Architecture { get; set; }
        public string Kernel { get; set; }
        public int Memory { get; set; }

        public Os(string name, string arch, string ker, int mem)
        {
            ++count;
            Id = count;
            OsName = name;
            Architecture = arch;
            Kernel = ker;
            Memory = mem;
        }

        public static List<Os> OsTable()
        {
            return new List<Os>()
            {
                new Os ("Windows 98","x86","Windows 9x",128),
                new Os ("Windows 2000","x86","Windows NT kernel",512),
                new Os ("Windows 2000","x86_64","Windows NT kernel",512),
                new Os ("Windows XP","x86","Windows NT kernel",512),
                new Os ("Windows XP","x86_64","Windows NT kernel",512),
                new Os ("Windows Server 2003","x86","Windows NT kernel",512),
                new Os ("Windows Server 2003","x86_64","Windows NT kernel",512),
                new Os ("Windows Server 2008","x86","Windows NT kernel",512),
                new Os ("Windows Server 2008","x86_64","Windows NT kernel",512),
                new Os ("ArchLinux 2020.06.01","x86","Linux 5.6.15",512),
                new Os ("ArchLinux 2020.06.01","x86_64","Linux 5.6.15",512),
                new Os ("ArchLinux 2020.07.01","x86","Linux  5.7.6",512),
                new Os ("ArchLinux 2020.07.01","x86_64","Linux  5.7.6",512),
                new Os ("ArchLinux 2020.08.01","x86","Linux  5.7.11",512),
                new Os ("ArchLinux 2020.08.01","x86_64","Linux  5.7.11",512),
                new Os ("Debian 2.0","x86","Linux 2.0.34",512),
                new Os ("Debian 2.0","x86_64","Linux 2.0.34",512),
                new Os ("Debian 7.0","x86","Linux 3.2",512),
                new Os ("Debian 7.0","x86_64","Linux 3.2",512),
                new Os ("Debian 10.6","x86","Linux 4.19",512),
                new Os ("Debian 10.6","x86_64","Linux 4.19",512),
                new Os ("Fedora 21","x86","Linux 3.17",512),
                new Os ("Fedora 21","x86_64","Linux 3.17",512),
                new Os ("Fedora 22","x86","Linux 4.0",512),
                new Os ("Fedora 22","x86_64","Linux 4.0",512),
                new Os ("Fedora 30","x86","Linux 5.0",512),
                new Os ("Fedora 30","x86_64","Linux 5.0",512),
                new Os ("Ubuntu 15.04","x86","Linux 3.19",512),
                new Os ("Ubuntu 15.04","x86_64","Linux 3.19",512),
                new Os ("Ubuntu 16.04","x86","Linux 4.4",512),
                new Os ("Ubuntu 16.04","x86_64","Linux 4.4",512),
                new Os ("Ubuntu 19.04","x86","Linux 5.0",512),
                new Os ("Ubuntu 19.04","x86_64","Linux 5.0",512),
                new Os ("Kali Linux 2019.1","x86","Linux  4.19.13",512),
                new Os ("Kali Linux 2019.1","x86_64","Linux  4.19.13",512),
                new Os ("Kali Linux 2020.1","x86","Linux  5.4.0",512),
                new Os ("Kali Linux 2020.1","x86_64","Linux  5.4.0",512),
                new Os ("CentOs 6","x86","Linux 3.10.0-229",1024),
                new Os ("CentOs 6","x86_64","Linux 3.10.0-229",1024),
                new Os ("CentOs 8","x86_64","Linux 3.10.0-229",1024),
                new Os ("CentOs 8","x86_64","Linux 3.10.0-229",1024),

                new Os ("FreeBSD i386 11.4","x86","FreeBSD",512),
                new Os ("FreeBSD amd64 11.4","x86_64","FreeBSD",512),
                new Os ("FreeBSD i386 12.1","x86","FreeBSD",512),
                new Os ("FreeBSD amd64 12.1","x86_64","FreeBSD",512),
                new Os ("OpenBSD i386 6.4","x86","OpenBSD",512),
                new Os ("OpenBSD amd64 6.4","x86_64","OpenBSD",512),
                new Os ("OpenBSD i386 6.8","x86","OpenBSD",512),
                new Os ("OpenBSD amd64 6.8","x86_64","OpenBSD",512),
                new Os ("NetBSD 7.0","x86","NetBSD",512),
                new Os ("NetBSD 7.0","x86_64","NetBSD",512),
                new Os ("NetBSD 8.0","x86","NetBSD",512),
                new Os ("NetBSD 8.0","x86_64","NetBSD",512),
                new Os ("NetBSD 9.0","x86","NetBSD",512),
                new Os ("NetBSD 9.0","x86_64","NetBSD",512)
            };
        }
    }
}
