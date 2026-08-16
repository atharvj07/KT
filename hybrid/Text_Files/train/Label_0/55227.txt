import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Integer.parseInt;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;


		while ((line = br.readLine()) != null && !line.isEmpty()) {
			int n = parseInt(line);
			if (n == 0) break;

			int count = 0;
			int steps = 0;

			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n; i++) {
				String step = st.nextToken();
				if (step.charAt(0) == 'l') {
					if (step.charAt(1) == 'u') {
						steps += 2;
					} else {
						steps -= 2;
					}
				} else {
					if (step.charAt(1) == 'u') {
						steps += 1;
					} else {
						steps -= 1;
					}
				}
				if (steps == 3) {
					steps = 7;
					count++;
				} else if (steps == 4) {
					steps = 0;
					count++;
				}
			}
			System.out.println(count);
		}
	} //end while
} //end main