// https://atcoder.jp/contests/abs/tasks/abc085_b
// ABC085B - Kagami Mochi

using System;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int[] d = new int[N];
        for (int i = 0; i < N; i++)
        {
            d[i] = int.Parse(Console.ReadLine());
        }
        Array.Sort(d);

        int count = 1;
        for (int i = 1; i < N; i++)
        {
            if (d[i] == d[i - 1])
            {
                break;
            }
            count++;
        }

        Console.WriteLine(count);
    }
}
