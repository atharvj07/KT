import java.util.Scanner;

public class Main {

	private static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int a = sc.nextInt(), b = sc.nextInt(), k = sc.nextInt();
		for (int i = 0; i < k; i++) {
			if (i % 2 == 0) {
				a /= 2;
				b += a;
			} else {
				b /= 2;
				a += b;
			}
		}
		System.out.println(a + " " + b);
	}
}