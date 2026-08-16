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
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt(), k = in.nextInt();
            int[] a = in.readIntArray(n);
            int le = 0;
            int ri = (int) 1e9 + 5;
            while (ri - le > 1) {
                int mid = (le + ri) >> 1;
                if (canMin(mid, k, a)) {
                    le = mid;
                } else {
                    ri = mid;
                }
            }
            int min = le;
            le = 0;
            ri = (int) 1e9 + 5;
            while (le < ri) {
                int mid = (le + ri) >> 1;
                if (canMax(mid, k, a)) {
                    ri = mid;
                } else {
                    le = mid + 1;
                }
            }
            int max = le;
            out.println(max - min);
        }

        boolean canMin(int value, int operations, int[] a) {
            long need = 0L;
            int n = a.length;
            for (int i = 0; i < n; i++) {
                if (a[i] < value) {
                    need += (1L * (value - a[i]));
                }
            }
            if (need > 1L * operations) {
                return false;
            }
            for (int i = 0; i < n; i++) {
                if (a[i] > value) {
                    need -= (1L * (a[i] - value));
                }
            }
            return need <= 0L;
        }

        boolean canMax(int value, int operations, int[] a) {
            long need = 0L;
            int n = a.length;
            for (int i = 0; i < n; i++) {
                if (a[i] > value) {
                    need += (1L * (a[i] - value));
                }
            }
            if (need > 1L * operations) {
                return false;
            }
            for (int i = 0; i < n; i++) {
                if (a[i] < value) {
                    need -= (1L * (value - a[i]));
                }
            }
            return need <= 0L;
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

        public int[] readIntArray(int n) {
            int[] ret = new int[n];
            for (int i = 0; i < n; i++) {
                ret[i] = nextInt();
            }
            return ret;
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

