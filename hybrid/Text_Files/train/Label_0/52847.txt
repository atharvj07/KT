import java.util.*;
public class Za {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		String x = " ";
		for (int i = 1; i <= m; i++)
			x += i + " ";
		for (int j = 1; j <= n; j++) {
			int k = sc.nextInt();
			for (int l = 0; l < k; l++) {
				int p = sc.nextInt();
				if (x.contains(" " + p + " "))
					x = x.replaceAll(" " + p + " ", " ");
			}
		}
		boolean zaza = true;
		for (int q = 0; q < x.length(); q++) {
			if (Character.isDigit(x.charAt(q))) {
				zaza = false;
				break;
			}
		}
		if (zaza) System.out.print("YES");
		else System.out.print("NO");
	}
}