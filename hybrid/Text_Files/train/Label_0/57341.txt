import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.Writer;
import java.util.NoSuchElementException;

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
        Task842A solver = new Task842A();
        solver.solve(1, in, out);
        out.close();
    }

    static class Task842A {
        private static final double EPS = 1e-9;

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int l = in.nextInt();
            int r = in.nextInt();
            int x = in.nextInt();
            int y = in.nextInt();
            int k = in.nextInt();

            for (int a = l; a <= r; ++a) {
                if (a % k > 0) {
                    continue;
                }
                double e = (1.0 * a) / k;

                if (e + EPS >= x && e - EPS <= y) {
                    out.println("YES");
                    return;
                }
            }

            out.println("NO");

        }

    }

    static class OutputWriter {
        private PrintWriter out;

        public OutputWriter(OutputStream stream) {
            out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(stream)));
        }

        public OutputWriter(Writer writer) {
            out = new PrintWriter(writer);
        }

        public void print(Object... objects) {
            for (int i = 0; i < objects.length; ++i) {
                if (i > 0) {
                    out.print(' ');
                }
                out.print(objects[i]);
            }
        }

        public void println(Object... objects) {
            print(objects);
            out.println();
        }

        public void close() {
            out.close();
        }

    }

    static class InputReader {
        private final byte[] buffer = new byte[8192];
        private InputStream in;
        private int pos = 0;
        private int len = 0;

        public InputReader(InputStream stream) {
            in = stream;
        }

        private static boolean isDigit(int c) {
            return c >= '0' && c <= '9';
        }

        private static boolean isPrintable(int c) {
            return c >= 33 && c <= 126;
        }

        public int nextInt() {
            return (int) nextLong();
        }

        public long nextLong() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            long num = 0;
            boolean neg = false;
            int b = readByte();
            if (!(isDigit(b) || b == '-')) {
                throw new NumberFormatException();
            } else {
                if (b == '-') {
                    neg = true;
                } else {
                    num += b - '0';
                }

                while ((b = readByte()) != -1 && isDigit(b)) {
                    num *= 10;
                    num += b - '0';
                }
            }
            return neg ? -num : num;
        }

        private boolean hasNext() {
            while (hasNextByte() && !isPrintable(buffer[pos])) {
                pos++;
            }
            return hasNextByte();
        }

        private boolean hasNextByte() {
            if (pos >= len) {
                pos = 0;
                try {
                    len = in.read(buffer);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (len <= 0) {
                    return false;
                }
            }
            return true;
        }

        private int readByte() {
            if (hasNextByte()) {
                return buffer[pos++];
            } else {
                return -1;
            }
        }

    }
}

