import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int x[] = new int[M];
		for (int i = 0; i < M; i++) {
			x[i] = sc.nextInt();
		}
		if (N >= M) {
			System.out.println(0);
			return;
		}
		Arrays.sort(x);

		Integer L[] = new Integer[M-1];

		for (int i = 0; i < M-1; i++) {
			L[i] = x[i+1] - x[i];
		}
		Arrays.sort(L,Collections.reverseOrder());

		int ans = 0;

		for (int i = 0; i < M-1; i++) {
			if (i < N-1) {
				continue;
			}
			ans += L[i];
		}
		System.out.println(ans);
	}
}
