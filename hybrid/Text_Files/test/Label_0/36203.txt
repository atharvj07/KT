import static java.lang.Math.min;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		new Main().run();
	}

	void run() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		for (int i = 0; i < n; i++)
			a[i] = sc.nextInt();




		boolean[] visited = new boolean[1 << n];
		visited[1] = true;
		int set = 0;
		for (int i = 1; i < n; i++) {

			ArrayList<Integer> comb = new ArrayList<Integer>();
			for (int j = 0; j < i; j++) for (int k = 0; k <= j; k++) if (a[i] == a[j] + a[k]) {
				comb.add(j);
				comb.add(k);
			}

			for (; set < (1 << i); ++set) if (visited[set]) {
				int b = set;
				for (int s = 0; s < comb.size(); s += 2) {
					int j = comb.get(s);
					int k = comb.get(s+1);
					if ((b >> j & 1) == 1 && ((b >> k) & 1) == 1) {
						{
							int nb = b | (1 << i);
							visited[nb] = true;
						}
						for (int l = 0; l < n; l++) if ((b >> l & 1) == 1) {
							int nb = b | (1 << i);
							nb = nb ^ (1 << l);
							visited[nb] = true;
						}
					}
				}
			}
		}

		int best = n + 1;
		for (; set < (1 << n); set++) if (visited[set]) {
			int b = set;
			best = min(best, Integer.bitCount(b));
		}
		if (best >= n + 1)
			best = -1;
		System.out.println(best);

	}
}