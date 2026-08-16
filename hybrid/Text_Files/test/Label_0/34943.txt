import java.util.*;
import java.util.stream.*;

/**
 * Permutation Oddness
 * P={p1, p2, ..., pn} 1,2,...,n の順列
 * d(P) = sum(|i-pi|, 1<=i<=n)
 * d(A)=k となる A の個数
 */
public class Main {
	Scanner sc;
	int N;
	int K;
	long[][][] dp;

//=============
// constructor
//
	public Main() {
		sc = new Scanner(System.in);
	}
	
//==================
// instance methods
//
	/**
	 * アルゴリズム本体
	 */
	private void calc() {
		long mod = 1000000007L;
		dp = new long[N+1][N+1][K+1];
		dp[0][0][0]=1;
		for (int i = 1; i <= N; i++) {
			for (int j = 0; j <=i; j++) {
				for (int k = 2*j; k <= K; k++) {
					if (j > 0) dp[i][j][k] = dp[i-1][j-1][k-2*j];
					dp[i][j][k] = (dp[i][j][k] + (2*j + 1) * dp[i-1][j][k-2*j]) % mod;
					if (j < N) dp[i][j][k] = (dp[i][j][k] + (j+1)*(j+1)*dp[i-1][j+1][k-2*j]) % mod;
				}
			}
		}
	}
	
	private void out(Object o) {
		System.out.println(o);
		System.out.flush();
	}
	
	private void input() {
		N = sc.nextInt();
		K = sc.nextInt();
	}
	
	private void output() {
		out(dp[N][0][K]);
	}
	
//======
// main
//
	public static void main(String[] args) {
		Main m = new Main();
		m.input();
		m.calc();
		m.output();
	}

}