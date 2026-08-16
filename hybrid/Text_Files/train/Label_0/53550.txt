import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int A, B, C;

	public static void main(String[] args) {
		while (true) {
			A = sc.nextInt();
			if (A == 0) break;
			B = sc.nextInt();
			int rem = B - A;
			int t = rem / 1000;
			rem -= t * 1000;
			int f = rem / 500;
			rem -= f * 500;
			System.out.println(rem / 100 + " " + f + " " + t);
		}
	}

}