import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.io.UncheckedIOException;
import java.io.Closeable;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) throws Exception {
        Thread thread = new Thread(null, new TaskAdapter(), "", 1 << 27);
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
            CKDMC solver = new CKDMC();
            solver.solve(1, in, out);
            out.close();
        }
    }

    static class CKDMC {
        public void solve(int testNumber, FastInput in, FastOutput out) {
            int n = in.readInt();
            char[] s = new char[n];
            in.readString(s, 0);
            int q = in.readInt();

            for (int i = 0; i < q; i++) {
                int k = in.readInt();
                long ans = 0;
                long dCnt = 0;
                long mCnt = 0;
                long dmCnt = 0;
                IntegerDeque deque = new IntegerRange2DequeAdapter(x -> x, 0, n - 1);
                for (int j = 0; j < n; j++) {
                    while (j - deque.peekFirst() >= k) {
                        int index = deque.removeFirst();
                        if (s[index] == 'D') {
                            dmCnt -= mCnt;
                            dCnt--;
                        }
                        if (s[index] == 'M') {
                            mCnt--;
                        }
                    }
                    if (s[j] == 'D') {
                        dCnt++;
                    }
                    if (s[j] == 'M') {
                        mCnt++;
                        dmCnt += dCnt;
                    }
                    if (s[j] == 'C') {
                        ans += dmCnt;
                    }
                }
                out.println(ans);
            }
        }

    }

    static class IntegerRange2DequeAdapter implements IntegerDeque {
        IntToIntegerFunction function;
        int l;
        int r;

        public IntegerRange2DequeAdapter(IntToIntegerFunction function, int l, int r) {
            this.function = function;
            this.l = l;
            this.r = r;
        }

        public int peekFirst() {
            return function.apply(l);
        }

        public int removeFirst() {
            return function.apply(l++);
        }

    }

    static interface IntegerStack {
    }

    static interface IntegerDeque extends IntegerStack {
        int removeFirst();

        int peekFirst();

    }

    static interface IntToIntegerFunction {
        int apply(int x);

    }

    static class FastInput {
        private final InputStream is;
        private byte[] buf = new byte[1 << 20];
        private int bufLen;
        private int bufOffset;
        private int next;

        public FastInput(InputStream is) {
            this.is = is;
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

        public int readString(char[] data, int offset) {
            skipBlank();

            int originalOffset = offset;
            while (next > 32) {
                data[offset++] = (char) next;
                next = read();
            }

            return offset - originalOffset;
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

