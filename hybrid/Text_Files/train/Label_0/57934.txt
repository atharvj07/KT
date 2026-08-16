import java.io.*;
import java.util.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

public class Main {
    FastScanner in;
    PrintWriter out;

    private void solve() throws IOException {
        int n = in.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = in.nextInt();

        int[][] p = new int[n][5];
        fill(p[0], 1613);
        for (int i = 1; i < n; i++)
            fill(p[i], -1);

        for (int i = 1; i < n; i++)
            for (int j = 0; j < 5; j++)
                if (a[i - 1] < a[i]) {
                    for (int k = 0; k < j; k++)
                        if (p[i - 1][k] != -1)
                            p[i][j] = k;

                } else if (a[i - 1] > a[i]) {
                    for (int k = j + 1; k < 5; k++)
                        if (p[i - 1][k] != -1)
                            p[i][j] = k;

                } else
                    for (int k = 0; k < 5; k++)
                        if (j != k && p[i - 1][k] != -1)
                            p[i][j] = k;

        int[] ans = new int[n];
        ans[n - 1] = -1;
        for (int i = 0; i < 5; i++)
            if (p[n - 1][i] != -1)
                ans[n - 1] = i;

        if (ans[n - 1] == -1) {
            out.println(-1);
            return;
        }

        for (int i = n - 2; i >= 0; i--)
            ans[i] = p[i + 1][ans[i + 1]];

        for (int i : ans)
            out.print(i + 1 + " ");
    }

    private void solveC() throws IOException {
        int n = in.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = in.nextInt();

        int[] b = new int[n];

        for (int i = 0; i < n; ) {
            if (i + 1 == n || a[i] == a[i + 1]) {
                if (b[i] == 0)
                    b[i] = 1;
                i++;

            } else if (a[i] < a[i + 1]) {
                b[i++] = 1;
                while (i < n && a[i - 1] < a[i]) {
                    b[i] = b[i - 1] + 1;
                    i++;
                }
                i--;
            } else {
                b[i++] = 5;
                while (i < n && a[i - 1] > a[i]) {
                    b[i] = b[i - 1] - 1;
                    i++;
                }
                i--;
            }
        }

        out.println(Arrays.toString(b));

        for (int i = 0; i + 1 < n; i++) {
            if (b[i] == b[i + 1]) {
                if (b[i] == 1) {

                } else if (b[i] == 5) {

                } else {

                }
            }
        }

    }

    class FastScanner {
        StringTokenizer st;
        BufferedReader br;

        FastScanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        boolean hasNext() throws IOException {
            return br.ready() || (st != null && st.hasMoreTokens());
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        String nextLine() throws IOException {
            return br.readLine();
        }

        boolean hasNextLine() throws IOException {
            return br.ready();
        }

    }

    private void run() throws IOException {
        in = new FastScanner(System.in); // new FastScanner(new FileInputStream(".in"));
        out = new PrintWriter(System.out); // new PrintWriter(new FileOutputStream(".out"));

        solve();

        out.flush();
        out.close();
    }

    public static void main(String[] args) throws IOException {
        new Main().run();
    }
}