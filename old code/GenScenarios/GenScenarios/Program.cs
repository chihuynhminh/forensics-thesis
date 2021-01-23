using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;
using System.Text;
using GenScenarios.Models;

namespace GenScenarios
{
    class Program
    {
        static void AddSce(StreamWriter file, Os os, List<Act> acts)
        {
            file.Write("\"" + os.OsName);
            file.Write("\",\"");
            file.Write(os.Architecture);
            file.Write("\",\"");
            file.Write(os.Kernel);
            file.Write("\",\"");
            file.Write(os.Memory.ToString());
            file.Write("\",\"");

            file.Write(String.Join(", ", acts));

            file.Write("\"\n");
        }

        //Vét cạn
        static void GenSce()
        {
            ForensicsThesisContext _context = new ForensicsThesisContext();

            List<Os> Oss = _context.Os.Where(o => o.Id < 2).ToList();
            using (System.IO.StreamWriter file =
                new System.IO.StreamWriter(@"scenarios.csv"))
            {
                foreach (Os os in Oss)
                {
                    List<int> actIds = _context.OsAct.Where(osac => osac.IdOs == os.Id).Select(osac => osac.IdAct).ToList();
                    List<Act> acts = _context.Act.Where(a => actIds.Contains(a.Id)).ToList();

                    BigInteger maxCount = BigInteger.Pow(2, acts.Count); //1000000000...0000

                    BigInteger count = 1;                                //0000000000...0001

                    while (count <= maxCount)
                    {
                        file.Write("\"" + os.OsName);
                        file.Write("\",\"");
                        file.Write(os.Architecture);
                        file.Write("\",\"");
                        file.Write(os.Kernel);
                        file.Write("\",\"");
                        file.Write(os.Memory.ToString());
                        file.Write("\",\"");

                        BigInteger temp = count;
                        int post = 0;
                        while (temp > 0)
                        {
                            if ((temp & 1) == 1)
                            {
                                file.Write(acts[post].ActName);
                                file.Write(",");
                            }
                            post += 1;
                            temp >>= 1;
                        }

                        file.Write("\"\n");
                        count += 2;                                      //0000000000...0010
                    }
                }
                file.Close();
            }
        }

        static void RandomGenSce()
        {
            ForensicsThesisContext _context = new ForensicsThesisContext();

            List<Os> Oss = _context.Os.ToList();
            using (System.IO.StreamWriter file =
                new System.IO.StreamWriter(@"scenarios.csv"))
            {
                foreach (Os os in Oss)
                {
                    Console.WriteLine(os.OsName);

                    List<int> actIds = _context.OsAct.Where(osac => osac.IdOs == os.Id).Select(osac => osac.IdAct).ToList();
                    List<Act> acts = _context.Act.Where(a => actIds.Contains(a.Id)).ToList();

                    List<List<int>> logs = new List<List<int>>();

                    AddSce(file, os, new List<Act>() { acts[0] });

                    foreach (Act act in acts.Where(ac => ac.Id != 1))
                    {
                        AddSce(file, os, new List<Act>() { acts[0], act });
                    }

                    foreach (List<int> l in MathFunc.RanComOfCom(20, 2, 1, acts.Count))
                    {
                        l.Insert(0, 0);
                        AddSce(file, os, l.Select(i => acts[i]).ToList());
                    }

                    foreach (List<int> l in MathFunc.RanComOfCom(20, 3, 1, acts.Count))
                    {
                        l.Insert(0, 0);
                        AddSce(file, os, l.Select(i => acts[i]).ToList());
                    }

                    foreach (List<int> l in MathFunc.RanComOfCom(20, 4, 1, acts.Count))
                    {
                        l.Insert(0, 0);
                        AddSce(file, os, l.Select(i => acts[i]).ToList());
                    }

                    foreach (List<int> l in MathFunc.RanComOfCom(20, 5, 1, acts.Count))
                    {
                        l.Insert(0, 0);
                        AddSce(file, os, l.Select(i => acts[i]).ToList());
                    }
                }
                file.Close();
            }
        }

        static void Test()
        {
            for (int i = 0; i < 11; i++)
            {
                Console.WriteLine(MathFunc.nCr(10, i));
            }
        }

        static void Main(string[] args)
        {
            RandomGenSce();
            //Test();
        }
    }
}
