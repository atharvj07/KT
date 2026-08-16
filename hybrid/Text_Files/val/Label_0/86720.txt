import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		new Main().run();
	}

	void run() {
		Scanner sc = new Scanner(System.in);
		while (true) {
			int N = sc.nextInt();
			if (N == 0)
				break;
			int[] A = new int[N];
			for (int i = 0; i < N; ++i) {
				A[i] = sc.nextInt();
			}

			solve(N, A);
		}
	}

	void solve(int N, int[] A) {
		boolean[] vis = new boolean[N];
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		for (int v : A) {
			pq.add(v);
		}
		int ans = 0;
		while (!pq.isEmpty()) {
			int v = pq.poll();
			ArrayList<Integer> lis = new ArrayList<>();
			for (int i = 0; i < N; ++i) {
				if (vis[i] || A[i] % v != 0)
					continue;
				for (int j = 0; j < 10; ++j) {
					if (A[i] / v == (1 << j)) {
						lis.add(1 << j);
						vis[i] = true;
					}
				}
			}
			ans = Math.max(ans, calc(lis));
		}
		System.out.println(ans);
	}

	int calc(ArrayList<Integer> lis) {
		int sum = 0;
		for (int v : lis) {
			sum += v;
		}

		int[] dp = new int[sum + 1];
		Arrays.fill(dp, -Integer.MAX_VALUE / 16);
		dp[0] = 0;
		for (int v : lis) {
			for (int i = sum / v * v; i >= v; i -= v) {
				dp[i] = Math.max(dp[i], dp[i - v] + 1);
			}
		}
		int ret = 0;
		for (int i = 1; i <= sum; i <<= 1) {
			ret = Math.max(ret, dp[i]);
		}
		return ret;
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}