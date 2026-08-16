import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		PrintWriter pw = new PrintWriter(System.out);
		int h = sc.nextInt(), w = sc.nextInt(), k = sc.nextInt(), x1 = sc.nextInt() - 1, y1 = sc.nextInt() - 1,
				x2 = sc.nextInt() - 1, y2 = sc.nextInt() - 1;
		char[][] grid = new char[h][];
		for (int i = 0; i < grid.length; i++) {
			grid[i] = sc.next().toCharArray();
		}
		int[][] dist = new int[h][w];
		for (int[] x : dist)
			Arrays.fill(x, -1);
		Queue<int[]> q = new LinkedList<int[]>();
		q.add(new int[] { x1, y1 });
		dist[x1][y1] = 0;
		int[] dx = { 0, 0, -1, 1 };
		int[] dy = { 1, -1, 0, 0 };
		while (!q.isEmpty()) {
			int[] cur = q.poll();
			int curdist = dist[cur[0]][cur[1]];
			for (int j = 0; j < 4; j++) {
				for (int i = 1; i <= k; i++) {
					int nxtx = cur[0] + i * dx[j];
					int nxty = cur[1] + i * dy[j];
					if (nxtx >= h || nxtx < 0 || nxty < 0 || nxty >= w || grid[nxtx][nxty] == '@')
						break;
					if (dist[nxtx][nxty] == curdist + 1)
						continue;
					if (dist[nxtx][nxty] != -1)
						break;
					dist[nxtx][nxty] = curdist + 1;
					q.add(new int[] { nxtx, nxty });
				}
			}
		}
		pw.println(dist[x2][y2]);
		pw.close();
	}

	static class Scanner {
		BufferedReader br;
		StringTokenizer st;

		public Scanner(InputStream s) {
			br = new BufferedReader(new InputStreamReader(s));
		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}

		public int[] nextIntArr(int n) throws IOException {
			int[] arr = new int[n];
			for (int i = 0; i < n; i++) {
				arr[i] = Integer.parseInt(next());
			}
			return arr;
		}

	}

}
