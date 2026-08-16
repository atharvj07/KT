import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int sum = A + B;
		if (sum % 2 == 0) {
			System.out.println(sum / 2);
		} else {
			System.out.println("IMPOSSIBLE");
		}
		sc.close();
	}
}