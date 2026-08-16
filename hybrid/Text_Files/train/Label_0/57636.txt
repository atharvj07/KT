import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.*;
import java.util.Calendar.Builder;

import javax.jws.soap.SOAPBinding.Use;



public class Main {
	static int INF = 2 << 27;
	public static void main(String[] args) {	
		//FastScanner sc = new FastScanner();
		Scanner sc = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		while(true) {
			int T = sc.nextInt();
			if(T == 0) break;
			int[] t = new int[T];
			for(int i = 0; i < T; i++) {
				t[i] = sc.nextInt();
			}
			int N = sc.nextInt();
			int[] DM = new int[100];
			for(int i = 0; i < DM.length; i++) {
				DM[i] = INF;
			}
			for(int i = 0; i < N; i++) {
				int D = sc.nextInt()-1;
				DM[D] = Math.min(DM[D], sc.nextInt());
			}
			int[][] dp = new int[101][T];
			for(int i = 0; i < dp.length; i++) {
				Arrays.fill(dp[i], INF);
			}
			dp[0][0] = 0;
			for(int i = 0; i < DM.length; i++) {
				for(int j = 0; j < T; j++) {
					if(dp[i][j] == INF) continue;
					if(t[j] <= DM[i]) {
						dp[i+1][(j + 1) % T] = Math.min(dp[i + 1][(j + 1) % T], dp[i][j]);
					}
					dp[i + 1][1] = Math.min(dp[i+1][1], dp[i][j]+1);
				}
			}
			int min = INF;
			for(int i = 0; i < T; i++) {
				min = Math.min(min, dp[100][i]);
			}
			System.out.println(min);
		}
	}
}