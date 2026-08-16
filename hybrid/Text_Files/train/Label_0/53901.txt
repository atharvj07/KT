import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int N, M, K;
	static int[] A, B;

	public static void main(String[] args) {
		N = sc.nextInt();
		M = sc.nextInt();
		K = sc.nextInt();
		A = new int[N];
		B = new int[N];
		for (int i = 0; i < N; ++i) {
			A[i] = sc.nextInt();
		}
		for (int i = 0; i < N; ++i) {
			B[i] = sc.nextInt();
		}
		boolean[] used = new boolean[N];
		System.out.println(rec(0, M, used));
	}

	static int rec(int idx, int rest, boolean[] used) {
		if (idx == K) return rest;
		if (rest == 0) return 0;
		int ret = 0;
		for (int i = 0; i < N; ++i) {
			if (used[i]) continue;
			int use = Math.min(rest, B[i]);
			used[i] = true;
			ret = Math.max(ret, use * A[i] + rec(idx + 1, rest - use, used));
			used[i] = false;
		}
		return ret;
	}
}