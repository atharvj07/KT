import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		while (true) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			int H = sc.nextInt();
			int K = sc.nextInt();
			if (N == 0) break;
			int[] v = new int[N];
			for (int i = 0; i < N; ++i) {
				v[i] = sc.nextInt();
			}
			int[] bar = new int[M];
			for (int i = 0; i < M; ++i) {
				int a = sc.nextInt() - 1;
				int b = sc.nextInt();
				bar[i] = (b << 10) + a;
			}
			Arrays.sort(bar);
			int[] to = new int[N];
			int[] from = new int[N];
			for (int i = 0; i < N; ++i) {
				to[i] = from[i] = i;
			}
			for (int i = M - 1; i >= 0; --i) {
				int a = bar[i] & 1023;
				swap(to, a, a + 1);
			}
			int base = 0;
			for (int i = 0; i < K; ++i) {
				base += v[to[i]];
			}
			int minDiff = 0;
			for (int i = 0; i < M; ++i) {
				int a = bar[i] & 1023;
				int fa = from[a];
				int fb = from[a + 1];
				if (fa < K && fb >= K) {
					minDiff = Math.min(minDiff, v[to[fb]] - v[to[fa]]);
				} else if (fa >= K && fb < K) {
					minDiff = Math.min(minDiff, v[to[fa]] - v[to[fb]]);
				}
				swap(from, a, a + 1);
			}
			System.out.println(base + minDiff);
		}
	}

	static void swap(int[] a, int x, int y) {
		int tmp = a[x];
		a[x] = a[y];
		a[y] = tmp;
	}

}