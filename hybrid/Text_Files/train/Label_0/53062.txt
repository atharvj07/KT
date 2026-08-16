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
        TaskC solver = new TaskC();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskC {
        static final int MAX_BIT = 60;
        static final long BIGX = (1L << (MAX_BIT - 1));
        static final long BIGY = (1L << MAX_BIT);

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            long[] x = new long[n];
            long[] y = new long[n];
            for (int i = 0; i < n; ++i) {
                x[i] = in.nextLong();
                y[i] = in.nextLong();
            }
            long res = BIGX;
            for (int bit = 0; bit < MAX_BIT; ++bit) {
                long y0 = -(BIGY + (BIGY - 1) - (1L << bit));
                long x0 = BIGX;
                long r = 0;
                for (int i = 0; i < n; ++i) {
                    long dy = y[i] - y0;
                    long dx = x0 - x[i];
                    if ((dy & dx) == dx) {
                        r ^= 1;
                    }
                }
                if (r == 0) res -= (1L << bit);
            }
            out.println(res);
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

        public long nextLong() {
            return Long.parseLong(next());
        }

    }
}

