
import java.awt.Polygon;
import java.awt.geom.Line2D;
import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			int n = scanner.nextInt();
			if (n == 0)
				break;
			while (n-- > 0) {
				int m = scanner.nextInt();
				Polygon[] polygons = new Polygon[m];
				Line2D[][] lines = new Line2D[m][4];
				for (int i = 0; i < m; i++) {
					int[] xx = new int[4];
					int[] yy = new int[4];
					for (int j = 0; j < 4; j++) {
						xx[j] = scanner.nextInt();
						yy[j] = scanner.nextInt();
					}
					for (int k = 0; k < 4; k++) {
						lines[i][k] = new Line2D.Double(xx[k], yy[k],
								xx[(k + 1) % 4], yy[(k + 1) % 4]);
					}
					polygons[i] = new Polygon(xx, yy, 4);
				}

				Unionfin unionfin = new Unionfin(m);
				for (int j = 0; j < m - 1; j++) {
					for (int j2 = j + 1; j2 < m; j2++) {
						if (unionfin.isSame(j, j2))
							continue;
						boolean flag = false;
						if (polygons[j].contains(polygons[j2].xpoints[0],
								polygons[j2].ypoints[0])
								|| polygons[j2].contains(
										polygons[j].xpoints[0],
										polygons[j].ypoints[0])) {
							flag = true;
						} else {
							for (int k = 0; k < 4; k++) {
								for (int k2 = 0; k2 < 4; k2++) {
									if (lines[j][k]
											.intersectsLine(lines[j2][k2])) {
										flag = true;
										break;
									}
								}
							}
						}
						if (flag)
							unionfin.unite(j, j2);
					}
				}
				System.out.println(unionfin.num);
			}
		}
	}

	class Unionfin {
		int[] rank, par;
		int num;

		Unionfin(int size) {
			rank = new int[size];
			par = new int[size];
			num = size;
			for (int i = 0; i < size; i++) {
				par[i] = i;
			}
		}

		int root(int x) {
			if (par[x] == x)
				return x;
			else
				return par[x] = root(par[x]);
		}

		boolean isSame(int x, int y) {
			return root(x) == root(y);
		}

		void unite(int x, int y) {
			x = root(x);
			y = root(y);
			if (x == y)
				return;
			if (rank[x] < rank[y])
				par[x] = y;
			else {
				par[y] = x;
				if (rank[x] == rank[y])
					rank[x]++;
			}
			num--;
		}

	}
}