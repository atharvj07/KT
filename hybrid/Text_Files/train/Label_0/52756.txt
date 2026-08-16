import java.util.*;
import java.io.*;
import java.lang.reflect.Array;
import java.math.BigInteger;

import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
 
public class Main{
    static long mod=1000000007;
//    static int dx[]={-1,0,1,0};
//    static int dy[]={0,-1,0,1};

    public  static void main(String[] args)   throws Exception, IOException{        
        Reader sc = new Reader(System.in);
        PrintWriter out=new PrintWriter(System.out);

        int n = sc.nextInt();
        int a[]=new int[n];
        int s=0;
        for (int i = 0; i < a.length; i++) {
			a[i]=sc.nextInt();
			s+=a[i];
		}
        int mx=90000;
        mod=998244353;
//        mx=10;
        long dp[][]=new long[n+1][mx+301];
        long dp2[][]=new long[n+1][mx+301];
        dp[0][0]++;
        dp2[0][0]++;
        long ans=1;
        for (int i = 1; i <= n; i++) {
        	ans*=3; ans%=mod;
//        	dp[i-1][0]=1;
			for (int t = 0; t <= mx; t++) {
				dp[i][t+a[i-1]] += dp[i-1][t];
				dp[i][t] += 2*dp[i-1][t]; 
				dp[i][t+a[i-1]]%=mod;
				dp[i][t]%=mod;
				dp2[i][t+a[i-1]] += dp2[i-1][t];
				dp2[i][t] += dp2[i-1][t];
				dp2[i][t+a[i-1]]%=mod;
				dp2[i][t]%=mod;
			}
		}
        if(s%2==0)ans+=3*dp2[n][s/2];
        for (int i = (s+1)/2; i <= s ; i++) {
			ans-=3*dp[n][i];
	        ans%=mod;
		}
        ans=(ans+mod)%mod;
        db(s);
        out.println(ans);
        out.flush();
    }

    static boolean validpos(int x,int y,int r, int c){
        return x<r && 0<=x && y<c && 0<=y;
    }

    static void db(Object... os){
        System.err.println(Arrays.deepToString(os));
    }  
}

//class P {
//    int id, d;
//    P(int  id, int d) {
//        this.id=id;
//        this.d=d;
//    }
//}

//class P implements Comparable<P>{
//    int id,T;
//    P(int id, int T) {
//        this.id=id;
//        this.T=T;
//    }
//    public int compareTo(P p){
//        return id-p.id; //des
//    }
//}

class Reader
{ 
    private BufferedReader x;
    private StringTokenizer st;
    
    public Reader(InputStream in)
    {
        x = new BufferedReader(new InputStreamReader(in));
        st = null;
    }
    public String nextString() throws IOException
    {
        while( st==null || !st.hasMoreTokens() )
            st = new StringTokenizer(x.readLine());
        return st.nextToken();
    }
    public int nextInt() throws IOException
    {
        return Integer.parseInt(nextString());
    }
    public int[] nextIntArray(int size) throws IOException{
    	int r[] = new int[size];
    	for (int i = 0; i < size; i++) {
			r[i] = this.nextInt(); 
		}
    	return r;
    }
    public long[] nextLongArray(int size) throws IOException{
    	long r[] = new long[size];
    	for (int i = 0; i < size; i++) {
			r[i] = this.nextLong(); 
		}
    	return r;
    }
    public long nextLong() throws IOException
    {
        return Long.parseLong(nextString());
    }
    public double nextDouble() throws IOException
    {
        return Double.parseDouble(nextString());
    }
}
