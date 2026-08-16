import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;

public class Main {

	Scanner sc = new Scanner(System.in);

	int INF = 1 << 28;
	double EPS = 1e-9;

	int n;
	P ps1, ps2, ps3;
	P k, s;

	void run() {
		n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			int xp1 = sc.nextInt();
			int yp1 = sc.nextInt();
			int xp2 = sc.nextInt();
			int yp2 = sc.nextInt();
			int xp3 = sc.nextInt();
			int yp3 = sc.nextInt();
			int xk = sc.nextInt();
			int yk = sc.nextInt();
			int xs = sc.nextInt();
			int ys = sc.nextInt();
			ps1 = new P(xp1, yp1);
			ps2 = new P(xp2, yp2);
			ps3 = new P(xp3, yp3);
			k = new P(xk, yk);
			s = new P(xs, ys);
			solve();
		}
	}

	void solve() {
		if (crsSS(k, s, ps1, ps2) ^ crsSS(k, s, ps2, ps3)
				^ crsSS(k, s, ps3, ps1)) {
			println("OK");
		} else {
			println("NG");
		}
	}

	boolean crsSS(P p1, P p2, P q1, P q2) {
		if (max(p1.x, p2.x) + EPS < min(q1.x, q2.x))
			return false;
		if (max(q1.x, q2.x) + EPS < min(p1.x, p2.x))
			return false;
		if (max(p1.y, p2.y) + EPS < min(q1.y, q2.y))
			return false;
		if (max(q1.y, q2.y) + EPS < min(p1.y, p2.y))
			return false;
		return signum(p2.sub(p1).det(q1.sub(p1)))
				* signum(p2.sub(p1).det(q2.sub(p1))) < EPS
				&& signum(q2.sub(q1).det(p1.sub(q1)))
						* signum(q2.sub(q1).det(p2.sub(q1))) < EPS;
	}

	class P {
		double x, y;

		P() {
			this(0, 0);
		}

		P(double x, double y) {
			this.x = x;
			this.y = y;
		}

		P add(P p) {
			return new P(x + p.x, y + p.y);
		}

		P sub(P p) {
			return new P(x - p.x, y - p.y);
		}

		P mul(double m) {
			return new P(x * m, y * m);
		}

		P div(double d) {
			return new P(x / d, y / d);
		}

		double abs() {
			return Math.sqrt(abs2());
		}

		double abs2() {
			return x * x + y * y;
		}

		double arg() {
			return Math.atan2(y, x);
		}

		// inner product
		double dot(P p) {
			return x * p.x + y * p.y;
		}

		// outer product
		double det(P p) {
			return x * p.y - y * p.x;
		}

		P rot90() {
			return new P(-y, x);
		}

		// conjugation
		P conj() {
			return new P(x, -y);
		}
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
		// System.setOut(new PrintStream(new BufferedOutputStream(System.out)));
		new Main().run();
	}
}