import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		new Main().run();
	}

	static int N;
	static int[] d;
	static int[] cnt;
	static int[] ans;
	static int L;
	static ArrayList<int[]> ansLis;

	void run() {
		Scanner sc = new Scanner(System.in);
		while (true) {
			N = sc.nextInt();
			if (N == 0)
				break;
			ans = new int[N];
			cnt = new int[401];
			Arrays.fill(ans, -1);
			d = new int[N * (N - 1) / 2];
			for (int i = 0; i < d.length; ++i) {
				d[i] = sc.nextInt();
				++cnt[d[i]];
			}
			L = d[0];
			ans[0] = 0;
			ans[N - 1] = L;
			--cnt[L];
			ansLis = new ArrayList<>();
			solve(0, N - 1);

			ansLis.sort(new Comparator<int[]>() {
				@Override
				public int compare(int[] o1, int[] o2) {
					for (int i = 0; i < o1.length; ++i) {
						if (o1[i] != o2[i])
							return Integer.compare(o1[i], o2[i]);
					}
					return 0;
				}
			});

			for (int i = 0; i + 1 < ansLis.size(); ++i) {
				while (i + 1 < ansLis.size() && sameArr(ansLis.get(i), ansLis.get(i + 1))) {
					ansLis.remove(i + 1);
				}
			}

			for (int i = 0; i < ansLis.size(); ++i) {
				for (int j = 0; j < N - 1; ++j) {
					System.out.print(ansLis.get(i)[j]);
					System.out.print(j + 1 == N - 1 ? "\n" : " ");
				}
			}
			System.out.println("-----");
		}
	}

	boolean sameArr(int[] arr1, int[] arr2) {
		for (int i = 0; i < arr1.length; ++i) {
			if (arr1[i] != arr2[i])
				return false;
		}
		return true;
	}

	void solve(int left, int right) {
		if (right - left == 1) {
			for (int v : cnt) {
				if (v != 0)
					return;
			}
			int[] arr = new int[N - 1];
			for (int i = 0; i + 1 < N; ++i) {
				arr[i] = ans[i + 1] - ans[i];
			}
			ansLis.add(arr);
		}
		for (int i = cnt.length - 1; i >= 0; --i) {
			if (cnt[i] == 0)
				continue;
			boolean f = true;
			for (int j = 0; j < ans.length; ++j) {
				--cnt[Math.abs(i - ans[j])];
				if (cnt[Math.abs(i - ans[j])] < 0) {
					f = false;
				}
				if (j == left)
					j = right - 1;
			}
			ans[right - 1] = i;
			if (f) {
				solve(left, right - 1);
			}
			ans[left + 1] = -1;
			for (int j = 0; j < ans.length; ++j) {
				++cnt[Math.abs(i - ans[j])];
				if (j == left)
					j = right - 1;
			}
			f = true;
			for (int j = 0; j < ans.length; ++j) {
				--cnt[Math.abs(L - i - ans[j])];
				if (cnt[Math.abs(L - i - ans[j])] < 0) {
					f = false;
				}
				if (j == left)
					j = right - 1;
			}
			ans[left + 1] = L - i;
			if (f) {
				solve(left + 1, right);
			}
			ans[right - 1] = -1;
			for (int j = 0; j < ans.length; ++j) {
				++cnt[Math.abs(L - i - ans[j])];
				if (j == left)
					j = right - 1;
			}
			break;
		}

	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}

}