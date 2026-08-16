import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class Main {
	public static void main(String[] args) throws IOException {
		new Main().run();
	}

	void run() throws IOException {
		Scanner sc = new Scanner(System.in);
		while (true) {
			int W = sc.nextInt();
			int H = sc.nextInt();
			if (W == 0 && H == 0)
				break;
			char[][] map = new char[H][W];
			for (int i = 0; i < H; ++i) {
				map[i] = sc.next().toCharArray();
			}
			int Ax = -1, Ay = -1;
			int Qx = -1, Qy = -1;
			for (int i = 0; i < H; ++i) {
				for (int j = 0; j < W; ++j) {
					if (map[i][j] == 'A') {
						Ay = i;
						Ax = j;
					} else if (map[i][j] == 'Q') {
						Qy = i;
						Qx = j;
					}
				}
			}
			int[][][] memo = new int[H * W][H * W][2];

			for (int q = 0; q < H * W; ++q) {
				if (!valid(q, map, H, W))
					continue;
				for (int a = 0; a < H * W; ++a) {
					if (!valid(a, map, H, W))
						continue;
					for (int t = 0; t < 2; ++t) {
						if (q == a) {
							memo[q][a][t] = -1;// Q?????????
						} else if (t == 0 && map[q / W][q % W] == 'E') {
							memo[q][a][t] = 1;// Q?????????
						}
					}
				}
			}
			int[] d = { 0, W, -W, 1, -1 };

			for (boolean update = true; update;) {
				update = false;
				for (int q = 0; q < H * W; ++q) {
					if (!valid(q, map, H, W))
						continue;
					for (int a = 0; a < H * W; ++a) {
						if (!valid(a, map, H, W))
							continue;
						for (int t = 0; t < 2; ++t) {
							if (memo[q][a][t] != 0) {
								continue;
							}
							int v = (t == 0 ? -999 : 999);
							for (int i = 0; i < 5; ++i) {
								int na = a, nq = q;
								if (t == 0)
									nq += d[i];
								else
									na += d[i];
								if ((t == 1 && !valid(a, d[i], map, H, W)) || (t == 0 && !valid(q, d[i], map, H, W)))
									continue;
								if (t == 0) {
									v = Math.max(v, memo[nq][na][t ^ 1]);
								} else {
									v = Math.min(v, memo[nq][na][t ^ 1]);
								}
							}
							if (v != 0) {
								memo[q][a][t] = v;
								update = true;
							}
						}
					}
				}

			}
			int Q = Qy * W + Qx;
			int A = Ay * W + Ax;
			if (memo[Q][A][0] == 0) {
				System.out.println("Queen can not escape and Army can not catch Queen.");
			} else if (memo[Q][A][0] == -1) {
				System.out.println("Army can catch Queen.");
			} else if (memo[Q][A][0] == 1) {
				System.out.println("Queen can escape.");
			}
		}

	}

	boolean valid(int a, int d, char[][] map, int H, int W) {
		if (!valid(a, map, H, W) || !valid(a + d, map, H, W)) {
			return false;
		}
		int h = a / W;
		int w = a % W;
		int nh = (a + d) / W;
		int nw = (a + d) % W;
		if (Math.abs(nh - h) + Math.abs(nw - w) <= 1) {
			return true;
		} else {
			return false;
		}
	}

	boolean valid(int a, char[][] map, int H, int W) {
		if (a < 0 || a >= H * W)
			return false;
		int h = a / W;
		int w = a % W;
		if (map[h][w] == '#')
			return false;
		return true;
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}