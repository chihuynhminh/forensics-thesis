using System;
using System.Collections.Generic;

namespace GenScenarios.Models
{
    public partial class OsAct
    {
        public int IdOs { get; set; }
        public int IdAct { get; set; }

        public virtual Act IdActNavigation { get; set; }
        public virtual Os IdOsNavigation { get; set; }
    }
}
