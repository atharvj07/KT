import java.io.*;
import java.util.*;

public class CF716D {
	static class E {
		int u, v, w;
		E(int u, int v, int w) {
			this.u = u;
			this.v = v;
			this.w = w;
		}
	}
	static class V {
		ArrayList<E> list = new ArrayList<>();
		int i, d;
		V(int i) {
			this.i = i;
		}
	}
	static void setw(ArrayList<E> list0, int w, int k) {
		int i = 0;
		for (E e : list0)
			e.w = i++ < k ? w + 1 : w;
	}
	static int dijkstra(V[] vv, int s, int t, int INF) {
		for (int i = 0; i < vv.length; i++)
			vv[i].d = INF;
		TreeSet<V> q = new TreeSet<>((u, v) -> u.d != v.d ? u.d - v.d : u.i - v.i);
		vv[s].d = 0;
		q.add(vv[s]);
		while (!q.isEmpty()) {
			V u = q.first();
			q.remove(u);
			if (u == vv[t])
				return u.d;
			for (E e : u.list) {
				V v = vv[e.u + e.v - u.i];
				int d = Math.min(u.d + e.w, INF);
				if (v.d > d) {
					q.remove(v);	// if (q.contains(v))
					v.d = d;
					q.add(v);
				}
			}
		}
		return INF;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int L = Integer.parseInt(st.nextToken());
		int s = Integer.parseInt(st.nextToken());
		int t = Integer.parseInt(st.nextToken());
		V[] vv = new V[n];
		for (int i = 0; i < n; i++)
			vv[i] = new V(i);
		ArrayList<E> list = new ArrayList<>();
		ArrayList<E> list0 = new ArrayList<>();
		int m0 = 0;
		while (m-- > 0) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			E e = new E(u, v, w);
			vv[u].list.add(e);
			vv[v].list.add(e);
			list.add(e);
			if (w == 0) {
				list0.add(e);
				m0++;
			}
		}
		setw(list0, 1, 0);
		int d = dijkstra(vv, s, t, L + 1);
		if (d > L) {
			System.out.println("NO");
			return;
		}
		setw(list0, L + 1, 0);
		d = dijkstra(vv, s, t, L + 1);
		if (d < L) {
			System.out.println("NO");
			return;
		}
		if (m0 > 0) {
			long lower = 1 * m0 - 1, upper = (long) (L + 1) * m0, wk;
			int w, k;
			while (upper - lower > 1) {
				wk = (lower + upper) / 2;
				w = (int) (wk / m0);
				k = (int) (wk % m0);
				setw(list0, w, k);
				d = dijkstra(vv, s, t, L + 1);
				if (d < L)
					lower = wk;
				else if (d >= L)
					upper = wk;
			}
			wk = upper;
			w = (int) (wk / m0);
			k = (int) (wk % m0);
			setw(list0, w, k);
		}
		PrintWriter pw = new PrintWriter(System.out);
		pw.println("YES");
		for (E e : list)
			pw.println(e.u + " " + e.v + " " + e.w);
		pw.close();
	}
}
