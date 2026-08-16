import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Ben King
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        FDisjointTriangles solver = new FDisjointTriangles();
        solver.solve(1, in, out);
        out.close();
    }

    static class FDisjointTriangles {
        long[][] A;

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int N = in.nextInt();
            long total = 0;
            A = new long[N][2];
            for (int i = 0; i < N; i++) {
                A[i][0] = in.nextLong();
                A[i][1] = in.nextLong();
            }


            ArrayList<long[]> left = new ArrayList<>();
            ArrayList<long[]> right = new ArrayList<>();

            for (int startPoint = 0; startPoint < N; startPoint++) {
                left.clear();
                right.clear();
                long[] point = A[startPoint];
                for (int i = 0; i < N; i++) {
                    if (i == startPoint) continue;
                    long[] x = new long[]{A[i][0] - point[0], A[i][1] - point[1]};
                    long[] hor = new long[]{1, 0};
                    if (x[0] > 0L || (x[0] == 0 && x[1] > 0L)) {
                        left.add(x);
                    }
                    else {
                        right.add(neg(x));
                    }
                }

                long lc = left.size();
                long rc = right.size();

                // sort by angle
                Collections.sort(left, (a, b) -> Long.compare(det(b, a), 0L));
                Collections.sort(right, (a, b) -> Long.compare(det(b, a), 0L));
//            for (long[] x : left) {
//                System.out.println(Arrays.toString(x));
//            }
//            System.out.println();
//            for (long[] x : right) {
//                System.out.println(Arrays.toString(x));
//            }

//            System.out.println(lc + " " + rc);

                int rp = 0;
                for (int i = 0; i < left.size(); i++) {
                    lc--;
//                System.out.println(lc + " " + rc + " " + total);
                    while (rp < right.size() && det(right.get(rp), left.get(i)) >= 0L) {
                        rp++;
                        lc++;
                        rc--;
                    }
                    total += lc * (lc - 1L) / 2L * rc * (rc - 1L) / 2L;
                    rc++;
                }

            }

            out.println(total);

            out.flush();
        }

        private long det(long[] a, long[] b) {
            return a[0] * b[1] - a[1] * b[0];
        }

        private long[] neg(long[] a) {
            return new long[]{-1L * a[0], -1L * a[1]};
        }

    }

    static class OutputWriter {
        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(
                outputStream)));
        }

        public OutputWriter(java.io.Writer outputStreamWriter) {
            writer = new PrintWriter(new BufferedWriter(outputStreamWriter));
        }

        public void flush() {
            writer.flush();
        }

        public void close() {
            writer.flush();
            writer.close();
        }

        public void println(long i) {
            writer.println(i);
        }

    }

    static class InputReader {
        private static final int DEFAULT_BUFFER_SIZE = 1 << 16;
        private static final InputStream DEFAULT_STREAM = System.in;
        private int c;
        private byte[] buf;
        private int bufferSize;
        private int bufIndex;
        private int numBytesRead;
        private InputStream stream;
        private static final byte EOF = -1;
        private static final byte SPACE = 32;
        private static final byte DASH = 45;
        private char[] charBuffer;
        private static byte[] bytes = new byte[58];
        private static int[] ints = new int[58];
        private static char[] chars = new char[128];

        static {
            char ch = ' ';
            int value = 0;
            byte _byte = 0;
            for (int i = 48; i < 58; i++) bytes[i] = _byte++;
            for (int i = 48; i < 58; i++) ints[i] = value++;
            for (int i = 32; i < 128; i++) chars[i] = ch++;
        }

        public InputReader() {
            this(DEFAULT_STREAM, DEFAULT_BUFFER_SIZE);
        }

        public InputReader(int bufferSize) {
            this(DEFAULT_STREAM, bufferSize);
        }

        public InputReader(InputStream stream) {
            this(stream, DEFAULT_BUFFER_SIZE);
        }

        public InputReader(InputStream stream, int bufferSize) {
            if (stream == null || bufferSize <= 0)
                throw new IllegalArgumentException();
            buf = new byte[bufferSize];
            charBuffer = new char[128];
            this.bufferSize = bufferSize;
            this.stream = stream;
        }

        private int readJunk(int token) {

            if (numBytesRead == EOF) return EOF;

            // Seek to the first valid position index
            do {

                while (bufIndex < numBytesRead) {
                    if (buf[bufIndex] > token) return 0;
                    bufIndex++;
                }

                // reload buffer
                try {
                    numBytesRead = stream.read(buf);
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
                if (numBytesRead == EOF) return EOF;
                bufIndex = 0;

            } while (true);

        }

        public int nextInt() {
            try {
                if (readJunk(DASH - 1) == EOF) throw new IOException();
                int sgn = 1, res = 0;

                c = buf[bufIndex];
                if (c == DASH) {
                    sgn = -1;
                    bufIndex++;
                }

                do {

                    while (bufIndex < numBytesRead) {
                        if (buf[bufIndex] > SPACE) {
                            res = (res << 3) + (res << 1);
                            res += ints[buf[bufIndex++]];
                        }
                        else {
                            bufIndex++;
                            return res * sgn;
                        }
                    }

                    // Reload buffer
                    numBytesRead = stream.read(buf);
                    if (numBytesRead == EOF) return res * sgn;
                    bufIndex = 0;

                } while (true);
            }
            catch (IOException e) {
                e.printStackTrace();
                return -1;
            }

        }

        public long nextLong() {
            try {
                if (readJunk(DASH - 1) == EOF) throw new IOException();
                int sgn = 1;
                long res = 0L;
                c = buf[bufIndex];
                if (c == DASH) {
                    sgn = -1;
                    bufIndex++;
                }

                do {

                    while (bufIndex < numBytesRead) {
                        if (buf[bufIndex] > SPACE) {
                            res = (res << 3) + (res << 1);
                            res += ints[buf[bufIndex++]];
                        }
                        else {
                            bufIndex++;
                            return res * sgn;
                        }
                    }

                    // Reload buffer
                    numBytesRead = stream.read(buf);
                    if (numBytesRead == EOF) return res * sgn;
                    bufIndex = 0;

                } while (true);
            }
            catch (IOException e) {
                e.printStackTrace();
                return -1;
            }

        }

    }
}

