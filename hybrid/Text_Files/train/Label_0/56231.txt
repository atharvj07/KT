import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		while (scanner.hasNext()) {
			int a = scanner.nextInt();
			int b = scanner.nextInt();
			int sum = a + b;
			int count = 0;
			while (sum > 0) {
				sum /= 10;
				count ++;
			}
			System.out.println(count);
		}
	}
}