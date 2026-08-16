import java.util.*;

public class Main implements Runnable {

	private static final long MOD = 1000000009;
	private static final int MAX = 62;

	@Override
	public void run() {
		Scanner sc = new Scanner(System.in);
		for (int c = 1; sc.hasNext(); c++) {
			final int W = sc.nextInt();
			final long H = sc.nextLong();
			final int N = sc.nextInt();
			if (H == 0 && W == 0 && N == 0)
				return;

			NavigableMap<Long, List<Integer>> obs = new TreeMap<Long, List<Integer>>();
			for (int i = 0; i < N; i++) {
				final int x = sc.nextInt() - 1;
				final long y = sc.nextLong() - 1;
				if (!obs.containsKey(y))
					obs.put(y, new ArrayList<Integer>());
				obs.get(y).add(x);
			}
			if (!obs.containsKey(H - 1))
				obs.put(H - 1, new ArrayList<Integer>());
			final long[][][] ms = new long[MAX][W][W];
			for (int i = 0; i < W; i++)
				for (int j = 0; j < W; j++)
					ms[0][i][j] = Math.abs(i - j) <= 1 ? 1 : 0;
			for (int p = 1; p < MAX; p++)
				for (int i = 0; i < W; i++)
					for (int j = 0; j < W; j++)
						for (int k = 0; k < W; k++) {
							ms[p][i][j] += ms[p - 1][i][k] * ms[p - 1][k][j];
							ms[p][i][j] %= MOD;
						}
			long[] v = new long[W];
			v[0] = 1l;
			for (long y = 0; !obs.isEmpty();) {
				Map.Entry<Long, List<Integer>> e = obs.pollFirstEntry();
				final long p = e.getKey() - y;
				for (int b = 0; b < MAX; b++)
					if ((p & (1L << b)) > 0) {
						long[] u = new long[W];
						for (int i = 0; i < W; i++)
							for (int j = 0; j < W; j++) {
								u[i] += ms[b][i][j] * v[j];
								u[i] %= MOD;
							}
						v = u;
					}
				for (final int x : e.getValue())
					v[x] = 0l;
				y += p;
			}
			System.out.println("Case " + c + ": " + v[W - 1]);
		}
	}

	public static void main(String... args) {
		new Main().run();
	}
}