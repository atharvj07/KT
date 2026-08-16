import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Bus Line
 */
public class Main {

	// 15 stations
	final static int[] route = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 3, 2, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = "";

		while ((line = br.readLine()) != null && !line.isEmpty()) {

			int n = Integer.parseInt(line);
			int s, g, step1, step2;

			for (int i = 0; i < n; ++i) {
				line = br.readLine();
				s = Integer.parseInt(line.substring(0, line.indexOf(' ')));
				g = Integer.parseInt(line.substring(line.indexOf(' ') + 1));

				step1 = 0;
				step2 = Integer.MAX_VALUE;

				StringBuilder sb1 = new StringBuilder();
				StringBuilder sb2 = new StringBuilder();
				for (int j = s;; j++) {
					if (j > 14) {
						j -= 15;
					}
					++step1;
					sb1.append(route[j] + " ");
					if (route[j] == g) {
						break;
					}
				}
				if (s <= 5) {
					s = 15 - s;
					step2 = 0;
					for (int j = s;; j++) {
						if (j > 14) {
							j -= 15;
						}
						++step2;
						sb2.append(route[j] + " ");
						if (route[j] == g) {
							break;
						}
					}
				}
				if (step1 <= step2) {
					System.out.println(sb1.substring(0, sb1.length() - 1)
							.toString());
				} else {
					System.out.println(sb2.substring(0, sb2.length() - 1)
							.toString());
				}
			}
		}

	}
}