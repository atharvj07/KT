import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int N;
	static double T;
	static double[] S, P, Q, TH;

	public static void main(String[] args) {
		while (sc.hasNext()) {
			N = sc.nextInt();
			if (N == 0) break;
			T = sc.nextDouble();
			S = new double[N];
			P = new double[N];
			Q = new double[N];
			TH = new double[N];
			for (int i = 0; i < N; ++i) {
				S[i] = Double.parseDouble(sc.next());
				P[i] = Double.parseDouble(sc.next());
				Q[i] = Double.parseDouble(sc.next());
				TH[i] = Double.parseDouble(sc.next());
			}
			System.out.printf("%.8f\n", solve());
		}
	}

	static double solve() {
		double lo = 0;
		double hi = 10000000;
		for (int i = 0; i < 200; ++i) {
			double m1 = (lo * 2 + hi) / 3;
			double m2 = (lo + hi * 2) / 3;
			double v1 = calc(m1);
			double v2 = calc(m2);
			if (v1 < v2) {
				hi = m2;
			} else {
				lo = m1;
			}
		}
		return calc((lo + hi) / 2);
	}

	static double calc(double a) {
		double ret = a * T;
		for (int i = 0; i < N; ++i) {
			double rest = TH[i] - S[i] * a;
			if (rest > 0) ret += rest / Q[i] * P[i];
		}
		return ret;
	}

}