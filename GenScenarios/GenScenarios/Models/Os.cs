using System;
using System.Collections.Generic;

namespace GenScenarios.Models
{
    public partial class Os
    {
        public int Id { get; set; }
        public string OsName { get; set; }
        public string Architecture { get; set; }
        public string Kernel { get; set; }
        public int? Memory { get; set; }
    }
}
