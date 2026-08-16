import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		while (true) {
			int n = sc.nextInt();
			if (n == 0)
				break;
			int m = sc.nextInt();
			char[] s = sc.next().toCharArray();
			if (m < 3) {
				System.out.println(0);
				continue;
			}
			int ans = 0;
			int c = 0;
			for (int i = 2; i < m; i++) {
				if (s[i] == 'I' && s[i - 1] == 'O' && s[i - 2] == 'I') {
					c++;
				} else if (s[i] == 'O' && s[i - 1] == 'I' && s[i - 2] == 'O') {
					;
				} else {
					ans += Math.max(0, c - n + 1);
					c = 0;
				}
			}
			System.out.println(ans);
		}
	}
}