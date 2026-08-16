import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		try (Scanner scn = new Scanner(System.in)) {
			final long N = scn.nextLong();
			if (N % 2 == 1) {
				System.out.println(0);
			} else {
				long ret = 0;
				for (long l = N / 5; l > 0; l /= 5) {
					ret += l / 2;
				}
				System.out.println(ret);
			}
		}
	}
}
