import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		Long N = scan.nextLong();

		System.out.println((double)(N - Math.floor(N/2)) / N);

	}
}