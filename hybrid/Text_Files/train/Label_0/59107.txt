import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int N = sc.nextInt();
		int M = sc.nextInt();
		long[] A = new long[N + 2];
		long[] B = new long[M];
		for (int i = 0; i < N; i++) {
			A[i + 1] = Integer.parseInt(sc.next());
		}
		A[N + 1] = 1000000;
		for (int i = 0; i < M; i++) {
			B[i] = Integer.parseInt(sc.next());
		}
		Arrays.sort(A);
		long[] AS = new long[N + 2];
		for (int i = 0; i < N + 1; i++) {
			AS[i + 1] = AS[i] + A[i + 1];
		}
		long ans = 0;
		long[] cache = new long[501];
		Arrays.fill(cache, -1);
		for (int i = 0; i < M; i++) {
			int MOD = (int) B[i];
			if (MOD < cache.length) {
				if (cache[MOD] != -1) {
					ans += cache[MOD];
					continue;
				}
				long sum = 0;
				for (int j = 0; j < N; j++) {
					sum += A[j + 1] % MOD;
				}
				cache[MOD] = sum;
				ans += sum;
			} else {
				int left = 0;
				for (long j = 0; j <= A[N] + MOD;) {
					int prev = left;
					int right = N + 1;
					while (right - left > 1) {
						int mid = (left + right) >> 1;
						if (A[mid] >= j + MOD) {
							right = mid;
						} else {
							left = mid;
						}
					}
					long len = left - prev;
					ans += AS[left] - AS[prev] - len * j;
					j = A[right] / MOD * MOD;
				}
			}
		}
		System.out.println(ans);
	}


}

