
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		int N = scn.nextInt();
		int M = scn.nextInt();
		int[] A = new int[M+1];
		long[] fib = new long[N + 1];
		final long MOD = 1000000007;
		long ans = 1;
		boolean can = true;
		for (int i = 0; i < M; i++) {
			A[i] = scn.nextInt();
			if (i != 0 && A[i] - A[i - 1] == 1)
				can = false;
		}
		A[M] = N+1;
		if (can) {
			fib[1] = 1;
			fib[0] = 1;
			for (int i = 2; i <= N; i++) {
				fib[i] = fib[i - 1] + fib[i - 2];
				fib[i] %= MOD;
			}
			int b = 0;

			for (int i = 0; i < M+1; i++) {
				int a = A[i];
				ans *= fib[a - b-1];
				ans %= MOD;
				b = a+1;
			}
		} else {
			ans = 0;
		}
		System.out.println(ans);
	}

}
