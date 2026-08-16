import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.io.UncheckedIOException;
import java.util.Objects;
import java.util.Vector;
import java.util.StringTokenizer;
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
        PrintWriter out = new PrintWriter(outputStream);
        ENegativeDoubling solver = new ENegativeDoubling();
        solver.solve(1, in, out);
        out.close();
    }

    static class ENegativeDoubling {
        public void solve(int testNumber, LightScanner in, PrintWriter out) {
            int n = in.ints();
            long[] a = in.longs(n);
            long[] dpr = new long[n + 1];
            long[] dpl = new long[n + 1];
            Stack<Vec2l> cap = new Stack<>();
            for (int i = n - 2; i >= 0; i--) {
                long v = a[i + 1];
                long withdraw = 0;
                while (a[i] > v) {
                    v *= 4;
                    withdraw++;
                }


                long ans = 0;
                while (withdraw > 0 && !cap.isEmpty()) {
                    Vec2l c = cap.pop();
                    if (c.getY() <= withdraw) {
                        withdraw -= c.getY();
                        ans += c.getY() * (c.getX() - i);
                    } else {
                        ans += withdraw * (c.getX() - i);
                        cap.push(new Vec2l(c.getX(), c.getY() - withdraw));
                        withdraw = 0;
                    }
                }
                if (withdraw > 0) {
                    ans += withdraw * (n - i - 1);
                }

                long w = a[i];
                long store = 0;
                while (w * 4 <= v) {
                    w *= 4;
                    store++;
                }
                if (store > 0) {
                    cap.push(new Vec2l(i, store));
                }

                dpr[i] = dpr[i + 1] + ans;
            }

            cap.clear();
            for (int i = 1; i < n; i++) {
                long v = a[i - 1];

                long withdraw = 0;
                while (a[i] > v) {
                    v *= 4;
                    withdraw++;
                }


                long ans = 0;
                while (withdraw > 0 && !cap.isEmpty()) {
                    Vec2l c = cap.pop();
                    if (c.getY() <= withdraw) {
                        withdraw -= c.getY();
                        ans += c.getY() * (i - c.getX());
                    } else {
                        ans += withdraw * (i - c.getX());
                        cap.push(new Vec2l(c.getX(), c.getY() - withdraw));
                        withdraw = 0;
                    }
                }
                if (withdraw > 0) {
                    ans += withdraw * i;
                }

                long w = a[i];
                long store = 0;
                while (w * 4 <= v) {
                    w *= 4;
                    store++;
                }
                if (store > 0) {
                    cap.push(new Vec2l(i, store));
                }

                dpl[i + 1] = dpl[i] + ans;
            }

            long ans = Long.MAX_VALUE;
            for (int i = 0; i <= n; i++) {
                ans = Math.min(ans, dpl[i] * 2 + i + dpr[i] * 2);
            }
            out.println(ans);
            //out.println(Arrays.toString(dpr));
            //out.println(Arrays.toString(dpl));
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

    static class Vec2l {
        private final long x;
        private final long y;

        public Vec2l(long x, long y) {
            this.x = x;
            this.y = y;
        }

        public long getX() {
            return x;
        }

        public long getY() {
            return y;
        }

        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Vec2l vec2i = (Vec2l) o;
            return x == vec2i.x &&
                    y == vec2i.y;
        }

        public int hashCode() {
            return Objects.hash(x, y);
        }

        public String toString() {
            return "(" + x + ", " + y + ")";
        }

    }
}

