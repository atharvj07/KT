import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

	Scanner sc = new Scanner(System.in);

	void run() {
		for (;;) {

			int n = sc.nextInt();
			if (n == 0)
				break;
			int map[][][] = new int[n][n][2];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					map[i][j][0] = sc.nextInt();
					map[i][j][1] = sc.nextInt();
				}
			}
			UnionFind uf = new UnionFind(n * n);
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					int pos = pos(j, i, n);
					int jump_x = map[i][j][0];
					int jump_y = map[i][j][1];
					int jump = pos(jump_x, jump_y, n);
					uf.unite(pos, jump);
				}
			}
			Set<Integer> set = new HashSet<Integer>();
			for (int i = 0; i < uf.par.length; i++) {
				uf.find(i);
				set.add(uf.par[i]);
			}
			System.out.println(set.size());
		}
	}

	public static void main(String[] args) {
		new Main().run();

	}

	int pos(int x, int y, int w) {
		return x + y * w;
	}
}

class UnionFind {
	public int par[];
	public int rank[];

	UnionFind(int n) {
		par = new int[n];
		rank = new int[n];
		for (int i = 0; i < n; i++) {
			par[i] = i;
		}
	}

	public int find(int x) {
		if (par[x] == x)
			return x;
		else
			return par[x] = find(par[x]);
	}

	public void unite(int x, int y) {
		x = find(x);
		y = find(y);
		if (x == y)
			return;

		if (rank[x] < rank[y]) {
			par[x] = y;
		} else {
			par[y] = x;
			if (rank[x] == rank[y])
				rank[x]++;
		}
	}

	public boolean same(int x, int y) {
		return find(x) == find(y);
	}
}