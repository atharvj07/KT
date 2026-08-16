import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int N;
	static int[] P;
	static ArrayList<ArrayList<Integer>> g = new ArrayList<>();

	public static void main(String[] arg) {
		N = sc.nextInt();
		for (int i = 0; i < N; ++i) {
			g.add(new ArrayList<>());
		}
		for (int i = 0; i < N - 1; ++i) {
			int U = Integer.parseInt(sc.next()) - 1;
			int V = Integer.parseInt(sc.next()) - 1;
			g.get(U).add(V);
			g.get(V).add(U);
		}
		P = new int[N];
		P[0] = -1;
		int[] order = new int[N];
		int pos = 1;
		for (int i = 0; i < N; ++i) {
			for (int c : g.get(order[i])) {
				if (c == P[order[i]]) continue;
				P[c] = order[i];
				order[pos++] = c;
			}
		}
		int[] dp = new int[N];
		int[] dp2 = new int[N];
		for (int i = N - 1; i >= 0; --i) {
			int node = order[i];
			for (int c : g.get(node)) {
				if (c == P[node]) continue;
				if (dp[c] + 1 > dp[node]) {
					dp2[node] = dp[node];
					dp[node] = dp[c] + 1;
				} else if (dp[c] + 1 > dp2[node]) {
					dp2[node] = dp[c] + 1;
				}
			}
		}
		for (int i = 1; i < N; ++i) {
			int p = P[order[i]];
			int pv = (dp[p] == dp[order[i]] + 1 ? dp2[p] : dp[p]) + 1;
			if (pv > dp[order[i]]) {
				dp2[order[i]] = dp[order[i]];
				dp[order[i]] = pv;
			} else if (pv > dp2[order[i]]) {
				dp2[order[i]] = pv;
			}
		}
		int[] ans = new int[N];
		for (int i = 0; i < N; ++i) {
			ans[order[i]] = (N - 1) * 2 - dp[order[i]];
		}
		for (int i = 0; i < N; ++i) {
			System.out.println(ans[i]);
		}
	}
}