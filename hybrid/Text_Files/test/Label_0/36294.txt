import java.util.*;
import java.io.*;
import java.lang.*;

class Main
{
	public static void main(String[] args)
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		try{
			for(int cnt=0;; ++cnt){
				int w = Integer.parseInt(bf.readLine());
				if(w==0) break;
				int n = Integer.parseInt(bf.readLine());
				int[] vs = new int[n];
				int[] ws = new int[n];

				for(int i=0; i<n; ++i){
					String[] strs = bf.readLine().split(",");
					vs[i] = Integer.parseInt(strs[0]);
					ws[i] = Integer.parseInt(strs[1]);
				}

				int ansv = -1;
				int answ = 0;
				int[][] dp = new int[n][w+1];

				for(int i=0; i<n; ++i){
					for(int j=0; j<w+1; ++j){
						if(i == 0)
							dp[i][j] = ws[i]<=j ? vs[i] : 0;
						else{
							dp[i][j] = dp[i-1][j];
							if(j-ws[i]>=0)
								dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-ws[i]]+vs[i]);
						}
						if(ansv < dp[i][j] || (ansv == dp[i][j] && answ > j)){
							ansv = dp[i][j];
							answ = j;
						}
					}
				}

				System.out.println("Case " + (cnt+1) + ":\n" + ansv + "\n" + answ);
			}
		}
		catch(IOException ex)
		{}
	}
}