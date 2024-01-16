// https://atcoder.jp/contests/abs/tasks/arc089_a
// ABC086C - Traveling

using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        int[][] txy = new int[N][];
        for (int i = 0; i < N; i++)
        {
            txy[i] = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        }

        bool isPossible = true;
        int t_ = 0, x_ = 0, y_ = 0;
        for (int i = 0; i < N; i++)
        {
            (int t, int x, int y) = (txy[i][0], txy[i][1], txy[i][2]);
            int dt = t - t_;
            int distance = Math.Abs(x - x_) + Math.Abs(y - y_);
			(t_, x_, y_) = (t, x, y);
            if (dt < distance || dt % 2 != distance % 2)
            {
                isPossible = false;
                break;
            }
        }
		Console.WriteLine(isPossible ? "Yes" : "No");
    }
}
