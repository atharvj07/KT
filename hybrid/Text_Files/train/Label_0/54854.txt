import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Prob6 {
	
	static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		public String next() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		public int nextInt() {
			return Integer.parseInt(next());
		}

		public long nextLong() {
			return Long.parseLong(next());
		}

		public double nextDouble() {
			return Double.parseDouble(next());
		}

		public String nextLine() {
			String str = "";
			try {
				str = br.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			return str;
		}
	}


	public static void main(String[] args) {
		FastReader fr = new FastReader();
		int z = fr.nextInt();
		for (int o = 0; o < z; o++) {
			int n = fr.nextInt();
			String s = fr.nextLine();
			String t = fr.nextLine();
			int[][] charFreqS = new int[256][n];
			int[][] charFreqT = new int[256][n];
			for (int i = 0; i < n; i++) {
				charFreqS[s.charAt(i)][i] += i-1 >= 0 ? charFreqS[s.charAt(i)][i - 1] + 1 : 1;
				charFreqT[t.charAt(i)][i] += i-1 >= 0 ? charFreqT[t.charAt(i)][i - 1] + 1 : 1;
				for (int j=0; j<256; j++) {
					char charJ = (char)(j);
					if (s.charAt(i) != charJ) {
						charFreqS[j][i] = i-1 >= 0 ? charFreqS[j][i-1]  : 0;
					}
					if (t.charAt(i) != charJ) {
						charFreqT[j][i] = i-1 >= 0 ? charFreqT[j][i-1] : 0;
					}
				}
			}
			int[][] dp = new int[n + 1][n + 1];
			for (int i=1; i<=n; i++) {
				Arrays.fill(dp[i], Integer.MAX_VALUE - 1);
			}
			dp[0][0] = 0;
			boolean possible = true;
			for (int i=0; i<256; i++) {
				if (charFreqS[(char)i][n-1] != charFreqT[(char)i][n-1]) {
					possible = false;
				}
			}
			if (possible) {
				for (int i=0; i<n; i++) {
					for (int j=i; j<n; j++) {
						dp[i+1][j+1] = dp[i][j+1] + 1;
						if (charFreqS[t.charAt(j)][n - 1] - charFreqS[t.charAt(j)][i] > (charFreqT[t.charAt(j)][n - 1]
								- charFreqT[t.charAt(j)][j])) {
							dp[i+1][j+1] = Math.min(dp[i+1][j], dp[i+1][j+1]);
						} 
						if (s.charAt(i) == t.charAt(j)) {
							dp[i+1][j+1] = Math.min(dp[i][j], dp[i+1][j+1]);
						}
					}
				}
				System.out.println(dp[n][n]);
			} else {
				System.out.println(""+-1);
			}
		}
	}

}
