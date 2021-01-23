using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace GenScenarios
{
    class MathFunc
    {
        static Random rand = new Random();

        public static int nPr(int n, int r)
        {
            if (r == 0)
                return 1;
            if (r == 1)
                return n;
            return (n - r + 1) * nPr(n, r - 1);
        }

        public static int nCr(int n, int r)
        {
            return nPr(n, r) / nPr(r, r);
        }

        public static List<int> RanCom(int count, int minVal, int maxVal)
        {
            List<int> returnList = new List<int>();
            for (int i = 0; i < count; ++i)
            {
                int ranInt;
                do
                {
                    ranInt = rand.Next(minVal, maxVal);
                }
                while (returnList.Contains(ranInt));

                returnList.Add(ranInt);
            }

            returnList.Sort();
            return returnList;
        }

        public static List<List<int>> RanComOfCom(int count, int countEle, int minVal, int maxVal)
        {
            int ncr = nCr(maxVal - minVal, countEle);
            if (count > ncr)
                count = ncr;

            List<List<int>> returnList = new List<List<int>>();
            for (int i = 0; i < count; ++i)
            {
                List<int> ranInts;
                do
                {
                    ranInts = RanCom(countEle, minVal, maxVal);
                }
                while (returnList.Any(l => l.SequenceEqual(ranInts)));

                returnList.Add(ranInts);
            }

            return returnList;
        }
    }
}
