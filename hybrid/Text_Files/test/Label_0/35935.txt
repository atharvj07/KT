import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		String s = sc.next();
		String msg = "Good";

		for (int i = 0; i < 3; i++) {
			if (s.substring(i, i + 1).equals(s.substring(i + 1, i + 2))) {
				msg = "Bad";
			}
		}

		System.out.println(msg);

	}
}
