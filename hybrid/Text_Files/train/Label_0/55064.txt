import java.util.Scanner;

public class Main{
	public static boolean isnum(char c) {
		return ('0' <= c && c <= '9');
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String s = sc.next();

		String s1[] = new String[n];

		for (int i = 0; i < n; i++) {
			s1[i] = sc.next();
		}

		for (int i = 0; i < n; i++) {

			if (s.equals(s1[i])) {
				System.out.println('+');
				continue;
			}
			int a = 0, b = 0;
			for (a = 0, b = 0; a < s.length() && b < s1[i].length();) {
				if (isnum(s.charAt(a)) && !isnum(s1[i].charAt(b))) {
					System.out.println('+');
					break;
				}
				if (!isnum(s.charAt(a)) && isnum(s1[i].charAt(b))) {
					System.out.println('-');
					break;
				}
				if (!isnum(s.charAt(a)) && !isnum(s1[i].charAt(b))) {
					if (s.charAt(a) < s1[i].charAt(b)) {
						System.out.println('+');
						break;
					} else if (s.charAt(a) > s1[i].charAt(b)) {
						System.out.println('-');
						break;
					}
				}
				if (isnum(s.charAt(a)) && isnum(s.charAt(b))) {
					int numa = 0, numb = 0;
					while (isnum(s.charAt(a)) && a < s.length()) {
						numa *= 10;

						numa += s.charAt(a) - '0';
						a++;

						if (a == s.length()) {

							break;
						}

					}
					while (isnum(s1[i].charAt(b)) && b < s1[i].length()) {
						numb *= 10;

						numb += s1[i].charAt(b) - '0';
						b++;
						if (b == s1[i].length()) {

							break;
						}
					}

					if (numa < numb) {
						System.out.println('+');
						break;
					}
					if (numb < numa) {
						System.out.println('-');
						break;
					}
					a--;
					b--;
				}
				a++;
				b++;
				if (a < s.length() && b >= s1[i].length()) {
					System.out.println('-');
					break;
				} else if (a >= s.length() && b < s1[i].length()) {
					System.out.println('+');
					break;
				}
			}

		}

	}
}

