
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {

		new Main().run();
	}

	private void run() throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(
				System.in));
		StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
		int N = Integer.parseInt(tokenizer.nextToken());
		int R = Integer.parseInt(tokenizer.nextToken());
		int L = Integer.parseInt(tokenizer.nextToken());
		int[] po = new int[N];
		int[] c = new int[N];
		int now = 0;
		int index = 0;

		for (int i = 0; i < R; i++) {
			tokenizer = new StringTokenizer(reader.readLine());
			int d = Integer.parseInt(tokenizer.nextToken()) - 1;
			int t = Integer.parseInt(tokenizer.nextToken());
			int x = Integer.parseInt(tokenizer.nextToken());
			c[index] += t - now;
			po[d] += x;
			now = t;
			if (x > 0) {
				if (d == index)
					continue;
				if (po[index] < po[d])
					index = d;
				else if (po[index] == po[d] && index > d)
					index = d;
			} else {
				if (d != index)
					continue;
				int maxp = Integer.MIN_VALUE;
				for (int j = 0; j < N; j++) {
					if (maxp < po[j]) {
						maxp = po[j];
						index = j;
					}
				}
			}

			
		}
		c[index] += L - now;
		int ans = 0;
		int max = 0;
		for (int i = 0; i < N; i++) {
			if (c[i] > max) {
				max = c[i];
				ans = i;
			}
		}
		System.out.println(ans + 1);

	}
}