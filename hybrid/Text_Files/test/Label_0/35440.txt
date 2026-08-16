import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Scanner;

class Main {
	static double dist;
	static int n;
	static double[] S;
	static int m;
	static double[] D;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		dist = sc.nextDouble();
		n = sc.nextInt();
		S = new double[n];
		for (int i = 0; i < n; ++i) {
			S[i] = sc.nextDouble();
		}
		m = sc.nextInt();
		D = new double[m];
		for (int i = 0; i < m; ++i) {
			D[i] = sc.nextDouble();
		}

		int[] ord1 = new int[n];// ord1[i]:i???????????????????????¬??????ord1[i]
		int[] ord2 = new int[n];// ord2[i]:i??????????????¶??????ord2[i]???????????????????????¬???
		for (int i = 0; i < n; ++i) {
			ord1[i] = i;
		}

		double ans = Double.MAX_VALUE / 10;
		// do {
		for (int i = 0; i < n; ++i) {
			ord2[i] = i;
		}
		do {
			if (ord2[0] != 0)
				continue;
			double[] departTime = new double[n];
			Arrays.fill(departTime, -1);
			departTime[0] = 0;
			ans = Math.min(ans, dfs(ord1, ord2, departTime, 1));
		} while (nextPermutation(ord2));
		// } while (nextPermutation(ord1));
		System.out.println((long) ans);
	}

	// ord1[i]:i???????????????????????¬??????ord1[i]
	// ord2[i]:i??????????????¶??????ord2[i]???????????????????????¬???
	// departTime[i]:i???????????????????????¬????????????

	static double dfs(int[] ord1, int[] ord2, double[] departTime, int cnt) {
		double ans = Double.MAX_VALUE / 10;
		double[] env = new double[m + 1];
		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < n; ++j) {
				if (departTime[j] == -1)
					continue;
				env[i] = Math.max(env[i], S[ord1[j]] * D[i] + departTime[j]);
			}
		}
		for (int i = 0; i < n; ++i) {
			if (departTime[i] == -1)
				continue;
			env[m] = Math.max(env[m], S[ord1[i]] * dist + departTime[i]);
		}
		if (cnt == n) {
			return env[m];
		}
		int curIdx1 = ord2[cnt];
		if (departTime[curIdx1 - 1] != -1) {
			if (check(ord1, ord2, curIdx1, departTime[curIdx1 - 1] + 1, departTime)) {
				departTime[curIdx1] = departTime[curIdx1 - 1] + 1;
				ans = Math.min(ans, dfs(ord1, ord2, departTime, cnt + 1));
				departTime[curIdx1] = -1;
			}
		}

		for (int i = 0; i <= m; ++i) {
			double curDepartTime = env[i] - S[ord1[curIdx1]] * (i == m ? dist : D[i]);
			if (curDepartTime <= 0)
				continue;
			if (check(ord1, ord2, curIdx1, curDepartTime, departTime)) {
				departTime[curIdx1] = curDepartTime;
				ans = Math.min(ans, dfs(ord1, ord2, departTime, cnt + 1));
				departTime[curIdx1] = -1;
			}
		}
		return ans;

	}

	static boolean check(int[] ord1, int[] ord2, int curIdx1, double curDepartTime, double[] departTime) {
		for (int i = 0; i < n; ++i) {
			if (departTime[i] == -1)
				continue;
			if (i < curIdx1 && departTime[i] + 1 > curDepartTime)
				return false;
			if (curIdx1 < i && curDepartTime + 1 > departTime[i])
				return false;
		}
		for (int i = 0; i < n; ++i) {
			if (i == curIdx1 || departTime[i] == -1)
				continue;
			double crossX = -(departTime[i] - curDepartTime) / (S[ord1[i]] - S[ord1[curIdx1]]);
			if (S[ord1[i]] - S[ord1[curIdx1]] == 0)
				continue;
			if (0 < crossX && crossX < dist - 1e-6) {
				boolean f = false;
				for (int j = 0; j < m; ++j) {// X=D??\???????????§??´???cur??¨??´???i???????????£?????????????????????
					if (Math.abs(crossX - D[j]) < 1e-6)
						f = true;
				}
				if (!f)
					return false;
			}
		}
		for (int i = 0; i < m; ++i) {// X=Di??§2?????\??????????????¨????????£?????????????????????
			double curHeight = S[ord1[curIdx1]] * D[i] + curDepartTime;
			int cnt = 0;
			for (int j = 0; j < n; ++j) {
				if (j == curIdx1 || departTime[j] == -1)
					continue;
				double height = S[ord1[j]] * D[i] + departTime[j];
				if (Math.abs(curHeight - height) < 1e-6)
					++cnt;
			}
			if (cnt > 1)
				return false;
		}
		return true;
	}

	static boolean nextPermutation(int[] ord) {
		int len = ord.length;
		int i = len - 1;
		while (i > 0 && ord[i - 1] > ord[i])
			--i;
		if (i == 0)
			return false;
		int j = i;
		while (j + 1 < len && ord[j + 1] > ord[i - 1])
			++j;
		int tmp = ord[i - 1];
		ord[i - 1] = ord[j];
		ord[j] = tmp;
		int s = i;
		int t = len - 1;
		while (t - s > 0) {
			tmp = ord[s];
			ord[s] = ord[t];
			ord[t] = tmp;
			++s;
			--t;
		}
		return true;
	}

	static void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}