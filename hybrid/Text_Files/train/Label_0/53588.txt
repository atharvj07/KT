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
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskC solver = new TaskC();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskC {
        final long infinity = Long.MAX_VALUE / 3;
        FastScanner in;

        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            this.in = in;
            long bytesLeft0 = assertedNextInt();
            long timeLeft0 = assertedNextInt();
            long t0 = assertedNextInt();

            long a1 = assertedNextInt();
            long t1 = assertedNextInt();
            long p1 = assertedNextInt();

            long a2 = assertedNextInt();
            long t2 = assertedNextInt();
            long p2 = assertedNextInt();
            long u = solve(bytesLeft0, timeLeft0, t0, a1, t1, p1, a2, t2, p2);
            long v = solve(bytesLeft0, timeLeft0, t0, a2, t2, p2, a1, t1, p1);
            long ans = Math.min(u, v);
            if (ans >= infinity) {
                ans = -1;
            }
            out.println(ans);
        }

        private long solve(long bytesLeft0, long timeLeft0, long t0, long a1, long t1, long p1, long a2, long t2, long p2) {
            final int N = (int) 1e7 + 20;
            long ans = infinity;
            for (int k1 = 0; k1 <= N; k1++) {
                long cost1 = k1 * p1;
                long bytesDownloaded1 = Math.min(bytesLeft0, k1 * a1);
                long time1 = bytesDownloaded1 * t1;
                long bytesLeft1 = bytesLeft0 - bytesDownloaded1;
                long timeLeft1 = timeLeft0 - time1;
                if (timeLeft1 < 0) {
                    continue;
                }
                if (bytesLeft1 == 0) {
                    ans = Math.min(ans, cost1);
                    continue;
                }
                if (t0 * bytesLeft1 <= timeLeft1) {
                    ans = Math.min(ans, cost1);
                    continue;
                }
                if (t0 <= t2) {
                    continue;
                }
                if (bytesLeft1 * t2 > timeLeft1) {
                    continue;
                }
                long bytes0 = Math.min(bytesLeft1, (timeLeft1 - bytesLeft1 * t2) / (t0 - t2));
                long bytes2 = bytesLeft1 - bytes0;
                long k2 = (bytes2 + a2 - 1) / a2;

                long cost2 = k2 * p2;
                ans = Math.min(ans, cost1 + cost2);
            }
            return ans;
        }

        private long assertedNextInt() {
            long x = in.nextLong();
            if (x < 1 || x > (int) 1e7) {
                throw new AssertionError();
            }
            return x;
        }

    }

    static class FastScanner {
        private BufferedReader in;
        private StringTokenizer st;

        public FastScanner(InputStream stream) {
            in = new BufferedReader(new InputStreamReader(stream));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(in.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

    }
}

