import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

/** @see http://d.hatena.ne.jp/komiyam/20120402/1333373895 */
public class Main {
	Scanner sc = new Scanner(System.in);

	int INF = 1 << 28;
	double EPS = 1e-12;

	int n, q;
	int[] ps;
	int[] queryType, queryNode;

	void run() {
		for (;;) {
			n = sc.nextInt();
			q = sc.nextInt();
			if ((n | q) == 0) {
				break;
			}
			ps = new int[n];
			for (int i = 1; i < n; i++) {
				ps[i] = sc.nextInt() - 1;
			}
			queryType = new int[q];
			queryNode = new int[q];
			for (int i = 0; i < q; i++) {
				queryType[i] = sc.next().charAt(0) == 'M' ? 0 : 1;
				queryNode[i] = sc.nextInt() - 1;
			}
			solve();
		}
	}

	class Heap {
		Heap l, r;
		int val;

		Heap(int _val) {
			val = _val;
		}

		int top() {
			return val;
		}

		Heap push(int val) {
			return meld(this, new Heap(val));
		}

		Heap pop() {
			return meld(l, r);
		}
	}

	Heap meld(Heap a, Heap b) {
		if (a == null)
			return b;
		if (b == null)
			return a;
		// if (a.val > b.val)
		if (-a.val > -b.val)
			return meld(b, a);
		a.r = meld(a.r, b);
		Heap t = a.l;
		a.l = a.r;
		a.r = t;
		// swap(a.l, a.r);
		return a;
	}

	class V extends ArrayList<V> {
		Heap h;
		int id,state;
		int markedTime;
		ArrayList<Integer> askedTimes = new ArrayList<Integer>();

		V(int _id) {
			id = _id;
		}
	}

	long ans;

	Heap rec(V v) {
		// vが答えになる
		Heap h = null;
		for (int t : v.askedTimes) {
			h = meld(h, new Heap(t));
		}
		for (V u : v) {
			h = meld(h, rec(u));
		}
		for (; h != null && h.top() > v.markedTime; h = h.pop()) {
			ans += v.id;
			// debug("vid",v.id);
		}
		return h;
	}

	void solve() {
		ans = 0;
		V[] vs = new V[n];
		for (int i = 0; i < n; i++) {
			vs[i] = new V(i + 1);
			vs[i].markedTime = INF;
		}
		// root = 1(0)
		for (int i = 1; i < n; i++) {
			// ps[i]
			vs[ps[i]].add(vs[i]);
		}
		vs[0].markedTime = -1;
		for (int i = 0; i < q; i++) {
			int v = queryNode[i], tick = i + 1;
			if (queryType[i] == 0) {
				// mark
				vs[v].markedTime = min(vs[v].markedTime, tick);
			} else {
				// query
				vs[v].askedTimes.add(tick);
			}
		}

		ps = null;
		queryNode = null;
		queryType = null;

		Stack<V> stackV = new Stack<V>();

		stackV.push(vs[0]);

		for (; !stackV.isEmpty();) {
			V v = stackV.pop();
			if (v.state == 0) {
				// 最初
				for (int t : v.askedTimes) {
					v.h = meld(v.h, new Heap(t));
				}
				stackV.push(v);
				v.state=1;
				for (V u : v) {
					stackV.push(u);
				}
			} else {
				// さいき＼(^o^)／
				for (V u : v) {
					v.h = meld(v.h, u.h);
				}
				for (; v.h != null && v.h.top() > v.markedTime; v.h = v.h.pop()) {
					ans += v.id;
				}
			}
		}
		
		System.gc();

		println(ans + "");
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}

	void print(String s) {
		System.out.print(s);
	}

	void println(String s) {
		System.out.println(s);
	}

	public static void main(String[] args) {
		new Main().run();
	}
}