import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int N, M, E;
	static int[] from;
	static long[] cost;

	static boolean disjoint() {
		UnionFind uf = new UnionFind(N);
		for (int i = 0; i < N; ++i) {
			if (from[i] != -1) uf.union(i, from[i]);
		}
		return uf.size(0) != N;
	}

	static long solve() {
		if (E <= N - 2) return 0;
		if (disjoint()) return 0;
		long ret = Long.MAX_VALUE;
		for (int i = 0; i < N; ++i) {
			if (from[i] == -1) continue;
			for (int j = i + 1; j < N; ++j) {
				if (from[j] == -1) continue;
				ret = Math.min(ret, cost[i] + cost[j]);
			}
		}
		for (int i = 0; i < N; ++i) {
			if (from[i] == -1) continue;
			int tmp = from[i];
			from[i] = -1;
			if (disjoint()) ret = Math.min(ret, cost[i]);
			from[i] = tmp;
		}
		return ret;
	}

	public static void main(String[] args) throws Exception {
		while (true) {
			N = sc.nextInt();
			M = sc.nextInt();
			if (N == 0) break;
			from = new int[N];
			cost = new long[N];
			Arrays.fill(from, -1);
			long minus = 0;
			E = 0;
			for (int i = 0; i < M; ++i) {
				int X = sc.nextInt();
				int Y = sc.nextInt();
				long C = sc.nextLong();
				if (C <= 0) {
					minus += C;
				} else {
					from[Y] = X;
					cost[Y] = C;
					++E;
				}
			}
			System.out.println(solve() + minus);
		}
	}

	static class UnionFind {
		int[] set;

		UnionFind(int n) {
			set = new int[n];
			Arrays.fill(set, -1);
		}

		void union(int a, int b) {
			int rtA = root(a);
			int rtb = root(b);
			if (rtA == rtb) {
				return;
			}
			set[rtA] += set[rtb];
			set[rtb] = rtA;
		}

		boolean find(int a, int b) {
			return root(a) == root(b);
		}

		int root(int a) {
			if (set[a] < 0) {
				return a;
			} else {
				set[a] = root(set[a]);
				return set[a];
			}
		}

		int size(int a) {
			return -set[root(a)];
		}
	}

}