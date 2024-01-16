// https://atcoder.jp/contests/abs/tasks/abc081_b
// ABC081B - Shift only

using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int[] A = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);

        int count = 0;
        while (A.All(a => a % 2 == 0))
        {
            A = A.Select(a => a / 2).ToArray();
            count++;
        }
        Console.WriteLine(count);
    }
}
