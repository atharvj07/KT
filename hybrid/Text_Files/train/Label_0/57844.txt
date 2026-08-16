import java.io.*;
import java.util.*;

import static java.lang.Math.*;
import static java.util.Arrays.fill;
import static java.util.Arrays.binarySearch;
import static java.util.Arrays.sort;

public class Main {
	public static void main(String[] args) throws IOException {
		new Thread(null, new Runnable() {
			public void run() {
				try {
					try {
						if (new File("input.txt").exists())
							System.setIn(new FileInputStream("input.txt"));
					} catch (SecurityException e) {}
					new Main().run();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}, "1", 1L << 24).start(); 
	}

	BufferedReader in;
	PrintWriter out;
	StringTokenizer st = new StringTokenizer("");
	
	int N;
	int M;
	Item[] items;
	int[] map;
	
	void run() throws IOException {
		in = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		
		N = nextInt();
		M = N * 3;
		items = new Item [M];
		map = new int [M];
		
		for (int i = 0; i < M; i++) {
			items[i] = new Item(i, nextInt() - 1);
			map[items[i].num] = i;
		}
		
		Item[] input = new Item [M];
		Comparator<Item> cmp = new CmpId();
		for (int i = 0; i < N; i++) {
			input[3 * i + 0] = items[map[nextInt() - 1]];
			input[3 * i + 1] = items[map[nextInt() - 1]];
			input[3 * i + 2] = items[map[nextInt() - 1]];
			sort(input, 3 * i, 3 * i + 3, cmp);
		}
		
		int K = nextInt() - 1;
		
		for (int i = 0; i < N; i++) {
			if (input[3 * i + 0].num == K) {
				int a = input[3 * i + 1].num;
				int b = input[3 * i + 2].num;
				sort(input, 0, 3 * i + 3);
				int lst = -1;
				for (int j = 0; j < M; j++)
					if (input[j].num == a || input[j].num == b)
						lst = j;
				sort(input, lst + 1, M);
				boolean blank = false;
				for (int j = 0; j < M; j++) {
					if (input[j].num == K)
						continue;
					if (blank)
						out.print(' ');
					blank = true;
					out.print(input[j].num + 1);
				}
				break;
			} else if (input[3 * i + 1].num == K || input[3 * i + 2].num == K) {
				boolean blank = false;
				for (int j = 0; j < M; j++) {
					if (j == K)
						continue;
					if (blank)
						out.print(' ');
					blank = true;
					out.print(j + 1);
				}
				out.println();
				break;
			}
		}
		
		out.close();
	}
	
	class Item implements Comparable<Item> {
		int id;
		int num;
		
		Item(int id, int num) {
			this.id = id;
			this.num = num;
		}

		@Override
		public int compareTo(Item item) {
//			return id - item.id;
			return num - item.num;
		}
		
		@Override
		public String toString() {
			return "" + num;
		}
	}
	
	class CmpId implements Comparator<Item> {

		@Override
		public int compare(Item i1, Item i2) {
			return i1.id - i2.id;
		}
	}
	
	String nextToken() throws IOException {
		while (!st.hasMoreTokens()) {
			st = new StringTokenizer(in.readLine());
		}
		
		return st.nextToken();
	}
	
	int nextInt() throws IOException {
		return Integer.parseInt(nextToken());
	}
	
	long nextLong() throws IOException {
		return Long.parseLong(nextToken());
	}
	
	double nextDouble() throws IOException {
		return Double.parseDouble(nextToken());
	}
	
	String nextLine() throws IOException {
		st = new StringTokenizer("");
		return in.readLine();
	}
	
	boolean EOF() throws IOException {
		while (!st.hasMoreTokens()) {
			String s = in.readLine();
			
			if (s == null) {
				return true;
			}
			
			st = new StringTokenizer(s);
		}
		
		return false;
	}
}
