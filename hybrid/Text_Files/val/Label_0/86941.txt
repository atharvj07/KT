import java.util.*;
import java.io.*;
import java.math.*;

public class Main {

    public static InputReader in;
    public static PrintWriter out;
    public static void main(String[] args) {
        in = new InputReader(System.in);
        out = new PrintWriter(System.out);
        int L = in.nextInt();
        int N = in.nextInt();
        int[] a = new int[N + 5];
        for (int i = 1; i <= N; i++) {
            a[i] = in.nextInt();
        }
        long ans = 0;
        ans = Math.max(ans, solve(N, a, L));
        int[] aa = new int[N + 5];
        for (int i = 1; i <= N; i++) {
            aa[i] = L - a[N + 1 - i];
        }
        ans = Math.max(ans, solve(N, aa, L));
        out.print(ans);
        out.close();
    }
    public static long solve(int n, int[] a, int l) {
        int[] b = new int[n + 5];
        int m = n + 1;
        for (int i = 1; i <= n; i++) {
            if (i == 1) b[i] = a[i];
            else b[i] = a[i] - a[i - 1];
        }
        b[m] = l - a[n];
        long[] sum = new long[n + 5];
        long[] sum135 = new long[n + 5];
        for (int i = 1; i <= m; i++) {
            sum[i] = sum[i - 1] + b[i];
            sum135[i] = (long)(2 * i - 1) * b[i] + sum135[i - 1];
        }
        long ans = 0;
        for (int Rnum = 0; Rnum < n; Rnum++) {
            long cur = sum[m - 1 - Rnum] * (Rnum + 1);
            int zero_i = m - (Rnum + 1) / 2;
            int len = Rnum / 2;
            if ((Rnum & 1) == 0) {
                cur += (sum135[m] - sum135[zero_i]) - (2 * zero_i - 1) * (sum[m] - sum[zero_i]);
                cur += Rnum * (sum[zero_i - 1] - sum[zero_i - len - 1]) - ((sum135[zero_i - 1] - sum135[zero_i - len - 1]) - (2 * (zero_i - len) - 2) * (sum[zero_i - 1] - sum[zero_i - len - 1]));
            }
            else {
                cur += (sum135[m] - sum135[zero_i]) - (2 * zero_i) * (sum[m] - sum[zero_i]);
                cur += Rnum * (sum[zero_i - 1] - sum[zero_i - len - 1]) - ((sum135[zero_i - 1] - sum135[zero_i - len - 1]) - (2 * (zero_i - len) - 2) * (sum[zero_i - 1] - sum[zero_i - len - 1]));
            }
            ans = Math.max(ans, cur);
        }
        return ans;
    }
    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;
        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }
        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
        public int nextInt() {
            return Integer.parseInt(next());
        }
        public Long nextLong() {
            return Long.parseLong(next());
        }
        public Double nextDouble() {
            return Double.parseDouble(next());
        }
    }
}
