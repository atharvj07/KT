import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.ArrayList;
import java.io.OutputStreamWriter;
import java.util.function.LongPredicate;
import java.io.OutputStream;
import java.io.IOException;
import java.io.UncheckedIOException;
import java.util.List;
import java.io.Closeable;
import java.io.Writer;
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
            EApplemanAndAGame solver = new EApplemanAndAGame();
            solver.solve(1, in, out);
            out.close();
        }
    }

    static class EApplemanAndAGame {
        long linf = (long) 1e18 + 10;
        int inf = (int) 1e8;

        private long[][] mul(long[][] a, long[][] b) {
            long[][] ans = new long[4][4];
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    ans[i][j] = linf;
                    for (int k = 0; k < 4; k++) {
                        ans[i][j] = Math.min(a[i][k] + b[k][j], ans[i][j]);
                    }
                }
            }
            return ans;
        }

        private long[][] pow(long[][] x, long k) {
            if (k == 0) {
                long[][] ans = new long[4][4];
                SequenceUtils.deepFill(ans, linf);
                for (int i = 0; i < 4; i++) {
                    ans[i][i] = 0;
                }
                return ans;
            }
            long[][] ans = pow(x, k / 2);
            ans = mul(ans, ans);
            if (k % 2 == 1) {
                ans = mul(ans, x);
            }
            return ans;
        }

        public long atLeast(long[][] dp, long k) {
            long[][] res = pow(dp, k);
            long ans = linf;
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    ans = Math.min(ans, res[i][j]);
                }
            }
            return ans;
        }

        public void solve(int testNumber, FastInput in, FastOutput out) {
            long n = in.rl();
            char[] s = new char[(int) 1e5];
            int m = in.rs(s);
            SuffixAutomaton sa = new SuffixAutomaton('A', 'D');
            sa.prepareBuild();
            for (int i = 0; i < m; i++) {
                sa.build(s[i]);
            }
            SuffixAutomaton.SANode root = sa.root;
            long[][] dp = new long[4][4];
            for (int i = 0; i < 4; i++) {
                dp[i] = dp(root.next[i]);
            }
//        long[][] before = new long[4][4];
//        for(int i = 0; i <= 4; i++){
//            debug.debug("i", i);
//            debug.debug("x^i", before);
//            before = mul(before, dp);
//        }
//        debug.debug("dp", dp);
//        debug.debug("check", atLeast(dp, 4));
            LongPredicate predicate = mid -> {
                return atLeast(dp, mid) < n;
            };
            long ans = BinarySearch.lastTrue(predicate, 0, n) + 1;
            out.println(ans);
        }

        public long[] dp(SuffixAutomaton.SANode root) {
            if (root.nearest == null) {
                root.nearest = new long[4];
                Arrays.fill(root.nearest, inf);
                for (int i = 0; i < 4; i++) {
                    if (root.next[i] == null) {
                        root.nearest[i] = 1;
                        continue;
                    }
                    long[] res = dp(root.next[i]);
                    for (int j = 0; j < 4; j++) {
                        root.nearest[j] = Math.min(root.nearest[j], 1 + res[j]);
                    }
                }
            }
            return root.nearest;
        }

    }

    static class SuffixAutomaton {
        final int minCharacter;
        final int maxCharacter;
        final int alphabet;
        public SuffixAutomaton.SANode root;
        public SuffixAutomaton.SANode buildLast;
        public List<SuffixAutomaton.SANode> all;
        public boolean sorted = true;
        public long realTimeDistinctSubstr = -1;

        public void prepareBuild() {
            buildLast = root;
        }

        public SuffixAutomaton(int minCharacter, int maxCharacter) {
            this(minCharacter, maxCharacter, 0);
        }

        public SuffixAutomaton(int minCharacter, int maxCharacter, int cap) {
            this.minCharacter = minCharacter;
            this.maxCharacter = maxCharacter;
            all = new ArrayList<>(cap * 2 + 1);
            alphabet = maxCharacter - minCharacter + 1;
            buildLast = root = newNode();
            root.fail = null;
        }

        private SuffixAutomaton.SANode newNode() {
            SuffixAutomaton.SANode ans = new SuffixAutomaton.SANode(alphabet);
            all.add(ans);
            return ans;
        }

        private SuffixAutomaton.SANode cloneNode(SuffixAutomaton.SANode x) {
            SuffixAutomaton.SANode ans = x.clone();
            all.add(ans);
            return ans;
        }

        public void build(int c) {
            sorted = false;
            int index = c - minCharacter;
            SuffixAutomaton.SANode now = newNode();
            now.maxlen = buildLast.maxlen + 1;

            SuffixAutomaton.SANode p = visit(index, buildLast, null, now);
            if (p == null) {
                now.fail = root;
            } else {
                SuffixAutomaton.SANode q = p.next[index];
                if (q.maxlen == p.maxlen + 1) {
                    now.fail = q;
                } else {
                    SuffixAutomaton.SANode clone = cloneNode(q);
                    clone.maxlen = p.maxlen + 1;
                    now.fail = q.fail = clone;
                    if (realTimeDistinctSubstr != -1) {
                        realTimeDistinctSubstr -= q.maxlen - clone.fail.maxlen;
                        realTimeDistinctSubstr += q.maxlen - q.fail.maxlen;
                        realTimeDistinctSubstr += clone.maxlen - clone.fail.maxlen;
                    }
                    visit(index, p, q, clone);
                }
            }
            if (realTimeDistinctSubstr != -1) {
                realTimeDistinctSubstr += now.maxlen - now.fail.maxlen;
            }
            buildLast = now;
        }

        public SuffixAutomaton.SANode visit(int index, SuffixAutomaton.SANode trace, SuffixAutomaton.SANode target, SuffixAutomaton.SANode replacement) {
            while (trace != null && trace.next[index] == target) {
                trace.next[index] = replacement;
                trace = trace.fail;
            }
            return trace;
        }

        public static class SANode implements Cloneable {
            public SuffixAutomaton.SANode[] next;
            public long[] nearest;
            public SuffixAutomaton.SANode fail;
            public int maxlen;

            public SANode(int alphabet) {
                next = new SuffixAutomaton.SANode[alphabet];
            }

            public SuffixAutomaton.SANode clone() {
                try {
                    SuffixAutomaton.SANode res = (SuffixAutomaton.SANode) super.clone();
                    res.next = res.next.clone();
                    return res;
                } catch (CloneNotSupportedException e) {
                    throw new RuntimeException(e);
                }
            }

        }

    }

    static class SequenceUtils {
        public static void deepFill(Object array, long val) {
            if (!array.getClass().isArray()) {
                throw new IllegalArgumentException();
            }
            if (array instanceof long[]) {
                long[] longArray = (long[]) array;
                Arrays.fill(longArray, val);
            } else {
                Object[] objArray = (Object[]) array;
                for (Object obj : objArray) {
                    deepFill(obj, val);
                }
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

        public long rl() {
            return readLong();
        }

        public long readLong() {
            int sign = 1;

            skipBlank();
            if (next == '+' || next == '-') {
                sign = next == '+' ? 1 : -1;
                next = read();
            }

            long val = 0;
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

        public int rs(char[] data, int offset) {
            return readString(data, offset);
        }

        public int rs(char[] data) {
            return rs(data, 0);
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
        private static final int THRESHOLD = 32 << 10;
        private final Writer os;
        private StringBuilder cache = new StringBuilder(THRESHOLD * 2);

        public FastOutput append(CharSequence csq) {
            cache.append(csq);
            return this;
        }

        public FastOutput append(CharSequence csq, int start, int end) {
            cache.append(csq, start, end);
            return this;
        }

        private void afterWrite() {
            if (cache.length() < THRESHOLD) {
                return;
            }
            flush();
        }

        public FastOutput(Writer os) {
            this.os = os;
        }

        public FastOutput(OutputStream os) {
            this(new OutputStreamWriter(os));
        }

        public FastOutput append(char c) {
            cache.append(c);
            afterWrite();
            return this;
        }

        public FastOutput append(long c) {
            cache.append(c);
            afterWrite();
            return this;
        }

        public FastOutput append(String c) {
            cache.append(c);
            afterWrite();
            return this;
        }

        public FastOutput println(long c) {
            return append(c).println();
        }

        public FastOutput println() {
            return append(System.lineSeparator());
        }

        public FastOutput flush() {
            try {
//            boolean success = false;
//            if (stringBuilderValueField != null) {
//                try {
//                    char[] value = (char[]) stringBuilderValueField.get(cache);
//                    os.write(value, 0, cache.length());
//                    success = true;
//                } catch (Exception e) {
//                }
//            }
//            if (!success) {
                os.append(cache);
//            }
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

    static class BinarySearch {
        private BinarySearch() {
        }

        public static long lastTrue(LongPredicate predicate, long l, long r) {
            assert l <= r;
            while (l != r) {
                long mid = DigitUtils.ceilAverage(l, r);
                if (predicate.test(mid)) {
                    l = mid;
                } else {
                    r = mid - 1;
                }
            }
            if (!predicate.test(l)) {
                l--;
            }
            return l;
        }

    }

    static class DigitUtils {
        private DigitUtils() {
        }

        public static long ceilAverage(long x, long y) {
            return (x | y) - ((x ^ y) >> 1);
        }

    }
}

