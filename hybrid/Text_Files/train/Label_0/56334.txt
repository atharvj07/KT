import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		String a = s.next(), b = s.next();
		for (int i = 0; i < a.length(); i++) {
			System.out.print(a.charAt(i) + "" + b.charAt(i));
		}
	}

}
