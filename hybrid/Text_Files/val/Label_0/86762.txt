import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.stream.IntStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.stream.Collectors;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.Comparator;
import java.util.Collections;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author out_of_the_box
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        FSummoningMinions solver = new FSummoningMinions();
        int testCount = Integer.parseInt(in.next());
        for (int i = 1; i <= testCount; i++)
            solver.solve(i, in, out);
        out.close();
    }

    static class FSummoningMinions {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.nextInt();
            int k = in.nextInt();
            int[] a = new int[n];
            int[] b = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = in.nextInt();
                b[i] = in.nextInt();
            }
            int[][] dp = new int[n][k + 1];
            int[] indexes = new int[n];
            for (int i = 0; i < n; i++) {
                indexes[i] = i;
            }
            indexes = Arrays.stream(indexes).boxed().sorted(Comparator.comparingInt(ind -> b[ind])).mapToInt(i -> i)
                    .toArray();
            boolean[][] select = new boolean[n][k + 1];
            dp[0][0] = (k - 1) * b[indexes[0]];
            dp[0][1] = a[indexes[0]];
            select[0][1] = true;
            for (int i = 1; i < n; i++) {
                dp[i][0] = dp[i - 1][0] + (k - 1) * (b[indexes[i]]);
            }
            for (int i = 1; i < n; i++) {
                int maxJ = Math.min(i + 1, k);
                for (int j = 1; j <= maxJ; j++) {
                    int first = dp[i - 1][j - 1] + a[indexes[i]] + (j - 1) * b[indexes[i]];
                    int second = (j <= i) ? dp[i - 1][j] + (k - 1) * b[indexes[i]] : (-1);
                    if (first >= second) {
                        dp[i][j] = first;
                        select[i][j] = true;
                    } else {
                        dp[i][j] = second;
                    }
                }
            }
            List<Integer> selected = new ArrayList<>();
            boolean[] selectedFlag = new boolean[n];
            int tbs = k;
            for (int i = n - 1; i >= 0; i--) {
                if (tbs == 0) break;
                if (select[i][tbs]) {
                    selected.add(indexes[i]);
                    selectedFlag[indexes[i]] = true;
                    tbs--;
                }
            }
            List<Integer> listA = Arrays.stream(a).boxed().collect(Collectors.toList());
            List<Integer> listB = Arrays.stream(b).boxed().collect(Collectors.toList());
            String message =
                    String.format("Selected size mismatch. size = %d, k = %d, n = %d, a = %s, b = %s", selected.size(),
                            k, n, listA, listB);
            MiscUtility.assertion(selected.size() == k, message);
            Collections.reverse(selected);
            int m = k + (n - k) * 2;
            out.println(m);
            for (int i = 0; i < (k - 1); i++) {
                out.print((selected.get(i) + 1) + " ");
            }
            for (int i = 0; i < n; i++) {
                if (!selectedFlag[i]) {
                    out.print((i + 1) + " ");
                    out.print(-(i + 1) + " ");
                }
            }
            out.print(selected.get(k - 1) + 1);
            out.println();
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

        public void print(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                if (i != 0) {
                    writer.print(' ');
                }
                writer.print(objects[i]);
            }
        }

        public void println() {
            writer.println();
        }

        public void close() {
            writer.close();
        }

        public void print(int i) {
            writer.print(i);
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

        public String nextString() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            StringBuilder res = new StringBuilder();
            do {
                if (Character.isValidCodePoint(c)) {
                    res.appendCodePoint(c);
                }
                c = read();
            } while (!isSpaceChar(c));
            return res.toString();
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

        public String next() {
            return nextString();
        }

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);

        }

    }

    static class MiscUtility {
        public static void assertion(boolean condition, String message) {
            if (!condition) {
                throw new RuntimeException("Assertion failed. " + message);
            }
        }

    }
}

