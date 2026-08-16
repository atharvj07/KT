import java.util.*;
import java.math.*;
import java.io.*;

public class CF320E {
	class CHT {
		class Line {
			long m, b;  double left = Long.MIN_VALUE;
			public Line(long mm, long x, long y) {
				m = mm;  b = -m * x + y;
			}
			public Line(long mm, long bb) {
				m = mm;  b = bb;
			}
			long eval(long x) { return m * x + b; }
			double inter(Line x) { return (double) (x.b - b) / (double) (m - x.m); }
		}
		TreeSet<Line> hull;
		int type;  boolean query = false;
		Comparator<Line> cmp = new Comparator<Line>() {
			public int compare(Line a, Line b) {
				if(!query) return type * Long.compare(a.m, b.m);
				if(a.left == b.left) return Long.compare(a.m, b.m);
				return Double.compare(a.left, b.left);
			}
		};
		public CHT(int tt) { type = tt;  hull = new TreeSet<>(cmp); }
		void add(long m, long b) { add(new Line(m, b)); }
		void add(Line a) {
			Line[] LR =  { hull.lower(a), hull.ceiling(a) };
			for(int i = 0 ; i < 2 ; i++) {
				if(LR[i] != null && LR[i].m == a.m) {
					if(type == 1 && LR[i].b >= a.b) return;
					if(type == -1 && LR[i].b <= a.b) return;
					remove(LR[i]);
				}
			}
			hull.add(a);
			Line L = hull.lower(a), R = hull.higher(a);
			if(L != null && R != null && a.inter(R) <= R.left) {
				remove(a);
				return;
			}
			Line LL = (L != null) ? hull.lower(L) : null;
			Line RR = (R != null) ? hull.higher(R) : null;
			if(L != null) a.left = a.inter(L);
			if(R != null) R.left = a.inter(R);
			while(LL != null && L.left >= a.inter(LL)) {
				remove(L);
				a.left = a.inter(L = LL);
				LL = hull.lower(L);
			}
			while(RR != null && R.inter(RR) <= a.inter(RR)) {
				remove(R);
				RR.left = a.inter(R = RR);
				RR = hull.higher(R);
			}
		}
		long query(long x) {
			Line tmp = new Line(0, 0, 0);
			tmp.left = x;  query = true;
			long res = (long) hull.floor(tmp).eval(x);
			query = false;  return res;
		}
		void remove(Line x) { hull.remove(x); }
		int size() { return hull.size(); }
	}
		public CF320E() {
			FS scan = new FS();
			int n = scan.nextInt();
			int[] height = new int[n];
			int[] cost = new int[n];
			for(int i = 0 ; i < n ; i++)
				height[i] = scan.nextInt();
			for(int i = 0 ; i < n ; i++)
				cost[i] = scan.nextInt();
			CHT hull = new CHT(-1);
			hull.add(cost[0], 0);
			for(int i = 1 ; i < n - 1 ; i++)
				hull.add(cost[i], hull.query(height[i]));
			System.out.println(hull.query(height[n - 1]));
		}
		class FS {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			StringTokenizer st = new StringTokenizer("");
			public String next() {
				while(!st.hasMoreTokens()) {
					try { st = new StringTokenizer(br.readLine()); }
					catch(Exception e) { e.printStackTrace(); }
				}
				return st.nextToken();
			}
			public int nextInt() { return Integer.parseInt(next()); }
		}
		public static void main(String[] args) { new CF320E(); }
	}
