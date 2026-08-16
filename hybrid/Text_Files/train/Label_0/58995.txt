// practice with rainboy
import java.io.*;
import java.util.*;

public class CF888G {
	static final int INF = 0x3fffffff, L = 30;
	static int[][] vv;
	static int n_;
	static int update(int v, int a, int b) {
		if (v == 0)
			v = ++n_;
		if (b != 0) {
			int c = (a & b) == 0 ? 0 : 1;
			vv[v][c] = update(vv[v][c], a, b >> 1);
		}
		return v;
	}
	static long ans;
	static int dfs2(int u, int v, int b) {
		if (u == 0 || v == 0)
			return INF;
		if (b == 0)
			return 0;
		int u0 = vv[u][0];
		int u1 = vv[u][1];
		int v0 = vv[v][0];
		int v1 = vv[v][1];
		int a00 = dfs2(u0, v0, b >> 1);
		int a11 = dfs2(u1, v1, b >> 1);
		int a = Math.min(a00, a11);
		if (a == INF) {
			int a01 = dfs2(u0, v1, b >> 1);
			int a10 = dfs2(u1, v0, b >> 1);
			a = b | Math.min(a01, a10);
		}
		return a;
	}
	static void dfs1(int v, int b) {
		if (v == 0 || b == 0)
			return;
		int v0 = vv[v][0];
		int v1 = vv[v][1];
		int w = dfs2(v0, v1, b >> 1);
		if (w != INF)
			ans += b | w;
		dfs1(v0, b >> 1);
		dfs1(v1, b >> 1);
	}
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		vv = new int[n * (L + 1)][2];
		int v = 0;
		while (n-- > 0) {
			int a = sc.nextInt();
			v = update(v, a, 1 << 29);
		}
		dfs1(v, 1 << 29);
		System.out.println(ans);
	}
}
