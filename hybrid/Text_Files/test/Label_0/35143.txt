import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args){
		FastScanner sc = new FastScanner();
		int N = sc.nextInt();
		int A[] = new int[N];
		for (int i=0;i<N;i++) {
			A[i] = sc.nextInt();
		}

		int dp[][] = new int[N+1][2];
		dp[0][0] = 1;
		dp[0][1] = 0;
		
		for (int i=0;i<N;i++) {
			if (A[i]%2 == 0) {
				dp[i+1][0] += dp[i][0] * 2;
				dp[i+1][1] += dp[i][1] * 2;
				
				dp[i+1][1] += dp[i][0] * 1;
				dp[i+1][1] += dp[i][1] * 1;
			} else {
				dp[i+1][0] += dp[i][0] * 1;
				dp[i+1][1] += dp[i][1] * 1;
				
				dp[i+1][1] += dp[i][0] * 2;
				dp[i+1][1] += dp[i][1] * 2;
				
			}
		}
		
		System.out.println(dp[N][1]);
	}

	public static class FastScanner {
		BufferedReader br;
		StringTokenizer st;

		public FastScanner(String s) {
			try {
				br = new BufferedReader(new FileReader(s));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}

		public FastScanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String nextToken() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(nextToken());
		}

		long nextLong() {
			return Long.parseLong(nextToken());
		}

		double nextDouble() {
			return Double.parseDouble(nextToken());
		}
	}
}