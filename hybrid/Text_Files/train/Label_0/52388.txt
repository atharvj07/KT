import java.util.*;
import java.io.*;
import java.awt.geom.*;
import java.math.*;

public class Main implements Runnable {

	static final Scanner in = new Scanner(System.in);
	static final PrintWriter out = new PrintWriter(System.out,false);
	static boolean debug = false;

	static int[][][] undirectedGraph(int n, int[] v1, int[] v2, int[] cost) {
		int[] cnt = new int[n];
		for (int i : v1) cnt[i]++;
		for (int i : v2) cnt[i]++;

		int[][][] g = new int[n][][];
		for (int i=0; i<n; i++) g[i] = new int[cnt[i]][2];
		for (int i=0; i<v1.length; i++) {
			int s = v1[i];
			int t = v2[i];

			g[s][--cnt[s]][0] = t;
			g[s][cnt[s]][1] = cost[i];

			g[t][--cnt[t]][0] = s;
			g[t][cnt[t]][1] = cost[i];
		}

		return g;
	}

	static ArrayList<Integer> articularionPoint(int[][][] g) {
		int n = g.length;
		int[] low = new int[n];
		int[] ord = new int[n];
		Arrays.fill(ord, -1);
		ArrayList<Integer> res = new ArrayList<>();

		for (int cur=0; cur<n; cur++) {
			if (ord[cur] == -1) {
				dfsAP(g, cur, low, ord, new int[]{0}, res);
			}
		}

		res = new ArrayList<>(new HashSet<>(res));
		Collections.sort(res);

		return res;
	}

	static void dfsAP(int[][][] g, int cur, int[] low, int[] ord, int[] p, ArrayList<Integer> res) {
		low[cur] = ord[cur] = p[0]++;
		for (int[] to : g[cur]) {
			int next = to[0];
			if (ord[next] == -1) {
				dfsAP(g, next, low, ord, p, res);
				low[cur] = Math.min(low[cur], low[next]);
				if ((ord[cur] == 0 && ord[next] != 1) || (ord[cur] != 0 && low[next] >= ord[cur])) {
					res.add(cur);
				}
			} else {
				low[cur] = Math.min(low[cur], ord[next]);
			}
		}
	}

	public void run() {
		int v = in.nextInt();
		int e = in.nextInt();
		int[] s = new int[e];
		int[] t = new int[e];
		int[] c = new int[e];
		for (int i=0; i<e; i++) {
			s[i] = in.nextInt();
			t[i] = in.nextInt();
			c[i] = 0;
		}

		int[][][] g = undirectedGraph(v, s, t, c);
		ArrayList<Integer> ans = articularionPoint(g);
		for (int i=0; i<ans.size(); i++) {
			out.println(ans.get(i));
		}

		out.flush();
		in.close();
		out.close();
	}

	public static void main(String[] args) {
		new Thread(null, new Main(), "", 16 * 1024 * 1024).start();
	}

	static void dump(Object... o) { if (debug) System.err.println(Arrays.deepToString(o)); }
}