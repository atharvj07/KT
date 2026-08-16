import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
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
 * @author Rustam Musin (PloadyFree@gmail.com)
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        TaskE solver = new TaskE();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskE {
        int n;
        double k;
        boolean[][] g;

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            n = in.readInt();
            k = in.readInt();

            g = new boolean[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    g[i][j] = in.readInt() == 1;
                }
            }

            double answer = solve();
            out.printFormat("%.20f", answer);
        }

        private double solve() {
            int firstPartSize = g.length / 2;
            int secondPartSize = g.length - firstPartSize;

            int[] firstPart = findMaxCliqueSize(firstPartSize);

            int m1Full = (1 << firstPartSize) - 1;
            int maxCliqueSize = 1;
            for (int m = 0; m < 1 << secondPartSize; m++) {
                if (isClique(secondPartSize, m, firstPartSize)) {
                    int m1 = m1Full;
                    for (int j = 0; j < secondPartSize; j++) {
                        if (bit(m, j)) {
                            for (int i = 0; i < firstPartSize; i++) {
                                if (bit(m1, i) && !g[i][j + firstPartSize]) {
                                    m1 ^= 1 << i;
                                }
                            }
                        }
                    }
                    int firstCliqueSize = firstPart[m1];
                    int secondCliqueSize = Integer.bitCount(m);
                    int curCliqueSize = firstCliqueSize + secondCliqueSize;
                    if (curCliqueSize > maxCliqueSize) {
                        maxCliqueSize = curCliqueSize;
                    }
                }
            }

            return k * k * (maxCliqueSize - 1) / (2 * maxCliqueSize);
        }

        private int[] findMaxCliqueSize(int size) {
            int[] dp = new int[1 << size];
            for (int m = 1; m < 1 << size; m++) {
                if (isClique(size, m, 0)) {
                    dp[m] = Integer.bitCount(m);
                }
            }
            for (int m = 1; m < 1 << size; m++) {
                for (int i = 0; i < size; i++) {
                    if ((m >> i & 1) == 0) {
                        dp[m | (1 << i)] = Math.max(dp[m | (1 << i)], dp[m]);
                    }
                }
            }
            return dp;
        }

        private boolean isClique(int size, int m, int offset) {
            for (int i = 0; i < size; i++) {
                if (bit(m, i)) {
                    for (int j = i + 1; j < size; j++) {
                        if (bit(m, j) && !g[i + offset][j + offset]) {
                            return false;
                        }
                    }
                }
            }
            return true;
        }

        private boolean bit(int m, int b) {
            return (m >> b & 1) != 0;
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

        public int readInt() {
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

    static class OutputWriter {
        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }

        public void printFormat(String format, Object... objects) {
            writer.printf(format, objects);
        }

        public void close() {
            writer.close();
        }

    }
}

