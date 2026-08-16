import java.io.*;
import java.util.*;
public class  Main{
	public static void main(String[] args) throws Exception{
		MScanner sc=new MScanner(System.in);
		PrintWriter pw=new PrintWriter(System.out);
		int r=sc.nextInt(),c=sc.nextInt();
		if(r==1 && c==1) {
			pw.println(0);pw.flush();return;
		}
		int num=2;
		if(r==1 || c==1) {
			for(int i=0;i<r;i++) {
				for(int j=0;j<c;j++) {
					pw.print((num++)+" ");
				}
				pw.println();
			}
			pw.flush();return;
		}
		int[][]ans=new int[r][c];
		for(int i=0;i<c;i++) {
			ans[0][i]=num++;
		}
		int i=1,j=0;
		
		while(i<r) {
			while(j<c) {
				ans[i][j]=num*ans[0][j];j++;
			}
			i++;j=0;num++;
		}
		
		for(int ii=0;ii<r;ii++) {
			for(int jj=0;jj<c;jj++) {
				pw.print(ans[ii][jj]+" ");
			}
			pw.println();
		}
		pw.flush();
	}	
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
		public int[] takearr(int n) throws IOException {
	        int[]in=new int[n];for(int i=0;i<n;i++)in[i]=nextInt();
	        return in;
		}
		public long[] takearrl(int n) throws IOException {
	        long[]in=new long[n];for(int i=0;i<n;i++)in[i]=nextLong();
	        return in;
		}
		public Integer[] takearrobj(int n) throws IOException {
	        Integer[]in=new Integer[n];for(int i=0;i<n;i++)in[i]=nextInt();
	        return in;
		}
		public Long[] takearrlobj(int n) throws IOException {
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
 
		public Long nextLong() throws IOException {
			return Long.parseLong(next());
		}
 
		public boolean ready() throws IOException {
			return br.ready();
		}
 
		public void waitForInput() throws InterruptedException {
			Thread.sleep(3000);
		}
	}
}