import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Arrays;
import java.io.IOException;
import java.util.Random;
import java.io.UncheckedIOException;
import java.util.Objects;
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
            DLargestSubmatrix3 solver = new DLargestSubmatrix3();
            solver.solve(1, in, out);
            out.close();
        }
    }

    static class DLargestSubmatrix3 {
        public void solve(int testNumber, FastInput in, FastOutput out) {
            int n = in.ri();
            int m = in.ri();
            int[][] mat = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    mat[i][j] = in.ri();
                }
            }
            int ans = RectOnGridProblem.maxAreaDistinctRect(mat).a;
            out.println(ans);
        }

    }

    static class SequenceUtils {
        public static boolean equal(int[] a, int al, int ar, int[] b, int bl, int br) {
            if ((ar - al) != (br - bl)) {
                return false;
            }
            for (int i = al, j = bl; i <= ar; i++, j++) {
                if (a[i] != b[j]) {
                    return false;
                }
            }
            return true;
        }

    }

    static interface IntegerIterator {
        boolean hasNext();

        int next();

    }

    static class Pair<A, B> implements Cloneable {
        public A a;
        public B b;

        public Pair(A a, B b) {
            this.a = a;
            this.b = b;
        }

        public String toString() {
            return "a=" + a + ",b=" + b;
        }

        public int hashCode() {
            return a.hashCode() * 31 + b.hashCode();
        }

        public boolean equals(Object obj) {
            Pair<A, B> casted = (Pair<A, B>) obj;
            return Objects.equals(casted.a, a) && Objects.equals(casted.b, b);
        }

        public Pair<A, B> clone() {
            try {
                return (Pair<A, B>) super.clone();
            } catch (CloneNotSupportedException e) {
                throw new RuntimeException(e);
            }
        }

    }

    static class RandomWrapper {
        private Random random;
        public static final RandomWrapper INSTANCE = new RandomWrapper();

        public RandomWrapper() {
            this(new Random());
        }

        public RandomWrapper(Random random) {
            this.random = random;
        }

        public RandomWrapper(long seed) {
            this(new Random(seed));
        }

        public int nextInt(int l, int r) {
            return random.nextInt(r - l + 1) + l;
        }

    }

    static class IntegerArrayList implements Cloneable {
        private int size;
        private int cap;
        private int[] data;
        private static final int[] EMPTY = new int[0];

        public IntegerArrayList(int cap) {
            this.cap = cap;
            if (cap == 0) {
                data = EMPTY;
            } else {
                data = new int[cap];
            }
        }

        public IntegerArrayList(int[] data) {
            this(0);
            addAll(data);
        }

        public IntegerArrayList(IntegerArrayList list) {
            this.size = list.size;
            this.cap = list.cap;
            this.data = Arrays.copyOf(list.data, size);
        }

        public IntegerArrayList() {
            this(0);
        }

        public void ensureSpace(int req) {
            if (req > cap) {
                while (cap < req) {
                    cap = Math.max(cap + 10, 2 * cap);
                }
                data = Arrays.copyOf(data, cap);
            }
        }

        public void addAll(int[] x) {
            addAll(x, 0, x.length);
        }

        public void addAll(int[] x, int offset, int len) {
            ensureSpace(size + len);
            System.arraycopy(x, offset, data, size, len);
            size += len;
        }

        public void addAll(IntegerArrayList list) {
            addAll(list.data, 0, list.size);
        }

        public void sort() {
            if (size <= 1) {
                return;
            }
            Randomized.shuffle(data, 0, size);
            Arrays.sort(data, 0, size);
        }

        public void unique() {
            if (size <= 1) {
                return;
            }

            sort();
            int wpos = 1;
            for (int i = 1; i < size; i++) {
                if (data[i] != data[wpos - 1]) {
                    data[wpos++] = data[i];
                }
            }
            size = wpos;
        }

        public int binarySearch(int x) {
            return Arrays.binarySearch(data, 0, size, x);
        }

        public int size() {
            return size;
        }

        public int[] toArray() {
            return Arrays.copyOf(data, size);
        }

        public String toString() {
            return Arrays.toString(toArray());
        }

        public boolean equals(Object obj) {
            if (!(obj instanceof IntegerArrayList)) {
                return false;
            }
            IntegerArrayList other = (IntegerArrayList) obj;
            return SequenceUtils.equal(data, 0, size - 1, other.data, 0, other.size - 1);
        }

        public int hashCode() {
            int h = 1;
            for (int i = 0; i < size; i++) {
                h = h * 31 + Integer.hashCode(data[i]);
            }
            return h;
        }

        public IntegerArrayList clone() {
            IntegerArrayList ans = new IntegerArrayList();
            ans.addAll(this);
            return ans;
        }

    }

    static interface IntegerComparator {
        public static final IntegerComparator REVERSE_ORDER = (a, b) -> Integer.compare(b, a);

        public int compare(int a, int b);

    }

    static interface IntegerStack {
    }

    static class RectOnGridProblem {
        public static Pair<Integer, int[]> maxAreaDistinctRect(int[][] mat) {
            int best = 1;
            int rectL = 0;
            int rectR = 0;
            int rectB = 0;
            int rectU = 0;

            int n = mat.length;
            int m = mat[0].length;
            int[][] left = new int[n][m];
            int[][] right = new int[n][m];
            IntegerArrayList all = new IntegerArrayList(n * m);
            for (int i = 0; i < n; i++) {
                all.addAll(mat[i]);
            }
            all.unique();
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    mat[i][j] = all.binarySearch(mat[i][j]);
                }
            }

            int k = all.size();
            int[] leftReg = new int[k];
            Arrays.fill(leftReg, -1);
            int[] rightReg = new int[k];
            Arrays.fill(rightReg, m);
            int[] size = new int[m];
            IntegerMinQueue dq = new IntegerMinQueue(m, IntegerComparator.REVERSE_ORDER);
            for (int u = n - 1; u >= 0; u--) {
                //update left and right
                for (int j = 0; j < m; j++) {
                    left[u][j] = leftReg[mat[u][j]];
                    leftReg[mat[u][j]] = j;
                    for (int r = u + 1; r < n; r++) {
                        left[r][j] = Math.max(left[r][j], leftReg[mat[r][j]]);
                    }
                }
                for (int j = 0; j < m; j++) {
                    leftReg[mat[u][j]] = -1;
                }
                for (int j = m - 1; j >= 0; j--) {
                    right[u][j] = rightReg[mat[u][j]];
                    rightReg[mat[u][j]] = j;
                    for (int r = u + 1; r < n; r++) {
                        right[r][j] = Math.min(right[r][j], rightReg[mat[r][j]]);
                    }
                }
                for (int j = 0; j < m; j++) {
                    rightReg[mat[u][j]] = m;
                }
                for (int j = 0; j < m; j++) {
                    size[j] = m - j;
                }
                //consider top to bot
                for (int b = u; b < n; b++) {
                    dq.clear();
                    for (int j = m - 1; j >= 0; j--) {
                        dq.addLast(left[b][j]);
                        if (j + 1 < m) {
                            size[j] = Math.min(size[j], size[j + 1] + 1);
                        }
                        size[j] = Math.min(size[j], right[b][j] - j);
                        while (dq.size() > size[j]) {
                            dq.removeFirst();
                        }
                        while (!dq.isEmpty() && dq.min() >= j) {
                            dq.removeFirst();
                        }
                        size[j] = dq.size();
                        int area = size[j] * (b - u + 1);
                        if (area > best) {
                            best = area;
                            rectL = j;
                            rectR = rectL + size[j] - 1;
                            rectU = u;
                            rectB = b;
                        }
                    }
                }
            }

            return new Pair<>(best, new int[]{rectL, rectR, rectU, rectB});
        }

    }

    static class Randomized {
        public static void shuffle(int[] data, int from, int to) {
            to--;
            for (int i = from; i <= to; i++) {
                int s = nextInt(i, to);
                int tmp = data[i];
                data[i] = data[s];
                data[s] = tmp;
            }
        }

        public static int nextInt(int l, int r) {
            return RandomWrapper.INSTANCE.nextInt(l, r);
        }

    }

    static class IntegerMinQueue {
        IntegerDequeImpl minQueue;
        IntegerDequeImpl data;
        IntegerComparator comparator;

        public IntegerMinQueue(int cap, IntegerComparator comparator) {
            minQueue = new IntegerDequeImpl(cap);
            data = new IntegerDequeImpl(cap);
            this.comparator = comparator;
        }

        public void clear() {
            minQueue.clear();
            data.clear();
        }

        public void addLast(int val) {
            data.addLast(val);
            while (!minQueue.isEmpty() && comparator.compare(minQueue.peekLast(), val) > 0) {
                minQueue.removeLast();
            }
            minQueue.addLast(val);
        }

        public int removeFirst() {
            assert size() > 0;
            int val = data.removeFirst();
            if (minQueue.peekFirst() == val) {
                minQueue.removeFirst();
            }
            return val;
        }

        public int size() {
            return data.size();
        }

        public int min() {
            assert size() > 0;
            return minQueue.peekFirst();
        }

        public boolean isEmpty() {
            return data.isEmpty();
        }

        public String toString() {
            return data.toString();
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

        public int ri() {
            return readInt();
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

        public FastOutput append(int c) {
            cache.append(c);
            afterWrite();
            return this;
        }

        public FastOutput println(int c) {
            return append(c).println();
        }

        public FastOutput println() {
            return append('\n');
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

    static interface IntegerDeque extends IntegerStack {
    }

    static class IntegerDequeImpl implements IntegerDeque {
        private int[] data;
        private int bpos;
        private int epos;
        private static final int[] EMPTY = new int[0];
        private int n;

        public IntegerDequeImpl(int cap) {
            if (cap == 0) {
                data = EMPTY;
            } else {
                data = new int[cap];
            }
            bpos = 0;
            epos = 0;
            n = cap;
        }

        private void expandSpace(int len) {
            while (n < len) {
                n = Math.max(n + 10, n * 2);
            }
            int[] newData = new int[n];
            if (bpos <= epos) {
                if (bpos < epos) {
                    System.arraycopy(data, bpos, newData, 0, epos - bpos);
                }
            } else {
                System.arraycopy(data, bpos, newData, 0, data.length - bpos);
                System.arraycopy(data, 0, newData, data.length - bpos, epos);
            }
            epos = size();
            bpos = 0;
            data = newData;
        }

        public IntegerIterator iterator() {
            return new IntegerIterator() {
                int index = bpos;


                public boolean hasNext() {
                    return index != epos;
                }


                public int next() {
                    int ans = data[index];
                    index = IntegerDequeImpl.this.next(index);
                    return ans;
                }
            };
        }

        public int removeFirst() {
            int ans = data[bpos];
            bpos = next(bpos);
            return ans;
        }

        public int removeLast() {
            int ans = data[last(epos)];
            epos = last(epos);
            return ans;
        }

        public void addLast(int x) {
            ensureMore();
            data[epos] = x;
            epos = next(epos);
        }

        public int peekFirst() {
            return data[bpos];
        }

        public int peekLast() {
            return data[last(epos)];
        }

        public void clear() {
            bpos = epos = 0;
        }

        private int last(int x) {
            return (x == 0 ? n : x) - 1;
        }

        private int next(int x) {
            return x + 1 >= n ? 0 : x + 1;
        }

        private void ensureMore() {
            if (next(epos) == bpos) {
                expandSpace(n + 1);
            }
        }

        public int size() {
            int ans = epos - bpos;
            if (ans < 0) {
                ans += data.length;
            }
            return ans;
        }

        public boolean isEmpty() {
            return bpos == epos;
        }

        public String toString() {
            StringBuilder builder = new StringBuilder();
            for (IntegerIterator iterator = iterator(); iterator.hasNext(); ) {
                builder.append(iterator.next()).append(' ');
            }
            return builder.toString();
        }

    }
}

