     

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	static final int MOD = 1000000007;
	static Scanner sc = new Scanner(System.in);
	static int N, M;
	static int[][] pos;
	static int[][] Y;

	static long solveCycle(ArrayList<Cell> list) {
		long ret = 0;

		// start = 0
		long[][] dp = new long[list.size()][2];
		dp[0][0] = 0;
		dp[0][1] = 1;
		for (int i = 1; i < list.size(); ++i) {
			if (list.get(i - 1).s == list.get(i).f) {
				dp[i][0] = dp[i - 1][1];
			} else {
				dp[i][0] = dp[i - 1][0];
			}
			dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % MOD;
		}
		if (list.get(list.size() - 1).s == list.get(0).f) {
			ret += dp[list.size() - 1][0];
		} else {
			ret += dp[list.size() - 1][1];
		}

		// start = 1
		dp = new long[list.size()][2];
		dp[0][0] = 1;
		dp[0][1] = 1;
		for (int i = 1; i < list.size(); ++i) {
			if (list.get(i - 1).s == list.get(i).f) {
				dp[i][0] = dp[i - 1][1];
			} else {
				dp[i][0] = dp[i - 1][0];
			}
			dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % MOD;
		}
		if (list.get(list.size() - 1).s == list.get(0).f) {
			ret += dp[list.size() - 1][1];
		} else {
			ret += dp[list.size() - 1][0];
		}

		return ret % MOD;
	}

	static long solveChain(ArrayList<Cell> list) {
		long[][] dp = new long[list.size()][2];
		dp[0][0] = 1;
		dp[0][1] = 2;
		for (int i = 1; i < list.size(); ++i) {
			if (list.get(i - 1).s == list.get(i).f) {
				dp[i][0] = dp[i - 1][1];
			} else {
				dp[i][0] = dp[i - 1][0];
			}
			dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % MOD;
		}
		return (dp[list.size() - 1][0] + dp[list.size() - 1][1]) % MOD;
	}

	public static void main(String[] args) {
		N = sc.nextInt();
		M = sc.nextInt();
		pos = new int[N + 1][2];
		Y = new int[M][2];
		for (int[] a : pos) {
			Arrays.fill(a, -1);
		}
		for (int i = 0; i < M; ++i) {
			Y[i][0] = sc.nextInt();
			int x = Math.abs(Y[i][0]);
			if (pos[x][0] == -1) {
				pos[x][0] = i;
			} else {
				pos[x][1] = i;
			}
			Y[i][1] = sc.nextInt();
			x = Math.abs(Y[i][1]);
			if (pos[x][0] == -1) {
				pos[x][0] = i;
			} else {
				pos[x][1] = i;
			}
		}
		boolean[] used = new boolean[M];
		long ans = 1;
		for (int i = 0; i < M; ++i) {
			if (Math.abs(Y[i][0]) == Math.abs(Y[i][1])) {
				used[i] = true;
				if (Y[i][0] == -Y[i][1]) {
					ans *= 2;
					ans %= MOD;
				}
			}
		}
		while (true) {
			boolean update = false;
			for (int i = 0; i < M; ++i) {
				if (used[i]) continue;
				update = true;
				ArrayList<Cell> forward = new ArrayList<Cell>();
				ArrayList<Cell> backward = new ArrayList<Cell>();
				forward.add(new Cell(Y[i][0], Y[i][1]));
				used[i] = true;

				boolean cycle = false;
				int cur = i;
				int x = Math.abs(Y[cur][1]);
				while (true) {
					int otherI = pos[x][0] == cur ? 1 : 0;
					if (pos[x][otherI] == -1) break;
					cur = pos[x][otherI];
					if (used[cur]) {
						cycle = true;
						break;
					}
					used[cur] = true;
					int inI = x == Math.abs(Y[cur][0]) ? 0 : 1;
					x = Math.abs(Y[cur][1 - inI]);
					forward.add(new Cell(Y[cur][inI], Y[cur][1 - inI]));
				}
				if (cycle) {
					ans *= solveCycle(forward);
					ans %= MOD;
					continue;
				}

				cur = i;
				x = Math.abs(Y[cur][0]);
				while (true) {
					int otherI = pos[x][0] == cur ? 1 : 0;
					if (pos[x][otherI] == -1) break;
					cur = pos[x][otherI];
					if (used[cur]) {
						throw new RuntimeException();
					}
					used[cur] = true;
					int inI = x == Math.abs(Y[cur][0]) ? 0 : 1;
					x = Math.abs(Y[cur][1 - inI]);
					backward.add(new Cell(Y[cur][1 - inI], Y[cur][inI]));
				}
				Collections.reverse(backward);
				backward.addAll(forward);
				ans *= solveChain(backward);
				ans %= MOD;
			}
			if (!update) break;
		}
		System.out.println(ans);
	}

	static class Cell {
		int f;
		int s;

		Cell(int f, int s) {
			this.f = f;
			this.s = s;
		}
	}

}