import java.util.Scanner;
import java.io.PrintStream;

public class TaskC {

	public static Scanner in = new Scanner(System.in);
	public static PrintStream out = System.out;

	public static void main(String[] args) {
		int n = in.nextInt();
		int m = in.nextInt();
		int maximum = 0;
		int dPrev = 0, hPrev = 0;
		boolean possible = true;
		for (int i = 0; i < m && possible; i++) {
			int d = in.nextInt();
			int h = in.nextInt();
			maximum = Math.max(maximum, h);
			if (i == 0) {
				maximum = Math.max(maximum, h + d - 1);
			}
			if (i == m - 1) {
				maximum = Math.max(maximum, h + n - d);
			}
			if (i > 0) {
				if (Math.abs(h - hPrev) > d - dPrev) {
					possible = false;
				}
				else {
					int delta = (d - dPrev + h - hPrev) / 2;
					maximum = Math.max(maximum, hPrev + delta);
				}
			}
			dPrev = d;
			hPrev = h;
		}
		if (possible) {
			System.out.println(maximum);
		}
		else {
			System.out.println("IMPOSSIBLE");
		}
	}

}