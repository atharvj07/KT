import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String x = sc.next();
		String y = sc.next();

		if (x.equals(y.subSequence(0, y.length() - 1))) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}


		sc.close();
	}

}
