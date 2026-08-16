import java.util.Scanner;

public class Main {
	static char a[];
	static int id;
	static int n;

	public static int exp() {
		int left = term();
		while (true) {
			int c = a[id++];
			if (c == '+') {
				int right = term();
				left += right;
			} else if (c == '-') {
				int right = term();
				left -= right;
			} else {
				id--;
				break;
			}
		}
		return left;
	}

	public static int term() {
		int left = fact();
		while (true) {
			int c = a[id++];
			if (c == '*') {
				int right = fact();
				left *= right;
			} else if (c == '/') {
				int right = fact();
				left /= right;
			} else {
				id--;
				break;
			}
		}
		return left;
	}

	public static int fact() {
		int c = a[id++];
		if (c == '+') {
			return exp();
		} else if (c == '-') {
			return -exp();
		} else if (c == '(') {
			int left = exp();
			id++;
			return left;
		} else {
			int x = c - '0';
			while (true) {
				if (Character.isDigit(a[id])) {
					x *= 10;
					x += a[id++] - '0';
				} else {
					break;
				}
			}
			c = x;
		}
		return c;
	}

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
		while (m-- != 0) {
			a = sc.next().toCharArray();
			id = 0;
			n = a.length;
			System.out.println(exp());
		}
	}
}