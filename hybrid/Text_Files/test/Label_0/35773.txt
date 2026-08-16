
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n + 1];
		long[] sum = new long[n + 1];
		a[0] = 0;
		sum[0] = 0;
		for(int i = 1; i < n + 1; i++) {
			a[i] = sc.nextInt();
			sum[i] = sum[i - 1] + Math.abs(a[i] - a[i - 1]);
		}
		for(int i = 1; i < n + 1; i++) {
			long ans = 0;
			ans += sum[i - 1];
			if(i != n) {
				ans += Math.abs(a[i + 1] - a[i - 1]);
				ans += sum[n] - sum[i + 1];
				ans += Math.abs(a[n]);
			} else {
				ans += Math.abs(a[n - 1]);
			}
			System.out.println(ans);
		}

	}

}
