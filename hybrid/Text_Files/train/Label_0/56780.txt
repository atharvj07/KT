import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		long pow = 1;
		for (int i = 1; i <= n; i++) {
			pow = pow * i % 1_000_000_007;
		}
		System.out.println(pow);
		sc.close();
	}

}