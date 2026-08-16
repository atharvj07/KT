import java.util.Scanner;
import java.util.SortedSet;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		for (;;) {
			int n = Integer.parseInt(scan.next());
			int m = Integer.parseInt(scan.next());
			if (n == 0 && m == 0) break;
			int a[] = new int[n];
			int w[] = new int[m];
			for (int i = 0; i < n; i++) {
				a[i] = Integer.parseInt(scan.next());
			}
			for (int j = 0; j < m; j++) {
				w[j] = Integer.parseInt(scan.next());				
			}
			SortedSet<Integer> commonAdditions = null;
			for (int i = 0; i < n; i++) {
				SortedSet<Integer> additions = new TreeSet<Integer>();
				boolean bJust = calcNearestWeight(a[i], w, 0, 0, additions);
				if (!bJust) {
					if (commonAdditions == null) {
						commonAdditions = additions;
					} else {
						commonAdditions.retainAll(additions);
					}
				}
			}
			if (commonAdditions == null) {
				System.out.println(0);				
			} else {
				if (commonAdditions.size() > 0) {
					System.out.println(commonAdditions.first());
				} else {
					System.out.println(-1);
				}
			}
		}
		scan.close();
	}

	private static boolean calcNearestWeight(int x, int w[], int i, int sum, SortedSet<Integer> additions) {
		if (x == sum) return true;
		if (i == w.length) {
			additions.add(Math.abs(x - sum));
			return false;
		}
		if (calcNearestWeight(x, w, i + 1, sum, additions)) return true;
		if (calcNearestWeight(x, w, i + 1, sum + w[i], additions)) return true;
		return calcNearestWeight(x, w, i + 1, sum - w[i], additions);
	}
}

