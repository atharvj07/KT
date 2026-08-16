import java.util.*;
import java.lang.*;
import java.math.*;

public class Main {
	Scanner sc = new Scanner(System.in);

	void run() {
		int h = sc.nextInt();
		int m = sc.nextInt();
		int p = sc.nextInt();
		int n = sc.nextInt();
		int k = sc.nextInt()+1;

		int b[] = new int[h + 1];

		for (int i = 0; i < n; i++) {
			b[h - sc.nextInt()] = sc.nextInt();
		}

		double[][] dp = new double[m][k];
		dp[p - 1][0] = 1;
		for (int i = 0; i < h; i++) {
			double dp2[][] = new double[m][k];
			if (b[i] != 0) {
				for (int j = 0; j < m; j++) {
					for (int s = 0; s < k; s++) {
						if (b[i] == j) {
							dp2[j][s] = dp[j - 1][s];
						} else if (b[i] == j + 1) {
							dp2[j][s] = dp[j + 1][s];
						} else {
							dp2[j][s] = dp[j][s];
						}
					}
				}
			} else {
				for (int j = 0; j < m; j++) {
					for (int s = 0; s < k; s++) {
						dp2[j][s] = dp[j][s];
					}
				}
				for (int j = 0; j < m; j++) {
					for (int s = 0; s < k - 1; s++) {
						for (int q = 1; q < m; q++) {
							if (q == j) {
								dp2[j][s + 1] += dp[j - 1][s];
							} else if (q == j + 1) {
								dp2[j][s + 1] += dp[j + 1][s];
							} else {
								dp2[j][s + 1] += dp[j][s];
							}
						}
					}
				}
			}
			dp = dp2;
//			System.out.println(Arrays.deepToString(dp));
//			System.out.println("--");
		}
		double sum = 0;
		double max = 0;
		for(int i =0 ; i < m;i++){
			sum += dp[i][k-1];
			max = Math.max(dp[i][k-1],max );
		}
		System.out.println(max/sum);
	}

	public static void main(String[] args) {
		Main m = new Main();
		m.run();
	}
}