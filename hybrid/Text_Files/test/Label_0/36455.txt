import java.math.*;
import java.io.*;
import java.util.*;

public class Solution {
	static long[] a;
	static int max;
	public static void main(String[] args) throws IOException{
		FastScanner sc = new FastScanner(System.in);
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = sc.nextInt();
		while (t-->0) {
			int n = sc.nextInt();
			max= 0 ;
			a = new long[n];
			for (int i=0;i<n ;i++ ) {
				a[i] = sc.nextLong();
			}
			for (int i=1;i<=n ;i++ ) {
				doit(i,1);
			}
			bw.write(max+"\n");
		}
		bw.close();
	}
	static void doit(int n, int p){
		//if(n>=a.length) return;
		max = Math.max(max, p);
		for (int i=2;i*n<=a.length ;i++ ) {
			if (a[i*n-1]>a[n-1]) {
				doit(i*n,p+1);
			}
		}
	}
	static class Pair implements Comparable<Pair>{
		long a;
		long b;
		public Pair(long c, long d){
			a = c;
			b = d;
		}
		public int compareTo(Pair p){
			return (int)(a-p.a);
		}
	}
	static int gcd(int a, int b){
	    if(b==0) return a;
	    return gcd(b,a%b);
	}
	static long power(long a, long b, long c){
	    if(b==0) return 1L;
	    if(b==1) return a;
	    long temp = power(a, b/2, c);
	    if(b%2==0) return (temp*temp)%c;
	    else return (((temp*temp)%c)*a)%c;
	}
	static class FastScanner {
		BufferedReader br;
		StringTokenizer st;
		FastScanner(File f) {
			try {
				br = new BufferedReader(new FileReader(f));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}
		FastScanner(InputStream f) {
			br = new BufferedReader(new InputStreamReader(f));
		}
		String nextLine() {
			try {
				return br.readLine();
			} catch (IOException e) {
				return null;
			}
		}
		String next() {
			while (st == null || !st.hasMoreTokens()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}
		int nextInt() {
			return Integer.parseInt(next());
		}
		long nextLong() {
			return Long.parseLong(next());
		}
		double nextDouble() {
			return Double.parseDouble(next());
		}
	}
}