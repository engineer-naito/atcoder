// https://atcoder.jp/contests/abs/tasks/arc065_a
// ABC049C - 白昼夢

using System;

class Program
{
    static void Main()
    {
        string S = Console.ReadLine();
        if (S.Replace("eraser", "*").Replace("erase", "*").Replace("dreamer", "*").Replace("dream", "*").Replace("*", "") == "")
        {
            Console.WriteLine("YES");
        }
        else
        {
            Console.WriteLine("NO");
        }
    }
}
