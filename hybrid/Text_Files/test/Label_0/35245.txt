import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;
import java.util.Map;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.Collections;
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
        FSumDifference solver = new FSumDifference();
        solver.solve(1, in, out);
        out.close();
    }

    static class FSumDifference {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            // x
            int n = in.readInt();
            long x = in.readLong();
            long d = in.readLong();

            if (d == 0) {
                out.printLine(x == 0 ? 1 : n + 1);
                return;
            }

            if (d < 0) {
                d = -d;
                x = -x;
            }

            Map<Long, List<LongLongPair>> map = new TreeMap<>();
            map.put(Constants.LINF % d, new ArrayList<>());
            map.get(Constants.LINF % d).add(new LongLongPair(Constants.LINF / d, Constants.LINF / d));
            long max = 0;
            long min = 0;
            for (int i = 1; i <= n; i++) {
                max += n - i;
                min += i - 1;
                long p = (Constants.LINF + i * x) / d;
                long q = (Constants.LINF + i * x) % d;
                if (!map.containsKey(q)) map.put(q, new ArrayList<>());
                map.get(q).add(new LongLongPair(p + min, p + max));
            }

            long ans = 0;
            for (long t : map.keySet()) {
                long pos = 0;
                Collections.sort(map.get(t));
                for (LongLongPair ll : map.get(t)) {
                    ans += Math.max(0, ll.second - Math.max(pos, ll.first) + 1);
                    pos = Math.max(pos, ll.second + 1);
                }
            }
            out.printLine(ans);
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

        public long readLong() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            long res = 0;
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

    static class LongLongPair implements Comparable<LongLongPair> {
        public final long first;
        public final long second;

        public LongLongPair(long first, long second) {
            this.first = first;
            this.second = second;
        }

        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }

            LongLongPair pair = (LongLongPair) o;

            return first == pair.first && second == pair.second;
        }

        public int hashCode() {
            int result = Long.hashCode(first);
            result = 31 * result + Long.hashCode(second);
            return result;
        }

        public String toString() {
            return "(" + first + "," + second + ")";
        }

        public int compareTo(LongLongPair o) {
            int value = Long.compare(first, o.first);
            if (value != 0) {
                return value;
            }
            return Long.compare(second, o.second);
        }

    }

    static class Constants {
        public static final long LINF = (long) 1e18 + 1;

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

        public void printLine(long i) {
            writer.println(i);
        }

        public void printLine(int i) {
            writer.println(i);
        }

    }
}

