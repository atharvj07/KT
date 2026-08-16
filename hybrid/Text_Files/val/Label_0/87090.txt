import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
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
        DBinaryStringToSubsequences solver = new DBinaryStringToSubsequences();
        solver.solve(1, in, out);
        out.close();
    }

    static class DBinaryStringToSubsequences {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int ntc = 1;
            ntc = in.nextInt();
            while ((ntc--) > 0) {
                int n = in.nextInt();
                String s = in.nextString();
                int[] ansSequence = new int[n];
                int count = 0;
                ArrayDeque<Integer> zeroseq = new ArrayDeque<>();
                ArrayDeque<Integer> oneseq = new ArrayDeque<>();
                for (int i = 0; i < n; i++) {
                    if (s.charAt(i) == '1') {
                        if (!zeroseq.isEmpty()) {
                            int x = zeroseq.removeFirst();
                            ansSequence[i] = x;
                            oneseq.addLast(x);
                        } else {
                            count++;
                            ansSequence[i] = count;
                            oneseq.add(count);
                        }
                    } else {
                        if (!oneseq.isEmpty()) {
                            int x = oneseq.removeFirst();
                            ansSequence[i] = x;
                            zeroseq.addLast(x);
                        } else {
                            count++;
                            ansSequence[i] = count;
                            zeroseq.add(count);
                        }
                    }
                }
                out.println(count);
                out.println(ansSequence);
            }
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

        public void print(int[] array, int startFrom) {
            for (int i = startFrom; i < array.length; ++i) {
                if (i != startFrom) {
                    writer.print(' ');
                }
                writer.print(array[i]);
            }
        }

        public void println(int[] array, int startFrom) {
            print(array, startFrom);
            writer.println();
        }

        public void println(int[] array) {
            println(array, 0);
        }

        public void close() {
            writer.close();
        }

        public void println(long i) {
            writer.println(i);
        }

    }
}

