import java.util.Arrays;
import java.util.Scanner;

class Main {

	void run() {
		Scanner sc = new Scanner(System.in);
		double[][] p = new double[3][2];
		for (int i = 0; i < 3; ++i) {
			p[i][0] = sc.nextDouble();
			p[i][1] = sc.nextDouble();
		}
		p[1][0] -= p[0][0];
		p[1][1] -= p[0][1];
		p[2][0] -= p[0][0];
		p[2][1] -= p[0][1];
		double a = dist(p[1]);
		double b = dist(p[2]);
		double c = dist(new double[] { p[1][0] - p[2][0], p[1][1] - p[2][1] });
		double s = 0.5
				* Math.sqrt(dist(p[1]) * dist(p[1]) * dist(p[2]) * dist(p[2]) - dot(p[1], p[2]) * dot(p[1], p[2]));
		double r = 2 * s / (a + b + c);
		double d = Math.max(a, Math.max(b, c));
		System.out.println(d * r / (2 * r + d));
	}

	double dist(double[] p) {
		double x = p[0];
		double y = p[1];
		return Math.sqrt(x * x + y * y);
	}

	double dot(double[] p1, double[] p2) {
		return p1[0] * p2[0] + p1[1] * p2[1];
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}