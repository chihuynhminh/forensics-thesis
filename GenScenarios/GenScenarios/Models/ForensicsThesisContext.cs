using System;
using System.Collections.Generic;

namespace GenScenarios.Models
{
    public partial class ForensicsThesisContext
    {
        public ForensicsThesisContext()
        {
            Os = Models.Os.OsTable();
            Act = Models.Act.ActTable();
            OsAct = Models.OsAct.OsActTable();
        }

        public List<Act> Act { get; set; }
        public List<Os> Os { get; set; }
        public List<OsAct> OsAct { get; set; }

    }
}
