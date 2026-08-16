import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import static java.lang.Integer.parseInt;

/**
 * Russian Flag
 */
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;

		line = br.readLine();

		int N, M;
		N = parseInt(line.substring(0, line.indexOf(' ')));
		M = parseInt(line.substring(line.indexOf(' ') + 1));
		int[][] wbr = new int[N][3];

		for (int i = 0; i < N; i++) {
			line = br.readLine();
			int w = 0;
			int b = 0;
			int r = 0;
			for (char c : line.toCharArray()) {
				if (c == 'W') w++;
				else if (c == 'B') b++;
				else r++;
			}
			wbr[i][0] = b + r;
			wbr[i][1] = w + r;
			wbr[i][2] = w + b;
		}

		int min = N * M;
		for (int i = 1; i < N - 1; i++) {
			for (int j = i; j < N - 1; j++) {
				int change = 0;
				for (int k = 1; k < N - 1; k++) {
					if (k < i) {
						change += wbr[k][0];
					} else if (i <= k && k <= j) {
						change += wbr[k][1];
					} else {
						change += wbr[k][2];
					}
				}
				min = Math.min(min, change);
			}
		}

		System.out.println(wbr[0][0] + min + wbr[N - 1][2]);
	}
}