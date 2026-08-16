import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.*;

/*2A*/

public class Main {
	public static void main(String[] args) throws Exception {
		Main mainClass = new Main();
	}

	BufferedReader in;
	PrintWriter out;
	StringTokenizer st;

	public String next() throws Exception {
		if (st == null || !st.hasMoreTokens()) {
			st = new StringTokenizer(in.readLine());
		}
		return st.nextToken();
	}

	public int nextInt() throws Exception {
		return Integer.parseInt(next());
	}

	public double nextDouble() throws Exception {
		return Double.parseDouble(next());
	}

	public long nextLong() throws Exception {
		return Long.parseLong(next());
	}

	public Main() throws Exception {
		in = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(new OutputStreamWriter(System.out));

		solve();
		out.close();
	}
	final static double eps = 1e-9;

	static class Point {
		double x, y;
		Point(double _x, double _y) {
			x = _x; y = _y;
		}
		double times(Point o) {
			return this.x * o.y - this.y * o.x;
		}
		double dot(Point o) {
			return x*o.x + y*o.y;
		}
		Point minus(Point o) {
			return new Point(x - o.x, y - o.y);
		}
		double theta() {
			return Math.atan2(y, x);
		}
		double r() {
			return Math.sqrt(x*x + y*y);
		}

	}

	ArrayList<Point> a;
	int n;
	Point P;


	public void solve() throws Exception {
		a = new ArrayList<Point>();
		n = nextInt();
		P = new Point(nextDouble(), nextDouble());
		for (int i = 0 ; i < n ; i ++) {
			Point X = new Point(nextDouble(), nextDouble());
			a.add(X);
		}

		double minDist = 1e30;
		double maxDist = 0.0;

		for (int i = 0 ; i < n ; i ++) {
			Point X = a.get(i), Y = a.get((i + 1) % n);
			double dx = P.minus(X).r();
			double dy = P.minus(Y).r();
			if (minDist > dx || minDist > dy) {
				minDist = Math.min(dx, dy);
			}
			if (maxDist < dx || maxDist < dy) {
				maxDist = Math.max(dx, dy);
			}
			Point XP = P.minus(X);
			Point XY = Y.minus(X);

			Point YP = P.minus(Y);
			Point YX = X.minus(Y);

			if (XP.dot(XY) > 0 && YP.dot(YX) > 0) {
				double d = Math.abs(XP.times(XY)) / XY.r();
				minDist = Math.min(d, minDist);
			}
		}
		double res = Math.PI * (maxDist * maxDist - minDist * minDist);
		out.println(String.format("%.12f", res));
	}
}