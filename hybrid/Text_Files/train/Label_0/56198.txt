import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Integer.MAX_VALUE;
import static java.lang.Integer.parseInt;

/**
 * Problem 05: Split Up!
 */
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		String[] words;

		while ((line = br.readLine()) != null && !line.isEmpty()) {

			int n = parseInt(line);
			if (n == 0) break;

			int[] a = new int[n];

			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n; i++) {
				a[i] = parseInt(st.nextToken());
			}

			int min = MAX_VALUE;

			for (int i = 0; i < 1 << n; i++) {
				int A = 0, B = 0;
				for (int j = 0; j < n; j++) {
					if ((i >> j & 1) == 1) {A += a[j];} else {B += a[j];}
				}
				min = Math.min(min, Math.abs(A - B));
			}

			System.out.println(min);
		}
	}
}