import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) throws Exception {
		while (true) {
			int N = sc.nextInt();
			long K = sc.nextLong();
			if (N == 0 && K == 0) break;
			solve(N, K);
		}
	}

	static void solve(int N, long K) {
		if (N % 2 != 0 || K > (1 << (N / 2))) {
			System.out.println("No");
			System.out.println();
			return;
		}
		--K;
		boolean[][] f = new boolean[N][N];
		for (int i = 0; i < N / 2; ++i) {
			f[i][i] = i % 2 == 0 ^ (K & (1 << (N / 2 - i - 1))) == 0;
			for (int j = 1; j <= i; ++j) {
				f[i - j][i + j] = f[i + j][i - j] = f[i][i] ^ j % 2 != 0;
			}
			for (int j = 0; j <= i; ++j) {
				int r = i - j;
				int c = i + 1 + j;
				int count = 0;
				if (f[r][c - 1] == f[r + 1][c - 1]) ++count;
				if (r != 0 && f[r][c - 1] == f[r - 1][c - 1]) ++count;
				if (c > 1 && f[r][c - 1] == f[r][c - 2]) ++count;
				f[r][c] = count >= 2 ? !f[r][c - 1] : f[r][c - 1];
			}
			for (int j = 0; j <= i; ++j) {
				int r = i + 1 + j;
				int c = i - j;
				int count = 0;
				if (f[r - 1][c] == f[r - 1][c + 1]) ++count;
				if (c != 0 && f[r - 1][c] == f[r - 1][c - 1]) ++count;
				if (r > 1 && f[r - 1][c] == f[r - 2][c]) ++count;
				f[r][c] = count >= 2 ? !f[r - 1][c] : f[r - 1][c];
			}
		}
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N - i - 1; ++j) {
				f[N - 1 - i][N - 1 - j] = f[i][j];
			}
		}
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				System.out.print(f[i][j] ? 'E' : '.');
			}
			System.out.println();
		}
		System.out.println();
	}
}