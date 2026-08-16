import java.nio.charset.IllegalCharsetNameException;
import java.util.*;
import java.lang.*;


public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[] a = new long[n];
		for (int i = 0; i < n; i++) {
			a[i] = sc.nextLong();
		}
		long oddsum = 0;
		long oddcount = 0;
		for (int i = 0; i < n / 2; i++) {
			oddsum += a[2 * i];
			if (oddsum <= 0) {
				oddcount += Math.abs(1 - oddsum);
				oddsum = 1;
			}
			oddsum += a[2 * i + 1];
			if (oddsum >= 0) {
				oddcount += Math.abs(-1 - oddsum);
				oddsum = -1;
			}
		}
		long evensum = 0;
		long evencount = 0;
		for (int i = 0; i < n / 2; i++) {
			evensum += a[2 * i];
			if (evensum >= 0) {
				evencount += Math.abs(-1 - evensum);
				evensum = -1;
			}
			evensum += a[2 * i + 1];
			if (evensum <= 0) {
				evencount += Math.abs(1 - evensum);
				evensum = 1;
			}
		}
		if (n % 2 != 0) {
			oddsum += a[n - 1];
			if (oddsum <= 0) {
				oddcount += Math.abs(1 - oddsum);
				oddsum = 1;
			}
			evensum += a[n - 1];
			if (evensum >= 0) {
				evencount += Math.abs(-1 - evensum);
				evensum = -1;
			}
		}
		System.out.println(Math.min(oddcount, evencount));
	}
}