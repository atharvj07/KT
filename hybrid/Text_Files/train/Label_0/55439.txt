import java.util.Arrays;
import java.util.Scanner;

public class Main {

	@SuppressWarnings("resource")
	public static void main(String args[]) {
		Scanner scanner = new Scanner(System.in);
		int a = scanner.nextInt();
		int b = scanner.nextInt();
		int c = scanner.nextInt();
		int[] h = new int[3];

		h[0] = a;
		h[1] = b;
		h[2] = c;

		Arrays.sort(h);

		System.out.println(h[0] + h[1]);
	}
}
