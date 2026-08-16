import java.util.Scanner;

public class Main {
	static int w, h;
	static int a[][];

	public static void f(int x, int y, int c) {
		if (x < 0 || w <= x || y < 0 || h <= y) {
			return ;
		}
		if (a[y][x] != c) {
			return ;
		}
		a[y][x] = -1;
		f(x + 1, y, c);
		f(x - 1, y, c);
		f(x, y + 1, c);
		f(x, y - 1, c);
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n;
		int sx, sy;
		int gx, gy;
		int dx0[] = {0, 0, 1, 1, 2, 2, 3, 3};
		int dy0[] = {0, 1, 0, 1, 0, 1, 0, 1};
		int dx1[] = {0, 0, 0, 0, 1, 1, 1, 1};
		int dy1[] = {0, 1, 2, 3, 0, 1, 2, 3};

		while (true) {
			w = sc.nextInt();
			h = sc.nextInt();
			if ((w | h) == 0) {
				break;
			}
			sx = sc.nextInt() - 1;
			sy = sc.nextInt() - 1;
			gx = sc.nextInt() - 1;
			gy = sc.nextInt() - 1;
			n = sc.nextInt();
			a = new int[h][w];
			while (n-- != 0) {
				int c = sc.nextInt();
				int d = sc.nextInt();
				int x = sc.nextInt() - 1;
				int y = sc.nextInt() - 1;
				if (d == 0) {
					for (int i = 0; i < 8; i++) {
						a[y + dy0[i]][x + dx0[i]] = c;
					}
				} else {
					for (int i = 0; i < 8; i++) {
						a[y + dy1[i]][x + dx1[i]] = c;
					}
				}
			}

			f(sx, sy, a[sy][sx]);
			if (a[sy][sx] == 0 || a[gy][gx] == 0) {
				System.out.println("NG");
			} else if (0 <= a[gy][gx]) {
				System.out.println("NG");
			} else {
				System.out.println("OK");
			}
		}
	}
}