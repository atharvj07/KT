import java.util.*;
import java.lang.*;

public class Main {
	static long mod = 998244353;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[] a = new long[n];
		int count = 0;
		for (int i = 0; i < n; i++) {
			a[i] = sc.nextLong();
			if (a[i] < 0) {
				count++;
			}
		}
		long ans = 0;
		if (count % 2 == 0) {
			for (int i = 0; i < n; i++) {
				ans += Math.abs(a[i]);
			}
		} else {
			long min = 1000000001;
			for (int i = 0; i < n; i++) {
				if (Math.abs(a[i]) < min) {
					min = Math.abs(a[i]);
				}
			}
			for (int i = 0; i < n; i++) {
				ans += Math.abs(a[i]);
			}
			ans -= min * 2;
		}
		System.out.println(ans);
	}
}