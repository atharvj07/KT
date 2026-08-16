import java.util.Scanner;
public class Main
{
	double[][] dp;
	boolean[][] used;
	int N,T,L,B;
	int[] LB;
	public void solve()
	{
		Scanner cin = new Scanner(System.in);
		while(true)
		{
			N = cin.nextInt();
			T = cin.nextInt();
			L = cin.nextInt();
			B = cin.nextInt();
			if(N + T + L + B == 0)break;
			LB = new int[N + 1];
			dp = new double[T + 1][N + 1];
			used = new boolean[T + 1][N + 1];
			for(int i = 0;i < L;i++)LB[cin.nextInt()] = 'L';
			for(int i = 0;i < B;i++)LB[cin.nextInt()] = 'B';
			dp[0][0] = 1.0;
			for(int i = 0;i < T;i++)
			{
				for(int j = 0;j < N;j++)
				{
					for(int k = 1;k <= 6;k++)
					{
						int next = j + k;
						if(next > N)next = N - (next - N);
						if(LB[next] == 'L')
						{
							if(i + 2 <= T)dp[i + 2][next] += dp[i][j] * 1.0 / 6.0;
							else dp[i + 1][next] += dp[i][j] * 1.0 / 6.0;
						}else if(LB[next] == 'B')
						{
							dp[i + 1][0] += dp[i][j] * 1.0 / 6.0;
						}else
						{
							dp[i + 1][next] += dp[i][j] * 1.0 / 6.0;
						}
					}
				}
			}
			double ans = 0.0;
			for(int i = 0;i <= T;i++)
			{
				ans += dp[i][N];
			}
			System.out.println(String.format("%.6f",ans));
		}
	}
	public static void main(String[] args)
	{
		new Main().solve();
	}
}