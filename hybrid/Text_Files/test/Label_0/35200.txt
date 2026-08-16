import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskF solver = new TaskF();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskF {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; ++i) a[i] = in.nextInt();
            int s1 = 0;
            int s2 = 0;
            for (int i = 0; i < n; ++i) {
                if (i % 2 == 0)
                    s1 += a[i];
                else
                    s2 += a[i];
            }
            if (n % 2 == 0) {
                out.println(Math.max(s1, s2) + " " + Math.min(s1, s2));
                return;
            }
            int left = s1 - s2;
            int right = s1 + s2 + 1;
            outer:
            while (right - left > 1) {
                int middle = (left + right) / 2;
                long bestSoFar = s1 - s2;
                int r1 = s1;
                int r2 = s2;
                for (int i = 1; i <= n; i += 2) {
                    r1 -= a[i - 1];
                    long cost = bestSoFar - (r1 - r2);
                    if (i < n) r2 -= a[i];
                    if (cost >= middle) {
                        if (i == n) {
                            left = middle;
                            continue outer;
                        } else {
                            bestSoFar = Math.max(bestSoFar, r1 - r2);
                        }
                    }
                }
                right = middle;
            }
            out.println((s2 + left) + " " + (s1 - left));
        }

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

    }
}

