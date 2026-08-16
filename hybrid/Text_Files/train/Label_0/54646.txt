import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Random;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Vadim Semenov
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskB solver = new TaskB();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskB {
        public void solve(final int testNumber, final InputReader in, final PrintWriter out) {
            int counter = in.nextInt();
            int k = in.nextInt();
            int[] array = in.nextIntArray(counter);
            ArrayUtils.sort(array);
            long sum = 0;
            for (int i = 1; i < counter; ++i) {
                sum += array[i] - array[i - 1];
            }
            int big = counter % k;
            int small = k - big;
            int bigLength = (counter + k - 1) / k;
            int smallLength = counter / k;
            long[][] dp = new long[big + 1][small + 1];
            for (int x = 0; x <= big; ++x) {
                for (int y = 0; y <= small; ++y) {
                    int offset = x * bigLength + y * smallLength;
                    if (0 < offset && offset < counter) {
                        long val = dp[x][y] + (array[offset] - array[offset - 1]);
                        if (x < big) {
                            dp[x + 1][y] = Math.max(dp[x + 1][y], val);
                        }
                        if (y < small) {
                            dp[x][y + 1] = Math.max(dp[x][y + 1], val);
                        }
                    }
                }
            }
            out.println(sum - dp[big][small]);
        }

    }

    static class InputReader {
        private final BufferedReader reader;
        private StringTokenizer tokenizer;

        public InputReader(InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
        }

        public int[] nextIntArray(int size) {
            int[] array = new int[size];
            for (int i = 0; i < size; ++i) {
                array[i] = nextInt();
            }
            return array;
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                tokenizer = new StringTokenizer(readLine());
            }
            return tokenizer.nextToken();
        }

        public String readLine() {
            String line;
            try {
                line = reader.readLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            return line;
        }

    }

    static class ArrayUtils {
        private static final Random RANDOM = ThreadLocalRandom.current();

        private ArrayUtils() {
        }

        public static void shuffle(int[] array) {
            for (int i = 1; i < array.length; ++i) {
                int j = RANDOM.nextInt(i + 1);
                int tmp = array[i];
                array[i] = array[j];
                array[j] = tmp;
            }
        }

        public static void sort(int[] array) {
            shuffle(array);
            Arrays.sort(array);
        }

    }
}

