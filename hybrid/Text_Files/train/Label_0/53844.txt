
import java.util.Scanner;

public class Main{
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		int n = Integer.parseInt(scanner.nextLine());
		String[] list = scanner.nextLine().split(" ");
		int[] aaa = new int[n];

		for(int i = 0; i < n; i++) {

			aaa[i] = Integer.parseInt(list[i]);

		}

		int ans = 0;

		for(int i = 0; i < n; i++) {

			ans = Main.gcd(aaa[i], ans);


		}



		System.out.println(ans);
	}

	public static Integer gcd(int a, int b) {

		return b == 0 ? a : gcd(b, a % b);

	}
}

