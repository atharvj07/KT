import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
	ArrayList<P> calc(Circle c1, Circle c2) {
		ArrayList<P> ret = new ArrayList<>();
		double d = c1.center.dist(c2.center);
		double cos = (c1.r * c1.r + d * d - c2.r * c2.r) / (2 * d * c1.r);
		P p12 = c2.center.sub(c1.center);
		P midP = c1.center.add(p12.normalize().mul(c1.r * cos));
		double h = c1.r * Math.sqrt(1 - cos * cos);
		ret.add(midP.add(p12.normalize().rot(Math.PI / 2).mul(h)));
		if (h > 0)
			ret.add(midP.add(p12.normalize().rot(Math.PI / 2).mul(-h)));
		return ret;
	}

	void run(double c1x, double c1y, double c1r, double c2x, double c2y, double c2r) {
		P center1 = new P(c1x, c1y);
		P center2 = new P(c2x, c2y);
		Circle c1 = new Circle(center1, c1r);
		Circle c2 = new Circle(center2, c2r);
		ArrayList<P> ret = calc(c1, c2);
		Collections.sort(ret);
		if (ret.size() == 2)
			for (int i = 0; i < ret.size(); ++i) {
				System.out.printf("%.10f %.10f", ret.get(i).x, ret.get(i).y);
				System.out.print(i == ret.size() - 1 ? "\n" : " ");
			}
		else {
			System.out.printf("%.10f %.10f %.10f %.10f\n", ret.get(0).x, ret.get(0).y, ret.get(0).x, ret.get(0).y);
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double c1x, c1y, c1r, c2x, c2y, c2r;
		c1x = sc.nextDouble();
		c1y = sc.nextDouble();
		c1r = sc.nextDouble();
		c2x = sc.nextDouble();
		c2y = sc.nextDouble();
		c2r = sc.nextDouble();
		new Main().run(c1x, c1y, c1r, c2x, c2y, c2r);

	}

	class Circle {
		P center;
		double r;

		public Circle(P center, double r) {
			this.center = center;
			this.r = r;
		}

	}

	class P implements Comparable<P> {
		double x, y;

		public P(double x, double y) {
			this.x = x;
			this.y = y;
		}

		double norm() {
			return Math.sqrt(x * x + y * y);
		}

		P normalize() {
			return this.mul(1 / this.norm());
		}

		P add(P p) {
			return new P(x + p.x, y + p.y);
		}

		P sub(P p) {
			return this.add(p.mul(-1));
		}

		P mul(double coe) {
			return new P(x * coe, y * coe);
		}

		double dist(P p) {
			return Math.sqrt((x - p.x) * (x - p.x) + (y - p.y) * (y - p.y));
		}

		P rot(double ang) {
			double c = Math.cos(ang);
			double s = Math.sin(ang);
			return new P(c * x - s * y, s * x + c * y);
		}

		@Override
		public int compareTo(P o) {
			if (Math.abs(x - o.x) > 1e-6)
				return Double.compare(x, o.x);
			else {
				return Double.compare(y, o.y);
			}
		}

	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}