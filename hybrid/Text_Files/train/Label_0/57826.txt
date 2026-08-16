import java.io.*;
import java.util.*;

public class Main{
	static char[]in;
	static long[][]memo;
	static long inf=(long)1e14;
	static long dp(int i,int len) {
		if(len==0)return 1;
		if(i>=in.length)return 0;
		if(memo[i][len]!=-1)return memo[i][len];
		
		long take=dp(i+1,len-1);
		long leave=dp(i+1, len);
		long removeDuplicate=0;
		for(int j=i+1;j<in.length;j++) {
			if(in[i]==in[j]) {
				removeDuplicate=dp(j+1, len-1);
				break;
			}
		}
//		System.out.println(i+" "+len+" "+take+" "+leave+" "+removeDuplicate);
		return memo[i][len]=Math.min(inf, take+leave-removeDuplicate);
	}
	static void main() throws Exception{
		int n=sc.nextInt();
		long k=sc.nextLong();
		in=sc.nextLine().toCharArray();
		memo=new long[n][n+1];
		for(int i=0;i<n;i++)Arrays.fill(memo[i], -1);
		
		long ans=0;
		for(int len=n;len>=0 && k>=0;len--) {
			long cnt=dp(0, len);
//			System.out.println(cnt);
			long wanted=Math.min(k, cnt);
			k-=wanted;
			ans+=wanted*(n-len);
		}
		pw.println(k!=0?-1:ans);
	}
	public static void main(String[] args) throws Exception{
		pw=new PrintWriter(System.out);
		sc = new MScanner(System.in);
		int tc=1;
		while(tc-->0) main();
		pw.flush();
	}
	static PrintWriter pw;
	static MScanner  sc;
	static class MScanner {
		StringTokenizer st;
		BufferedReader br;
		public MScanner(InputStream system) {
			br = new BufferedReader(new InputStreamReader(system));
		}
 
		public MScanner(String file) throws Exception {
			br = new BufferedReader(new FileReader(file));
		}
 
		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}
		public int[] intArr(int n) throws IOException {
	        int[]in=new int[n];for(int i=0;i<n;i++)in[i]=nextInt();
	        return in;
		}
		public long[] longArr(int n) throws IOException {
	        long[]in=new long[n];for(int i=0;i<n;i++)in[i]=nextLong();
	        return in;
		}
		public int[] intSortedArr(int n) throws IOException {
	        int[]in=new int[n];for(int i=0;i<n;i++)in[i]=nextInt();
	        shuffle(in);
	        Arrays.sort(in);
	        return in;
		}
		public long[] longSortedArr(int n) throws IOException {
	        long[]in=new long[n];for(int i=0;i<n;i++)in[i]=nextLong();
	        shuffle(in);
	        Arrays.sort(in);
	        return in;
		}
		public Integer[] IntegerArr(int n) throws IOException {
	        Integer[]in=new Integer[n];for(int i=0;i<n;i++)in[i]=nextInt();
	        return in;
		}
		public Long[] LongArr(int n) throws IOException {
	        Long[]in=new Long[n];for(int i=0;i<n;i++)in[i]=nextLong();
	        return in;
		}
		public String nextLine() throws IOException {
			return br.readLine();
		}
 
		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}
 
		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}
 
		public char nextChar() throws IOException {
			return next().charAt(0);
		}
 
		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}
 
		public boolean ready() throws IOException {
			return br.ready();
		}
 
		public void waitForInput() throws InterruptedException {
			Thread.sleep(3000);
		}
	}
	static void shuffle(int[]in) {
		for(int i=0;i<in.length;i++) {
			int idx=(int)(Math.random()*in.length);
			int tmp=in[i];
			in[i]=in[idx];
			in[idx]=tmp;
		}
	}
	static void shuffle(long[]in) {
		for(int i=0;i<in.length;i++) {
			int idx=(int)(Math.random()*in.length);
			long tmp=in[i];
			in[i]=in[idx];
			in[idx]=tmp;
		}
	}
}