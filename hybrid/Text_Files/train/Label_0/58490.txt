import java.util.Scanner;


public class Main {

	void run() {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt(), M = sc.nextInt();

		int[][] g = new int[N+1][];
		for (int i = 0 ; i <= N ; i++) {
			g[i] = new int[i+2];
		}

		while (M-- != 0) {
			int a = Integer.parseInt(sc.next()),
				b = Integer.parseInt(sc.next()),
				x = Integer.parseInt(sc.next());
			g[a][b] = Math.max(g[a][b], x+1);
		}

		int count = 0;
		for (int x = 1 ; x <= N ; x++) {
			for (int y = 1 ; y <= x ; y++) {
				g[x][y] = Math.max(g[x][y], Math.max(g[x-1][y]-1, g[x-1][y-1]-1));
				if (g[x][y] > 0) count++;
			}
		}

		System.out.println(count);
	}

	public static void main(String[] args) {
		new Main().run();
	}

}