import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        int n = in.nextInt(), m = in.nextInt();
        while (n != 0 && m != 0) {
            long[] p = new long[n];
            long[] q = new long[n];
            for (int i = 0; i < m; i++) {
                int s = in.nextInt();
                int k = in.nextInt();
                if (k == 1) {
                    int c = in.nextInt() - 1;
                    q[c] += s;
                    p[c] += s;
                } else {
                    for (int j = 0; j < k; j++) {
                        p[in.nextInt() - 1] += s;
                    }
                }
            }

            long[] pl = new long[n + 1], pr = new long[n + 1];
            for (int i = 0; i < n; i++) {
                pl[i + 1] = Math.max(pl[i], p[i]);
            }
            for (int i = n - 1; i >= 0; i--) {
                pr[i] = Math.max(pr[i + 1], p[i]);
            }
            long ans = 0;
            for (int i = 0; i < n; i++) {
                ans = Math.max(ans, 1 + Math.max(pl[i], pr[i + 1]) - q[i]);
            }
            out.println(ans);

            n = in.nextInt();
            m = in.nextInt();
        }
        out.close();
    }
}

