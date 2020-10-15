using System;
using System.Collections.Generic;

namespace GenScenarios.Models
{
    public partial class Act
    {
        public int Id { get; set; }
        public string ActName { get; set; }

        public override string ToString() 
        {
            return ActName;
        }
    }
}
