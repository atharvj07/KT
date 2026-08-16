import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws FileNotFoundException {
		new Main().run();
	}

	int n;
	double[] x;
	double[] y;

	void run() throws FileNotFoundException {
		Scanner sc = new Scanner(System.in);
		while (true) {
			n = sc.nextInt();
			if (n == 0)
				break;
			x = new double[n];
			y = new double[n];
			for (int i = 0; i < n; ++i) {
				x[i] = sc.nextDouble();
				y[i] = -sc.nextDouble();
			}
			solver();
		}
	}

	@SuppressWarnings("unchecked")
	void solver() throws FileNotFoundException {

		ArrayList<Double> cand = new ArrayList<>();
		cand.add(0d);
		cand.add(Math.PI);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (i == j)
					continue;
				if (y[i] < y[j])
					continue;
				cand.add(Math.atan2(y[i] - y[j], x[i] - x[j]));
				if ((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]) >= 2 * 2)
					cand.addAll(f(x[i], y[i], x[j], y[j]));
			}
		}
		cand = reduct(cand);
		int sz = cand.size();
		for (int i = 0; i + 1 < sz; ++i) {
			double l = cand.get(i);
			double r = cand.get(i + 1);
			double m = h((l + r) / 2);
			if (l < m && m < r) {
				cand.add(m);
			}
		}
		cand = reduct(cand);
		double max = 0;
		double min = Double.MAX_VALUE / 16;
		double max_arg = -1, min_arg = -1;
		for (double d : cand) {
			if (d > Math.PI)
				throw new AssertionError();
			if (max < g(d)) {
				max = g(d);
				max_arg = d;
			}
			if (min > g(d)) {
				min = g(d);
				min_arg = d;
			}
		}
		System.out.println(min_arg);
		System.out.println(max_arg);
	}

	double[][] pos(double a) {
		double[][] pos = new double[n][2];
		double c = Math.cos(a);
		double s = Math.sin(a);
		for (int i = 0; i < n; ++i) {
			pos[i][0] = s * x[i] - c * y[i];
			pos[i][1] = i;
		}
		Arrays.sort(pos, new Comparator<double[]>() {
			@Override
			public int compare(double[] o1, double[] o2) {
				return Double.compare(o1[0], o2[0]);
			}
		});
		return pos;
	}

	double h(double a) {
		double[][] pos = pos(a);
		int[] coe = new int[n];
		for (int i = 0; i < n; ++i) {
			if (i + 1 < n && pos[i + 1][0] - pos[i][0] <= 2) {
				--coe[i];
			}
			if (i - 1 >= 0 && pos[i][0] - pos[i - 1][0] <= 2) {
				++coe[i];
			}
		}
		double A = 0, B = 0;
		for (int i = 0; i < n; ++i) {
			A += x[(int) Math.round(pos[i][1])] * coe[i];
			B += y[(int) Math.round(pos[i][1])] * coe[i];
		}
		return f(A, B);
	}

	double g(double a) {
		double[][] pos = pos(a);
		double ret = 2;
		for (int i = 0; i + 1 < n; ++i) {
			if (pos[i + 1][0] - pos[i][0] > 2) {
				ret += 2;
			} else {
				ret += pos[i + 1][0] - pos[i][0];
			}
		}
		return ret;
	}

	// 2->1
	ArrayList<Double> f(double x1, double y1, double x2, double y2) {
		ArrayList<Double> tmp = new ArrayList<>();
		double dx = x1 - x2;
		double dy = y1 - y2;
		double d = Math.sqrt(dx * dx + dy * dy);
		double shift = Math.atan2(1, Math.sqrt(d / 2 * d / 2 - 1));
		double theta = Math.atan2(dy, dx);
		tmp.add((shift + theta + 4 * Math.PI) % (2 * Math.PI));
		tmp.add((-shift + theta + 4 * Math.PI) % (2 * Math.PI));
		ArrayList<Double> ret = new ArrayList<>();
		for (double dumy : tmp) {
			if (dumy >= Math.PI) {
				dumy -= Math.PI;
			}
			ret.add(dumy);
		}
		return ret;
	}

	double f(double A, double B) {
		if (A < 0) {
			A *= -1;
			B *= -1;
		}
		double ret = Math.atan2(A, -B);
		if (!(0 <= ret && ret <= Math.PI)) {
			throw new AssertionError();
		}
		return ret;
	}

	ArrayList<Double> reduct(ArrayList<Double> lis) {
		Collections.sort(lis);
		for (int i = 0; i < lis.size(); ++i) {
			if (lis.get(i) > Math.PI) {
				lis.remove(i);
				--i;
			}
		}
		for (int i = 0; i < lis.size(); ++i) {
			while (i + 1 < lis.size() && lis.get(i + 1) - lis.get(i) < 1e-13) {
				lis.remove(i + 1);
			}
		}
		return lis;
	}

	private static void tr(Object... o) {
		System.out.println(Arrays.deepToString(o));
	}
}