import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int x = scanner.nextInt(),y = scanner.nextInt(),z = scanner.nextInt();
		int result = (x-z)/(y+z);
		System.out.println(result);
	}

}
