import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.TreeSet;
import java.util.HashSet;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author John Martin
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        ENewYearParties solver = new ENewYearParties();
        solver.solve(1, in, out);
        out.close();
    }

    static class ENewYearParties {
        public void solve(int testNumber, InputReader c, OutputWriter w) {
            int n = c.readInt();
            int a[] = c.readIntArray(n);
            Sort.mergeSort(a, 0, n);
            HashSet<Integer> ma = new HashSet<>();
            for (int i = 0; i < n; i++) {
                if (!ma.contains(a[i] - 1)) {
                    ma.add(a[i] - 1);
                } else if (!ma.contains(a[i])) {
                    ma.add(a[i]);
                } else {
                    ma.add(a[i] + 1);
                }
            }
            int max = ma.size();

            TreeSet<Integer> ts = new TreeSet<>();
            for (int i = 0; i < n; i++) {
                ts.add(a[i]);
            }

            int min = 0;
            while (!ts.isEmpty()) {
                int kk = ts.pollFirst();
                ts.remove(kk + 1);
                ts.remove(kk + 2);
                min++;
            }
            w.printLine(min, max);
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

        public void printLine(Object... objects) {
            print(objects);
            writer.println();
        }

        public void close() {
            writer.close();
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

    static class Sort {
        public static void mergeSort(int[] a, int low, int high) {
            if (high - low < 2) {
                return;
            }
            int mid = (low + high) >>> 1;
            mergeSort(a, low, mid);
            mergeSort(a, mid, high);
            int[] b = Arrays.copyOfRange(a, low, mid);
            for (int i = low, j = mid, k = 0; k < b.length; i++) {
                if (j == high || b[k] <= a[j]) {
                    a[i] = b[k++];
                } else {
                    a[i] = a[j++];
                }
            }
        }

    }
}

