import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Integer.parseInt;

/**
 * Planetary Exploration
 */
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		String[] words;

		int M, N, K;
		line = br.readLine();
		M = parseInt(line.substring(0, line.indexOf(' ')));
		N = parseInt(line.substring(line.indexOf(' ') + 1));
		K = parseInt(br.readLine());

		//
		int[][] J = new int[M + 1][N + 1];
		int[][] O = new int[M + 1][N + 1];
		int[][] I = new int[M + 1][N + 1];

		for (int i = 0; i < M; i++) {
			line = br.readLine();
			for (int j = 0; j < N; j++) {
				switch (line.charAt(j)) {
					case 'J':
						J[i + 1][j + 1] = 1;
						break;
					case 'O':
						O[i + 1][j + 1] = 1;
						break;
					case 'I':
						I[i + 1][j + 1] = 1;
						break;
				}
			}
		}

		//sum up
		for (int i = 1; i <= M; i++) {
			for (int j = 1; j <= N; j++) {
				J[i][j] += J[i][j - 1];
				O[i][j] += O[i][j - 1];
				I[i][j] += I[i][j - 1];
			}
		}

		for (int j = 1; j <= N; j++) {
			for (int i = 1; i <= M; i++) {
				J[i][j] += J[i - 1][j];
				O[i][j] += O[i - 1][j];
				I[i][j] += I[i - 1][j];
			}
		}

		//solve
		StringBuilder sb = new StringBuilder();

		for (int k = 0; k < K; k++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int a, b, c, d;
			a = parseInt(st.nextToken());
			b = parseInt(st.nextToken());
			c = parseInt(st.nextToken());
			d = parseInt(st.nextToken());

			int j, o, i;
			j = J[c][d] - J[a - 1][d] - J[c][b - 1] + J[a - 1][b - 1];
			o = O[c][d] - O[a - 1][d] - O[c][b - 1] + O[a - 1][b - 1];
			i = I[c][d] - I[a - 1][d] - I[c][b - 1] + I[a - 1][b - 1];

			sb.append(j).append(' ');
			sb.append(o).append(' ');
			sb.append(i).append('\n');
		}

		System.out.print(sb.toString());
	}
}