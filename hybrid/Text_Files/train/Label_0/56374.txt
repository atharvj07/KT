import java.io.*;
import java.math.*;
import java.util.*;

public class test {
	/*
	 * array list
	 * 
	 * ArrayList<Integer> al=new ArrayList<>(); creating BigIntegers
	 * 
	 * BigInteger a=new BigInteger(); BigInteger b=new BigInteger();
	 * 
	 * hash map
	 * 
	 * HashMap<Integer,Integer> hm=new HashMap<Integer,Integer>(); for(int
	 * i=0;i<ar.length;i++) { Integer c=hm.get(ar[i]); if(hm.get(ar[i])==null) {
	 * hm.put(ar[i],1); } else { hm.put(ar[i],++c); } }
	 * 
	 * while loop
	 * 
	 * int t=sc.nextInt(); while(t>0) { t--; }
	 * 
	 * array input
	 * 
	 * int n = sc.nextInt(); int ar[] = new int[n]; for (int i = 0; i < ar.length;
	 * i++) { ar[i] = sc.nextInt(); }
	 */

	static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() {
			while (st == null || !st.hasMoreElements()) {
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

		String nextLine() {
			String str = "";
			try {
				str = br.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			return str;
		}
	}

	static class Pair {
		int first, second;

		public Pair(int first, int second) {
			this.first = first;
			this.second = second;
		}

	}

	static class OutputWriter {
		private final PrintWriter writer;

		public OutputWriter(OutputStream outputStream) {
			writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
		}

		public OutputWriter(Writer writer) {
			this.writer = new PrintWriter(writer);
		}

		public void print(Object... objects) {
			for (int i = 0; i < objects.length; i++) {
				if (i != 0)
					writer.print(' ');
				writer.print(objects[i]);
			}
		}

		public void printLine(Object... objects) {
			print(objects);
			writer.println();
		}

		public void close() {
			writer.close();
		}

		public void flush() {
			writer.flush();
		}

	}

	private static final Scanner sc = new Scanner(System.in);
	private static final FastReader fs = new FastReader();
	private static final OutputWriter op = new OutputWriter(System.out);

	static int[] getintarray(int n) {
		int ar[] = new int[n];
		for (int i = 0; i < n; i++) {
			ar[i] = fs.nextInt();
		}
		return ar;
	}

	static long[] getlongarray(int n) {
		long ar[] = new long[n];
		for (int i = 0; i < n; i++) {
			ar[i] = fs.nextLong();
		}
		return ar;
	}

	static int[][] get2darray(int n, int m) {
		int ar[][] = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				ar[i][j] = fs.nextInt();
			}
		}
		return ar;
	}

	static Pair[] getpairarray(int n) {
		Pair ar[] = new Pair[n];
		for (int i = 0; i < n; i++) {
			ar[i] = new Pair(fs.nextInt(), fs.nextInt());
		}
		return ar;
	}

	static void printarray(int ar[]) {
		System.out.println(Arrays.toString(ar));
	}

	static boolean checkmyArray(int[] ar)

	{
		int temp = ar[0];
		for (int i = 1; i < ar.length; i++) {
			if (temp != ar[i])
				return false;
		}
		return true;
	}

	static int fact(int n) {
		int fact = 1;
		for (int i = 2; i <= n; i++) {
			fact *= i;
		}
		return fact;
	}

	public static void main(String[] args) {
//		int t = fs.nextInt();
		int t = 1;
		while (t > 0) {
			int n = fs.nextInt();
			if (n % 2 == 0)
				System.out.println("Mahmoud");
			else
				System.out.println("Ehab");

			t--;
		}
	}

}/*
	 * 1 5 -2 -3 -1 -4 -6till here
	 */
