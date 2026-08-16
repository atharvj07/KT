import java.util.*;
public class Main {

	public static void main(String[] args) {
		int MOD = 1_000_000_007;
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[] A = new long[N];
		Arrays.setAll(A, i -> sc.nextInt());
		long ans = 0;
		long[] s = new long[N+1];
		for(int i = 0; i < N; i++)
			s[i+1] = (s[i] + A[N-1-i]) % MOD;
		for(int i = 0; i < N; i++)
			ans = (ans + s[N-i-1]* A[i]) % MOD;
		System.out.println(ans);
	}

}
