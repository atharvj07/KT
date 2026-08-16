import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a, b;
		String x = "";
		while (true) {
			a = sc.nextInt();
			x = sc.next();
			b = sc.nextInt();
			if (x.equals("?"))
				break;
			if (x.equals("+"))
				System.out.println(a + b);
			if (x.equals("-"))
				System.out.println(a - b);
			if (x.equals("*"))
				System.out.println(a * b);
			if (x.equals("/"))
				System.out.println(a / b);
		}
	}
}
