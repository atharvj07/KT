import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			int n = Integer.parseInt(sc.next());
			int m = Integer.parseInt(sc.next());
			int a = Integer.parseInt(sc.next());
			if (n == 0)
				return;
			int[][] b = new int[1010][n + 1];
			for (int i = 0; i < m; i++) {
				int h = Integer.parseInt(sc.next());
				int p = Integer.parseInt(sc.next());
				int q = Integer.parseInt(sc.next());
				b[h][p] = q;
				b[h][q] = p;
			}
			for (int i = 1000; i >= 0; i--) {
				if (b[i][a] == 0) continue;
				a = b[i][a];
			}
			System.out.println(a);
		}
	}
}
