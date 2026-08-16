import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int N;
	static int[] P, id, W;
	static ArrayList<ArrayList<Integer>> loop;
	static int MOD = 100000007;
	static double EPS = 1e-8;

	public static void main(String[] args) throws Exception {
		while (true) {
			N = sc.nextInt();
			if (N == 0) break;
			P = new int[N];
			id = new int[N];
			W = new int[N];
			for (int i = 0; i < N; ++i) {
				P[i] = nextP();
				id[i] = sc.nextInt();
				W[i] = nextP();
			}
			loop = new ArrayList<ArrayList<Integer>>();
			boolean[] used = new boolean[N];
			for (int i = 0; i < N; ++i) {
				if (used[i]) continue;
				int pos = i;
				ArrayList<Integer> chain = new ArrayList<Integer>();
				while (!used[pos]) {
					chain.add(pos);
					used[pos] = true;
					pos = id[pos];
				}
				loop.add(chain);
			}
			solve();
		}
	}

	static void solve() {
		long combination = 1;
		double exp = 0;
		for (ArrayList<Integer> chain : loop) {
			int count = 0;
			double all = 0;
			for (int i = 0; i < chain.size(); ++i) {
				all += time(W[chain.get(i)]);
			}
			double min = Double.MAX_VALUE;
			for (int i = 0; i < chain.size(); ++i) {
				double v = all - time(W[chain.get(i)]) + time(P[chain.get(i)]);
				if (v < min - EPS) {
					min = v;
					count = 1;
				} else if (v < min + EPS) {
					++count;
				}
			}
			exp += min;
			combination *= count;
			combination %= MOD;
		}
		BigInteger comb = BigInteger.ONE;
		for (int i = 1; i <= N; ++i) {
			comb = comb.multiply(BigInteger.valueOf(i));
		}
		for (ArrayList<Integer> chain : loop) {
			for (int i = 1; i <= chain.size(); ++i) {
				comb = comb.divide(BigInteger.valueOf(i));
			}
		}
		comb = comb.remainder(BigInteger.valueOf(MOD));
		System.out.println(exp + " " + (comb.longValue() * combination % MOD));
	}

	static double time(int p) {
		return 1000.0 / p;
	}

	static int nextP() {
		return Integer.parseInt(sc.next().replaceAll("\\.", ""));
	}

}