import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        try (Scanner in = new Scanner(System.in)) {
            int L = in.nextInt();
            int[] A = new int[L];
            for (int i = 0; i < L; i++) {
                A[i] = in.nextInt();
//                A[i] = A[i] % 2 == 0 ? (A[i] == 0 ? 0 : 2) : 1;
            }

            long[][] dp = new long[L + 1][5];
            for (int i = 0; i <= L; i++) {
                if (i == 0) {
                    dp[i][0] = A[i];
                    dp[i][1] = (A[i] == 0 ? 0 : (A[i] % 2 == 0 ? 0 : 1));
                    dp[i][2] = (A[i] == 0 ? 0 : (A[i] % 2 == 0 ? 1 : 0));
                    dp[i][3] = (A[i] == 0 ? 0 : (A[i] % 2 == 0 ? 0 : 1));
                    dp[i][4] = A[i];
//                    Utils.debug("dp[" + i + "]", dp[i]);
                    continue;
                }
                for (int j = 0; j < 5; j++) {
                    if (j == 0) {
                        dp[i][j] = (i < L ? A[i] : 0) + dp[i - 1][j];
                    } else if (j == 1) {
                        dp[i][j] = (i < L ? (A[i] == 0 ? 2 : (A[i] % 2 == 0 ? 0 : 1)) : 0) + Math.min(dp[i - 1][j], dp[i - 1][0]);
                    } else if (j == 2) {
                        dp[i][j] = (i < L ? (A[i] == 0 ? 1 : (A[i] % 2 == 0 ? 1 : 0)) : 0) + Math.min(dp[i - 1][j], Math.min(dp[i - 1][1], dp[i - 1][0]));
                    } else if (j == 3) {
                        dp[i][j] = (i < L ? (A[i] == 0 ? 2 : (A[i] % 2 == 0 ? 0 : 1)) : 0) + Math.min(Math.min(dp[i - 1][3], dp[i - 1][2]), Math.min(dp[i - 1][1], dp[i - 1][0]));
                    } else if (j == 4) {
                        dp[i][j] = (i < L ? A[i] : 0) + Math.min(dp[i - 1][4], Math.min(Math.min(dp[i - 1][3], dp[i - 1][2]), Math.min(dp[i - 1][1], dp[i - 1][0])));
                    }
                }
//                Utils.debug("dp[" + i + "]", dp[i]);
            }

            System.out.println(dp[L][4]);
        }
    }
}
