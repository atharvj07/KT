import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.IOException;
import java.util.HashMap;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Map;
import java.io.BufferedReader;
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
        Map<Long, Long> cache = new HashMap<>();

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            long[] a = new long[n];
            for (int i = 0; i < n; ++i) {
                a[i] = in.nextInt();
            }
            long res = doit(a, 0, n - 1, 1, 1);
            out.println(res);
        }

        private long doit(long[] v, int left, int right, long a, long b) {
            if (left + 1 == right) {
                return v[left] * a + v[right] * b;
            }
            long key = left * 478156473535615131L + right * 4186574361539994L + a * 897748627637161L + b * 8548931758436781L;
            Long cached = cache.get(key);
            if (cached != null) return cached;
            long res = Long.MAX_VALUE;
            for (int mid = left + 1; mid < right; ++mid) {
                res = Math.min(res, doit(v, left, mid, a, a + b) + doit(v, mid, right, a + b, b) - v[mid] * (a + b));
            }
            cache.put(key, res);
            return res;
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

