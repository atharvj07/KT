import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UncheckedIOException;
import java.nio.charset.Charset;
import java.util.StringTokenizer;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author mikit
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        LightScanner in = new LightScanner(inputStream);
        LightWriter out = new LightWriter(outputStream);
        FXorSum3 solver = new FXorSum3();
        solver.solve(1, in, out);
        out.close();
    }

    static class FXorSum3 {
        private static final int BIT = 60;

        public void solve(int testNumber, LightScanner in, LightWriter out) {
            // out.setBoolLabel(LightWriter.BoolLabel.YES_NO_FIRST_UP);
            int n = in.ints();
            long[] a = in.longs(n);
            int[] cnt = new int[BIT];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < BIT; j++) {
                    if ((a[i] & (1L << j)) != 0) cnt[j]++;
                }
            }
            long ans = 0;
            for (int i = 0; i < BIT; i++) {
                if (cnt[i] % 2 == 1) {
                    long bit = 1L << i;
                    cnt[i] = 0;
                    ans |= bit;
                    for (int j = 0; j < n; j++) {
                        a[j] &= ~bit;
                    }
                }
            }


            int rank = 0;
            for (int col = BIT - 1; col >= 0; col--) {

                int pivot = -1;
                for (int row = rank; row < n; row++) {
                    if ((a[row] & (1L << col)) != 0) {
                        pivot = row;
                    }
                }
                if (pivot == -1) continue;


                long t = a[pivot];
                a[pivot] = a[rank];
                a[rank] = t;

                for (int row = 0; row < n; row++) {
                    if (row != rank && (a[row] & (1L << col)) != 0) {
                        a[row] ^= a[rank];
                    }
                }
                rank++;
            }
            long color = 0;
            for (int i = 0; i < n; i++) {
                if (color < (color ^ a[i])) {
                    color ^= a[i];
                }
            }

            out.ans(ans + (color << 1)).ln();
        }

    }

    static class LightScanner {
        private BufferedReader reader = null;
        private StringTokenizer tokenizer = null;

        public LightScanner(InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
        }

        public String string() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new UncheckedIOException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int ints() {
            return Integer.parseInt(string());
        }

        public long longs() {
            return Long.parseLong(string());
        }

        public long[] longs(int length) {
            return IntStream.range(0, length).mapToLong(x -> longs()).toArray();
        }

    }

    static class LightWriter implements AutoCloseable {
        private final Writer out;
        private boolean autoflush = false;
        private boolean breaked = true;

        public LightWriter(Writer out) {
            this.out = out;
        }

        public LightWriter(OutputStream out) {
            this(new BufferedWriter(new OutputStreamWriter(out, Charset.defaultCharset())));
        }

        public LightWriter print(char c) {
            try {
                out.write(c);
                breaked = false;
            } catch (IOException ex) {
                throw new UncheckedIOException(ex);
            }
            return this;
        }

        public LightWriter print(String s) {
            try {
                out.write(s, 0, s.length());
                breaked = false;
            } catch (IOException ex) {
                throw new UncheckedIOException(ex);
            }
            return this;
        }

        public LightWriter ans(String s) {
            if (!breaked) {
                print(' ');
            }
            return print(s);
        }

        public LightWriter ans(long l) {
            return ans(Long.toString(l));
        }

        public LightWriter ln() {
            print(System.lineSeparator());
            breaked = true;
            if (autoflush) {
                try {
                    out.flush();
                } catch (IOException ex) {
                    throw new UncheckedIOException(ex);
                }
            }
            return this;
        }

        public void close() {
            try {
                out.close();
            } catch (IOException ex) {
                throw new UncheckedIOException(ex);
            }
        }

    }
}

