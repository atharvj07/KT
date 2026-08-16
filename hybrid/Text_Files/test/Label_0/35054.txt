import java.io.*;
import java.util.*;

public class Main{
	
	static int mod=(int)1e9+7;
	
	public static void main(String[] args) throws IOException {
		Writer out=new Writer(System.out);
		Reader in=new Reader(System.in);
		int ts=in.nextInt();
		outer: while(ts-->0) {	
		
			int n=in.nextInt();
			int a[]=in.readArray(n);
			int max=Integer.MIN_VALUE;
			for(int i=0; i<n; i++) {
				if(a[i]>max) {
					max=a[i];
				}
				
			}
			
			
			for(int i=0; i<n-1; i++) {
				if(a[i]==max && a[i+1]!=max) {
					out.println(i+1);
					continue outer;
				}
			}
			for(int i=n-1; i>=1; i--) {
				if(a[i]==max && a[i-1]!=max) {
					out.println(i+1);
					continue outer;
				}
			}
			
			out.println(-1);
		}
		out.close();		
		
	}
	
/*********************************** UTILITY CODE BELOW **************************************/	
		
	static boolean prime(int n) {
		for(int i=2; i*i<=n; i++) if(n%i==0) return false;
		return true;
	}
	
	static int abs(int a) {
		return a>0 ? a : -a;
	}
	
	static int max(int a, int b) {
		return a>b ? a : b;
	}
	
	static int min(int a, int b) {
		return a<b ? a : b;
	}
	
	static long pow(long n, long m) {
		if(m==0) return 1;
		long temp=pow(n,m/2);
		long res=((temp*temp)%mod);
		if(m%2==0) return res;
		return (res*n)%mod;
	}
	
	static class Pair{
		int u, v;
		
		Pair(int u, int v){this.u=u; this.v=v;}
		
		static void sort(Pair [] coll) {		
			List<Pair> al=new ArrayList<>(Arrays.asList(coll));
			Collections.sort(al,new Comparator<Pair>() {
				public int compare(Pair p1, Pair p2) {
					return p1.u-p2.u;
				}	
			});
			for(int i=0; i<al.size(); i++) {
				coll[i]=al.get(i);
			}
		}
		
	}
	
	static void sort(int[] a) {
		ArrayList<Integer> list=new ArrayList<>();
		for (int i:a) list.add(i);
		Collections.sort(list);
		for (int i=0; i<a.length; i++) a[i]=list.get(i);
	}
	
	static void sort(long a[]) {
		ArrayList<Long> list=new ArrayList<>();
		for(long i: a) list.add(i);
		Collections.sort(list);
		for(int i=0; i<a.length; i++) a[i]=list.get(i);
	}
	
	static int [] array(int n, int value) {	
		int a[]=new int[n];
		for(int i=0; i<n; i++) a[i]=value;
		return a;
	}
	
	static class Reader{
		
		BufferedReader br;
		StringTokenizer to;
		
		Reader(InputStream stream){
			br=new BufferedReader(new InputStreamReader(stream));
			to=new StringTokenizer("");
		}
		
		String next() {
			while(!to.hasMoreTokens()) {
				try {
					to=new StringTokenizer(br.readLine());	
				}catch(IOException e) {}
				
			}
			return to.nextToken();
			
		}
		
		int nextInt() {
			return Integer.parseInt(next());
		}
		
		long nextLong() {
			return Long.parseLong(next());
		}
		
		int [] readArray(int n) {
			int a[]=new int[n];
			for(int i=0; i<n ;i++) a[i]=nextInt();
			return a;
		}
		long [] readLongArray(int n) {
			long a[]=new long[n];
			for(int i=0; i<n ;i++) a[i]=nextLong();
			return a;
		}
		
	}
	
	static class Writer extends PrintWriter{
		Writer(OutputStream stream){
			super(stream);
		}
		void println(int [] array) {
			for(int i=0; i<array.length; i++) {
				print(array[i]+" ");
			}
			println();
		}
		void println(long [] array) {
			for(int i=0; i<array.length; i++) {
				print(array[i]+" ");
			}
			println();
		}
	}
	
}