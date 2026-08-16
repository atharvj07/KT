import java.io.*;
import java.util.*;
public class cf383d {

	public static void main(String[] args)throws IOException {
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		PrintWriter out=new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
		StringTokenizer st=new StringTokenizer(bf.readLine());
		int n=Integer.parseInt(st.nextToken());
		int mod=(int)1e9+7;
		int[][] dp=new int[n+1][(int)2e4+1];
		st=new StringTokenizer(bf.readLine());
		int[] a=new int[n];
		for(int i=0;i<n;i++) {
			a[i]=Integer.parseInt(st.nextToken());
		}
		dp[0][10000]=0;
		for(int i=1;i<=n;i++) {
			for(int j=a[i-1];j<=20000-a[i-1];j++) {
				dp[i][j-a[i-1]]+=dp[i-1][j];
				dp[i][j-a[i-1]]%=mod;
				dp[i][j+a[i-1]]+=dp[i-1][j];
				dp[i][j+a[i-1]]%=mod;
			}
			dp[i][10000+a[i-1]]++;
			dp[i][10000-a[i-1]]++;
		}
		long ans=0;
		for(int i=1;i<=n;i++) {
			ans+=dp[i][10000];
			ans%=mod;
		}
		out.println(ans);
		out.close();
	}

}
