import java.io.PrintWriter;
import java.math.BigInteger;
import java.util.Scanner;

public class letsgooo {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int m = in.nextInt();
		PrintWriter out = new PrintWriter(System.out);
		BigInteger next = BigInteger.valueOf(n - 1);
		long newxt = next.nextProbablePrime().longValue();
		if (n == 2) {
			System.out.println(2 + " " + 2);
			System.out.println("1 2 2");
			return;
		}

		out.println(2 + " " + newxt);
		newxt -= n - 1;

		out.println(1 + " " + 2 + " " + newxt);
		m--;
		for (int i = 3; i <= n - 1; i++) {
			out.println(1 + " " + i + " " + 1);
			m--;
		}
		out.println(1 + " " + n + " " + 2);
		m--;
		for (int i = 2; i <= n && m > 0; i++) {
			for (int j = i + 1; j <= n && m > 0; j++) {
				out.println(i + " " + j + " " + 1000000000);
				m--;
			}
		}
		out.close();
	}

}
