import java.io.*;
import java.util.*;
public class Main
{
	long sum[][];
	private void solve()throws IOException
	{
		init();
		int n=nextInt();
		int c=nextInt();
		int a[]=new int[n+1];
		int b[]=new int[n+1];
		for(int i=1;i<=n;i++)
			a[i]=nextInt();
		for(int i=1;i<=n;i++)
			b[i]=nextInt();
		//dp[i][j] is the sum obtained by distributing j candies among [1..i] students
		long dp[][]=new long[n+1][c+1];
		dp[0][0]=1;
		for(int i=1;i<=n;i++)
			for(int j=0;j<=c;j++)
				for(int k=0;k<=j;k++)
					dp[i][j]=(dp[i][j]+(dp[i-1][j-k]*sum(a[i],b[i],k))%mod)%mod;
		out.println(dp[n][c]);
	}
	void init()
	{
		int maxn=400;
		sum=new long[maxn+1][maxn+1];
		for(int k=0;k<=maxn;k++)
			for(int i=1;i<=maxn;i++)
				sum[k][i]=(sum[k][i-1]+modpow(i,k))%mod;
	}
	//sum of a^k+(a+1)^k+...+b^k
	long sum(int a,int b,int k)
	{
		return (sum[k][b]-sum[k][a-1]+mod)%mod;
	}
	final long mod=(long)(1e9+7);
	long modpow(long a,long b){
	    long ret=1;
	    while(b!=0)
	    {
	        if(b%2==1)
	            ret=(ret*a)%mod;
	        a=(a*a)%mod;
	        b=b/2;
	    }
	    return ret;
	} 

	 
	///////////////////////////////////////////////////////////

	public void run()throws IOException
	{
		br=new BufferedReader(new InputStreamReader(System.in));
		st=null;
		out=new PrintWriter(System.out);

		solve();
		
		br.close();
		out.close();
	}
	public static void main(String args[])throws IOException{
		new Main().run();
	}
	BufferedReader br;
	StringTokenizer st;
	PrintWriter out;
	String nextToken()throws IOException{
		while(st==null || !st.hasMoreTokens())
		st=new StringTokenizer(br.readLine());
		return st.nextToken();
	}
	String nextLine()throws IOException{
		return br.readLine();
	}
	int nextInt()throws IOException{
		return Integer.parseInt(nextToken());
	}
	long nextLong()throws IOException{
		return Long.parseLong(nextToken());
	}
	double nextDouble()throws IOException{
		return Double.parseDouble(nextToken());
	}
}