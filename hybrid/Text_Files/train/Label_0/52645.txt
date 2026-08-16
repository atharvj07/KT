import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author prakhar17252
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        long[] sum = new long[1000010];
        long[] df = new long[1000010];
        long[] res = new long[1000010];
        int n;
        int[] p = new int[1000010];

        private void add(int lf, int rg, int k, int b) {
            if (lf > rg) return;
            sum[lf] += b;
            df[lf] += k;

            sum[rg + 1] -= b + (long) k * (rg - lf);
            df[rg] -= k;
        }

        private void calc() {
            long curdf = 0;
            for (int i = 0; i < n; i++) {
                sum[i] += curdf;
                curdf += df[i];
            }

            long cursm = 0;
            for (int i = 0; i < n; i++) {
                cursm += sum[i];
                res[i] += cursm;
            }
        }

        private int solver() {
            Arrays.fill(sum, 0);
            Arrays.fill(res, 0);
            Arrays.fill(df, 0);
            for (int i = 0; i < n; i++) {
                int c1 = i + 1, p1 = 0;
                int c2 = n, p2 = p1 + c2 - c1;
                int c3 = i, p3 = p2 + c3;

                if (p[i] <= c3) {
                    add(p1, p2, 1, c1 - p[i]);
                    add(p2 + 1, p2 + p[i], -1, p[i] - 1);
                    add(p2 + p[i] + 1, p3, 1, 1);
                } else {
                    add(p1, p1 + p[i] - c1, -1, p[i] - c1);
                    add(p1 + p[i] - c1 + 1, p2, 1, 1);
                    add(p2 + 1, p3, -1, p[i] - 1);
                }
            }

            calc();

            int ans = 0;
            for (int i = 0; i < n; i++) {
                if (res[ans] > res[i]) ans = i;
            }
            return ans;

        }

        public void solve(int testNumber, InputReader in, PrintWriter out) {

            n = in.nextInt();

            for (int i = 0; i < n; i++) {
                p[i] = in.nextInt();
            }
            int ans = solver();
            out.println(res[ans] + " " + ans);
        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private InputReader.SpaceCharFilter filter;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int read() {
            if (numChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }

        public int nextInt() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public boolean isSpaceChar(int c) {
            if (filter != null) {
                return filter.isSpaceChar(c);
            }
            return isWhitespace(c);
        }

        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);

        }

    }
}

