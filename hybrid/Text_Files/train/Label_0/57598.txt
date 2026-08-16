import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int N;
	static int[] hi, lo;
	static int[] pow10 = new int[8];

	public static void main(String[] args) {
		pow10[0] = 1;
		for (int i = 1; i < pow10.length; ++i) {
			pow10[i] = pow10[i - 1] * 10;
		}
		while (sc.hasNext()) {
			N = sc.nextInt();
			if (N == 0) break;
			hi = new int[N];
			lo = new int[N];
			for (int i = 0; i < N; ++i) {
				lo[i] = sc.nextInt();
				hi[i] = sc.nextInt();
			}
			long ans = solve();
			System.out.println(ans);
		}
	}

	static long solve() {
		boolean[] first = new boolean[1000000];
		boolean[] second = new boolean[1000000];
		enumerate(0, 0, N / 2, first);
		enumerate(0, N / 2, N, second);
		long ret = 0;
		for (int i = N; i <= 2 * N; ++i) {
			ret += solveDigits(i, first, second);
		}
		return ret;
	}

	static void enumerate(int cur, int idx, int ei, boolean[] bitmap) {
		if (idx == ei) {
			bitmap[cur] = true;
			return;
		}
		for (int i = lo[idx]; i <= Math.min(hi[idx], 9); ++i) {
			enumerate(cur * 10 + i, idx + 1, ei, bitmap);
		}
		for (int i = Math.max(10, lo[idx]); i <= hi[idx]; ++i) {
			enumerate(cur * 100 + i, idx + 1, ei, bitmap);
		}
	}

	// 全体がdigits桁あるパターン数を数える
	static long solveDigits(int digits, boolean[] first, boolean[] second) {
		long ret = 0;
		int fFix = Math.max(N / 2, digits - (N - N / 2) * 2); // 必ず前半部になる桁数
		int sFix = Math.max(N - N / 2, digits - (N / 2) * 2); // 必ず後半部になる桁数
		int center = digits - fFix - sFix;
		if (center == 0) {
			long fc = 0;
			long sc = 0;
			for (int i = pow10[fFix - 1]; i < pow10[fFix]; ++i) {
				if (first[i]) ++fc;
			}
			for (int i = pow10[sFix - 1]; i < pow10[sFix]; ++i) {
				if (second[i]) ++sc;
			}
			return fc * sc;
		}

		for (int i = 0; i < pow10[center]; ++i) {
			int[] fb = new int[pow10[fFix]];
			int[] sb = new int[pow10[sFix]];
			for (int j = 0; j <= center; ++j) { // 中央部の値がiであり、うち初めのj桁が前半部に含まれる場合
				int cf = i / pow10[center - j];
				int cs = i % pow10[center - j];
				int fd = fFix + j;
				for (int k = pow10[fd - 1] + cf; k < pow10[fd]; k += pow10[j]) {
					if (first[k]) {
						fb[k / pow10[j]] |= 1 << j;
					}
				}
				if (j != center && cs < pow10[center - j - 1]) {
					continue; // 後半部がleading zeroになっている
				}
				for (int k = (j == center ? pow10[sFix - 1] : 0); k < pow10[sFix]; ++k) {
					if (second[k + cs * pow10[sFix]]) {
						sb[k] |= 1 << j;
					}
				}
			}

			// inclusion-exclusion
			for (int j = 1; j < (1 << (center + 1)); ++j) {
				long fc = 0;
				long sc = 0;
				for (int k = 0; k < fb.length; ++k) {
					if ((fb[k] & j) == j) ++fc;
				}
				for (int k = 0; k < sb.length; ++k) {
					if ((sb[k] & j) == j) ++sc;
				}
				long count = fc * sc;
				ret += Integer.bitCount(j) % 2 == 0 ? -count : count;
			}
		}
		return ret;
	}

}