https://atcoder.jp/contests/abs/tasks/abc086_a
// ABC086A - Product

using System;

class Program
{
    static void Main()
    {
        string[] input = Console.ReadLine().Split(' ');
        (int a, int b) = (int.Parse(input[0]), int.Parse(input[1]));

        Console.WriteLine(a * b % 2 == 0 ? "Even" : "Odd");
    }
}
