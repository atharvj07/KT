import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.ArrayList;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author cunbidun
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        ECountTheRectangles solver = new ECountTheRectangles();
        solver.solve(1, in, out);
        out.close();
    }

    static class ECountTheRectangles {
        private InputReader in;
        private OutputWriter out;

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            this.in = in;
            this.out = out;

            int n = in.nextInt();
            ArrayList<TripIII> v = new ArrayList<>();
            ArrayList<TripIII> h = new ArrayList<>();
            for (int i = 1; i <= n; i++) {
                int x1 = in.nextInt();
                int y1 = in.nextInt();
                int x2 = in.nextInt();
                int y2 = in.nextInt();
                if (x1 > x2) {
                    int tmp = x2;
                    x2 = x1;
                    x1 = tmp;
                }
                if (y1 > y2) {
                    int tmp = y2;
                    y2 = y1;
                    y1 = tmp;
                }
                if (y1 == y2) {
                    h.add(new TripIII(y1, x1, x2));
                } else {
                    v.add(new TripIII(x1, y1, y2));
                }
            }
            if (v.size() > h.size()) {
                ArrayList<TripIII> tmp = new ArrayList<>(v);
                v = new ArrayList<>(h);
                h.clear();
                h = new ArrayList<>(tmp);
            }
            ImmutableBitSet[] bit = new ImmutableBitSet[v.size()];
            for (int i = 0; i < v.size(); i++) {
                bit[i] = new ImmutableBitSet(h.size());
                for (int j = 0; j < h.size(); j++) {
                    if (intersect(v.get(i), h.get(j))) bit[i].set(j);
                }
            }
            long ans = 0;
            for (int i = 0; i < v.size(); i++) {
                for (int j = i + 1; j < v.size(); j++) {
                    long res = bit[i].count(bit[j]);
                    ans += res * (res - 1) / 2;
                }
            }
            out.println(ans);
//        ImmutableBitSet t = new ImmutableBitSet(64);
//        for (int i = 0; i <= 63; i++) {
//            t.set(i);
//        }
//        out.println(Long.toString(Long.parseUnsignedLong("9223372036854775807"), 2));
        }

        private boolean intersect(TripIII a, TripIII b) {
            return a.first <= b.third && a.first >= b.second && b.first >= a.second && b.first <= a.third;
        }

    }

    static class ImmutableBitSet {
        private long[] array;
        private int size;

        public ImmutableBitSet(int size) {
            this.size = (size + 63) / 64;
            array = new long[this.size];
        }

        public int count(ImmutableBitSet that) {
            int ans = 0;
            for (int i = 0; i < size; ++i)
                ans += Long.bitCount(this.getIndex(i) & that.getIndex(i));
            return ans;
        }

        public void set(int i) {
            int j = i >> 6;
            array[j] |= 1L << (i - (j << 6));
        }

        private long getIndex(int i) {
            return array[i];
        }

    }

    static class InputReader extends InputStream {
        private InputStream stream;
        private byte[] buf = new byte[1 << 16];
        private int curChar;
        private int numChars;

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
            while (isSpaceChar(c))
                c = read();
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

        private static boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

    }

    static class OutputWriter {
        private final PrintWriter out;

        public OutputWriter(OutputStream outputStream) {
            out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.out = new PrintWriter(writer);
        }

        public void close() {
            out.close();
        }

        public void println(long i) {
            out.println(i);
        }

    }

    static class TripIII implements Comparable<TripIII> {
        public int first;
        public int second;
        public int third;

        public TripIII(int first, int second, int third) {
            this.first = first;
            this.second = second;
            this.third = third;
        }

        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }

            TripIII trip = (TripIII) o;

            return first == trip.first && second == trip.second && third == trip.third;
        }

        public String toString() {
            return "(" + first + "," + second + "," + third + ")";
        }

        public int compareTo(TripIII o) {
            int value = Integer.compare(first, o.first);
            if (value != 0) {
                return value;
            }
            value = Integer.compare(second, o.second);
            if (value != 0) {
                return value;
            }
            return Integer.compare(third, o.third);
        }

    }
}

