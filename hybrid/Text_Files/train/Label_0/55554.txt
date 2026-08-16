import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int age = Integer.parseInt(scan.next());
		if (age == 1) {
			System.out.println("Hello World");
		} else {
			int A = Integer.parseInt(scan.next());
			int B = Integer.parseInt(scan.next());
			System.out.println(A + B);
		}
	}
}
