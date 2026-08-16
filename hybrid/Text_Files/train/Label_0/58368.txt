import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		String s = sc.next();
		String t = sc.next();
		int x = s.length();
		int y = t.length();
		int[][] dp = new int[x + 10][y + 10];

		for (int i = 0; i < x; i++) {
			for (int j = 0; j < y; j++) {
				if (s.charAt(i) == t.charAt(j)) {
					dp[i + 1][j + 1] = Math.max(dp[i + 1][j + 1], dp[i][j] + 1);
				}
				dp[i + 1][j + 1] = Math.max(dp[i + 1][j + 1], dp[i + 1][j]);
				dp[i + 1][j + 1] = Math.max(dp[i + 1][j + 1], dp[i][j + 1]);
			}
		}

//		for(int i=0; i<=x; i++) {
//			for (int j=0; j<=y; j++) {
//				System.out.print(dp[i][j]+"\t");
//			}
//			System.out.println();
//		}

		String ans = "";

		while (x > 0 && y > 0) {
			if (dp[x][y] == dp[x - 1][y]) {
				x--;
			} else if (dp[x][y] == dp[x][y - 1]) {
				y--;
			} else {
				ans = s.charAt(x - 1) + ans;
				x--;
				y--;
			}
		}

		System.out.println(ans);
		sc.close();
	}
}