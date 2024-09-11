using System;
using System.Collections.Generic;

namespace Ejercicio7Diccionarios // Note: actual namespace depends on the project name.
{
    internal class Program
    {

        static void charFrequency(string strF) {
            Dictionary<char, int> dict = new Dictionary<char, int>();

            dict.Clear();
            foreach (char c in strF)
            {
                try
                {
                    dict.Add(c, 1);
                }
                catch (Exception ex) {
                    //Console.WriteLine("se rompio aaaaaahhhhhhh");
                    dict[c] +=1;
                }
            }


            foreach(KeyValuePair<char,int> kvp in dict)
            {
                Console.WriteLine("key = {0}, value = {1}",kvp.Key,kvp.Value);
            }
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            charFrequency("google.com");
        }
    }
}