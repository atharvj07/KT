import java.util.*;
import java.io.*;
public class Main
{


	/************************ SOLUTION STARTS HERE ***********************/


	static final long p[] = { (long) (1e9) + 9L , (long) (1e9) + 23L};  		 // mod1
	static final long x[] = {46399 , 18757}; 				   // base1

	static long sub(long a, long b , long mod) {return ((a % mod) - (b % mod) + mod) % mod;}
	static long mul(long a, long b , long mod) {return ((a % mod) * (b % mod)) % mod;}
	static long add(long a, long b , long mod) {return ((a % mod) + (b % mod)) % mod;}
	static long modPow(long a, long b , long mod) { // squared exponentiation
		if (b == 0L || a == 1L)
			return 1L;
		else if (b == 1L)
			return a;
		else {
			if ((b & 1L) == 0L) // Checking whether b is even (fast)
				return modPow((a * a) % mod, b >> 1 , mod);
			else
				return (a * modPow((a * a) % mod, b >> 1 , mod)) % mod;
		}
	}


	@SuppressWarnings("unchecked")
	private static void solve(FastScanner s1, PrintWriter out){

		char str1[] = s1.nextLine().toCharArray();
		char str2[] = s1.nextLine().toCharArray();

		int N = str1.length;
		int M = str2.length;

		int maxLen = 0;
		outer:
			for(int len = Math.min(N,M);len >= 1;len--) {

				long rollHash1[] = new long[2];
				for(int i=0;i<len;i++)
					for(int j=0;j<2;j++)
						rollHash1[j] = add(rollHash1[j], modPow(x[j], str1[i] - 'a', p[j]), p[j]);

				HashSet<Long> set[] = new HashSet[2];
				for(int j=0;j<2;j++) {
					set[j] = new HashSet<>();
					set[j].add(rollHash1[j]);
				}

				for(int i=len;i < N;i++) {
					for(int j=0;j<2;j++) {
						rollHash1[j] = sub(rollHash1[j], modPow(x[j], str1[i - len] - 'a', p[j]), p[j]);
						rollHash1[j] = add(rollHash1[j], modPow(x[j], str1[i] - 'a', p[j]), p[j]);
						set[j].add(rollHash1[j]);
					}
				}

				long rollHash2[] = new long[2];
				for(int i=0;i<len;i++)
					for(int j=0;j<2;j++)
						rollHash2[j] = add(rollHash2[j], modPow(x[j], str2[i] - 'a', p[j]), p[j]);

				if(set[0].contains(rollHash2[0]) && set[1].contains(rollHash2[1])) {
					// out.println(set);
					// out.println("hash " + rollHash2);
					maxLen = len;
					break;
				}

				for(int i=len;i<M;i++) {
					for(int j=0;j<2;j++) {
						rollHash2[j] = sub(rollHash2[j], modPow(x[j], str2[i - len] - 'a', p[j]), p[j]);
						rollHash2[j] = add(rollHash2[j], modPow(x[j], str2[i] - 'a', p[j]), p[j]);
					}
					if(set[0].contains(rollHash2[0]) && set[1].contains(rollHash2[1])) {
						// out.println(set);
						// out.println("hash " + rollHash2);
						maxLen = len;
						break outer;
					}
				}

			}

		out.println(maxLen);

	}



	/************************ SOLUTION ENDS HERE ************************/





	/************************ TEMPLATE STARTS HERE *********************/

	public static void main(String []args) throws IOException {
		FastScanner in  = new FastScanner(System.in);
		PrintWriter out = 
				new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)), false); 
		solve(in, out);
		in.close();
		out.close();
	}    

	static class FastScanner{
		BufferedReader reader;
		StringTokenizer st;
		FastScanner(InputStream stream){reader=new BufferedReader(new InputStreamReader(stream));st=null;}	
		String next()
		{while(st == null || !st.hasMoreTokens()){try{String line = reader.readLine();if(line == null){return null;}		    
		st = new StringTokenizer(line);}catch (Exception e){throw new RuntimeException();}}return st.nextToken();}
		String nextLine()  {String s=null;try{s=reader.readLine();}catch(IOException e){e.printStackTrace();}return s;}	    	  	
		int    nextInt()   {return Integer.parseInt(next());}
		long   nextLong()  {return Long.parseLong(next());}		
		double nextDouble(){return Double.parseDouble(next());}
		char   nextChar()  {return next().charAt(0);}
		int[]  nextIntArray(int n)         {int[] a= new int[n];   int i=0;while(i<n){a[i++]=nextInt();}  return a;}
		long[] nextLongArray(int n)        {long[]a= new long[n];  int i=0;while(i<n){a[i++]=nextLong();} return a;}	
		int[]  nextIntArrayOneBased(int n) {int[] a= new int[n+1]; int i=1;while(i<=n){a[i++]=nextInt();} return a;}	    	
		long[] nextLongArrayOneBased(int n){long[]a= new long[n+1];int i=1;while(i<=n){a[i++]=nextLong();}return a;}	    	
		void   close(){try{reader.close();}catch(IOException e){e.printStackTrace();}}				
	}

	/************************ TEMPLATE ENDS HERE ************************/
}