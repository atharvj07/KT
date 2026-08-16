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
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        FNezzarAndChocolateBars solver = new FNezzarAndChocolateBars();
        solver.solve(1, in, out);
        out.close();
    }

    static class FNezzarAndChocolateBars {
        static final int MAXN = 2048;
        static final int modulo = 998244353;

        public int add(int x, int y) {
            x += y;
            if (x >= modulo) x -= modulo;
            return x;
        }

        public int subtract(int x, int y) {
            x -= y;
            if (x < 0) x += modulo;
            return x;
        }

        public int multiply(int x, int y) {
            return (int) ((x * 1L * y) % modulo);
        }

        public int power(int x, long y) {
            int ans = 1;
            for (; y > 0; y >>= 1, x = (int) ((x * 1L * x) % modulo))
                if (y % 2 == 1) ans = (int) ((ans * 1L * x) % modulo);
            return ans;
        }

        public int inverse(int x) {
            return power(x, modulo - 2);
        }

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int[] fact = new int[MAXN];
            int[] ifact = new int[MAXN];
            fact[0] = ifact[0] = 1;
            for (int i = 1; i < MAXN; i++) {
                fact[i] = multiply(fact[i - 1], i);
                ifact[i] = inverse(fact[i]);
            }
            int n = in.nextInt(), k = in.nextInt();
            int[] l = in.readIntArray(n);
            int[][][] dp = new int[2][MAXN][n + 1];
            dp[1][0][0] = 1;
            int s = 0;

            for (int p = 0; p < n; p++) {
                int L = l[p];
                int invL = inverse(L);
                int[] coeffs = new int[L / k + 1];
                int[] coeffs2 = new int[L / k + 1];
                for (int i = 0; i <= L / k; i++) {
                    if (k * i == L) continue;
                    int z = ifact[i];
                    if (i % 2 == 1) z = subtract(0, z);
                    coeffs[i] = multiply(z, power(L - k * i, i));

                    if (i >= 1) {
                        coeffs2[i] = multiply(z, multiply(i, power(L - k * i, i - 1)));
                    }
                }
                int r = p & 1;
                int h = r ^ 1;
                for (int i = 0; i <= s / k; i++) Arrays.fill(dp[r][i], 0);
                for (int i = 0; i <= s / k; i++)
                    for (int j = 0; j <= p; j++)
                        if (dp[h][i][j] != 0) {
                            int value = dp[h][i][j];
                            for (int t = 0; t <= L / k; t++) {
                                dp[r][i + t][j] = add(dp[r][i + t][j], multiply(value, coeffs[t]));
                                if (t > 0) {
                                    dp[r][i + t - 1][j + 1] = add(dp[r][i + t - 1][j + 1], multiply(value, coeffs2[t]));
                                }
                            }
                        }
                s += L;
            }
            int answer = 0;
            for (int i = 0; i <= s / k; i++)
                for (int r = 0; r <= n; r++) {
                    int value = dp[(n - 1) & 1][i][r];
                    int j = i + r;
                    if (j == 0) continue;
                    int temp = multiply(fact[i], inverse(power(k * j, i + 1)));
                    answer = add(answer, multiply(value, temp));
                }
            out.println(multiply(subtract(0, s), answer));
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

        public int[] readIntArray(int size) {
            int[] array = new int[size];
            for (int i = 0; i < size; i++) {
                array[i] = readInt();
            }
            return array;
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
            while (isSpaceChar(c)) c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
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

        public void println(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                if (i != 0) {
                    writer.print(' ');
                }
                writer.print(objects[i]);
            }
            writer.print('\n');
        }

        public void close() {
            writer.close();
        }

    }
}

