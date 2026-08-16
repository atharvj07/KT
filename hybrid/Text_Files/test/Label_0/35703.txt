import java.util.*;
import java.io.*;
public class EdC {

	public static void main(String[] args) throws Exception{
		int num = 998244353;

		// TODO Auto-generated method stub
 		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
 		PrintWriter out = new PrintWriter(System.out);
 		StringTokenizer st = new StringTokenizer(bf.readLine());
 		long n = Long.parseLong(st.nextToken());
 		long x = Long.parseLong(st.nextToken());
 		long y = Long.parseLong(st.nextToken());
 		long[] dp = new long[(int)(n+2)];
 		for(int j = 1;j<dp.length;j++){
 			long temp = j;
 			dp[j] = x*j;
 			long count = 0;
 			while(temp%2 == 0){
 				temp/=2;
 				count++;
 				dp[j] = Math.min(dp[j],  temp*x+y*count);
 			}
 		}
 		dp[1] = x;
 		for(int j = 2;j<dp.length;j++){
 			if (j%2 == 0)
 				dp[j] = Math.min(dp[j], dp[j/2]+y);
 			else
 				dp[j] = Math.min(dp[j] , Math.min(dp[(j+1)/2]+x+y, dp[(j-1)/2]+x+y));
 			
 		}
 		
 		out.println(dp[(int)(n)]);
	 		
 		out.close();
 		
 		
 		
 	}
}
 	
 
//StringJoiner sj = new StringJoiner(" "); 
//sj.add(strings)
//sj.toString() gives string of those stuff w spaces or whatever that sequence is

 		
 		
 		
 		
	


