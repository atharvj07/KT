import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int N;

	public static void main(String[] args) throws Exception {
		N = sc.nextInt();
		int[] a = new int[N];
		for (int i = 0; i < N; ++i) {
			a[i] = sc.nextInt();
		}
		Arrays.sort(a);
		int cur = 0;
		while (cur < a.length && a[cur] == 0) {
			++cur;
		}
		int c0 = cur;
		while (cur < a.length && a[cur] == 1) {
			++cur;
		}
		int c1 = cur - c0;
		if (c0 % 2 == 0) {
			solve(cur, a);
			for (int i = 0; i < c0; ++i) {
				System.out.println(0);
			}
			for (int i = 0; i < c1; ++i) {
				System.out.println(1);
			}
		} else {
			if (c1 > 0) {
				solve(cur, a);
				for (int i = 0; i < c0 - 1; ++i) {
					System.out.println(0);
				}
				System.out.println(1);
				System.out.println(0);
				for (int i = 0; i < c1 - 1; ++i) {
					System.out.println(1);
				}
			} else {
				solve(cur + 1, a);
				for (int i = 0; i < c0 - 1; ++i) {
					System.out.println(0);
				}
				if (cur < a.length) {
					System.out.println(a[cur]);
				}
				System.out.println(0);
			}
		}
	}

	static void solve(int pos, int[] a) {
		if (pos <= a.length - 2 && a[a.length - 2] == 2 && a[a.length - 1] == 3) {
			for (int i = pos; i < a.length - 2; ++i) {
				System.out.println(2);
			}
			System.out.println(3);
			System.out.println(2);
			return;
		}
		for (int i = pos; i < a.length; ++i) {
			System.out.println(a[i]);
		}
	}

}