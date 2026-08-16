import static java.lang.Math.*;
import static java.util.Arrays.*;
import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) {
		try {
			String packageName = new Main().getClass().getPackage().getName();
			System.setIn(new FileInputStream("src/" + packageName + "/input.txt"));
			// System.setOut(new PrintStream(new FileOutputStream("src/" + packageName + "/result.txt")));
		} catch (FileNotFoundException e) {
		} catch (NullPointerException e) {
		}
		new Main().run();
	}

	void tr(Object... os) {
		System.err.println(deepToString(os));
	}

	Scanner sc;
	void run() {
		sc = new Scanner(System.in);
		int t = sc.nextInt();
		while (t --> 0) solve();

	}
	void solve() {
		int n = sc.nextInt() + 1;
		int m = sc.nextInt();

		int sa = sc.nextInt();
		int sb = sc.nextInt();

		ArrayList<ArrayList<E>> g = new ArrayList<ArrayList<E>>();
		for (int i = 0; i < n; i++) g.add(new ArrayList<E>());

		for (int i = 0; i < m; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int t = sc.next().charAt(0);
			g.get(a).add(new E(b, t));
			g.get(b).add(new E(a, t));
		}

		int ans = inf;

		int[] fromGoal = dijk(g, 0, true);
		int[] fromCat = dijk(g, sb, true);
		int[] fromMan = dijk(g, sa, false);

		if (fromCat[0] == 0) ans = 0;
		else
			for (int i = 0; i < n; i++) {
				ans = min(ans, fromGoal[i] + fromCat[i] + fromMan[i]);
			}

		System.out.println(ans);
	}

	int inf = Integer.MAX_VALUE / 5;

	int[] dijk(ArrayList<ArrayList<E>> g, int s, boolean strict) {
		int n = g.size();
		int[] res = new int[n];
		fill(res, inf - 1);
		res[s] = 0;
		PriorityQueue<Tupple> q = new PriorityQueue<Tupple>();
		q.add(new Tupple(0, s));
		while (!q.isEmpty()) {
			int cost = q.peek().a;
			int here  = q.peek().b;
			q.poll();

			if (cost != res[here]) continue;

			for (E e : g.get(here)) {
				int ncost = 0;
				if (strict)
				{
					if (cost == 0 && e.type == 'L') ncost = 0;
					else if (cost > 0 && e.type == 'L') ncost = inf;
					else ncost = 1;
				}
				else
				{
					if (e.type == 'L') ncost = inf;
					else ncost = 1;
				}
				ncost += cost;
				if (res[e.to] > ncost) {
					res[e.to] = ncost;
					q.add(new Tupple(ncost, e.to));
				}
			}
		}
		return res;
	}

	class Tupple implements Comparable<Tupple> {
		int a, b;

		public int compareTo(Tupple o) {
			if (a != o.a) return a < o.a ? -1 : 1;
			if (b != o.b) return b < o.b ? -1 : 1;
			return 0;
		}

		public Tupple(int a, int b) {
			this.a = a;
			this.b = b;
		}

	}

	class E {
		public E(int to, int type) {
			this.to = to;
			this.type = type;
		}
		int to;
		int type;
	}

}