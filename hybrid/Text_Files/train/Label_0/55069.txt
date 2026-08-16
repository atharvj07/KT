import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	
	public static final int CAL_MAX = 100 * 100;
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		final int S = sc.nextInt();
		final int T = sc.nextInt();
		final int U = sc.nextInt();
		final int N = sc.nextInt();
		final int O = sc.nextInt();
		final int D = sc.nextInt();
		
		int[] es = new int[T];
		int[] cs = new int[T];
		for(int i = 0; i < T; i++){
			final int e = sc.nextInt();
			final int c = sc.nextInt();
			es[i] = e; // hp
			cs[i] = c; // cal
		}
		int[][] t_dp = new int[U + 1][S + 1];
		for(int i = 0; i <= U; i++){
			Arrays.fill(t_dp[i], -1);
		}
		t_dp[0][0] = 0;
		for(int t = 0; t < T; t++){
			for(int u = U - 1; u >= 0; u--){
				for(int s = S - es[t]; s >= 0; s--){
					if(t_dp[u][s] >= 0){
						final int next = t_dp[u + 1][s + es[t]];
						
						if(t_dp[u + 1][s + es[t]] < 0){
							t_dp[u + 1][s + es[t]] = t_dp[u][s] + cs[t];
						}else{
							t_dp[u + 1][s + es[t]] = Math.max(next, t_dp[u][s] + cs[t]);
						}
					}
				}
				//System.out.println(u + " :=> " + Arrays.toString(t_dp[u]));
			}
		}
		
		int[] c_dp = new int[CAL_MAX + 1];
		Arrays.fill(c_dp, -1);
		c_dp[0] = 0;
		
		for(int i = 0; i < N; i++){
			final int h = sc.nextInt();
			final int a = sc.nextInt();
		
			for(int j = 0; j <= (CAL_MAX - a); j++){
				if(c_dp[j] >= 0){
					c_dp[j + a] = Math.max(c_dp[j + a], c_dp[j] + h);
				}
			}
			for(int j = 1; j <= CAL_MAX; j++){
				c_dp[j] = Math.max(c_dp[j], c_dp[j - 1]);
			}
		}
		
		//System.out.println(Arrays.toString(c_dp));
		//System.out.println(Arrays.toString(t_dp[U]));
		
		int[][] dp = new int[D + 1][S + 1];
		for(int i = 0; i <= D; i++){
			Arrays.fill(dp[i], -1);
		}
		dp[0][S] = 0;
		for(int d = 0; d < D; d++){
			for(int s = 0; s <= S; s++){
				if(dp[d][s] < 0){
					continue;
				}
				
				for(int e = 0; e <= s; e++){
					final int cal = t_dp[U][e];
					if(cal < 0){
						continue;
					}
					
					final int happy = c_dp[cal];
					//System.out.println(cal + " : " + happy);
					
					dp[d + 1][Math.min(S, s - e + O)] = Math.max(dp[d + 1][Math.min(S, s - e + O)], dp[d][s] + happy);
				}
			}
			//System.out.println(Arrays.toString(dp[d]));
		}
		//System.out.println(Arrays.toString(dp[D]));
		
		int max = -1;
		for(int i = 0; i <= S; i++){
			max = Math.max(max, dp[D][i]);
		}
		
		System.out.println(max);
		
		sc.close();
	}

	public static class Scanner {
		private BufferedReader br;
		private StringTokenizer tok;

		public Scanner(InputStream is) throws IOException {
			br = new BufferedReader(new InputStreamReader(is));
		}

		private void getLine() throws IOException {
			while (!hasNext()) {
				tok = new StringTokenizer(br.readLine());
			}
		}

		private boolean hasNext() {
			if (tok == null) {
				return false;
			} else {
				return tok.hasMoreTokens();
			}
		}

		public String next() throws IOException {
			getLine();
			return tok.nextToken();
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}

		public void close() throws IOException {
			br.close();
		}
	}

}