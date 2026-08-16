/*
javac d.java && java d
*/

import java.io.*;
import java.util.*;

public class d {
	public static void main(String[] args) { new d(); }
	FS in = new FS();
	PrintWriter out = new PrintWriter(System.out);

	int n, m, k;	

	d() {
		n = in.nextInt();
		m = in.nextInt();
		k = in.nextInt();

		int roads = (4 * n * m - 2 * n - 2 * m);
		
		if (roads < k) out.println("NO");
		else {
			// this yucky stuff yeet
			out.println("YES");

			int x = 0, y = 0;
			// 0 <= x < n
			// 0 <= y < m
			
			int ptr = 0;
			
			int v = 0;
			int h = 0;

			char[] use = {'L', 'R', 'U', 'D'};
			int[][] dir = new int[3000][2];
			
			int ret = 0;
			while (k > 0) {
				int mv;
				if (x == 0) {
					if (v == 0 && h == 0) {
						if (m == 1) {
							h = 1;
							continue;
						}
						mv = min(k, m - 1);
						y += mv;
						k -= mv;

						dir[ptr++] = new int[]{mv, 1};
						v ^= 1;
					continue;
					}
					else if (v == 1) {
						mv = min(k, m - 1);
						y -= mv;
						k -= mv;

						dir[ptr++] = new int[]{mv, 0};
						v ^= 1;
						h ^= 1;
					continue;
					}
					else if (h == 1) {
						if (n == 1) {
							h = 0;
							continue;
						}
						mv = 1;
						x++;
						k--;

						dir[ptr++] = new int[]{1, 3};
						h ^= 1;
					continue;
					}
				}
				if (x < n - 1) {
					if (v == 0 && h == 0) {
						if (m == 1) {
							h = 1;
							continue;
						}
						mv = min(k, m - 1);
						y += mv;
						k -= mv;

						dir[ptr++] = new int[]{mv, 1};
						v ^= 1;
					continue;
					}
					else if (v == 1) {
						mv = min(k, m - 1);
						y -= mv;
						k -= mv;

						dir[ptr++] = new int[]{mv, 0};
						v ^= 1;
						h ^= 1;
					continue;
					}
					else if (h == 1) {
						if (n == 1) {
							h = 0;
							continue;
						}
						mv = 1;
						x++;
						k--;

						dir[ptr++] = new int[]{1, 3};
						h ^= 1;
					continue;
					}
				}


				if (x == n - 1) {
					if (v == 0 && h == 0) {
						if (m == 1) {
							h = 1;
							continue;
						}

						mv = 1;
						y++;
						k--;

						dir[ptr++] = new int[]{1, 1};
						
						h ^= 1;
					continue;
					}
					else if (v == 1) {
						if (m == 1) {
							v = 0;
							continue;
						}
						mv = min(k, m - 1);
						y -= mv;
						k -= mv;

						dir[ptr++] = new int[]{mv, 0};
						h = 1;
						v ^= 1;
					continue;
					}
					else if (h == 1 && ret == 0) {
						if (n == 1) {
							h = 0;
							continue;
						}
						mv = min(k, n - 1);
						k -= mv;

						dir[ptr++] = new int[]{mv, 2};
						ret ^= 1;
					continue;
					}
					else if (h == 1 && ret == 1) {
						mv = min(k, n - 1);
						k -= mv;

						dir[ptr++] = new int[]{mv, 3};
						ret = 0;
						
						h ^= 1;
						if (y == m - 1) 
							v ^= 1;
					continue;
					}
				}
			}

			out.println(ptr);
			for (int i = 0; i < ptr; i++)
				out.println(dir[i][0] + " " + use[dir[i][1]]);
		}
		out.close();
	}

	
	
	int abs(int x) { return x < 0 ? -x : x; }
	long abs(long x) { return x < 0 ? -x : x; }
	double abs(double x) { return x < 0 ? -x : x; }
	int min(int x, int y) { return x < y ? x : y; }	
	int max(int x, int y) { return x > y ? x : y; }
	long min(long x, long y) { return x < y ? x : y; }	
	long max(long x, long y) { return x > y ? x : y; }
	double min(double x, double y) { return x < y ? x : y; }
	double max(double x, double y) { return x > y ? x : y; }
	int gcd(int x, int y) { while (y > 0) { x = y^(x^(y = x)); y %= x; } return x; }
	long gcd(long x, long y) { while (y > 0) { x = y^(x^(y = x)); y %= x; } return x; }
	long lcm(int x, int y) { return ((long) x / gcd(x, y)) * y; }
	long lcm(long x, long y) { return (x / gcd(x, y)) * y; }

	void sort(int[] arr) {
		int sz = arr.length, j;
		Random r = new Random();
		for (int i = 0; i < sz; i++) {
			j = r.nextInt(i + 1);
			arr[i] = arr[j]^(arr[i]^(arr[j] = arr[i]));
		} Arrays.sort(arr);
	}

	class FS {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer("");
		String next() {
			while (!st.hasMoreTokens()) {
				try { st = new StringTokenizer(br.readLine()); }
				catch (Exception e) {}
			} return st.nextToken();
		}
		int nextInt() { return Integer.parseInt(next()); }
		long nextLong() { return Long.parseLong(next()); }
		double nextDouble() { return Double.parseDouble(next()); }
	}
}
