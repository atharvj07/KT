import java.util.Scanner;

public class Main {
	int n, m;

	int tanri(int a, double per, int t) {
		int tmp = 0;
		for (int i = 0; i < n; i++) {
			int b = (int)(a * per);
			a -= t;
			tmp += b;
		}
		return a + tmp;
	}

	int fukuri(int a, double per, int t) {
		for (int i = 0; i < n; i++) {
			int b = (int)(a * per);
			a = a + b - t;
		}
		return a;
	}

	void run() {
		Scanner sc = new Scanner(System.in);

		for (int T = sc.nextInt() - 1; 0 <= T; T--) {
			int ini = sc.nextInt();
			n = sc.nextInt();
			m = sc.nextInt();

			int max = 0;
			for (int i = 0; i < m; i++) {
				int flg = sc.nextInt();
				double per = sc.nextDouble();
				int t = sc.nextInt();
				if (flg == 0) {
					max = Math.max(max, tanri(ini, per, t));
				} else {
					max = Math.max(max, fukuri(ini, per, t));
				}
			}
			System.out.println(max);
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}