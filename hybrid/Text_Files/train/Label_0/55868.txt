import java.util.Arrays;
import java.util.Scanner;

class Main {
	int N, M;
	int[] X, Y;

	public static void main(String[] args) {
		new Main().run();
	}

	void run() {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		X = new int[M];
		Y = new int[M];
		int[] deg = new int[N];
		for (int i = 0; i < M; ++i) {
			X[i] = sc.nextInt();
			Y[i] = sc.nextInt();
			--X[i];
			--Y[i];
			++deg[X[i]];
			++deg[Y[i]];
		}
		int[] sz = new int[N];
		Arrays.fill(sz, 1);
		boolean[] del = new boolean[N];
		for (int i = 0; i < M; ++i) {
			if (deg[X[i]] < deg[Y[i]]) {
				del[Y[i]] = true;
			} else if (deg[Y[i]] < deg[X[i]]) {
				del[X[i]] = true;
			} else {
				if (X[i] > Y[i]) {
					del[X[i]] = true;
				} else {
					del[Y[i]] = true;
				}
				++sz[X[i]];
				++sz[Y[i]];
			}
		}
		long ans1 = 0, ans2 = 1;
		for (int i = 0; i < N; ++i) {
			if (!del[i]) {
				++ans1;
				ans2 = (ans2 * sz[i]) % (1_000_000_000 + 9);
			}
		}
		System.out.println(ans1);
		System.out.println(ans2);
	}

}