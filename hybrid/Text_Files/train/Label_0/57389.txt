import java.util.*;

public class Main {
	static final long MODULO = 1_000_000_000 + 7;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		int C = sc.nextInt() - 1;
		int T = sc.nextInt();
		int[] a = new int[K];
		int[] b = new int[K];
		int[] t = new int[K];
		for (int i = 0; i < K; ++i) {
			a[i] = sc.nextInt();
			b[i] = sc.nextInt();
			t[i] = sc.nextInt();
		}
		// dp[t]=A[1]dp[t-1]+A[2]dp[t-2]+A[3]dp[t-3]
		long[][][] A = new long[6][N][N];
		for (int i = 0; i < K; ++i) {
			for (int j = 0; j < b[i]; ++j) {
				A[t[i]][j][(a[i] - 1) + j] += 1;
			}
			for (int j = 0; j < a[i] - 1; ++j) {
				A[t[i]][b[i] + j][j] += 1;
			}
			for (int j = a[i] + b[i] - 1; j < N; ++j) {
				A[t[i]][j][j] += 1;
			}
		}
		long[][] dp = new long[6][N];
		dp[0][C] = 1;
		for (int i = 1; i <= 5; ++i) {
			for (int j = 0; j < i; ++j) {
				dp[i] = addVec(dp[i], mulVec(A[i - j], dp[j]));
			}
		}
		long[] v = new long[N * 5];
		for (int i = 0; i < 5; ++i) {
			for (int j = 0; j < N; ++j) {
				v[j + i * N] = dp[i][j];
			}
		}
		long[][] mx = new long[5 * N][5 * N];
		for (int i = N; i < 5 * N; ++i) {
			mx[i - N][i] = 1;
		}
		for (int i = 1; i <= 5; ++i) {
			for (int j = 0; j < N; ++j) {
				for (int k = 0; k < N; ++k) {
					mx[4 * N + j][N * (5 - i) + k] = A[i][j][k];
				}
			}
		}

		v = mulVec(pow(mx, T), v);
		System.out.println(v[0]);
	}

	static long[][] mul(long[][] a, long[][] b) {
		int n = a.length;
		long[][] ret = new long[n][n];
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				for (int k = 0; k < n; ++k) {
					ret[i][j] += a[i][k] * b[k][j] % MODULO;
					ret[i][j] %= MODULO;
				}
			}
		}
		return ret;
	}

	static long[] mulVec(long[][] a, long[] v) {
		int n = v.length;
		long[] ret = new long[n];
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				ret[i] += a[i][j] * v[j] % MODULO;
				ret[i] %= MODULO;
			}
		}
		return ret;
	}

	static long[] addVec(long[] a, long[] b) {
		int n = a.length;
		long[] ret = new long[n];
		for (int i = 0; i < n; ++i) {
			ret[i] = (a[i] + b[i]) % MODULO;
		}
		return ret;
	}

	static long[][] pow(long[][] a, long n) {
		int len = a.length;
		long[][] ret = new long[len][len];
		for (int i = 0; i < len; ++i)
			ret[i][i] = 1;
		for (; n > 0; n >>= 1, a = mul(a, a)) {
			if (n % 2 == 1) {
				ret = mul(ret, a);
			}
		}
		return ret;
	}

	static void showMatrix(long[][] a) {
		int n = a.length;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				System.out.print(a[i][j] + " ");
			}
			System.out.println();
		}
	}

	static void showVec(long[] a) {
		for (int i = 0; i < a.length; ++i) {
			System.out.print(a[i] + " ");
		}
		System.out.println();
	}

	static void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}