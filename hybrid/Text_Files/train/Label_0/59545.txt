import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author prakharjain
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        _988F solver = new _988F();
        solver.solve(1, in, out);
        out.close();
    }

    static class _988F {
        long inf = 10000000000l;

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int a = in.nextInt();

            int n = in.nextInt();

            int m = in.nextInt();

            seg[] segs = new seg[n];

            for (int i = 0; i < n; i++) {
                int l = in.nextInt();
                int r = in.nextInt();

                segs[i] = new seg(l, r);
            }

            long[] uw = new long[a + 1];

            for (int i = 0; i <= a; i++) {
                uw[i] = inf;
            }
            for (int i = 0; i < m; i++) {
                int x = in.nextInt();
                int w = in.nextInt();

                uw[x] = Math.min(uw[x], w);
            }

            if (uw[a] == inf) {
                uw[a] = 0;
            }

            long[] dp = new long[a + 1];

            for (int i = 0; i <= a; i++) {
                dp[i] = inf;
            }

            Arrays.sort(segs, (s1, s2) -> s1.l - s2.l);

            int[] lsi = new int[a + 1];
            for (int i = a; i >= 0; i--) {
                if (uw[i] != inf) {
                    lsi[i] = -1;
                    for (int j = 0; j < n; j++) {
                        if (segs[j].l < i && segs[j].r >= i) {
                            lsi[i] = i;
                            break;
                        } else if (segs[j].r < i) {
                            lsi[i] = segs[j].r;
                        } else {
                            break;
                        }
                    }
                }
            }

            dp[a] = 0;

            for (int i = a - 1; i >= 0; i--) {
                if (uw[i] != inf) {
                    if (segs[n - 1].r <= i) {
                        dp[i] = 0;
                        continue;
                    }
                    for (int j = i + 1; j <= a; j++) {
                        if (uw[j] != inf) {
                            int li = lsi[j];
                            if (li <= i) {
                                dp[i] = Math.min(dp[i], dp[j]);
                            } else {
                                dp[i] = Math.min(dp[i], (li - i) * uw[i] + dp[j]);
                            }
                        }
                    }
                }
            }

            long min = inf;

            for (int i = segs[0].l; i >= 0; i--) {
                min = Math.min(min, dp[i]);
            }

            if (min == inf) {
                out.println(-1);
                return;
            }

            out.println(min);
        }

        class seg {
            int l;
            int r;

            public seg(int l, int r) {
                this.l = l;
                this.r = r;
            }

        }

    }

    static class OutputWriter {
        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }

        public void close() {
            writer.close();
        }

        public void println(long i) {
            writer.println(i);
        }

        public void println(int i) {
            writer.println(i);
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

        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
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

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);

        }

    }
}

