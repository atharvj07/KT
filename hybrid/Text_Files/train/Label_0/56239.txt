import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int[] x, y, z, r;
	static long[] l;

	public static void main(String[] args) {
		int N = sc.nextInt();
		int Q = sc.nextInt();
		x = new int[N];
		y = new int[N];
		z = new int[N];
		r = new int[N];
		l = new long[N];
		for (int i = 0; i < N; ++i) {
			x[i] = sc.nextInt();
			y[i] = sc.nextInt();
			z[i] = sc.nextInt();
			r[i] = sc.nextInt();
			l[i] = sc.nextLong();
		}
		for (int i = 0; i < Q; ++i) {
			int sx = sc.nextInt();
			int sy = sc.nextInt();
			int sz = sc.nextInt();
			int dx = sc.nextInt();
			int dy = sc.nextInt();
			int dz = sc.nextInt();
			long sum = 0;
			for (int j = 0; j < N; ++j) {
				double lo = 0;
				double hi = 1;
				for (int k = 0; k < 300; ++k) {
					double m1 = (lo * 2 + hi) / 3;
					double m2 = (lo + hi * 2) / 3;
					double d1 = dist(x[j], y[j], z[j], sx + (dx - sx) * m1, sy + (dy - sy) * m1, sz + (dz - sz) * m1);
					double d2 = dist(x[j], y[j], z[j], sx + (dx - sx) * m2, sy + (dy - sy) * m2, sz + (dz - sz) * m2);
					if (d1 < d2) {
						hi = m2;
					} else {
						lo = m1;
					}
				}
				if (dist(x[j], y[j], z[j], sx + (dx - sx) * lo, sy + (dy - sy) * lo, sz + (dz - sz) * lo) <= r[j] + 1e-8) {
					sum += l[j];
				}
			}
			System.out.println(sum);
		}
	}

	static double dist(double x1, double y1, double z1, double x2, double y2, double z2) {
		return Math.sqrt(sq(x1 - x2) + sq(y1 - y2) + sq(z1 - z2));
	}

	static double sq(double v) {
		return v * v;
	}

}