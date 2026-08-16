import java.util.*;
import java.awt.Point;
import java.io.*;
public class Solutions {

	static FastScanner scr=new FastScanner();
	static PrintStream out;
	static ArrayList<ArrayList<Integer>>list=new ArrayList<ArrayList<Integer>>();
	public static void main(String[] args) {
		out = new PrintStream(System.out);
		int n=read();
		int m=read();
		int k=read();
		TreeSet<Point>ts=new TreeSet<>(new Comparator<Point>() {
//			@Override
			public int compare(Point a,Point b) {
				 int diff=b.x-a.x;
				 return (diff==0)?(a.y-b.y):diff;
			}
		});
		for(int i=1;i<=n;i++) {
			int a=read();
			ts.add(new Point(a,i));
		}
		Iterator<Point>it=ts.iterator();
		
		TreeSet<Integer>index=new TreeSet<Integer>();
		long sum=0;
		for(int i=0;i<k*m;i++) {
			Point p=it.next();
			index.add(p.y);
			sum+=p.x;
		}
		System.out.println(sum);
		Iterator<Integer>itr=index.iterator();
		for(int l=1;l<k;l++) {
			int last=-1;
			for(int i=0;i<m;i++) {
				last=itr.next();
			}
			System.out.print(last+" ");
		}
		
	}
	static  int read() {
		return scr.nextInt();
	}
	static class FastScanner {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer("");
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
	}
	static int MAX=Integer.MAX_VALUE;
	static int MIN=Integer.MIN_VALUE;
}class Triplet{
	int first;
	int second;
	int third;
	Triplet(int fisrt,int second,int third){
		this.first=fisrt;
		this.second=second;
		this.third=third;
	}
}
class pair{
	long x=0;
	int y=0;
	pair(long first,int second){
		this.x=first;
		this.y=second;
	}
}
	