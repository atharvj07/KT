import java.io.*;
import java.util.*;


public class  Main{
	static int n,m,k;
	static int[]idxInMask;
	static event[]in;
	static class event implements Comparable<event>{
		int type,x,idx;
		event(int t,int xx,int ii){
			type=t;//start -> 0 , end -> 1
			x=xx;
			idx=ii;
		}
		@Override
		public int compareTo(event o) {
			return x==o.x?type-o.type:x-o.x;
		}
		
	}
	static int[][]memo;
	static int dp(int i,int msk) {
		if(i>=2*n)return 0;
		if(memo[i][msk]!=-1)return memo[i][msk];
		
		if(in[i].type==0) {
			int nxt=in[i+1].type;
			int newmsk=msk|(1<<idxInMask[in[i].idx]);
			int incTake=0,incLeave=0;
			if(Integer.bitCount(newmsk)%2==1) {
				incTake=in[i+1].x-in[i].x;
				if(nxt==1) {
					incTake++;
				}
				
			}
			else {
				incLeave=in[i+1].x-in[i].x;
				if(nxt==1) {
					incLeave++;
				}
			}
			return memo[i][msk]=Math.max(dp(i+1, newmsk)+incTake, dp(i+1, msk)+incLeave);
		}
		int inc=0;
		int newmsk=msk;
		if((newmsk&(1<<idxInMask[in[i].idx]))!=0)
			newmsk=msk^(1<<idxInMask[in[i].idx]);
		if(Integer.bitCount(newmsk)%2==1) {
			if(i+1<2*n) {
				inc=in[i+1].x-in[i].x;
				if(in[i+1].type==0)inc--;
			}
		}
		return memo[i][msk]=dp(i+1,newmsk)+inc;
	}
	public static void main(String[] args) throws Exception{
		MScanner sc=new MScanner(System.in);
		PrintWriter pw=new PrintWriter(System.out);
		n=sc.nextInt();m=sc.nextInt();k=sc.nextInt();
		in=new event[2*n];
		for(int i=0;i<n;i++) {
			in[2*i]=new event(0, sc.nextInt(), i);
			in[2*i+1]=new event(1, sc.nextInt(), i);
		}
		Arrays.sort(in);
		idxInMask=new int[n];
		boolean[]indices=new boolean[k];
		for(int i=0;i<2*n;i++) {
			if(in[i].type==0) {
				int idx=0;
				while(indices[idx])idx++;
				idxInMask[in[i].idx]=idx;
				indices[idx]=true;
			}
			else {
				int idx=idxInMask[in[i].idx];
				indices[idx]=false;
			}
		}
		memo=new int[2*n][1<<k];
		for(int[]i:memo)Arrays.fill(i, -1);
		pw.println(dp(0,0));
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