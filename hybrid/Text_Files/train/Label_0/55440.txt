import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		new Main().run();
	}

	void run() {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long K = sc.nextLong();
		int[] A = new int[N];
		int[][] B = new int[N][2];
		for (int i = 0; i < N; ++i) {
			A[i] = sc.nextInt();
			B[i] = new int[] { A[i], i };
		}

		Arrays.sort(B, new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				if (o1[0] != o2[0])
					return Integer.compare(o1[0], o2[0]);
				else
					return Integer.compare(o1[1], o2[1]);
			}
		});

		long[][] sum = new long[N][60];
		int[][] dst = new int[N][60];
		for (int i = 0; i < sum.length; ++i)
			for (int j = 0; j < sum[i].length; ++j)
				sum[i][j] = -1;
		for (int i = 0; i < N; ++i) {
			int j = i;
			while (j + 1 < N && B[j][0] == B[j + 1][0]) {
				dst[B[j][1]][0] = (B[j + 1][1] + 1) % N;
				sum[B[j][1]][0] = B[j + 1][1] - B[j][1] + 1;
				++j;
			}
			sum[B[j][1]][0] = N + B[i][1] - B[j][1] + 1;
			dst[B[j][1]][0] = (B[i][1] + 1) % N;
			i = j;
		}
		for (int i = 0; i + 1 < sum[0].length; ++i) {
			for (int j = 0; j < N; ++j) {
				sum[j][i + 1] = Math.min(sum[j][i] + sum[dst[j][i]][i], Long.MAX_VALUE / 3);
				dst[j][i + 1] = dst[dst[j][i]][i];
			}
		}

		long res = K * N;
		int pos = 0;
		while (res > 0) {
			int ok = -1;
			int ng = 60;
			while (ng - ok > 1) {
				int middle = (ok + ng) / 2;
				if (sum[pos][middle] > res) {
					ng = middle;
				} else {
					ok = middle;
				}
			}
			if (ok == -1)
				break;
			res -= sum[pos][ok];
			pos = dst[pos][ok];
		}

		ArrayDeque<Integer> dq = new ArrayDeque<>();
		while (res > 0) {
			if (res >= sum[pos][0]) {
				res -= sum[pos][0];
				pos += sum[pos][0];
			} else {
				dq.addLast(A[pos]);
				++pos;
				--res;
			}
			pos %= N;
		}
		PrintWriter pw = new PrintWriter(System.out);
		while (!dq.isEmpty()) {
			pw.print(dq.pollFirst() + (dq.isEmpty() ? "\n" : " "));
		}
		pw.close();
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}