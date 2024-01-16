// https://atcoder.jp/contests/abs/tasks/abc083_b
// ABC083B - Some Sums

using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int[] input = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        (int N, int A, int B) = (input[0], input[1], input[2]);

        int sum = 0;
        for (int i = 1; i <= N; i++)
        {
            int digitSum = i.ToString().Sum(c => int.Parse(c.ToString()));
            if (A <= digitSum && digitSum <= B)
            {
                sum += i;
            }
        }
        Console.WriteLine(sum);
    }
}
