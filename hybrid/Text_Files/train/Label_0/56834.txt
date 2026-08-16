import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws FileNotFoundException {
		new Main().run();
	}

	void run() throws FileNotFoundException {
		solver();
	}

	@SuppressWarnings("unchecked")
	void solver() throws FileNotFoundException {
		Scanner sc = new Scanner(System.in);
		int na = sc.nextInt();
		int nb = sc.nextInt();
		int w = sc.nextInt();
		int[][] p = new int[na + nb][3];
		for (int i = 0; i < na; ++i) {
			p[i][0] = 0;
			p[i][1] = sc.nextInt();// m
			p[i][2] = sc.nextInt();// c
		}
		for (int i = na; i < na + nb; ++i) {
			p[i][0] = 1;
			p[i][1] = sc.nextInt();// m
			p[i][2] = sc.nextInt();// c
		}

		Arrays.sort(p, new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				if (o1[2] != o2[2])
					return Integer.compare(o1[2], o2[2]);
				else
					return Integer.compare(o1[1], o2[1]);
			}
		});

		long[][] f = new long[2][w + 1];
		for (int i = 0; i < f.length; ++i) {
			for (int j = 0; j < f[i].length; ++j) {
				f[i][j] = -1;
			}
		}
		long ans = Long.MAX_VALUE / 16;
		int t = 0;
		for (int i = 0; i < na + nb; ++i) {
			t = Math.max(0, t - 2);
			if (p[i][1] > w)
				continue;
			for (int j = w - p[i][1]; j >= 1; --j) {
				f[p[i][0]][j + p[i][1]] = Math.max(f[p[i][0]][j + p[i][1]], f[p[i][0]][j]);
			}
			f[p[i][0]][p[i][1]] = p[i][2];
			while (t + 1 <= i && Math.max(g(f, p[t][2]), p[i][2] - p[t][2]) >= Math.max(g(f, p[t + 1][2]),
					p[i][2] - p[t + 1][2])) {
				++t;
			}
			ans = Math.min(ans, Math.max(g(f, p[t][2]), p[i][2] - p[t][2]));
		}
		System.out.println(ans);
	}

	long g(long[][] f, long lower) {
		long ret = Long.MAX_VALUE / 16;
		long las = Long.MAX_VALUE / 16;
		for (int i = 1; i < f[0].length; ++i) {
			if (f[1][i] >= lower)
				las = i;
			if (f[0][i] < lower)
				continue;
			ret = Math.min(ret, Math.abs(i - las));
		}
		las = -Long.MAX_VALUE / 16;
		for (int i = 1; i < f[1].length; ++i) {
			if (f[0][i] >= lower)
				las = i;
			if (f[1][i] < lower)
				continue;
			ret = Math.min(ret, Math.abs(i - las));
		}
		return ret;
	}

	private static void tr(Object... o) {
		System.out.println(Arrays.deepToString(o));
	}
}