// https://atcoder.jp/contests/abs/tasks/practice_1
// PracticeA - Welcome to AtCoder

using System;
class Program;
{
    static void Main()
    {
        int a = int.Parse(Console.ReadLine());
        string[] input = Console.ReadLine().Split(' ');
        (int b, int c) = (int.Parse(input[0]), int.Parse(input[1]));
        string s = Console.ReadLine();

        Console.WriteLine($"{a + b + c} {s}");
    }
}
