import java.util.*;
import java.math.*;
import java.io.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;



public class Main{
	
	// ArrayList<Integer> lis = new ArrayList<Integer>();
	// ArrayList<String> lis = new ArrayList<String>();
	// PriorityQueue<P> que = new PriorityQueue<P>();
	// PriorityQueue<Integer> que = new PriorityQueue<Integer>();
	//  Stack<Integer> que = new Stack<Integer>();
	//HashMap<Long,Long> map = new HashMap<Long,Long>();
    //	static long sum=0;
	// 1000000007 (10^9+7)
	//static int mod = 1000000007;
	static long mod = 1000000007;
	//static int mod = 1000000009; ArrayList<Integer> l[]= new ArrayList[n];
    //static int dx[]={1,-1,0,0};
	//static int dy[]={0,0,1,-1};
	//static int dx[]={1,-1,0,0,1,1,-1,-1};
    //static int dy[]={0,0,1,-1,1,-1,1,-1};
	
	//static Set<Integer> set = new HashSet<Integer>();
	//static ArrayList<Integer> l[];
    //static int parent[][],depth[],node,max_log;
//   static ArrayList<Integer> nd[]= new ArrayList[2001];


public  static void main(String[] args)   throws Exception, IOException{

	//Scanner sc =new Scanner(System.in);
	
	Reader sc = new Reader(System.in);
   

	//int n=sc.nextInt();//,m=sc.nextInt(),k=sc.nextInt();
	//int a=sc.nextInt(),b=sc.nextInt(),c=sc.nextInt();
	
	int n=sc.nextInt(),k=sc.nextInt();//,m=sc.nextInt();//,k=sc.nextInt(),s=0;
	char c[]=sc.nextString().toCharArray();
	long hi[]=new long[n];
	long lo[]=new long[n];
	hi[0]=lo[0]=1;
	for (int i = 1; i < n; i++) {
		hi[i]=hi[i-1]*i; hi[i]%=mod;
		lo[i]=lo[i-1]*exGCD(i, mod)[1];
		lo[i]%=mod;
	}


	
	long v=0,as=0,te=1,tei=exGCD(10,mod)[1];  
	
	
	for (int i = 0; i < c.length; i++) {
	 	int x=c.length-i-1;
	 	int y=c[x]-'0';
		
	 	if( n-1-i>=k ){
	 		as+=te*y*hi[n-1-i]%mod*lo[k]%mod*lo[n-1-i-k];
	 		as%=mod;
	 		as+=mod;
	 	}
	 	if(i>0 && n-i-1>=k-1 && k>=1 ){
	 		v+=te*tei%mod*hi[n-i-1]%mod*lo[k-1]%mod*lo[n-i-k];
	 		v%=mod;
	 		as+=v*y;
	 		as%=mod;
	 		as+=mod;
	 	}
	 	else{
	 		as+=v*y;
	 		as%=mod;
	 		as+=mod;}
	 	//db(as,te,v);
	 	te*=10; te%=mod;
	}
	
	System.out.println(as%mod);
  
}

 static long[] exGCD(long a, long b)
{
	if(a == 0 || b == 0)return null;
	int as = Long.signum(a);
	int bs = Long.signum(b);
	a = Math.abs(a); b = Math.abs(b);
	long p = 1, q = 0, r = 0, s = 1;
	while(b > 0){
		long c = a / b;
		long d;
		d = a; a = b; b = d % b;
		d = p; p = q; q = d - c * q;
		d = r; r = s; s = d - c * s;
	}
	return new long[]{a, p * as, r * bs};
}
/*
  static class P implements Comparable<P>{
	int id, d; ;
	P(int id,int d){
		this.id=id;
		this.d=d;
	} 
	
	public int compareTo(P x){
	//	return  (-x.d+d)>=0?1:-1  ; // ascend long
	//	return   -x.d+d  ; // ascend
		 return   x.d-d  ; //descend
	   }
 
}//*/


static void db(Object... os){
    System.err.println(Arrays.deepToString(os));

}

static boolean validpos(int x,int y,int r, int c){
	
	return x<r && 0<=x && y<c && 0<=y;
	
}

static boolean bit(int x,int k){
	// weather k-th bit (from right) be one or zero
	return  ( 0 < ( (x>>k) & 1 )  )  ? true:false;
}

}


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
	public long nextLong() throws IOException
	{
		return Long.parseLong(nextString());
	}
	public double nextDouble() throws IOException
	{
		return Double.parseDouble(nextString());
	}
}