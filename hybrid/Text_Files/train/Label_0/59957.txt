
import java.io.InputStream;
import java.io.PrintStream;
import java.util.Scanner;

/**
 */
public class MainB {
	public static void main(String[] args) {
		run(System.in, System.out);
	}

	public static void run(InputStream in, PrintStream out) {

		try (Scanner sc = new Scanner(in)) {
			int n = sc.nextInt();
			int a = sc.nextInt();
			int b = sc.nextInt();

			int r = n;
			while (r >= 0) {
				if (r % b == 0) {
					out.println("YES");
					out.print((n - r) / a + " " + r / b);
					return;
				}
				r -= a;
			}

			out.print("NO");
		}
	}

}