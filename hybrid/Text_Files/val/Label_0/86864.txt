import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Collection;
import java.io.IOException;
import java.util.Deque;
import java.io.UncheckedIOException;
import java.io.Closeable;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) throws Exception {
        Thread thread = new Thread(null, new TaskAdapter(), "", 1 << 29);
        thread.start();
        thread.join();
    }

    static class TaskAdapter implements Runnable {
        @Override
        public void run() {
            InputStream inputStream = System.in;
            OutputStream outputStream = System.out;
            FastInput in = new FastInput(inputStream);
            FastOutput out = new FastOutput(outputStream);
            DKeepDistances solver = new DKeepDistances();
            solver.solve(1, in, out);
            out.close();
        }
    }

    static class DKeepDistances {
        public void solve(int testNumber, FastInput in, FastOutput out) {
            int n = in.readInt();
            int k = in.readInt();
            int[] x = new int[n];
            in.populate(x);

            int[][] pre = new int[20][n];
            int[][] post = new int[20][n];
            long[][] preSum = new long[20][n];
            long[][] postSum = new long[20][n];

            Deque<Integer> dq = new ArrayDeque<>(n);
            dq.clear();
            for (int i = 0; i < n; i++) {
                while (!dq.isEmpty() && x[i] - x[dq.peekFirst()] >= k) {
                    post[0][dq.removeFirst()] = i;
                }
                dq.addLast(i);
            }
            while (!dq.isEmpty()) {
                post[0][dq.removeFirst()] = n;
            }
            for (int i = n - 1; i >= 0; i--) {
                while (!dq.isEmpty() && x[dq.peekFirst()] - x[i] >= k) {
                    pre[0][dq.removeFirst()] = i;
                }
                dq.addLast(i);
            }
            while (!dq.isEmpty()) {
                pre[0][dq.removeFirst()] = -1;
            }
            for (int i = 0; i < n; i++) {
                if (pre[0][i] >= 0) {
                    preSum[0][i] += pre[0][i];
                }
                if (post[0][i] < n) {
                    postSum[0][i] += post[0][i];
                }
            }

            for (int i = 0; i + 1 < 20; i++) {
                for (int j = 0; j < n; j++) {
                    pre[i + 1][j] = pre[i][j] == -1 ? -1 : pre[i][pre[i][j]];
                    post[i + 1][j] = post[i][j] == n ? n : post[i][post[i][j]];
                    preSum[i + 1][j] = pre[i][j] == -1 ? preSum[i][j] :
                            preSum[i][j] + preSum[i][pre[i][j]];
                    postSum[i + 1][j] = post[i][j] == n ? postSum[i][j] :
                            postSum[i][j] + postSum[i][post[i][j]];
                }
            }


            int q = in.readInt();

            for (int i = 0; i < q; i++) {
                int l = in.readInt() - 1;
                int r = in.readInt() - 1;

                int lr = l;
                long sumLR = l;
                int size = 1;
                for (int j = 20 - 1; j >= 0; j--) {
                    if (post[j][lr] <= r) {
                        size += 1 << j;
                        sumLR += postSum[j][lr];
                        lr = post[j][lr];
                        continue;
                    }
                }

                int rl = r;
                long sumRL = r;
                for (int j = 20 - 1; j >= 0; j--) {
                    if (pre[j][rl] >= l) {
                        sumRL += preSum[j][rl];
                        rl = pre[j][rl];
                        continue;
                    }
                }

                long ans = sumRL - sumLR + size;
                out.println(ans);
            }

        }

    }

    static class FastInput {
        private final InputStream is;
        private byte[] buf = new byte[1 << 13];
        private int bufLen;
        private int bufOffset;
        private int next;

        public FastInput(InputStream is) {
            this.is = is;
        }

        public void populate(int[] data) {
            for (int i = 0; i < data.length; i++) {
                data[i] = readInt();
            }
        }

        private int read() {
            while (bufLen == bufOffset) {
                bufOffset = 0;
                try {
                    bufLen = is.read(buf);
                } catch (IOException e) {
                    bufLen = -1;
                }
                if (bufLen == -1) {
                    return -1;
                }
            }
            return buf[bufOffset++];
        }

        public void skipBlank() {
            while (next >= 0 && next <= 32) {
                next = read();
            }
        }

        public int readInt() {
            int sign = 1;

            skipBlank();
            if (next == '+' || next == '-') {
                sign = next == '+' ? 1 : -1;
                next = read();
            }

            int val = 0;
            if (sign == 1) {
                while (next >= '0' && next <= '9') {
                    val = val * 10 + next - '0';
                    next = read();
                }
            } else {
                while (next >= '0' && next <= '9') {
                    val = val * 10 - next + '0';
                    next = read();
                }
            }

            return val;
        }

    }

    static class FastOutput implements AutoCloseable, Closeable, Appendable {
        private StringBuilder cache = new StringBuilder(10 << 20);
        private final Writer os;

        public FastOutput append(CharSequence csq) {
            cache.append(csq);
            return this;
        }

        public FastOutput append(CharSequence csq, int start, int end) {
            cache.append(csq, start, end);
            return this;
        }

        public FastOutput(Writer os) {
            this.os = os;
        }

        public FastOutput(OutputStream os) {
            this(new OutputStreamWriter(os));
        }

        public FastOutput append(char c) {
            cache.append(c);
            return this;
        }

        public FastOutput append(long c) {
            cache.append(c);
            return this;
        }

        public FastOutput println(long c) {
            return append(c).println();
        }

        public FastOutput println() {
            cache.append(System.lineSeparator());
            return this;
        }

        public FastOutput flush() {
            try {
                os.append(cache);
                os.flush();
                cache.setLength(0);
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
            return this;
        }

        public void close() {
            flush();
            try {
                os.close();
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        }

        public String toString() {
            return cache.toString();
        }

    }
}

