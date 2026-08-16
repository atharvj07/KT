import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author silviase
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        ECommonSubsequence solver = new ECommonSubsequence();
        solver.solve(1, in, out);
        out.close();
    }

    static class ECommonSubsequence {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            int m = in.nextInt();
            int[] s = new int[n + 1];
            int[] t = new int[m + 1];
            s[0] = 0;
            t[0] = 0;
            ModInt[][] sum = new ModInt[n + 1][m + 1];
            ModInt[][] dp = new ModInt[n + 1][m + 1];

            for (int i = 1; i <= n; i++) {
                s[i] = in.nextInt();
            }

            for (int i = 1; i <= m; i++) {
                t[i] = in.nextInt();
            }

            for (int i = 0; i <= n; i++) {
                for (int j = 0; j <= m; j++) {
                    if (i == 0 || j == 0) {
                        sum[i][j] = new ModInt(0);
                    } else {
                        sum[i][j] = sum[i - 1][j].add(sum[i][j - 1]).sub(sum[i - 1][j - 1]);
                        if (s[i] == t[j]) {
                            sum[i][j] = sum[i][j].add(sum[i - 1][j - 1]).add(1);
                        }
                    }
                }
            }


            out.println(sum[n][m].getVal() + 1);
        }

    }

    static class ModInt {
        long val;
        int MOD = (int) 1e9 + 7;

        public ModInt(long i) {
            this.val = (i + MOD) % MOD;
        }

        public ModInt add(long l) {
            return new ModInt(this.val + l);
        }

        public ModInt add(ModInt m) {
            return new ModInt(this.val + m.getVal());
        }

        public ModInt sub(ModInt m) {
            return new ModInt(this.val - m.getVal());
        }

        public long getVal() {
            return val;
        }

        public String toString() {
            return Long.toString(val);
        }

    }
}

