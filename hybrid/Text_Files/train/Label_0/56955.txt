import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.math.BigInteger;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Random;
import java.util.TreeSet;

public final class CF_542_D1_C
{


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


	static long pgcd(long a,long b){
		if (a<b)
			return pgcd(b,a);
		while (b!=0){
			long c=b;
			b=a%b;
			a=c;
		}
		return a;
	}

	static int time;
	static int[] visited;

	// inclusive

	static void test(){

		log("testing");
		int NTESTS=1000;

		Random r=new Random();
		for (int t=0;t<NTESTS;t++){

		}
		log("testing done");
	}

	static int ln2max(int x){
		int res=1;
		for (;(1 << res) <=x;res++);
		res--;
		return res;

	}


	
	// Global vars
	static BufferedWriter out;
	static InputReader reader;

	static int MX=Integer.MAX_VALUE;

	static void process() throws Exception {

		//test();

		out = new BufferedWriter(new OutputStreamWriter(System.out));
		reader = new InputReader(System.in);

		int k=reader.readInt();
		
		long VX=1000001;
		long NX=2001;
		if (k<VX/2){
			output("3");
			output(0+" "+(-k)+" "+(2*k));
		} else {
			log("case 2");
			loop:for (long A=Math.max(100, k/(VX-1));A<NX;A++){
				{
					long w=k/A;
					long c=k%A;
					//log("b:"+b+" c:"+c);
					for (int e=1;e<w;e++){
						long b=w+e;
						long rem=b*A-k;
						//log("rem:"+rem+" A:"+A);
						for (long B=2;B<A;B++){
							//log("B:"+B+" rem%B:"+rem%B);
							if (rem%B==0){
								//log("step 2");
								long a=rem/B;
								if (a>b){
									//log("step 3");
									// total on B elements must be a
									// total on A elements must be b
									log(k+" "+(A*b-B*a));
									long diff=a-b;
									long delta=A-B;
									if (delta*(VX-1)>=diff){
										if (a<=(VX-1)*B){
											long[] ar=new long[(int)A];
											int st=0;
											long item=diff/delta;
											if (item==0)
												item=1;
											for (int i=0;i<delta;i++){
													long bob=Math.min(diff,item);
													ar[(int)delta-1-st]=-bob;
													st++;
													diff-=bob;
													
												
											}
											
											for (int i=0;i<B;i++){
												long bob=Math.min(a,VX-1);
												a-=bob;
												ar[st++]=bob;
											}
										
											
											// check
											
											boolean bad=false;
											for (int i=0;i<A;i++){
												if (Math.abs(ar[i])>=VX){
													bad=true;
													break;
												}
											}
											
											if (!bad){
												output(A);
												for (int i=0;i<A;i++){
													outputWln(ar[i]+" ");
												}
												output("");
											
												
											
											long sum=0;
											for (long x:ar)
												sum+=x;
											
											long ssum=0;
											for (int i=0;i<B;i++){
												ssum+=ar[(int)A-1-i];
											}
											
											if (A*sum-B*ssum!=k)
												log("Error");
											else
												log("ok");
											
											
											break loop;
											}
										}
									}
								}
							}
						}
						
					}
				}
				
			}
		}

		try {
			out.close();
		} catch (Exception e) {
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