import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Scanner;

class Main {
	public static void main(String[] args) throws IOException {
		new Main().run();

	}

	class P implements Comparable<P> {
		int xl1;
		int xu1;
		int f;

		public P(int xl1, int xu1, int f) {
			this.xl1 = xl1;
			this.xu1 = xu1;
			this.f = f;
		}

		@Override
		public int compareTo(P o) {
			return Integer.compare(xl1, o.xl1);
		}
	}

	void solve(int n, long[][] xl, long[][] xu) {
		// xl[i][0]????°?????????????????????????.
		// f(x):=?¬????????????????xl[i][0]??????xl[*][1]????°???????xu[*][1]???x??\?????§?????????????????????????????§???
		// xl[i][0]?????????????????¨??????
		// f(xu[i][0])+1????±????,xl[i][1]????????§??????xl[*][0]?????????????????¨??????f(xu[i][1])???????????????
		SegTree seg = new SegTree(1_000_000);
		PriorityQueue<P> pq = new PriorityQueue<>();
		for (int i = 0; i < n; ++i) {
			while (!pq.isEmpty() && pq.peek().xl1 < xl[i][0]) {
				P p = pq.poll();
				seg.setVal(p.xu1, p.f);
			}
			int f = (int) seg.query(0, (int) xu[i][0]) + 1;
			pq.add(new P((int) xl[i][1], (int) xu[i][1], f));
		}
		while (!pq.isEmpty()) {
			P p = pq.poll();
			seg.setVal(p.xu1, p.f);
		}
		System.out.println(seg.query(0, seg.n));
	}

	void run() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[][] xl = new long[n][2];
		long[][] xu = new long[n][2];
		ArrayList<Long> tmp = new ArrayList<>();
		for (int i = 0; i < n; ++i) {
			xl[i][0] = sc.nextLong();
			xl[i][1] = sc.nextLong();
			xu[i][0] = sc.nextLong();
			xu[i][1] = sc.nextLong();
			tmp.add(xl[i][0]);
			tmp.add(xl[i][1]);
			tmp.add(xu[i][0]);
			tmp.add(xu[i][1]);
		}
		Collections.sort(tmp);
		for (int i = 0; i < tmp.size(); ++i) {
			while (i + 1 < tmp.size() && tmp.get(i) == tmp.get(i + 1)) {
				tmp.remove(i + 1);
			}
		}
		HashMap<Long, Integer> numbering = new HashMap<>();
		for (int i = 0; i < tmp.size(); ++i) {
			numbering.put(tmp.get(i), i);
		}

		for (int i = 0; i < n; ++i) {
			xl[i][0] = numbering.get(xl[i][0]);
			xl[i][1] = numbering.get(xl[i][1]);
			xu[i][0] = numbering.get(xu[i][0]);
			xu[i][1] = numbering.get(xu[i][1]);
		}
		long[][] a = new long[n][4];
		for (int i = 0; i < n; ++i) {
			a[i][0] = xl[i][0];
			a[i][1] = xl[i][1];
			a[i][2] = xu[i][0];
			a[i][3] = xu[i][1];
		}

		Arrays.sort(a, new Comparator<long[]>() {
			@Override
			public int compare(long[] o1, long[] o2) {
				return Long.compare(o1[0], o2[0]);
			}
		});

		for (int i = 0; i < n; ++i) {
			xl[i][0] = a[i][0];
			xl[i][1] = a[i][1];
			xu[i][0] = a[i][2];
			xu[i][1] = a[i][3];
		}
		solve(n, xl, xu);
	}

	class SegTree {
		int n = 1;
		long[] val;

		public SegTree(int n) {
			while (this.n < n)
				this.n *= 2;
			val = new long[2 * this.n - 1];
		}

		void setVal(int k, int v) {
			k += n - 1;
			val[k] = Math.max(v, val[k]);
			while (k > 0) {
				k = (k - 1) / 2;
				val[k] = Math.max(val[2 * k + 1], val[2 * k + 2]);
			}
		}

		long query(int a, int b) {
			return query(a, b, 0, n, 0);
		}

		// [a,b)?±????????????????
		// [l,r)?????¨?????????
		long query(int a, int b, int l, int r, int k) {
			if (b <= l || r <= a) {
				return 0;
			} else if (a <= l && r <= b) {
				return val[k];
			} else {
				long vl = query(a, b, l, (l + r) / 2, 2 * k + 1);
				long vr = query(a, b, (l + r) / 2, r, 2 * k + 2);
				return Math.max(vl, vr);
			}
		}
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}