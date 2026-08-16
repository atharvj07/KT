import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int total;
		int book;

		total = sc.nextInt();
		while (total != 0) {
			for (int i = 0; i < 9; i++) {
				total -= sc.nextInt();
			}
			System.out.println(total);
			total = sc.nextInt();
		}
	}
}