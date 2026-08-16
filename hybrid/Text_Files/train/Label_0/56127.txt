import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n, a[];
		long psum[], sum = 0;
		n = sc.nextInt();
		a = new int[n];
		psum = new long[n];
		for (int i = 0; i < n; ++i) {
			a[i] = sc.nextInt();
			sum += a[i];
			psum[i] = sum;
		}
		sc.close();

		long min = (long)Math.pow(10,  10), sub;

		for (int i = 0; i < n - 1; ++i) {
			sub = Math.abs(sum - 2 * psum[i]);
			min = Math.min(min, sub);
		}

		System.out.println(min);
	}

}
