import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();
		long X = sc.nextLong();
		long sum = N + func(Math.min(N-X, X), Math.max(N-X, X));
		System.out.println(sum);
		sc.close();
	}

	private static long func(long a, long b) {
		if (a==0) return -b;
		return 2*a*(long)(b/a)+func(b%a, a);
	}
}
