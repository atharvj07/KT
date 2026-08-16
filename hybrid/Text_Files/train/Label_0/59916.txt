import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) throws Exception {
		while (true) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			if (N == 0) break;
			int min = N;
			for (int i = 0; i < M; ++i) {
				min = Math.min(min, sc.nextInt());
			}
			System.out.printf("%.5f\n", min == 1 ? 0.0 : N / 2.0);
		}
	}

}