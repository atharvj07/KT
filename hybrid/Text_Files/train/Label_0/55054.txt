import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

class Main {
	public static void main(String[] args) throws IOException {
		new Main().run();
	}

	int N;
	long A, B;
	int[] r;// nutrition value
	int[] s;// deliciousness value
	int[] sum;

	void run() {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		A = sc.nextLong();
		B = sc.nextLong();
		r = new int[N];
		s = new int[N];
		sum = new int[N];
		for (int i = 0; i < N; ++i) {
			r[i] = sc.nextInt();
			s[i] = sc.nextInt();
		}
		for (int i = N - 1; i >= 0; --i) {
			sum[i] = (i + 1 < N ? sum[i + 1] : 0) + s[i];
		}
		solve();
	}

	void solve() {
		boolean[] num = new boolean[151];
		num[0] = true;
		for (int v : s) {
			for (int i = 150; i >= 0; --i) {
				if (num[i])
					num[i + v] |= num[i];
			}
		}
		ArrayList<Integer> lis = new ArrayList<>();
		for (int i = 0; i <= 150; ++i) {
			if (num[i])
				lis.add(i);
		}
		long diff = A - B;
		int high = lis.size();
		int low = 0;
		while (high - low > 1) {
			int middle = (high + low) / 2;
			if (diff >= f(lis.get(middle), 0, false)) {
				low = middle;
			} else {
				high = middle;
			}
		}
		System.out.println(lis.get(low) + " " + (sum[0] - lis.get(low)));
	}

	HashMap<List<Integer>, Long> map = new HashMap<>();

	long f(int p, int k, boolean f) {
		if (p <= 0) {
			return -Long.MAX_VALUE / 16;
		} else if (p > sum[k]) {
			return Long.MAX_VALUE / 16;
		}
		if (k == N - 1) {
			if (sum[k] >= p)
				return -Long.MAX_VALUE / 16;
			else
				return Long.MAX_VALUE / 16;
		}
		if (map.containsKey(toList(p, k, f))) {
			return map.get(toList(p, k, f));
		}
		long ret = Long.MAX_VALUE / 16;
		// f????????°A-B<=0??§???????????¨???????¨????????????????????????°????????????
		if (!f) {
			long zeta = f(sum[k] - p + 1, k, true);
			ret = Math.max(1, 2 - zeta);
		}
		long xi = f(sum[k + 1] - (p - s[k]) + 1, k + 1, false);
		ret = Math.min(ret, 1 + (-xi - r[k]));
		map.put(toList(p, k, f), ret);
		return ret;
	}

	List<Integer> toList(int p, int k, boolean f) {
		List<Integer> lis = new ArrayList<>();
		lis.add(p);
		lis.add(k);
		lis.add(f ? 1 : 0);
		return lis;
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}