import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		final Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
		if(a+b < c) {
			System.out.println("No");
		} else {
			System.out.println("Yes");
		}
	}
}