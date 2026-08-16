import java.io.PrintWriter;
import java.util.*;

public class Main {
    private static int n, m;
    private static char[] s, t;
    private static int[][] sp, tp;
    private static short[][] dp;

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in); PrintWriter out = new PrintWriter(System.out)) {
            s = in.next().toCharArray();
            t = in.next().toCharArray();
            n = s.length;
            m = t.length;
            sp = new int[2][n + 2];
            tp = new int[2][m + 2];
            dp = new short[n + 2][m + 2];
            sp[0][n] = sp[1][n] = n;
            tp[0][m] = tp[1][m] = m;

            // 不可能な遷移先
            sp[0][n + 1] = sp[1][n + 1] = n + 1;
            tp[0][m + 1] = tp[1][m + 1] = m + 1;
            // とり尽くした
            sp[0][n] = sp[1][n] = n + 1;
            tp[0][m] = tp[1][m] = m + 1;
            // 通常遷移
            for (int i = n - 1; i >= 0; i--) {
                for (int j = 0; j < 2; j++) sp[j][i] = sp[j][i + 1];
                sp[s[i] - '0'][i] = i + 1;
            }
            for (int i = m - 1; i >= 0; i--) {
                for (int j = 0; j < 2; j++) tp[j][i] = tp[j][i + 1];
                tp[t[i] - '0'][i] = i + 1;
            }


            int len = dp(0, 0);
            //Arrays.stream(dp).map(Arrays::toString).forEach(System.out::println);
            int i = 0, j = 0;
            StringBuilder ans = new StringBuilder();
            for (int k = 0; k < len; k++) {
                if (dp(sp[0][i], tp[0][j]) <= dp(sp[1][i], tp[1][j])) {
                    i = sp[0][i];
                    j = tp[0][j];
                    ans.append('0');
                } else {
                    i = sp[1][i];
                    j = tp[1][j];
                    ans.append('1');
                }
            }
            out.println(ans.toString());
        }
    }

    private static short dp(int i, int j) {
        if (i == n + 1 && j == m + 1) return 0;
        if (dp[i][j] > 0) return dp[i][j];
        short res = Short.MAX_VALUE;
        for (int k = 0; k < 2; k++) {
            int di = sp[k][i], dj = tp[k][j];
            short t = dp(di, dj);
            if (t < res) res = t;
        }
        res++;
        return dp[i][j] = res;
    }
}
