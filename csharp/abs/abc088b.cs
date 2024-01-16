// https://atcoder.jp/contests/abs/tasks/abc088_b
// ABC088B - Card Game for Two

using System;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int[] a = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        Array.Sort(a);

        int diff = 0;
        for (int i = 0; i < N; i++)
        {
            if (i % 2 == 0)
            {
                diff += a[i];
            }
            else
            {
                diff -= a[i];
            }
        }
        Console.WriteLine(diff);
    }
}
