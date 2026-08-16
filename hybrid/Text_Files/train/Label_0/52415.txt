import java.io.*;
import java.util.*;

public class E {

	static class Point {
		int x, y, id;

		public Point(int x, int y, int id) {
			this.x = x;
			this.y = y;
			this.id = id;
		}
	}

	static Comparator<Point> byAngle = new Comparator<E.Point>() {

		@Override
		public int compare(Point o1, Point o2) {
			return -Long.compare((long) o1.x * o2.y, (long) o2.x * o1.y);
		}
	};

	static Comparator<Point> byAngleRev = new Comparator<E.Point>() {

		@Override
		public int compare(Point o1, Point o2) {
			return Long.compare((long) o1.x * o2.y, (long) o2.x * o1.y);
		}
	};

	void submit() {
		int r = nextInt();
		int q = nextInt();

		int[][] qs = new int[q][3];
		int n = 0;

		for (int i = 0; i < q; i++) {

			qs[i][0] = nextInt();
			if (qs[i][0] == 1) {
				n++;
				qs[i][1] = nextInt();
				qs[i][2] = nextInt();
			} else if (qs[i][0] == 2) {
				qs[i][1] = nextInt() - 1;
			} else if (qs[i][0] == 3) {
				qs[i][1] = nextInt() - 1;
				qs[i][2] = nextInt() - 1;
			}
		}

		int[] xs, ys;

		Point[] px, py;

		int[] treeXIdx = new int[n];
		int[] askX;
		
		Point[] a;
		
		{
			a = new Point[n];
			int ptr = 0;
			for (int i = 0; i < q; i++) {
				if (qs[i][0] == 1) {
					a[ptr] = new Point(qs[i][1] - r, qs[i][2], ptr);
					ptr++;
				}
			}

			Arrays.sort(a, byAngle);

			for (int i = 0; i < n; i++) {
				treeXIdx[a[i].id] = i;
			}

			px = makeUnique(a, byAngle, false);
			xs = new int[n];

			for (Point p : a) {
				xs[p.id] = Arrays.binarySearch(px, p, byAngle);
			}

			askX = new int[px.length];
			askX[px.length - 1] = n;

			int pptr = px.length - 1;
			for (int i = n - 2; i >= 0; i--) {
				if ((long) a[i].x * a[i + 1].y != (long) a[i].y * a[i + 1].x) {
					askX[--pptr] = i + 1;
				}
			}

			if (pptr != 0) {
				throw new AssertionError();
			}
		}

		{
//			Point[] a = new Point[n];
			int ptr = 0;
			for (int i = 0; i < q; i++) {
				if (qs[i][0] == 1) {
					a[ptr] = new Point(qs[i][1] + r, qs[i][2], ptr);
					ptr++;
				}
			}

			py = makeUnique(a, byAngleRev, true);
			ys = new int[n];

			for (Point p : a) {
				ys[p.id] = Arrays.binarySearch(py, p, byAngleRev);
			}
		}

//		 System.err.println(Arrays.toString(xs));
//		 System.err.println(Arrays.toString(ys));

		int ptr = 0;

		root = new Node(0, n);

		for (int i = 0; i < q; i++) {
			if (qs[i][0] == 1) {
				root.set(treeXIdx[ptr], ys[ptr]);
				ptr++;
			} else if (qs[i][0] == 2) {
				int what = qs[i][1];
				root.set(treeXIdx[what], Integer.MAX_VALUE);
			} else if (qs[i][0] == 3) {
				int p1 = qs[i][1];
				int p2 = qs[i][2];

				int qx = Math.max(xs[p1], xs[p2]);
				int qy = Math.max(ys[p1], ys[p2]);

				if (isInside(px[qx], py[qy])) {
					out.println("NO");
					continue;
				}

				root.set(treeXIdx[p1], Integer.MAX_VALUE);
				root.set(treeXIdx[p2], Integer.MAX_VALUE);

				out.println(root.get(0, askX[qx]) > qy ? "YES" : "NO");

				root.set(treeXIdx[p1], ys[p1]);
				root.set(treeXIdx[p2], ys[p2]);
			}
		}
	}

	TreeSet<Integer>[] set;
	Node root;

	static class Node {
		int l, r;
		Node left, right;

		int val;

		public Node(int l, int r) {
			this.l = l;
			this.r = r;
			val = Integer.MAX_VALUE;

			if (r - l > 1) {
				int m = (l + r) >> 1;
				left = new Node(l, m);
				right = new Node(m, r);
			}
		}

		void set(int x, int y) {
			if (r - l == 1) {
				val = y;
				return;
			}
			(x < left.r ? left : right).set(x, y);
			val = Math.min(left.val, right.val);
		}

		int get(int ql, int qr) {
			if (ql <= l && r <= qr) {
				return val;
			}
			if (l >= qr || ql >= r) {
				return Integer.MAX_VALUE;
			}
			return Math.min(left.get(ql, qr), right.get(ql, qr));
		}
	}

	boolean isInside(Point vl, Point vr) {
		return (long) vl.x * vr.x + (long) vl.y * vr.y < 0;
	}

	Point[] makeUnique(Point[] a, Comparator<Point> cmp, boolean doSort) {
		a = a.clone();
		if (doSort) {
			Arrays.sort(a, cmp);
		}
		
		int sz = 1;
		for (int i = 1; i < a.length; i++) {
			if ((long) a[i].x * a[sz - 1].y != (long) a[i].y * a[sz - 1].x) {
				a[sz++] = a[i];
			}
		}
		return Arrays.copyOf(a, sz);
	}

	void preCalc() {

	}

	void stress() {

	}

	void test() {

	}

	E() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		preCalc();
		submit();
		// stress();
		// test();
		out.close();
	}

	static final Random rng = new Random();

	static int rand(int l, int r) {
		return l + rng.nextInt(r - l + 1);
	}

	public static void main(String[] args) throws IOException {
		new E();
	}

	BufferedReader br;
	PrintWriter out;
	StringTokenizer st;

	String nextToken() {
		while (st == null || !st.hasMoreTokens()) {
			try {
				st = new StringTokenizer(br.readLine());
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}
		return st.nextToken();
	}

	String nextString() {
		try {
			return br.readLine();
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}

	int nextInt() {
		return Integer.parseInt(nextToken());
	}

	long nextLong() {
		return Long.parseLong(nextToken());
	}

	double nextDouble() {
		return Double.parseDouble(nextToken());
	}
}
