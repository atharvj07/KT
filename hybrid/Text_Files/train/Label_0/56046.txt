import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.SplittableRandom;

public class Main {
	static boolean LOCAL = false;
	static Scanner sc = new Scanner(System.in);
	static int M = 20;
	static int[][] g = new int[M][M];

	public static void main(String[] args) {
		int N, S, T;
		if (LOCAL) {
			SplittableRandom rnd = new SplittableRandom();
			for (int i = 0; i < M; i++) {
				for (int j = 0; j < i; j++) {
					g[i][j] = g[j][i] = rnd.nextInt(10) + 1;
				}
			}
			for (int i = 0; i < M; i++) {
				for (int j = 0; j < M; j++) {
					for (int k = 0; k < M; k++) {
						g[j][k] = Math.min(g[j][k], g[j][i] + g[i][k]);
					}
				}
			}
			for (int i = 0; i < M; i++) {
				for (int j = 0; j < M; j++) {
					System.out.printf("%2d ", g[i][j]);
				}
				System.out.println();
			}
			N = g.length;
			S = 0;
			T = N - 1;
		} else {
			N = sc.nextInt();
			S = sc.nextInt() - 1;
			T = sc.nextInt() - 1;
		}
		ArrayList<Node> nodes = new ArrayList<>();
		int all = query(S, T);
		for (int i = 0; i < N; i++) {
			if (i == S || i == T) continue;
			int d1 = query(S, i);
			int d2 = query(i, T);
			if (d1 + d2 == all) {
				nodes.add(new Node(d1, i));
			}
		}
		Collections.sort(nodes, (n1, n2) -> Integer.compare(n1.d, n2.d));
		ArrayList<Integer> ans = new ArrayList<>();
		ans.add(S);
		int pi = S;
		int pd = 0;
		for (int i = 0; i < nodes.size(); i++) {
			Node n = nodes.get(i);
			if (query(pi, n.i) == n.d - pd) {
				ans.add(n.i);
				pi = n.i;
				pd = n.d;
			}
		}
		ans.add(T);
		System.out.print("!");
		for (int n : ans) {
			System.out.print(" " + (n + 1));
		}
		System.out.println();
	}

	static class Node {
		int d, i;

		public Node(int d, int i) {
			this.d = d;
			this.i = i;
		}
	}

	static int query(int s, int t) {
		if (LOCAL) {
			System.err.println(s + " " + t + " " + g[s][t]);
			return g[s][t];
		}
		System.out.println("? " + (s + 1) + " " + (t + 1));
		System.out.flush();
		int ret = sc.nextInt();
		if (ret == -1) System.exit(0);
		return ret;
	}
}

