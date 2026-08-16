import java.util.Arrays;
import java.util.Scanner;

public class P913C
{
	static long[] cost;
	static long[][] dp;
	static int min;
	static long oo = Long.MAX_VALUE;
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		min = scan.nextInt();
		cost = new long[31];
		Arrays.fill(cost, oo);
		for (int i = 0; i < n; i++)
			cost[i] = scan.nextInt();
		long best = cost[0];
		for (int i = 1; i < cost.length; i++)
		{
			best *= 2;
			if (best <= cost[i])
				cost[i] = best;
			else
			{
				best = cost[i];
				for (int j = 0; j < i; j++)
					cost[j] = Math.min(cost[j], best);
			}
		}
		dp = new long[31][2];
		for (long[] a : dp)
			Arrays.fill(a, -1);
		System.out.println(go(30, 1));
	}
	private static long go(int pow, int bounded)
	{
		if (pow < 0)
			return 0;
		if (dp[pow][bounded] >= 0)
			return dp[pow][bounded];
		long ans = oo;
		int s = bounded == 1 ? ((min & (1 << pow)) != 0 ? 1 : 0) : 0;
		for (int i = s; i <= 1; i++)
		{
			long c = i == 1 ? cost[pow] : 0;
			ans = Math.min(ans, c + go(pow-1, bounded == 0 || i != s ? 0 : 1));
		}
		return dp[pow][bounded] = ans;
	}
}
