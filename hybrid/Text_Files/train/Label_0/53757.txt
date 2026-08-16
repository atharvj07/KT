import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[] a = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = sc.nextInt();
		}
		sc.close();

		int m = 0;
		int z = 0;
		int p = 0;
		for (int i = 0; i < n; i++) {
			if (a[i] == 0) {
				z++;
			} else if (a[i] > 0) {
				p++;
			} else {
				m++;
			}
		}

		boolean bz = false;
		if (z > 0) {
			bz = true;
		}
		boolean bp = false;
		if (p + m == k) {
			if (m % 2 == 0) {
				bp = true;
			}
		} else if (p + m > k) {
			if (p > 0 || k % 2 == 0) {
				bp = true;
			}
		}

		int mod = 1000000007;
		if (bp) {
			PriorityQueue<Integer> qp = new PriorityQueue<>((o1, o2) -> o2 - o1);
			PriorityQueue<Integer> qm = new PriorityQueue<>();
			for (int i = 0; i < n; i++) {
				if (a[i] > 0) {
					qp.add(a[i]);
				} else {
					qm.add(a[i]);
				}
			}
			qp.add(0);
			qp.add(0);
			qm.add(0);
			qm.add(0);

			long ans = 1;
			for (int i = 0; i < k; i++) {
				Integer np = qp.poll();
				Integer np2 = qp.poll();
				Integer nm = qm.poll();
				Integer nm2 = qm.poll();
				long vp = (long) np * np2;
				long vm = (long) nm * nm2;
				if (vp >= vm || i == k - 1) {
					ans *= np;
					qp.add(np2);
					qm.add(nm);
					qm.add(nm2);
				} else {
					ans *= vm % mod;
					qp.add(np);
					qp.add(np2);
					i++;
				}
				ans %= mod;
			}
			System.out.println(ans);

		} else if (bz) {
			System.out.println(0);

		} else {
			for (int i = 0; i < n; i++) {
				if (a[i] < 0) {
					a[i] = -a[i];
				}
			}
			Arrays.sort(a);
			long ans = 1;
			for (int i = 0; i < k; i++) {
				ans *= a[i];
				ans %= mod;
			}
			ans = mod - ans;
			ans %= mod;
			System.out.println(ans);
		}
	}
}
