import java.io.*;
import java.util.*;

/**
 * @author Alexander Tsupko (alexander.tsupko@outlook.com)
 * (c) Codeforces Round 364. All rights reserved. July 22, 2016.
 */
public class B {
    private static class Solve {
        // instance variables

        private void solve(InputReader in, OutputWriter out) {
            int n = in.nextInt();
            int m = in.nextInt();
            long answer = (long) n * n;
            boolean[] row = new boolean[n + 1];
            boolean[] col = new boolean[n + 1];
            int r, c; r = c = 0;
            for (int i = 0; i < m; i++) {
                int x = in.nextInt();
                if (!row[x]) {
                    row[x] = true;
                    r++;
                    answer -= (n - c);
                }
                int y = in.nextInt();
                if (!col[y]) {
                    col[y] = true;
                    c++;
                    answer -= (n - r);
                }
                out.println(answer);
            }
        }

        // instance methods
    }

    // static classes

    private static class InputReader {
        private BufferedReader bufferedReader;
        private StringTokenizer stringTokenizer;

        private InputReader(InputStream inputStream) {
            bufferedReader = new BufferedReader(new InputStreamReader(inputStream), 32768);
        }

        private void close() throws IOException {
            bufferedReader.close();
        }

        private String next() {
            while (stringTokenizer == null || !stringTokenizer.hasMoreTokens()) {
                try {
                    stringTokenizer = new StringTokenizer(bufferedReader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return stringTokenizer.nextToken();
        }

        private byte nextByte() {
            return Byte.parseByte(next());
        }

        private short nextShort() {
            return Short.parseShort(next());
        }

        private int nextInt() {
            return Integer.parseInt(next());
        }

        private long nextLong() {
            return Long.parseLong(next());
        }

        private float nextFloat() {
            return Float.parseFloat(next());
        }

        private double nextDouble() {
            return Double.parseDouble(next());
        }

        private boolean nextBoolean() {
            return Boolean.parseBoolean(next());
        }
    }

    private static class OutputWriter {
        private final PrintWriter printWriter;

        private OutputWriter(OutputStream outputStream) {
            printWriter = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)), true);
        }

        private void close() {
            printWriter.close();
        }

        private void print(Object... objects) {
            int n = objects.length;
            for (int i = 0; i < n; i++) {
                if (i != 0) {
                    printWriter.print(' ');
                }
                printWriter.print(objects[i]);
            }
        }

        private void println(Object... objects) {
            print(objects);
            printWriter.println();
        }
    }

    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        Solve solve = new Solve();
        solve.solve(in, out);
        in.close();
        out.close();
    }
}
