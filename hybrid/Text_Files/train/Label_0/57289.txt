import java.util.*;
import java.io.*;


public class hello {
	public static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException  e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		public int nextInt() {
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
	public static FastReader sc = new FastReader();
	public static void take_array(long arr[], int size) {
		for (int i = 0; i < size; i++) {
			arr[i] = sc.nextLong();
		}
	}
	public static void print_arr(long arr[]) {
		for (long x : arr)
			System.out.print(x + " ");
	}
	public static String[] convert_String_to_arr(String s) {
		String arr[] = new String[s.length()];
		for (int i = 0; i < s.length(); i++) {
			arr[i] = String.valueOf(s.charAt(i));
		}
		return arr;
	}
	public static void take_prefix_array(long arr[], int size, long []prefix) {
		long temp = 0;
		for (int i = 0; i < size; i++) {
			temp += arr[i];
			prefix[i] = temp;
		}
	}
	public static void print(Object c, int a) {
		if (a == -1)
			System.out.print(c + " ");
		else
			System.out.println(c);
	}
	public static void space() {
		System.out.println();
	}
	public static void swap(int a, int b) {
		int temp = a;
		a = b;
		b = temp;
	}
	public static void max_pillows(int beds, int pillows, int index) {
		int len = 0;
		int Sirana = 1;
		pillows -= beds;
		while (((len <= index - 1) || len <= (beds - index)) && pillows >= Math.min(len, beds - index) + Math.min(len, index - 1) + 1) {
			pillows -= Math.min(len, beds - index) + Math.min(len, index - 1) + 1;
			len++;
			Sirana++;
		}
		Sirana += pillows / beds;
		print(Sirana, 0);
	}
	public static void main(String []args) {
		int beds = sc.nextInt();
		int pillows = sc.nextInt();
		int index = sc.nextInt();
		max_pillows(beds, pillows, index);
	}
}