
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	static int N;
	static double[] r;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		r = new double[N];
		for (int i = 0; i < N; ++i)
			r[i] = sc.nextDouble();
		Arrays.sort(r);
		int s = 0;
		int t = r.length - 1;
		while (s < t) {
			double d = r[s];
			r[s] = r[t];
			r[t] = d;
			++s;
			--t;
		}
		double ans = 0;
		while (N >= 3) {
			int[] ord = new int[N];
			for (int i = 0; i < N; ++i)
				ord[i] = i;
			do {
				double min = Double.MAX_VALUE / 16;
				for (int i = 0; i < N; ++i)
					min = Math.min(min, r[ord[i]] * r[ord[(i + 1) % N]]);

				double upper = Math.PI;
				double lower = 0;
				double okSum = 0;
				for (int i = 0; i < 100; ++i) {
					double middle = (upper + lower) / 2;
					double sum = 0;
					for (int j = 0; j < N; ++j) {
						sum += Math.acos(min / (r[ord[j]] * r[ord[(j + 1) % N]]) * Math.cos(middle));
					}
					if (sum > 2 * Math.PI)
						upper = middle;
					else {
						lower = middle;
						okSum = sum;
					}
				}
				if (okSum / (2 * Math.PI) < 1e-5) {
					continue;
				}
				double tmp = 0;
				for (int i = 0; i < N; ++i) {
					double sin = min / (r[ord[i]] * r[ord[(i + 1) % N]]) * Math.cos(lower);
					tmp += 0.5 * r[ord[i]] * r[ord[(i + 1) % N]] * Math.sqrt(1 - sin * sin);
				}
				ans = Math.max(ans, tmp);

			} while (nextPermutation(ord));
			--N;
		}
		System.out.println(ans);
	}

	static boolean nextPermutation(int[] ord) {
		int n = ord.length;
		int i = n - 1;
		while (i - 1 >= 0 && ord[i - 1] > ord[i])
			--i;
		if (i == 0)
			return false;
		int j = i;
		while (j + 1 < n && ord[j + 1] > ord[i - 1])
			++j;
		int d = ord[i - 1];
		ord[i - 1] = ord[j];
		ord[j] = d;
		int t = n - 1;
		int s = i;
		while (s < t) {
			d = ord[s];
			ord[s] = ord[t];
			ord[t] = d;
			++s;
			--t;
		}
		return true;
	}

	static void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}

}