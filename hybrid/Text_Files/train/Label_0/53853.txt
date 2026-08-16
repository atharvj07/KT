import java.io.*;
import java.util.*;

public class F {
	FastScanner in;
	PrintWriter out;

	int n, m;

	class Segment {
		int l, r;
		int num;

		public Segment(int l, int r, int num) {
			super();
			this.l = l;
			this.r = r;
			this.num = num;
		}
	}

	final int ITEM_OPEN = 0, ITEM_CLOSE = 1;
	final int BAG_OPEN = 2, BAG_CLOSE = 3;

	class Event implements Comparable<Event> {
		int num;
		int x;
		int type;

		public Event(int x, int num, int type) {
			super();
			this.x = x;
			this.num = num;
			this.type = type;
		}

		@Override
		public int compareTo(Event o) {
			if (x != o.x)
				return Integer.compare(x, o.x);
			if (type != o.type)
				return Integer.compare(type, o.type);
			return Integer.compare(num, o.num);
		}
	}

	int[] c;

	long ans = 0;
	int ansitem = -1, ansbag = -1;

	void solve() {
		ArrayList<Event> events = new ArrayList<>();
		n = in.nextInt();
		m = in.nextInt();
		Segment[] item = new Segment[n];
		Segment[] bags = new Segment[m];
		for (int i = 0; i < n; i++) {
			item[i] = new Segment(in.nextInt(), in.nextInt(), i);
			Event e1 = new Event(item[i].l, i, ITEM_OPEN);
			Event e2 = new Event(item[i].r, i, ITEM_CLOSE);
			events.add(e1);
			events.add(e2);
		}
		c = new int[m];
		for (int i = 0; i < m; i++) {
			bags[i] = new Segment(in.nextInt(), in.nextInt(), i);
			Event e1 = new Event(bags[i].l, i, BAG_OPEN);
			Event e2 = new Event(bags[i].r, i, BAG_CLOSE);
			c[i] = in.nextInt();
			events.add(e1);
			events.add(e2);
		}
		Collections.sort(events);
		TreeSet<Segment> whole = new TreeSet<>(new Comparator<Segment>() {

			@Override
			public int compare(Segment o1, Segment o2) {
				return Integer.compare(o1.l, o2.l);
			}
		});
		int maxR = Integer.MIN_VALUE;
		int itemi = -1;
		for (Event e : events) {
			if (e.type == BAG_OPEN) {
				if (maxR >= bags[e.num].r) {
					long cur = bags[e.num].r - bags[e.num].l;
					cur *= c[e.num];
					if (cur > ans) {
						ans = cur;
						ansitem = itemi;
						ansbag = e.num;
					}
				}
			} else if (e.type == ITEM_OPEN) {
				if (item[e.num].r > maxR) {
					maxR = item[e.num].r;
					itemi = e.num;
				}
			}
		}
		for (Event e : events) {
			if (e.type == BAG_CLOSE) {
				Segment s = new Segment(bags[e.num].l - 1, bags[e.num].l - 1, -1);
				Segment seg = whole.higher(s);
				if (seg != null) {
					long cur = (seg.r - seg.l);
					cur *= c[e.num];
					if (ans < cur) {
						ans = cur;
						ansbag = e.num;
						ansitem = seg.num;
					}
				}
			} else if (e.type == ITEM_CLOSE) {
				Segment toAdd = item[e.num];
				Segment seg = whole.ceiling(toAdd);
				if (seg == null
						|| seg.r - seg.l < toAdd.r - toAdd.l) {
					while (true) {
						Segment prev = whole.floor(toAdd);
						if (prev != null && prev.r - prev.l < toAdd.r - toAdd.l) {
							whole.remove(prev);
						} else {
							break;
						}
					}
					whole.add(toAdd);		
				}
			}
		}

		{
			int p = 0;
			int sz = events.size();
			while (p < sz && events.get(p).type != ITEM_OPEN)
				p++;
			for (int i = 0; i < sz; i++) {
				Event e = events.get(i);
				if (e.type == BAG_CLOSE) {
					while (p < sz) {
						int num = events.get(p).num;
						if (item[num].r > bags[e.num].r)
							break;
						p++;
						while (p < sz && events.get(p).type != ITEM_OPEN) {
							p++;
						}
					}
					if (p != sz) {
						Segment seg = item[events.get(p).num];
						long len = bags[e.num].r - Math.max(bags[e.num].l, seg.l);
						long cur = len * c[e.num];
						if (cur > ans) {
							ans = cur;
							ansbag = e.num;
							ansitem = seg.num;
						}
					}
				}
			}
		}
		
		
		{
			int sz = events.size();
			int p = sz - 1;
			while (p >= 0 && events.get(p).type != ITEM_CLOSE)
				p--;
			for (int i = sz - 1; i >= 0; i--) {
				Event e = events.get(i);
				if (e.type == BAG_OPEN) {
					while (p >= 0) {
						int num = events.get(p).num;
						if (item[num].l < bags[e.num].l)
							break;
						p--;
						while (p >= 0 && events.get(p).type != ITEM_CLOSE) {
							p--;
						}
					}
					if (p != -1) {
						Segment seg = item[events.get(p).num];
						long len = Math.min(bags[e.num].r, seg.r) - bags[e.num].l;
						long cur = len * c[e.num];
						if (cur > ans) {
							ans = cur;
							ansbag = e.num;
							ansitem = seg.num;
						}
					}
				}
			}
		}

		out.println(ans);
		if (ans != 0) {
			out.println((ansitem + 1) + " " + (ansbag + 1));
		}
	}

	void run() {
		in = new FastScanner();
		out = new PrintWriter(System.out);

		solve();

		out.close();
	}

	class FastScanner {
		BufferedReader br;
		StringTokenizer st;

		public FastScanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() {
			while (st == null || !st.hasMoreTokens()) {
				try {
					st = new StringTokenizer(in.br.readLine());
				} catch (IOException e) {
					// TODO Auto-generated catch block
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

		double nextDouble() {
			return Double.parseDouble(next());
		}
	}

	public static void main(String[] args) {
		new F().run();
	}
}