import java.util.*;
import java.io.*;

public class File {
	public static class FastScanner {
		BufferedReader br;
		StringTokenizer st;
		
		public FastScanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}
		
		String next() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				}
				catch (IOException e) {
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
	}
	
	public static void main(String[] args) {
		FastScanner sc = new FastScanner();
		PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
		
		
		
		int m = sc.nextInt();
		int n = sc.nextInt();
		
		boolean onEdge = false;
		
		int[][] grid = new int[m][n];
		for (int r = 0; r < m; r++) {
			for (int c = 0; c < n; c++) {
				grid[r][c] = sc.nextInt();
				
				if (grid[r][c] == 1) {
					if (r == 0 || r == m-1 || c == 0 || c == n-1) {
						onEdge = true;
					}
				}
			}
		}
		
		if (onEdge) {
			out.println(2);
		}
		else {
			out.println(4);
		}
		
		out.close();
	}		
}






















