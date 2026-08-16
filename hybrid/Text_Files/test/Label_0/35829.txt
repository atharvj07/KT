import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line = "";

		while ((line = br.readLine()) != null) {

			int n = Integer.parseInt(line.substring(0, line.indexOf(' ')));
			int m = Integer.parseInt(line.substring(line.indexOf(' ') + 1));
			if (n == 0 && m == 0)
				break;

			//
			m++;
			int[] wish = new int[m];
			for (int i = 0; i < n; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 1; j < m; j++) {
					if (st.nextToken().equals("1"))
						wish[j]++;
				}
			}
			int[] rank = new int[m];
			rank = Arrays.copyOf(wish, m);
			Arrays.sort(rank);

			//
			StringBuilder sb = new StringBuilder();
			int i1 = -1, i2 = -1;
			for (int i = m - 1; i >= 0; i--) {
				i1 = rank[i];
				if (i1 == i2)
					continue;
				for (int j = 1; j < m; j++) {
					if (wish[j] == i1)
						sb.append(j + " ");
				}
				i2 = i1;
			}
			System.out.println(sb.toString().substring(0, sb.length() - 1));
		}
	}
}