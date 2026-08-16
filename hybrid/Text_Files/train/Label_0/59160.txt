import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		new Main().run();
	}

	void run() {
		Scanner sc = new Scanner(System.in);
		while (true) {
			int H = sc.nextInt();
			int W = sc.nextInt();
			if (H == 0 && W == 0)
				break;
			char[][] initial_map = new char[H][W];
			char[][] desired_map = new char[H][W];
			for (int i = 0; i < H; ++i) {
				initial_map[i] = sc.next().toCharArray();
			}
			for (int i = 0; i < H; ++i) {
				desired_map[i] = sc.next().toCharArray();
			}

			solve(H, W, initial_map, desired_map);
		}
	}

	void solve(int H, int W, char[][] initial_map, char[][] desired_map) {
		int cnt = 1;
		for (int i = 1; i <= H + W; ++i) {
			cnt *= i;
		}
		for (int i = 1; i <= H; ++i) {
			cnt /= i;
		}
		for (int i = 1; i <= W; ++i) {
			cnt /= i;
		}
		// the number of the states is cnt

		ArrayList<ArrayList<Integer>> lis = dfs(H, W, 0, H);
		lis = reverse(lis);

		int idx = 0;
		HashMap<List<Integer>, Integer> numbering = new HashMap<>();

		for (ArrayList<Integer> a : lis) {
			numbering.put(a, idx++);
		}

		// numbering is done.

		char[] col = { 'B', 'W' };
		double[][] mx = new double[cnt][cnt];
		double[][] v = new double[cnt][1];
		for (int i = 0; i < cnt; ++i) {
			v[i][0] = -1d / 4 * (W + 1) * (H + 1);
		}
		for (int i = 0; i < cnt; ++i) {
			mx[i][i] = -1;
		}
		Arrays.fill(mx[cnt - 1], 0);
		v[cnt - 1][0] = 0;
		for (Entry<List<Integer>, Integer> entry : numbering.entrySet()) {
			List<Integer> arr = entry.getKey();
			int curIdx = entry.getValue();
			if (curIdx == idx - 1)
				continue;
			boolean[][] bMap = to_map(arr, H, W);
			for (char c : col) {
				for (int i = 0; i < H; ++i) {
					for (int j = 0; j < W; ++j) {
						ArrayList<Integer> tmp = paint(bMap, H, W, i, j, c, desired_map);
						int nidx = numbering.get(tmp);
						mx[curIdx][nidx] += 1d / (2 * H * W);
					}
				}
			}
		}

		int id = numbering.get(to_arr(initial_map, H, W, desired_map));
		double ans = MtPrd(Rev(mx), v)[id][0];
		System.out.printf("%.20f\n", ans);
	}

	ArrayList<ArrayList<Integer>> dfs(int H, int W, int curIdx, int curHeight) {
		ArrayList<ArrayList<Integer>> ret = new ArrayList<>();
		if (curIdx == W) {
			ret.add(new ArrayList<>());
			return ret;
		}
		for (int i = curHeight; i >= 0; --i) {
			ArrayList<ArrayList<Integer>> tmp = dfs(H, W, curIdx + 1, i);
			for (ArrayList<Integer> lis : tmp) {
				lis.add(i);
				ret.add(lis);
			}
		}
		return ret;
	}

	// the color is incorrect:false
	// the color is correct:true
	boolean[][] to_map(List<Integer> lis, int H, int W) {
		boolean[][] map = new boolean[H][W];

		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				map[i][j] = true;
			}
		}

		for (int i = 0; i < W; ++i) {
			for (int j = lis.get(i) - 1; j >= 0; --j) {
				map[j][i] = false;
			}
		}
		return map;

	}

	ArrayList<Integer> to_arr(char[][] src, int H, int W, char[][] dst) {
		ArrayList<Integer> lis = new ArrayList<>();
		for (int i = 0; i < W; ++i) {
			lis.add(0);
		}

		for (int k = H + W - 2; k >= 0; --k) {
			for (int i = 0; i < H; ++i) {
				int j = k - i;
				if (j < 0 || j >= W)
					continue;
				if (dst[i][j] == src[i][j])
					continue;
				lis = paint(to_map(lis, H, W), H, W, i, j, src[i][j], dst);
			}
		}
		return lis;
	}

	ArrayList<Integer> paint(boolean[][] bMap, int H, int W, int h, int w, char c, char[][] dst) {
		boolean[][] map = new boolean[H][W];
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				map[i][j] = bMap[i][j];
			}
		}
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (i <= h && j <= w) {
					map[i][j] = (dst[i][j] == c);
				}
			}
		}

		for (int k = H + W - 2; k >= 0; --k) {
			for (int i = 0; i < H; ++i) {
				int j = k - i;
				if (j < 0 || j >= W)
					continue;
				if (!map[i][j]) {
					for (int ii = 0; ii <= i; ++ii) {
						for (int jj = 0; jj <= j; ++jj) {
							map[ii][jj] = false;
						}
					}
				}
			}
		}

		ArrayList<Integer> ret = new ArrayList<>();
		for (int i = 0; i < W; ++i) {
			int cnt = 0;
			for (int j = 0; j < H; ++j) {
				if (!map[j][i])
					++cnt;
			}
			ret.add(cnt);
		}
		return ret;
	}

	ArrayList<ArrayList<Integer>> reverse(ArrayList<ArrayList<Integer>> lis) {
		ArrayList<ArrayList<Integer>> ret = new ArrayList<>();
		for (ArrayList<Integer> a : lis) {
			ArrayList<Integer> tmp = new ArrayList<>();
			for (int i = a.size() - 1; i >= 0; --i) {
				tmp.add(a.get(i));
			}
			ret.add(tmp);
		}
		return ret;

	}

	public static double[][] Rev(double[][] OM) {
		int n = OM.length, m = OM[0].length;
		if (n != m)
			return null;

		double[][] M = new double[n][2 * n];
		m = 2 * n;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				M[i][j] = OM[i][j];
			}
			M[i][n + i] = 1;
		}

		double[][] res = operateElementarily(M);
		if (res == null)
			return null;

		// resotration
		double[][] ret = new double[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				ret[i][j] = res[i][j + n];
			}
		}

		return ret;
	}

	public static double[][] operateElementarily(double[][] M) {
		int n = M.length, m = M[0].length;
		int rank = n - 1;

		// Forward Elimination
		for (int i = 0; i < n; i++) {
			// select pivot
			double max = 1E-9;
			int maxj = -1;
			for (int j = i; j < n; j++) {
				double v = Math.abs(M[j][i]);
				if (v > max) {
					max = v;
					maxj = j;
				}
			}
			if (maxj == -1) {
				rank = i - 1;
				break;
			}
			if (maxj != i) {
				double[] dum = M[i];
				M[i] = M[maxj];
				M[maxj] = dum;
			}

			double D = M[i][i];
			M[i][i] = 1;
			for (int j = i + 1; j < m; j++) {
				M[i][j] /= D;
			}

			for (int j = i + 1; j < n; j++) {
				double B = -M[j][i];
				M[j][i] = 0;
				for (int k = i + 1; k < m; k++) {
					M[j][k] += M[i][k] * B;
				}
			}
		}

		// Back Substitution
		for (int i = rank; i >= 0; i--) {
			for (int j = rank; j >= i + 1; j--) {
				double B = -M[i][j];
				M[i][j] = 0;
				for (int k = rank + 1; k < m; k++) {
					M[i][k] += B * M[j][k];
				}
			}
		}

		return M;
	}

	double[][] MtPrd(double[][] A, double[][] B) {
		double[][] C = new double[A.length][B[0].length];
		for (int i = 0; i < A.length; i++) {
			for (int j = 0; j < B[0].length; j++) {
				for (int k = 0; k < A[0].length; k++) {
					C[i][j] += A[i][k] * B[k][j];
				}
			}
		}
		return C;
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}