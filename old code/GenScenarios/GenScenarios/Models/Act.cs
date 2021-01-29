using System;
using System.Collections.Generic;

namespace GenScenarios.Models
{
    public partial class Act
    {
        static public int count = 0;

        public int Id { get; set; }
        public string ActName { get; set; }

        public Act(string name)
        {
            ++count;
            Id = count;
            ActName = name;
        }

        public override string ToString() 
        {
            return ActName;
        }

        public static List<Act> ActTable()
        {
            return new List<Act>()
            {
                new Act ("Start"),
                new Act ("Run cmd"),
                new Act ("Run notepad"),
                new Act ("Run mspaint"),
                new Act ("Run calculator"),
                new Act ("Run game pinball"),
                new Act ("Run game hover"),
                new Act ("Run game solitaire"),
                new Act ("Run game minesweeper"),
                new Act ("Run game freecell"),
                new Act ("Run Windows Media Player"),
                new Act ("Open a picture"),
                new Act ("Open a video"),
                new Act ("Run Internet Explorer"),
                new Act ("Run Word"),
                new Act ("Run Excel"),
                new Act ("Run Powerpoint"),
                new Act ("Run Firefox (blank page)"),
                new Act ("Run Firefox (Youtube)"),
                new Act ("Run Firefox (Google Search)"),
                new Act ("Run Firefox (Facebook)"),
                new Act ("Run Firefox (Twitter)"),
                new Act ("Run Firefox (Gmail)"),
                new Act ("Run Google Chrome (blank page)"),
                new Act ("Run Google Chrome (Youtube)"),
                new Act ("Run Google Chrome (Google Search)"),
                new Act ("Run Google Chrome (Facebook)"),
                new Act ("Run Google Chrome (Twitter)"),
                new Act ("Run Google Chrome (Gmail)"),
                new Act ("Close Server Manager"),
                new Act ("Run Control Panel"),
                new Act ("Turn off firewall"),
                new Act ("Run gedit"),
                new Act ("Run LibreOffice Writer"),
                new Act ("Run LibreOffice Calc"),
                new Act ("Run LibreOffice Impress")
            };
        }
    }
}
