
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int a = scanner.nextInt();
		int[] b = new int[a];
		for (int i = 0; i < a; i++)
			b[i] = scanner.nextInt();
		for (int i = b.length - 1; i >= 0; i--) {
			if (i == b.length - 1)
				System.out.print(b[i]);
			else
				System.out.print(" " + b[i]);
		}
		System.out.println();
	}
}