
// Problem : A. Battlefield
// Contest : Codeforces - Codeforces Round #117 (Div. 2)
// URL : https://codeforces.com/contest/182/problem/A
// Memory Limit : 256 MB
// Time Limit : 2000 ms
// Powered by CP Editor (https://github.com/cpeditor/cpeditor)

import java.io.*;
import java.util.*;
import java.util.stream.*;

public class a implements Runnable{
	
    public static void main(String[] args) {
        new Thread(null, new a(), "process", 1<<26).start();
    }
	public void run() {
		FastReader scan = new FastReader();
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
		//PrintWriter out = new PrintWriter("file.out");
		Task solver = new Task();
		//int t = scan.nextInt();
		int t = 1;
		for(int i = 1; i <= t; i++) solver.solve(i, scan, out);
		out.close();
	}

	static class Task {
		static final int inf = Integer.MAX_VALUE;

		public void solve(int testNumber, FastReader sc, PrintWriter pw) {
			//CHECK FOR QUICKSORT TLE
			//***********************//
			//CHECK FOR INT OVERFLOW
			//***********************//
			int a = sc.nextInt();
			int b = sc.nextInt();
			int ax = sc.nextInt();
			int ay = sc.nextInt();
			int bx = sc.nextInt();
			int by = sc.nextInt();
			int tr = sc.nextInt();
			int[][] tren = new int[tr + 2][4];
			for(int i = 0; i < tr; i++) {
				for(int j = 0; j < 4; j++) {
					tren[i][j] = sc.nextInt();
				}
				if(tren[i][2] < tren[i][0]) {
					int temp = tren[i][2];
					tren[i][2] = tren[i][0];
					tren[i][0] = temp;
				}
				if(tren[i][3] < tren[i][1]) {
					int temp = tren[i][3];
					tren[i][3] = tren[i][1];
					tren[i][1] = temp;
				}
			}
			tren[tr][0] = ax;
			tren[tr][1] = ay;
			tren[tr][2] = ax;
			tren[tr][3] = ay;
			tren[tr+1][0] = bx;
			tren[tr+1][1] = by;
			tren[tr+1][2] = bx;
			tren[tr+1][3] = by;
			List<tup>[] adjl = Stream.generate(ArrayList::new).limit(tr + 2).toArray(List[]::new);
			for(int i = 0; i < tr + 2; i++) {
				for(int j = i + 1; j < tr + 2; j++) {
					double wei = inf;
					if(tren[i][0] >= tren[j][0] && tren[i][0] <= tren[j][2] ||
					tren[i][2] >= tren[j][0] && tren[i][2] <= tren[j][2] ||
					tren[i][2] >= tren[j][2] && tren[i][0] <= tren[j][0]) {
						wei = Math.min(Math.abs(tren[i][1] - tren[j][1]), Math.abs(tren[i][1] - tren[j][3]));
						wei = Math.min(wei, Math.abs(tren[i][3] - tren[j][3]));
						wei = Math.min(wei, Math.abs(tren[i][3] - tren[j][1]));
					}
					else if(tren[i][1] >= tren[j][1] && tren[i][1] <= tren[j][3] ||
					tren[i][3] >= tren[j][1] && tren[i][3] <= tren[j][3] ||
					tren[i][3] >= tren[j][3] && tren[i][1] <= tren[j][1]) {
						wei = Math.min(Math.abs(tren[i][0] - tren[j][2]), Math.abs(tren[i][0] - tren[j][2]));
						wei = Math.min(wei, Math.abs(tren[i][2] - tren[j][2]));
						wei = Math.min(wei, Math.abs(tren[i][2] - tren[j][0]));
					}
					else {
						wei = Math.min(dist(tren[i][0], tren[i][1], tren[j][0], tren[j][1]), dist(tren[i][0], tren[i][1], tren[j][2], tren[j][3]));
						wei = Math.min(wei, dist(tren[i][2], tren[i][3], tren[j][2], tren[j][3]));
						wei = Math.min(wei, dist(tren[i][2], tren[i][3], tren[j][0], tren[j][1]));
					}
					if(wei <= a) {
						adjl[i].add(new tup(j, wei));
						adjl[j].add(new tup(i, wei));
					}
				}
			}
			for(int i = 0; i < tr + 2; i++) {
				for(tup c : adjl[i]) {
					//pw.println(i + " " + c.a + " " + c.b);
				}
			}
			int[] djik = new int[tr + 2];
			double ans = inf; 
			Arrays.fill(djik, inf);
			PriorityQueue<tup2> pq = new PriorityQueue<>();
			pq.add(new tup2(tr, 0));
			while(!pq.isEmpty()) {
				tup2 c = pq.poll();
				for(tup x : adjl[c.a]) {
					if(djik[x.a] > c.b + 1) {
						djik[x.a] = c.b + 1;
						pq.add(new tup2(x.a, djik[x.a]));
					}
					if(x.a == tr + 1) {
						ans = Math.min(c.b * (a + b) + x.b, ans);
					}
				}
			}
			if(ans == inf) {
				pw.println(-1);return;
			}
			pw.println(ans);
		}
		double dist(int a, int b, int c, int d) {
			return Math.sqrt((c-a-0l)*(c-a) + (d-b-0l) * (d-b));
		}
	}
	static long binpow(long a, long b, long m) {
		a %= m;
		long res = 1;
		while (b > 0) {
			if ((b & 1) == 1)
				res = res * a % m;
			a = a * a % m;
			b >>= 1;
		}
		return res;
	}
	static void sort(int[] x){
		shuffle(x);
		Arrays.sort(x);
	}
	static void sort(long[] x){
		shuffle(x);
		Arrays.sort(x);
	}
	static class tup implements Comparable<tup>{
		int a;double b;
		tup(int a,double b){
			this.a=a;
			this.b=b;
		}
		@Override
		public int compareTo(tup o){
			return Double.compare(b,o.b);
		}
	}
	static class tup2 implements Comparable<tup2>{
		int a;int b;
		tup2(int a,int b){
			this.a=a;
			this.b=b;
		}
		@Override
		public int compareTo(tup2 o){
			return Integer.compare(b,o.b);
		}
	}
	static void shuffle(int[] a) {
		Random get = new Random();
		for (int i = 0; i < a.length; i++) {
			int r = get.nextInt(i + 1);
			int temp = a[i];
			a[i] = a[r];
			a[r] = temp;
		}
	}

	static void shuffle(long[] a) {
		Random get = new Random();
		for (int i = 0; i < a.length; i++) {
			int r = get.nextInt(i + 1);
			long temp = a[i];
			a[i] = a[r];
			a[r] = temp;
		}
	}

	static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		public FastReader(String s) throws FileNotFoundException {
			br = new BufferedReader(new FileReader(new File(s)));
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

}