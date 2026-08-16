import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.FileNotFoundException;
import java.util.StringTokenizer;
import java.io.Writer;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Asgar Javadov
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        DOmkarAndCircle solver = new DOmkarAndCircle();
        solver.solve(1, in, out);
        out.close();
    }

    static class DOmkarAndCircle {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.nextInt();
            int[] a = in.readIntArray(n);

            if (n == 1) {
                out.println(a[0]);
                return;
            }

            long oddSuffixSum = a[0];
            long evenSuffixSum = 0L;
            for (int i = 1; i < a.length; i += 2) {
                evenSuffixSum += a[i];
                oddSuffixSum += a[i + 1];
            }

            long result = compute(a[0], a[a.length - 1], evenSuffixSum);
            long oddPrefixSum = 0L;
            long evenPrefixSum = 0L;
            for (int i = 0; i < a.length - 1; ++i) {
                if (i % 2 == 0) {
                    oddSuffixSum -= a[i];
                    result = Math.max(result, compute(a[i], a[i + 1], evenPrefixSum + oddSuffixSum));
                    oddPrefixSum += a[i];
                } else {
                    evenSuffixSum -= a[i];
                    result = Math.max(result, compute(a[i], a[i + 1], oddPrefixSum + evenSuffixSum));
                    evenPrefixSum += a[i];
                }
            }

            out.println(result);
        }

        private long compute(int a, int b, long s) {
            return s + a + b - ArrayUtils.min(a, b, s);
        }

    }

    static class ArrayUtils {
        public static long min(long... args) {
            long res = args[0];
            for (int i = 1; i < args.length; ++i)
                if (res > args[i])
                    res = args[i];
            return res;
        }

    }

    static class OutputWriter extends PrintWriter {
        public OutputWriter(OutputStream outputStream) {
            super(outputStream);
        }

        public OutputWriter(Writer writer) {
            super(writer);
        }

        public OutputWriter(String filename) throws FileNotFoundException {
            super(filename);
        }

        public void close() {
            super.close();
        }

    }

    static class InputReader extends BufferedReader {
        StringTokenizer tokenizer;

        public InputReader(InputStream inputStream) {
            super(new InputStreamReader(inputStream), 32768);
        }

        public InputReader(String filename) {
            super(new InputStreamReader(Thread.currentThread().getContextClassLoader().getResourceAsStream(filename)));
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(readLine());
                } catch (IOException e) {
                    throw new RuntimeException();
                }
            }
            return tokenizer.nextToken();
        }

        public Integer nextInt() {
            return Integer.valueOf(next());
        }

        public int[] readIntArray(int size) {
            int[] array = new int[size];
            for (int i = 0; i < size; i++)
                array[i] = nextInt();
//        IntStream.generate(this::nextInt).limit(size).toArray();
            return array;
        }

    }
}

