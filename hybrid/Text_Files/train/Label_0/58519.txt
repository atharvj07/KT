import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Integer.parseInt;
import static java.lang.Double.parseDouble;

/**
 * Calender Colors
 */
public class Main {

	static int N, M;
	static double[][] cs, ds;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		String[] words;

		StringTokenizer st = new StringTokenizer(br.readLine());

		N = parseInt(st.nextToken());
		M = parseInt(st.nextToken());

		cs = new double[N][3];
		ds = new double[N][N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++) cs[i][j] = parseDouble(st.nextToken());
		}

		for (int i = 0; i < N; i++) {
			for (int j = i + 1; j < N; j++) {
				double d = 0.0;
				for (int k = 0; k < 3; k++) d += Math.pow(cs[i][k] - cs[j][k], 2);
				ds[i][j] = d;
			}
		}

		//solve
		double max = -0.0;

		for (int i = 0; i < 1 << N; i++) {
			int c = 0;
			for (int j = 0; j < N; j++) if ((i >> j & 1) == 1) c++;
			if (c == M) max = Math.max(max, total(i));
		}

		System.out.println(max);

	} //end main

	static double total(int b) {

		int[] c = new int[M];
		double d = 0.0;

		for (int i = 0, j = 0; i < N; i++) {
			if ((b >> i & 1) == 1) {
				c[j] = i;
				j++;
			}
		}

		for (int i = 0; i < M; i++) {
			for (int j = i + 1; j < M; j++) {
				d += ds[c[i]][c[j]];
			}
		}

		return d;
	}
}