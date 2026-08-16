import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Locale;
import java.util.Map.Entry;

import java.util.Random;
import java.util.Scanner;
import java.util.TreeSet;

public final class CF_626_D2_F2 {


	static boolean verb=true;
	static void log(Object X){if (verb) System.err.println(X);}
	static void log(Object[] X){if (verb) {for (Object U:X) System.err.print(U+" ");System.err.println("");}}
	static void log(int[] X){if (verb) {for (int U:X) System.err.print(U+" ");System.err.println("");}}
	static void log(int[] X,int L){if (verb) {for (int i=0;i<L;i++) System.err.print(X[i]+" ");System.err.println("");}}
	static void log(long[] X){if (verb) {for (long U:X) System.err.print(U+" ");System.err.println("");}}

	static void logWln(Object X){if (verb) System.err.print(X);}
	static void info(Object o){	System.out.println(o);}
	static void output(Object o){outputWln(""+o+"\n");	}
	static void outputWln(Object o){try {out.write(""+ o);} catch (Exception e) {}}

	//static long mod=1000000007;
	static long mod=998244353 ; 


	// Global vars
	static BufferedWriter out;
	static InputReader reader;


	static void test() {
		log("testing");
		Random r=new Random();
		int NMAX=100000;
		int VMAX=256;
		int AMAX=1000;
		int BMAX=1000;
		int CMAX=123453;
		int NTESTS=10000000;
		for (int t=0;t<NTESTS;t++) {

		}
		log("done");
	}


	static int[][] clone(int a[][]){
		int L=a.length;
		int M=a[0].length;
		int[][] tm=new int[L][M];
		for (int i=0;i<L;i++)
			System.arraycopy(a[i],0,tm[i],0,M);
		return tm;
	}



	static int[] fight(int end,int start,int num,int[] val) {
		//log("fight from :"+start+" to "+end+" with #:"+num+"....");

		int res=0;
		int cur=start; 
		while (num>0 && cur<end) {
			num/=2;
			cur++;
			res+=val[cur]*num;
		}
		//log("....num:"+num+" cur:"+cur+" res:"+res);
		return new int[] {num,res};

	}
	static void process() throws Exception {

		//test();

		Locale.setDefault(Locale.US);
		out = new BufferedWriter(new OutputStreamWriter(System.out));
		reader = new InputReader(System.in);




		int n=reader.readInt();
		int m=reader.readInt();
		int[] a=new int[n];
		for (int i=0;i<n;i++)
			a[i]=reader.readInt()-1;
		int[] s=new int[n];
		for (int i=0;i<n;i++)
			s[i]=reader.readInt();
		int[] c=new int[n+m];
		for (int i=0;i<n+m;i++)
			c[i]=reader.readInt();

		int[] sub=new int[n];
		for (int i=0;i<n;i++) {
			for (int j=i+1;j<n;j++) {
				if (a[j]<=a[i])
					sub[i]++;
			}
		}

		// state
		// dp[last][k]
		// last accepted before
		// k what's happening if a provide a carry of k, on value last

		int IMPOSSIBLE=Integer.MIN_VALUE;
		int A=m;
		int B=n;
		int C=m;

		int[][]dp=new int[A][B];

		for (int i=0;i<A;i++)
			Arrays.fill(dp[i],IMPOSSIBLE);


		int[] mem=new int[m];

		for (int i=0;i<n;i++) {
			// can work with ag>=a[i]
			// we start with the existing ones
			//int[][] nxt=clone(dp);

			int x=a[i];

			int[] nxtx=new int[B];
			System.arraycopy(dp[x], 0, nxtx, 0, B);


			// case 1: we already had x as the last
			if (mem[x]==1) {
				for (int k=0;k<=sub[i];k++) {
					nxtx[k]=Math.max(nxtx[k],dp[x][k+1]+c[x]-s[i]);
				}
			}



			// case 2: introduce x as first ever
			nxtx[0]=Math.max(nxtx[0],c[x]-s[i]);
			//log("introducing :"+i+" with agg:"+x+" dp:"+dp[x][0]);
			for (int k=1;k<=sub[i];k++) {
				int[] tm=fight(n+m-1,x,k+1,c);
				nxtx[k]=Math.max(nxtx[k],tm[1]+c[x]-s[i]);
			}



			mem[x]=1;

			int LIM=14;
			
			// case 3 : we had y, with y>x

			// if y is big enough compared to x, this does not change
			// for instance y>x+12

			for (int y=x+1;y<x+LIM && y<m;y++) {
				if (mem[y]==1) {
					// want to compute nxt[a[i]][k]
					// first k=0
					nxtx[0]=Math.max(dp[y][0]+c[x]-s[i],nxtx[0]);
					// then others, we need to fight
					for (int k=1;k<=sub[i];k++) {
						int[] tm=fight(y,x,k+1,c);
						nxtx[k]=Math.max(nxtx[k],dp[y][tm[0]]+tm[1]+c[x]-s[i]);
					}
				}
			}
			//  ======== now for the big y
			int bob=IMPOSSIBLE;
			for (int y=x+LIM;y<m;y++) {
				
				if (mem[y]==1) {
					bob=Math.max(bob, dp[y][0]);
					
					nxtx[0]=Math.max(dp[y][0]+c[x]-s[i],nxtx[0]);
			
					
					
				}
			}
			
			if (bob!=IMPOSSIBLE)
			for (int k=1;k<=sub[i];k++) {
				int[] tm=fight(m,x,k+1,c);
				nxtx[k]=Math.max(nxtx[k],bob+tm[1]+c[x]-s[i]);
			}
			
			//=========== end big y
			
			


			dp[x]=nxtx;
		
		}
		int ans=IMPOSSIBLE;
		for (int i=0;i<n;i++) {
			ans=Math.max(ans, dp[a[i]][0]);
		}
		if (ans<0)
			ans=0;
		output(ans);


		try {
			out.close();
		} catch (Exception E) {
		}

	}

	public static void main(String[] args) throws Exception {
		process();

	}

	static final class InputReader {
		private final InputStream stream;
		private final byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;

		public InputReader(InputStream stream) {
			this.stream = stream;
		}

		private int read() throws IOException {
			if (curChar >= numChars) {
				curChar = 0;
				numChars = stream.read(buf);
				if (numChars <= 0) {
					return -1;
				}
			}
			return buf[curChar++];
		}

		public final String readString() throws IOException {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			StringBuilder res = new StringBuilder();
			do {
				res.append((char) c);
				c = read();
			} while (!isSpaceChar(c));
			return res.toString();
		}

		public final int readInt() throws IOException {
			int c = read();
			boolean neg = false;
			while (isSpaceChar(c)) {
				c = read();
			}
			char d = (char) c;
			// log("d:"+d);
			if (d == '-') {
				neg = true;
				c = read();
			}
			int res = 0;
			do {
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			// log("res:"+res);
			if (neg)
				return -res;
			return res;

		}

		public final long readLong() throws IOException {
			int c = read();
			boolean neg = false;
			while (isSpaceChar(c)) {
				c = read();
			}
			char d = (char) c;
			// log("d:"+d);
			if (d == '-') {
				neg = true;
				c = read();
			}
			long res = 0;
			do {
				res *= 10;
				res += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			// log("res:"+res);
			if (neg)
				return -res;
			return res;

		}

		private boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}
	}

}