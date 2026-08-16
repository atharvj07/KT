

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


@SuppressWarnings("unused")
public class A {
	public  static  FastScannerA scan = new FastScannerA();
	public static PrintWriter out = new PrintWriter(System.out);
	static void sort(int[] a) {
		ArrayList<Integer> l=new ArrayList<>();
		for (int i:a) l.add(i);
		Collections.sort(l);
		for (int i=0; i<a.length; i++) a[i]=l.get(i);
	}
	public static void solve () {
		int n=scan.nextInt();
		int m=scan.nextInt();
		 PriorityQueue<Integer> first = new PriorityQueue<Integer>(), second = new PriorityQueue<Integer>();
		for(int i=0;i<n;i++) {
			first.add(scan.nextInt());
		}
		for(int i=0;i<m;i++) {
			second.add(scan.nextInt());
		}
		
		while(!first.isEmpty() && !second.isEmpty()) {
			int a=first.peek(),b=second.poll();
			if(b>=a) first.poll();
		}
		//System.out.println(first);
		System.out.println(first.size());
	}
	public static void main(String[] args) {
		
		solve();
		out.close();
	}

}
class FastScannerA {
	BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
	StringTokenizer st= new StringTokenizer("");
	String next() {
		while (!st.hasMoreTokens())
			try {
				st=new StringTokenizer(br.readLine());
			} catch (IOException e) {
				e.printStackTrace();
			}
		return st.nextToken();
	}
	int nextInt() {
		return Integer.parseInt(next());
	}
	int[] readArray(int n) {
		int[] a=new int[n];
		for (int i=0; i<n; i++) a[i]=nextInt();
		return a;
	}
	long nextLong() {
		return Long.parseLong(next());
	}
	void sort(long[] a) {
		ArrayList<Long> l=new ArrayList<>();
		for (long i:a) l.add(i);
		Collections.sort(l);
		for (int i=0; i<a.length; i++) a[i]=l.get(i);
	}
	

	
}


