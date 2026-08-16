
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		new Main().run();
	}

	private void run() {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			w = scanner.nextInt();
			h = scanner.nextInt();
			if ((w | h) == 0)
				break;
			ice = new int[h * w];
			hit = new int[h * w];
			dist = new int[h][w];
			m = new char[h][w];
			v = new boolean[h][w];
			for (int i = 0; i < h; i++)
				for (int j = 0; j < w; j++) {
					dist[i][j] = -1;
					m[i][j] = '#';
				}
			for (int i = 0; i < h; i++) {
				char[] c = scanner.next().toCharArray();
				for (int j = 0; j < w; j++) {
					m[i][j] = c[j];
					if (m[i][j] == 'S') {
						m[i][j] = '.';
						si = i;
						sj = j;
					} else if (m[i][j] == 'G') {
						m[i][j] = '.';
						gi = i;
						gj = j;
					}
				}

			}
			ice[0] = INF;
			id = new int[h][w];
			int ID = 1;
			for (int i = 0; i < h; i++)
				for (int j = 0; j < w; j++) {
					if (m[i][j] != 'X' || id[i][j] > 0)
						continue;
					mark(i, j, ID);
					if (ice[ID] == 1)
						m[i][j] = '#';
					ID++;
				}
			dist[gi][gj] = 0;
			Deque<int[]> deque = new ArrayDeque<int[]>();
			deque.offer(new int[] { gi, gj });
			while (!deque.isEmpty()) {
				int[] V = deque.poll();
				int pi = V[0];
				int pj = V[1];
				for (int[] mo : d) {
					int ni = pi + mo[0];
					int nj = pj + mo[1];
					if (!isOK(ni, nj))
						continue;
					if (m[ni][nj] != '#' && dist[ni][nj] == -1) {
						dist[ni][nj] = dist[pi][pj] + 1;
						deque.offer(new int[] { ni, nj });
					}
				}
			}
			res = 0;
			v[si][sj] = true;
			while (!f(si, sj, 0,-100)) {
				Arrays.fill(hit, 0);
				for (int i = 0; i < h; i++)
					for (int j = 0; j < w; j++)
						v[i][j] = false;
				v[si][sj] = true;
				res++;
			}
			System.out.println(res);
		}
	}

	private boolean f(int i, int j, int depth,int pre) {
		if (res < depth + dist[i][j])
			return false;
		if (gi == i && gj == j)
			return true;
		for (int r = 0;r<4;r++) {
			int ni = i + d[r][0];
			int nj = j + d[r][1];
			if (!isOK(ni, nj))
				continue;
			if(Math.max(r, pre)-Math.min(r,pre)==2)
				continue;
			if (!v[ni][nj] && m[ni][nj] != '#') {
				if (ice[id[ni][nj]] /2 > hit[id[ni][nj]] ) {
					hit[id[ni][nj]]++;
					v[ni][nj] = true;
					if (f(ni, nj, depth + 1,r))
						return true;
					v[ni][nj] = false;
					hit[id[ni][nj]]--;
				}
			}
		}
		return false;
	}

	private void mark(int i, int j, int x) {
		id[i][j] = x;
		ice[x]++;
		for (int[] mo : d) {
			int ni = i + mo[0];
			int nj = j + mo[1];
			if (!isOK(ni, nj))
				continue;
			if (m[ni][nj] == 'X' && id[ni][nj] == 0)
				mark(ni, nj, x);
		}
	}

	private boolean isOK(int i, int j) {
		if (0 <= i && i < h && 0 <= j && j < w)
			return true;
		return false;
	}

	int w, h, si, sj, gi, gj, INF = 1 << 29, res;
	int[][] d = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
	int[] ice, hit;
	int[][] id, dist;
	char[][] m;
	boolean[][] v;
}