import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		int n = sc.nextInt();
		int[] a = new int[n];
		int ct = 0;
		for (int i = 0; i < n; i++) {
			a[i] = sc.nextInt() % 2;
			if (a[i] == 0) {
				ct++;
			}
		}
		if (ct == 0 || ct == n) {
			out.println(0);
		} else if ((n - ct) % 2 == 0) {
			out.println(n - 2);
		} else {

			out.println(n - 1);
		}
		out.flush();
	}
}
