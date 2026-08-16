import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author varunvats32
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        EAlmostEverywhereZero solver = new EAlmostEverywhereZero();
        solver.solve(1, in, out);
        out.close();
    }

    static class EAlmostEverywhereZero {
        static int[][][] dp = new int[105][4][2];

        public void solve(int testNumber, Scanner in, PrintWriter out) {
            String s = in.nextLine();
            int K = in.nextInt();
            int n = s.length();
            dp[0][0][0] = 1;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < 4; j++) {
                    for (int k = 0; k < 2; k++) {
                        int nd = s.charAt(i) - '0';
                        for (int digit = 0; digit < 10; digit++) {
                            int ni = i + 1, nj = j, nk = k;
                            if (digit != 0) nj++;
                            if (nj > K) continue;
                            if (k == 0) {
                                if (digit > nd) continue;
                                if (digit < nd) nk = 1;
                            }
                            dp[ni][nj][nk] += dp[i][j][k];
                        }
                    }
                }
            }

            int ans = dp[n][K][0] + dp[n][K][1];
            out.println(ans);
        }

    }
}

