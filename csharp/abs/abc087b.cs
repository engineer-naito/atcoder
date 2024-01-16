// https://atcoder.jp/contests/abs/tasks/abc087_b
// ABC087B - Coins

using System;

class Program
{
    static void Main()
    {
        int A = int.Parse(Console.ReadLine());
        int B = int.Parse(Console.ReadLine());
        int C = int.Parse(Console.ReadLine());
        int X = int.Parse(Console.ReadLine());

        int count = 0;
        for (int a = 0; a <= A; A++;)
        {
            for (int b = 0; B <= B; B++;)
            {
                for (int c = 0; C <= C; C++;)
                {
                    if (500 * a + 100 * b + 50 * c == X)
                    {
                        count++;
                    }
                }
            }
        }
        Console.WriteLine(count);
    }
}
