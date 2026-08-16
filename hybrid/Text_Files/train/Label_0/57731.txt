import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int N = sc.nextInt();
		if (N % 2 != 0) {
			System.out.println("NA");
			return;
		}
		int[] X = new int[N];
		int[] Y = new int[N];
		int sx = 0;
		int sy = 0;
		for (int i = 0; i < N; ++i) {
			X[i] = sc.nextInt() * N;
			Y[i] = sc.nextInt() * N;
			sx += X[i];
			sy += Y[i];
		}
		sx /= N;
		sy /= N;
		for (int i = 0; i < N; ++i) {
			int dx = X[i] - sx;
			int dy = Y[i] - sy;
			if (X[(i + N / 2) % N] != sx - dx || Y[(i + N / 2) % N] != sy - dy) {
				System.out.println("NA");
				return;
			}
		}
		System.out.println((1.0 * sx / N) + " " + (1.0 * sy / N));
	}

}