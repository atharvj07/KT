import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			int n = Integer.parseInt(sc.next());
			int m = Integer.parseInt(sc.next());
			if (n == 0 && m == 0) break;
			int[] a = new int[n];
			for (int i = 0; i < n; i++)
				a[i] = Integer.parseInt(sc.next());
			int max = 0;
			for (int i = 0; i < n; i++) {
				for (int j = i + 1; j < n; j++) {
					if (a[i] + a[j] <= m)
						max = Math.max(max, a[i] + a[j]);
				}
			}
			if (max == 0)
				System.out.println("NONE");
			else
				System.out.println(max);
		}
	}
}
