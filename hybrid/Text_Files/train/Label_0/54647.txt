import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int N;
	static int[][] X, Y;
	static int[] minX = new int[4];
	static int[] minY = new int[4];

	public static void main(String[] args) {
		N = sc.nextInt();
		Arrays.fill(minX, Integer.MAX_VALUE);
		Arrays.fill(minY, Integer.MAX_VALUE);
		X = new int[4][N];
		Y = new int[4][N];
		for (int i = 0; i < N; ++i) {
			int x = Integer.parseInt(sc.next());
			int y = Integer.parseInt(sc.next());
			X[0][i] = x + y;
			Y[0][i] = x - y;
			X[1][i] = X[0][i];
			Y[1][i] = -Y[0][i];
			X[2][i] = -X[0][i];
			Y[2][i] = Y[0][i];
			X[3][i] = -X[0][i];
			Y[3][i] = -Y[0][i];
			for (int j = 0; j < 4; ++j) {
				minX[j] = Math.min(minX[j], X[j][i]);
				minY[j] = Math.min(minY[j], Y[j][i]);
			}
		}
		int l = 0;
		int r = 1000000;
		while (r - l > 1) {
			int m = (l + r) / 2;
			if (ok(m)) {
				r = m;
			} else {
				l = m;
			}
		}
		System.out.println(r);
	}

	static boolean ok(int len) {
		for (int i = 0; i < 4; ++i) {
			int left = 1 << 25;
			int right = -(1 << 25);
			int bottom = 1 << 25;
			int top = -(1 << 25);
			for (int j = 0; j < N; ++j) {
				if (X[i][j] <= minX[i] + len && Y[i][j] <= minY[i] + len) continue;
				left = Math.min(left, X[i][j]);
				right = Math.max(right, X[i][j]);
				bottom = Math.min(bottom, Y[i][j]);
				top = Math.max(top, Y[i][j]);
			}
			if (right - left <= len && top - bottom <= len) return true;
		}
		return false;
	}

}