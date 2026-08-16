import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		MyScanner sc = new MyScanner();
		PrintWriter out = new PrintWriter(System.out);
		int H = sc.nextInt();
		int W = sc.nextInt();
		char[][] grid = new char[H][];
		for (int i = 0; i < grid.length; i++) {
			grid[i] = sc.next().toCharArray();
		}
		short[][][][] max = new short[17][W][H][H];
		int tmp;
		for (int from2 = W-1; from2 >= 0; from2--) {
			for (int from1 = 0; from1 < H; from1++) {
				max[0][from2][from1][from1] = (short)(from2 + 1);
				if (from2 + 1 < W && grid[from1][from2] == grid[from1][from2 + 1]) {
					max[0][from2][from1][from1] = max[0][from2 + 1][from1][from1];
				}
			}
			for (int from1 = 0; from1 < H; from1++) {
				for (int to1 = from1 + 1; to1 < H; to1++) {
					max[0][from2][from1][to1] = (short)from2;
					if (grid[to1-1][from2] == grid[to1][from2]) {
						max[0][from2][from1][to1] = (short)Math.min(max[0][from2][from1][to1-1], max[0][from2][to1][to1]);
					}
				}
			}
		}
		for (int i = 1; i < 17; i++) {
			for (int from2 = 0; from2 < W; from2++) {
				for (int from1 = 0; from1 < H; from1++) {
					int med = from1;
					for (int to1 = from1; to1 < H; to1++) {
						tmp = max[i-1][from2][from1][to1];
						max[i][from2][from1][to1] = tmp < W ? max[i-1][tmp][from1][to1] : (short)W;
						int cur = med + 1 <= to1 ? Math.min(max[i-1][from2][from1][med], max[i-1][from2][med+1][to1]) : -1, next;
						while (med + 2 <= to1 && (next = Math.min(max[i-1][from2][from1][med+1], max[i-1][from2][med+2][to1])) >= cur) {
							med++;
							cur = next;
						}
						if (cur != -1) max[i][from2][from1][to1] = (short)Math.max(max[i][from2][from1][to1], cur);
					}
				}
			}
		}
		int ans;
		for (ans = 0; ans < 17; ans++) {
			if (max[ans][0][0][H-1] >= W) break;
		}
		out.println(ans);
		
		out.flush();
	}
	
	static class MyScanner {
		private BufferedReader br;
		private StringTokenizer tokenizer;
		
		public MyScanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}
		
		public String next() {
			while (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					tokenizer = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			return tokenizer.nextToken();
		}
		
		public int nextInt() {
			return Integer.parseInt(next());
		}
		
		public long nextLong() {
			return Long.parseLong(next());
		}
	}
}
