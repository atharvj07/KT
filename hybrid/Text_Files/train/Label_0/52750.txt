import java.io.*;
import java.util.*;

public class Main{
	static int n,m,mod=(int)1e9+7;
	static char[][]in;
	static long[][][][][]memo;
	static int allOnes;
	static long dp(int i,int j,int mskGuarded,int protectedRow,int notProtectedCell) {
		if(i>=n)return 1;
		if(j>=m) {
			return dp(i+1, 0, mskGuarded, 0, notProtectedCell);
		}
		if(memo[i][j][mskGuarded][protectedRow][notProtectedCell]!=-1) {
			return memo[i][j][mskGuarded][protectedRow][notProtectedCell];
		}
		if(in[i][j]=='x') {
			return memo[i][j][mskGuarded][protectedRow][notProtectedCell]=dp(i, j+1, (mskGuarded&(allOnes^(1<<j))), 0, notProtectedCell);
		}
		if(protectedRow==1 || (((mskGuarded>>j)&1)==1)) {
			long putGuard=dp(i, j+1, mskGuarded|(1<<j), 1, notProtectedCell);
			long noGuard=dp(i, j+1, mskGuarded, protectedRow, notProtectedCell);
			return memo[i][j][mskGuarded][protectedRow][notProtectedCell]=(putGuard+noGuard)%mod;
		}
		long putGuard=dp(i, j+1, mskGuarded|(1<<j), 1, notProtectedCell);
		long noGuard=notProtectedCell==1?0:dp(i, j+1, mskGuarded, protectedRow, 1);
		return memo[i][j][mskGuarded][protectedRow][notProtectedCell]=(putGuard+noGuard)%mod;
	}
	static void main() throws Exception{
		n=sc.nextInt();m=sc.nextInt();
		if(m>n) {
			in=new char[m][n];
			for(int i=0;i<n;i++) {
				char[]s=sc.nextLine().toCharArray();
				for(int j=0;j<m;j++) {
					in[j][i]=s[j];
				}
			}
			int tmp=n;
			n=m;
			m=tmp;
		}
		else {
			in=new char[n][m];
			for(int i=0;i<n;i++) {
				in[i]=sc.nextLine().toCharArray();
			}
		}
		//m<=16
		memo=new long[n][m][1<<m][2][2];
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				for(int k=0;k<1<<m;k++) {
					for(int o=0;o<2;o++) {
						memo[i][j][k][o][0]=memo[i][j][k][o][1]=-1;
					}
				}
			}
		}
		allOnes=(1<<m)-1;
		pw.println(dp(0, 0, 0, 0, 0));
	}
	public static void main(String[] args) throws Exception{
		sc=new MScanner(System.in);
		pw = new PrintWriter(System.out);
		int tc=1;
//		tc=sc.nextInt();
		while(tc-->0)
			main();
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