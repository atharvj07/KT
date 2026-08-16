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
        E2AbnormalPermutationPairsHardVersion solver = new E2AbnormalPermutationPairsHardVersion();
        solver.solve(1, in, out);
        out.close();
    }

    static class E2AbnormalPermutationPairsHardVersion {
        ModInt mod;

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.nextInt();
            int m = in.nextInt();
            mod = new ModInt(m);
            int[] factorial = new int[n + 1];
            factorial[0] = n;
            for (int i = 1; i < n; i++) factorial[i] = mod.multiply(factorial[i - 1], n - i);
            int[] dp = new int[n * (n - 1) + 1];
            int middle = (n * (n - 1)) / 2;
            int[] temp = dp.clone();
            dp[middle] = 1;
            int answer = 0;
            for (int i = n - 1; i >= 0; i--) {
                int c = n - 1 - i;
                temp = dp.clone();
                Arrays.fill(dp, 0);
                int limit = (c * (c - 1)) / 2;
                int count = 0;
                for (int cur = -c; cur < 0; cur++) {
                    int pairs = c + cur + 1;
                    for (int j = middle - cur + 1; j <= middle + limit; j++)
                        count = mod.add(count, mod.multiply(temp[j], pairs));
                }
                answer = mod.add(answer, mod.multiply(count, i == 0 ? 1 : factorial[i - 1]));
                for (int j = middle - limit; j <= middle + limit; j++) {
                    for (int cur = -c; cur <= c; cur++) {
                        int pairs = c - Math.abs(cur) + 1;
                        dp[j + cur] = mod.add(dp[j + cur], mod.multiply(pairs, temp[j]));
                    }
                }
            }
            out.println(answer);
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

    static class ModInt {
        int modulo;

        public ModInt(int m) {
            modulo = m;
        }

        public int add(int x, int y) {
            x += y;
            if (x >= modulo) x -= modulo;
            return x;
        }

        public int multiply(int x, int y) {
            return (int) ((x * 1L * y) % modulo);
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

