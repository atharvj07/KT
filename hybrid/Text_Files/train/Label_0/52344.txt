import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
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
        PrintWriter out = new PrintWriter(outputStream);
        TaskF solver = new TaskF();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskF {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            int k = in.nextInt();
            int[][][] ways = new int[n + 1][][];
            for (int i = 0; i <= n; ++i) {
                ways[i] = new int[i + 1][1 << i];
            }
            for (int i = 0; i <= n; ++i) {
                String x = in.next();
                for (int j = 0; j < x.length(); ++j) {
                    if (x.charAt(j) == '1') ++ways[i][0][j];
                }
            }
            int[] ntz = new int[1 << n];
            for (int i = 1; i < ntz.length; ++i) ntz[i] = Integer.numberOfTrailingZeros(i);
            for (int len = n; len >= 0; --len) {
                for (int pos = 0; pos < len; ++pos) {
                    for (int what = 0; what < (1 << len); ++what) {
                        int ow = ways[len][pos][what];
                        if (ow == 0) continue;
                        ways[pos][pos][what & ((1 << pos) - 1)] += ow;
                        int extra = what >> pos;
                        if (extra != 0) {
                            int oneAt = ntz[extra];//Integer.numberOfTrailingZeros(extra);
                            ways[len - oneAt][pos + 1][(what & ((1 << pos) - 1)) + ((extra >> oneAt) << pos)] += ow;
                        }
                        if (extra != (1 << (len - pos)) - 1) {
                            int zeroAt = ntz[extra + 1];//Integer.numberOfTrailingZeros(extra + 1);
                            ways[len - zeroAt][pos + 1][(what & ((1 << pos) - 1)) + ((extra >> zeroAt) << pos)] += ow;
                        }
                    }
                }
                for (int what = 0; what < (1 << len); ++what) {
                    if (ways[len][len][what] >= k) {
                        for (int pos = len - 1; pos >= 0; --pos)
                            if ((what & (1 << pos)) != 0) {
                                out.print('1');
                            } else {
                                out.print('0');
                            }
                        out.println();
                        return;
                    }
                }
            }
            throw new RuntimeException();
        }

    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

