import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.util.Random;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Rustam Musin (t.me/musin_acm)
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        ENikitaIPoryadkovayaStatistika solver = new ENikitaIPoryadkovayaStatistika();
        solver.solve(1, in, out);
        out.close();
    }

    static class ENikitaIPoryadkovayaStatistika {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            if (false) {
                new Tester().test();
            }
            int n = in.readInt();
            int x = in.readInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = in.readInt() < x ? 1 : 0;
            }
            long[] answer = new Solve().solve(a);
            out.print(answer);
        }

        int[] calcPrefixCount(int[] a) {
            int n = a.length;
            int[] cnt = new int[n + 1];
            int s = 0;
            for (int i = 0; i < n; i++) {
                s += a[i];
                cnt[s]++;
            }
            return cnt;
        }

        void reverse(int[] a) {
            int n = a.length;
            for (int i = 0; i < n - i - 1; i++) {
                int t = a[i];
                a[i] = a[n - i - 1];
                a[n - i - 1] = t;
            }
        }

        class Tester {
            Random rnd = new Random(239);

            void test() {
                for (int t = 0; ; t++) {
                    int n = rnd.nextInt(10) + 1;
                    int x = 1;
                    int[] a = new int[n];
                    for (int i = 0; i < n; i++) {
                        a[i] = rnd.nextInt(2);
                    }
                    long[] solve = new Solve().solve(a);
                    long[] naive = new Naive().solve(a);
                    if (!Arrays.equals(solve, naive)) {
                        System.err.println(Arrays.toString(a));
                        System.err.println(Arrays.toString(naive));
                        System.err.println(Arrays.toString(solve));
                    }
                }
            }

        }

        class Naive {
            long[] solve(int[] a) {
                int n = a.length;
                long[] answer = new long[n + 1];
                for (int i = 0; i < n; i++) {
                    int s = 0;
                    for (int j = i; j < n; j++) {
                        s += a[j];
                        answer[s]++;
                    }
                }
                return answer;
            }

        }

        class Solve {
            long[] solve(int[] a) {
                int n = a.length;
                int[] prefix = calcPrefixCount(a);
                reverse(a);
                int[] sufix = calcPrefixCount(a);
                reverse(a);
                long[] res = new FFT().multiply(prefix, sufix);
                int sum = 0;
                for (int val : a) {
                    sum += val;
                }
                res[sum] = 0;
                for (int i = 0; i < n; ) {
                    if (a[i] == 1) {
                        i++;
                        continue;
                    }
                    int j = i;
                    while (j + 1 < n && a[j + 1] == 0) {
                        j++;
                    }
                    int len = j - i + 1;
                    res[sum] += len * (len + 1L) / 2;
                    i = j + 1;
                }
                long[] ans = new long[n + 1];
                for (int i = 0; i < n + 1; i++) {
                    ans[i] = res[sum + i];
                }
                return ans;
            }

        }

        class FFT {
            void fft(double[] real, double[] imag, boolean inv) {
                int n = real.length;
                int m = 0;
                while (1 << m < n) {
                    m++;
                }
                int[] rev = new int[n];
                for (int i = 1, j = -1; i < n; i++) {
                    if ((i & (i - 1)) == 0) {
                        j++;
                    }
                    rev[i] = rev[i ^ (1 << j)] | (1 << (m - j - 1));
                    if (i < rev[i]) {
                        swap(real, i, rev[i]);
                        swap(imag, i, rev[i]);
                    }
                }

                for (int len = 1; len < n; len <<= 1) {
                    double w = Math.PI / len;
                    if (inv) {
                        w = -w;
                    }
                    double wReal = Math.cos(w);
                    double wImag = Math.sin(w);
                    for (int i = 0; i < n; i += len << 1) {
                        double rReal = 1;
                        double rImag = 0;
                        for (int j = 0; j < len; j++) {
                            double real1 = real[i + j];
                            double imag1 = imag[i + j];
                            double real2 = real[i + j + len];
                            double imag2 = imag[i + j + len];
                            double real3 = real2 * rReal - imag2 * rImag;
                            double imag3 = real2 * rImag + imag2 * rReal;
                            real[i + j] = real1 + real3;
                            imag[i + j] = imag1 + imag3;
                            real[i + j + len] = real1 - real3;
                            imag[i + j + len] = imag1 - imag3;
                            double nextRReal = rReal * wReal - rImag * wImag;
                            double nextRImag = rReal * wImag + rImag * wReal;
                            rReal = nextRReal;
                            rImag = nextRImag;
                        }
                    }
                }

                if (inv) {
                    for (int i = 0; i < n; i++) {
                        real[i] /= n;
                        imag[i] /= n;
                    }
                }
            }

            void swap(double[] a, int i, int j) {
                double t = a[i];
                a[i] = a[j];
                a[j] = t;
            }

            double[] copy(int[] a, int n) {
                double[] b = new double[n];
                for (int i = 0; i < a.length; i++) {
                    b[i] = a[i];
                }
                return b;
            }

            long[] multiply(int[] a, int[] b) {
                int n = Math.max(1, Integer.highestOneBit(Math.max(a.length, b.length) - 1) << 2);
                double[] aReal = copy(a, n);
                double[] aImag = new double[n];
                double[] bReal = copy(b, n);
                double[] bImag = new double[n];
                fft(aReal, aImag, false);
                fft(bReal, bImag, false);
                for (int i = 0; i < n; i++) {
                    double real = aReal[i] * bReal[i] - aImag[i] * bImag[i];
                    double imag = aReal[i] * bImag[i] + aImag[i] * bReal[i];
                    aReal[i] = real;
                    aImag[i] = imag;
                }
                fft(aReal, aImag, true);
                long[] result = new long[n];
                for (int i = 0; i < n; i++) {
                    result[i] = (long) (aReal[i] + 0.5);
                }
                return result;
            }

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

        public void print(long[] array) {
            for (int i = 0; i < array.length; i++) {
                if (i != 0) {
                    writer.print(' ');
                }
                writer.print(array[i]);
            }
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
}

