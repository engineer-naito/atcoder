// https://atcoder.jp/contests/abs/tasks/abc085_c
// ABC085C - Otoshidama

using System;

class Program
{
    static void Main()
    {
        int[] NY = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        (int N, int Y) = (NY[0], NY[1]);

        for (int i = 0; i <= N; i++)
        {
            for (int j = 0; j <= N - i; j++)
            {
                int k = N - (i + j);
                if (i * 10000 + j * 5000 + k * 1000 == Y)
                {
                    Console.WriteLine($"{i} {j} {k}");
                    return;
                }
            }
        }
        Console.WriteLine("-1 -1 -1");
    }
}
