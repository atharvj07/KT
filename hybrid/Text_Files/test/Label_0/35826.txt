import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Map.Entry;

import java.util.Random;
import java.util.TreeSet;

public final class CF_714_D2_E
{


	static boolean verb=true;
	static void log(Object X){if (verb) System.err.println(X);}
	static void log(Object[] X){if (verb) {for (Object U:X) System.err.print(U+" ");System.err.println("");}}
	static void log(int[] X){if (verb) {for (int U:X) System.err.print(U+" ");System.err.println("");}}
	static void logWln(int[] X){if (verb) {for (int U:X) System.err.print(U+" ");}}
	static void log(int[] X,int L){if (verb) {for (int i=0;i<L;i++) System.err.print(X[i]+" ");System.err.println("");}}
	static void log(long[] X){if (verb) {for (long U:X) System.err.print(U+" ");System.err.println("");}}

	static void logWln(Object X){if (verb) System.err.print(X);}
	static void info(Object o){	System.out.println(o);}
	static void output(Object o){outputWln(""+o+"\n");	}
	static void outputFlush(Object o){try {out.write(""+ o+"\n");out.flush();} catch (Exception e) {}}
	static void outputWln(Object o){try {out.write(""+ o);} catch (Exception e) {}}


	static void logBin(int[] tm) {for (int x:tm) logWln(bin(8,x)+" ");log("");}

	static String bin(int L,int x) {
		String s=Integer.toBinaryString(x);
		while (s.length()<L) s="0"+s;
		return s;
	}

	static long powerMod(long b,long e,long m){
		long x=1;
		while (e>0) {
			if (e%2==1)
				x=(b*x)%m;
			b=(b*b)%m;
			e=e/2;
		}
		return x; 
	}



	static long mod=1000000007;



	// Global vars
	static BufferedWriter out;
	static InputReader reader;




	static void process() throws Exception {


		//log(Integer.toBinaryString(200001).length());
		out = new BufferedWriter(new OutputStreamWriter(System.out));
		reader = new InputReader(System.in);
		//log("done");
		//test();

		int NX=100001;
		log("computing");
		long[] fact=new long[NX];
		fact[0]=1;
		long[] invFact=new long[NX];
		invFact[0]=1;

		for (int i=1;i<NX;i++) {
			fact[i]=fact[i-1]*i;
			if (fact[i]>=mod)
				fact[i]%=mod;
			invFact[i]=powerMod(fact[i],mod-2,mod);
		}
		log("done");

		int n=reader.readInt();

		int[] a=new int[n];
		long sum=0;
		for (int i=0;i<n;i++) {
			a[i]=reader.readInt();
			sum+=a[i];
		}
		log("sum:"+sum);
		long ans=0;
		// need to take care of special case where locnt==1 or hicnt==1
		//
		if (sum%n==0) {

			long med=sum/n;
			log("med:"+med);
			Arrays.parallelSort(a);
			int prev=-1;
			int cn=0;
			ArrayList<Integer> lonb=new ArrayList<Integer>();
			ArrayList<Integer> hinb=new ArrayList<Integer>();
			int locnt=0;
			int hicnt=0;

			for (int i=0;i<n;i++) {
				//log("i:"+a[i]);
				if (a[i]==prev) {
					cn++;
				} else {
					if (prev!=-1) {
						if (prev<med) {
							lonb.add(cn);
							locnt+=cn;
						} else if (prev>med) {
							hinb.add(cn);
							hicnt+=cn;
						}
					}
					prev=a[i];
					cn=1;

				}
				if (i==n-1) {
					if (a[i]>med) {
						hinb.add(cn);
						hicnt+=cn;
					}
				}
			}
			long big=fact[hicnt];
			for (int x:hinb) {
				big*=invFact[x];
				if (big>=mod)
					big%=mod;
			}
			log("big:"+big);
			long small=fact[locnt];
			for (int x:lonb) {
				small*=invFact[x];
				if (small>=mod)
					small%=mod;
			}
			log("small:"+small);

			int medcnt=n-hicnt-locnt;
			if (medcnt==n) {
				ans=1;
			} else 
			if (locnt==1 ||hicnt==1) {
				// can put anywhere
				log("special case");
				ans=fact[n];
				for (int x:lonb) {
					ans*=invFact[x];
					if (ans>=mod)
						ans%=mod;
				}
				for (int x:hinb) {
					ans*=invFact[x];
					if (ans>=mod)
						ans%=mod;
				}
			
				ans*=invFact[medcnt];
				ans%=mod;
			}  else {

				ans=big;
				ans*=small;
				ans%=mod;
				ans*=2;
				ans%=mod;
				if (medcnt>0) {
					ans*=fact[n];
					ans%=mod;
					ans*=invFact[medcnt];
					ans%=mod;
					ans*=invFact[n-medcnt];
					ans%=mod;
				}

				// we insert small in some position in big
				// there are hicnt+1 position
			}
		}

		output(ans);






		try {
			out.close();
		} catch (Exception Ex) {
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

		public final String readString(int L) throws IOException {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			StringBuilder res = new StringBuilder(L);
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