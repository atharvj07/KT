import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class D {
	private static BufferedReader in;
	private static StringTokenizer st;
	private static PrintWriter out;

	public static void main(String[] args) throws NumberFormatException, IOException {
		in = new BufferedReader(new InputStreamReader(System.in));
		st= new StringTokenizer("");
		out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
		int n = nextInt();
		int l = nextInt();
		int x = nextInt();
		int y = nextInt();
		int a[] = new int [n];
		for (int i = 0; i < n; i++) {
			a[i] = nextInt();
		}
		boolean X = false;
		boolean Y = false;
		for (int i = 0; i < n; i++) {
			int ind = Arrays.binarySearch(a, a[i]+x);
			if(ind >= 0){
				X = true;
			}
			ind = Arrays.binarySearch(a,a[i]+y);
			if(ind >= 0){
				Y = true;
			}
		}
		if(X && Y){
			System.out.println(0);
			return;
		}
		for (int i = 0; i < n; i++) {
			int ind = Arrays.binarySearch(a, a[i]+x+y);
			if(ind >= 0){
				System.out.println(1);
				System.out.println(a[i]+x);
				return;
			}
		}
		for (int i = 0; i < n; i++) {
			int ind = Arrays.binarySearch(a, a[i] + y - x);
			if(ind >= 0){
				if(a[i] - x >=0){
					System.out.println(1);
					System.out.println(a[i]-x);
					return;
				}
				if(a[i] + y <=l){
					System.out.println(1);
					System.out.println(a[i]+y);
					return;
				}
			}
		}
		ArrayList<Integer> list = new ArrayList<>();
		if(!X){
			for (int i = 0; i < n; i++) {
				if(a[i] - x >= 0){
					list.add(a[i]-x);
					X = true;
					break;
				}
				if(a[i] + x <= l){
					list.add(a[i]+x);
					X = true;
					break;
				}
			}
		}
		if(!Y){
			for (int i = 0; i < n; i++) {
				if(a[i] - y >= 0){
					list.add(a[i]-y);
					Y = true;
					break;
				}
				if(a[i] + y <= l){
					list.add(a[i]+y);
					Y = true;
					break;
				}
			}
		}
		if(!X && !Y){
			list.add(0);
			list.add(x);
			list.add(y);
		}else{
			if(!X){
				list.add(0);
				list.add(x);
			}
			if(!Y){
				list.add(0);
				list.add(y);
			}
		}
		System.out.println(list.size());
		for (int i : list) {
			System.out.print(i+" ");
		}
		out.close();
	}

	private static double nextDouble() throws NumberFormatException, IOException {
		return Double.parseDouble(next());
	}

	private static long nextLong() throws NumberFormatException, IOException {
		return Long.parseLong(next());
	}

	private static int nextInt() throws NumberFormatException, IOException {
		return Integer.parseInt(next());
	}

	private static String next() throws IOException {
		while(!st.hasMoreTokens())
			st = new StringTokenizer(in.readLine());
		return st.nextToken();
	}
}
