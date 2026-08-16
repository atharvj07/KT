import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int N, M;
	static int[] MP, CP, sum;
	static Colony[] cats;

	public static void main(String[] args) {
		while (true) {
			N = sc.nextInt();
			M = sc.nextInt();
			if (M == 0) break;
			cats = new Colony[N];
			int hi = 0;
			int[] cc = new int[20001];
			for (int i = 0; i < N; ++i) {
				int x = sc.nextInt() + 10000;
				sc.nextInt();
				cc[x] += sc.nextInt();
			}
			ArrayList<Colony> cats = new ArrayList<Colony>();
			cats.add(new Colony(-20000, 0));
			for (int i = 0; i < cc.length; ++i) {
				if (cc[i] != 0) cats.add(new Colony(i, cc[i]));
				hi += cc[i];
			}
			Collections.sort(cats);
			CP = new int[cats.size()];
			sum = new int[cats.size()];
			for (int i = 0; i < CP.length; ++i) {
				CP[i] = cats.get(i).x;
				if (i > 0) sum[i] = sum[i - 1] + cats.get(i).c;
			}
			MP = new int[M];
			for (int i = 0; i < M; ++i) {
				MP[i] = sc.nextInt() + 10000;
			}
			Arrays.sort(MP);
			int lo = 0;
			while (hi - lo > 1) {
				int mid = (hi + lo) / 2;
				if (ok(mid)) {
					hi = mid;
				} else {
					lo = mid;
				}
			}
			System.out.println(hi);
		}
	}

	static boolean ok(int num) {
		int[] dp = new int[M];
		Arrays.fill(dp, 1 << 30);
		dp[0] = count(MP[0]);
		for (int i = 1; i < M; ++i) {
			for (int j = i - 1; j >= 0; --j) {
				int add = count((MP[i] + MP[j]) / 2) - count(MP[j]);
				if (dp[j] + add > num) continue;
				dp[i] = count(MP[i]) - count((MP[i] + MP[j]) / 2);
				break;
			}
		}
		return dp[M - 1] + sum[sum.length - 1] - count(MP[M - 1]) <= num;
	}

	static int count(int pos) {
		int idx = Arrays.binarySearch(CP, pos);
		if (idx < 0) {
			idx = -idx - 2;
		}
		return sum[idx];
	}

	static class Colony implements Comparable<Colony> {
		int x, c;

		public Colony(int x, int c) {
			this.x = x;
			this.c = c;
		}

		public int compareTo(Colony o) {
			return this.x - o.x;
		}
	}

}