import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.NoSuchElementException;
import java.util.PrimitiveIterator;
import java.util.function.DoubleUnaryOperator;
import java.util.function.IntBinaryOperator;
import java.util.function.IntFunction;
import java.util.function.IntPredicate;
import java.util.function.IntSupplier;
import java.util.function.IntUnaryOperator;
import java.util.function.LongUnaryOperator;


public class Main {
    public static void main(String[] args) {
        StringBuilder out = new StringBuilder();
        solve(out);
        PrintWriter pw = new PrintWriter(System.out);
        pw.println(out);
        pw.flush();
        pw.close();
    }

    public static void solve(StringBuilder out) {
        int n = In.ni();
        long[] d = In.nl(n);
        int[] idx = IntArrayGenerator.indexToInt(n, i -> i);
        DependentSort.sortDescending(d, idx);
        HashMap<Long, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(d[i], i);
        }
        IntArrayList[] ch = new IntArrayList[n];
        for (int i = 0; i < n; i++) {
            ch[i] = new IntArrayList();
        }
        for (int v = 0; v < n - 1; v++) {
            long s = 0;
            for (int i : ch[v]) {
                s += (long) n - d[i] + d[v];
            }
            long du = s + d[v] - (n - 2);
            if (du >= d[v]) {
                out.append(-1);
                return;
            } else if (map.containsKey(du)) {
                ch[map.get(du)].add(v);
            } else {
                out.append(-1);
                return;
            }
        }
        long s = 0;
        int[] dep = new int[n];
        Arrays.fill(dep, 0, n - 1, -1);
        IntQueue q = new IntQueue(n);
        q.add(n - 1);
        while (q.size() > 0) {
            int u = q.poll();
            s += dep[u];
            for (int v : ch[u]) {
                if (dep[v] < 0) {
                    dep[v] = dep[u] + 1;
                    q.add(v);
                }
            }
        }
        if (s != d[n - 1]) {
            out.append(-1);
            return;
        }
        int[] p = new int[n];
        for (int i = 0; i < n; i++) {
            p[i] = idx[i];
        }
        for (int u = 0; u < n; u++) {
            for (int v : ch[u]) {
                out.append(p[u] + 1).append(' ').append(p[v] + 1).append('\n');
            }
        }
    }
}

final class InsertionSort {
    protected static void sort(final int[] a) {
        sort(a, 0, a.length);
    }

    protected static void sort(final int[] a, final int from, final int to) {
        for (int i = from + 1; i < to; i++) {
            final int tmp = a[i];
            if (a[i - 1] > tmp) {
                int j = i;
                do {
                    a[j] = a[j - 1];
                    j--;
                } while (j > from && a[j - 1] > tmp);
                a[j] = tmp;
            }
        }
    }

    protected static void sort(final long[] a) {
        sort(a, 0, a.length);
    }

    protected static void sort(final long[] a, final int from, final int to) {
        for (int i = from + 1; i < to; i++) {
            final long tmp = a[i];
            if (a[i - 1] > tmp) {
                int j = i;
                do {
                    a[j] = a[j - 1];
                    j--;
                } while (j > from && a[j - 1] > tmp);
                a[j] = tmp;
            }
        }
    }
}



/**
 * @author https://atcoder.jp/users/suisen
 */
final class IntArrayList implements Iterable<Integer> {
    private int[] a;
    private int tail = 0;

    private static final int DEFAULT_SIZE = 64;

    public IntArrayList(final int capacity) {
        this.a = new int[Math.max(1, capacity)];
    }

    public IntArrayList() {
        this(DEFAULT_SIZE);
    }

    public void add(final int v) {
        if (tail == a.length) {
            resize(2);
        }
        a[tail++] = v;
    }

    public int removeLast() {
        return a[tail--];
    }

    public int get(final int i) {
        if (i >= this.tail) {
            System.err.println("Error in IntArrayList::get(" + i + "): ArrayIndexOutOfBounds. list size = " + tail);
        }
        return a[i];
    }

    public void set(final int i, final int v) {
        if (i >= this.tail) {
            System.err.println("Error in IntArrayList::set(" + i + "): ArrayIndexOutOfBounds. list size = " + tail);
        }
        a[i] = v;
    }

    private void resize(final double grow) {
        final int[] b = new int[(int) Math.ceil(a.length * grow)];
        System.arraycopy(a, 0, b, 0, a.length);
        a = b;
    }

    public int size() {
        return tail;
    }

    public void reverse(final int begin, final int end) {
        IntArrays.reverse(a, begin, end);
    }

    public void reverse() {
        IntArrays.reverse(a, 0, tail);
    }

    public int[] toArray() {
        final int[] ret = new int[tail];
        System.arraycopy(a, 0, ret, 0, tail);
        return ret;
    }

    public boolean addIf(final int v, final IntPredicate p) {
        if (p.test(v)) {
            add(v);
            return true;
        }
        return false;
    }

    public PrimitiveIterator.OfInt iterator() {
        return new IntArrayListIterator();
    }

    private class IntArrayListIterator implements PrimitiveIterator.OfInt {
        private int i = 0;

        public boolean hasNext() {
            return i < tail;
        }

        public int nextInt() {
            return a[i++];
        }
    }
}


/**
 * @author https://atcoder.jp/users/suisen
 */
final class RadixSort {
    private static final int INT_INSERTION_SORT_THRESHOLD = 120;
    private static final int LONG_INSERTION_SORT_THRESHOLD = 250;

    private static final int BUCKET_SIZE = 256;
    private static final int BUCKET_HALF_SIZE = 128;
    private static final int INT_RECURSION = 4;
    private static final int LONG_RECURSION = 8;
    private static final int SHIFT = 3;
    private static final int MASK = 0xff;

    public static void sort(final int[] a) {
        sort(a, 0, a.length);
    }

    public static void sortDescending(final int[] a) {
        sortDescending(a, 0, a.length);
    }

    public static void sort(final int[] a, final int from, final int to) {
        if (to - from <= INT_INSERTION_SORT_THRESHOLD) {
            InsertionSort.sort(a, from, to);
            return;
        }
        final int len = to - from;
        final int[] bucket = new int[len];
        final int[] cnt = new int[BUCKET_SIZE + 1];
        for (int l = 0;;) {
            final int shift = l << SHIFT;
            for (int i = from; i < to; i++) {
                cnt[((a[i] >>> shift) & MASK) + 1]++;
            }
            for (int i = 0, j = 1; i < BUCKET_SIZE; i = j, j++) {
                cnt[j] += cnt[i];
            }
            final int positive = cnt[BUCKET_HALF_SIZE];
            for (int i = from; i < to; i++) {
                final int v = a[i];
                bucket[cnt[(v >>> shift) & MASK]++] = v;
            }
            if (++l == INT_RECURSION) {
                final int negative = len - positive;
                System.arraycopy(bucket, positive, a, from, negative);
                System.arraycopy(bucket, 0, a, from + negative, positive);
                return;
            }
            System.arraycopy(bucket, 0, a, from, len);
            Arrays.fill(cnt, 0);
        }
    }

    public static void sortDescending(final int[] a, final int from, final int to) {
        sort(a, from, to);
        int l = from, r = to - 1;
        while (l < r) {
            final int tmp = a[l];
            a[l] = a[r];
            a[r] = tmp;
            l++;
            r--;
        }
    }

    public static void sort(final long[] a) {
        sort(a, 0, a.length);
    }

    public static void sortDescending(final long[] a) {
        sortDescending(a, 0, a.length);
    }

    public static void sort(final long[] a, final int from, final int to) {
        if (to - from <= LONG_INSERTION_SORT_THRESHOLD) {
            InsertionSort.sort(a, from, to);
            return;
        }
        final int len = to - from;
        final long[] bucket = new long[len];
        final int[] cnt = new int[BUCKET_SIZE + 1];
        for (int l = 0;;) {
            final int shift = l << SHIFT;
            for (int i = from; i < to; i++) {
                cnt[(int) (((a[i] >>> shift) & MASK) + 1)]++;
            }
            for (int i = 0, j = 1; i < BUCKET_SIZE; i = j, j++) {
                cnt[j] += cnt[i];
            }
            final int positive = cnt[BUCKET_HALF_SIZE];
            for (int i = from; i < to; i++) {
                final int bi = (int) ((a[i] >>> shift) & MASK);
                bucket[cnt[bi]++] = a[i];
            }
            if (++l == LONG_RECURSION) {
                final int negative = len - positive;
                System.arraycopy(bucket, positive, a, from, negative);
                System.arraycopy(bucket, 0, a, from + negative, positive);
                return;
            }
            System.arraycopy(bucket, 0, a, from, len);
            Arrays.fill(cnt, 0);
        }
    }

    public static void sortDescending(final long[] a, final int from, final int to) {
        sort(a, from, to);
        int l = from, r = to - 1;
        while (l < r) {
            final long tmp = a[l];
            a[l] = a[r];
            a[r] = tmp;
            l++; r--;
        }
    }
}



/**
 * @author https://atcoder.jp/users/suisen
 * 
 * (NON-DESTRUCTIVE) methods that returns int array.
 */
final class IntArrayGenerator {

    private IntArrayGenerator(){}
    
    public static int[] filled(final int n, final int init) {
        final int[] ret = new int[n];
        Arrays.fill(ret, init);
        return ret;
    }

    public static int[][] filled(final int n, final int m, final int init) {
        final int[][] ret = new int[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(ret[i], init);
        }
        return ret;
    }

    public static int[] generate(final int n, final IntSupplier f) {
        final int[] a = new int[n];
        Arrays.setAll(a, i -> f.getAsInt());
        return a;
    }

    public static int[][] generate(final int n, final int m, final IntSupplier f) {
        final int[][] a = new int[n][m];
        for (int i = 0; i < n; i++) {
            a[i] = generate(m, f);
        }
        return a;
    }

    public static int[] indexToInt(final int n, final IntUnaryOperator f) {
        final int[] a = new int[n];
        Arrays.setAll(a, f);
        return a;
    }

    public static int[][] indexToInt(final int n, final int m, final IntBinaryOperator f) {
        final int[][] a = new int[n][m];
        for (int i = 0; i < n; i++) {
            final int ii = i;
            a[i] = indexToInt(m, j -> f.applyAsInt(ii, j));
        }
        return a;
    }

    public static int[] toArray(final Collection<? extends Number> collection) {
        final int n = collection.size();
        final int[] ret = new int[n];
        final Object[] coll = collection.toArray();
        for (int i = 0; i < n; i++) {
            ret[i] = ((Number) coll[i]).intValue();
        }
        return ret;
    }

    public static int[] unique(final int[] a) {
        final HashSet<Integer> set = new HashSet<>();
        for (final int e : a) {
            set.add(e);
        }
        final int m = set.size();
        final int[] b = new int[m];
        int index = 0;
        for (int i = 0; i < a.length; i++) {
            if (set.contains(a[i])) {
                b[index++] = a[i];
                set.remove(a[i]);
            }
        }
        return b;
    }

    public static int[][] transpose(final int[][] a) {
        final int n = a.length;
        final int m = a[0].length;
        final int[][] ret = new int[m][n];
        for (int j = 0; j < m; j++) {
            for (int i = 0; i < n; i++) {
                ret[j][i] = a[i][j];
            }
        }
        return ret;
    }

    public static int[] count(final int[] a, final int max) {
        final int[] ret = new int[max + 1];
        for (int i = 0; i < a.length; i++) {
            ret[a[i]]++;
        }
        return ret;
    }

    public static int[] map(final int[] a, final IntUnaryOperator f) {
        final int[] b = new int[a.length];
        Arrays.setAll(b, i -> f.applyAsInt(a[i]));
        return b;
    }

    public static int[] filter(final int[] a, final IntPredicate p) {
        final IntArrayList ret = new IntArrayList();
        for (final int e : a) {
            ret.addIf(e, p);
        }
        return ret.toArray();
    }

    public static int[] filterIndex(final int beginIndex, final int endIndex, final IntPredicate p) {
        final IntArrayList ret = new IntArrayList();
        for (int i = beginIndex; i < endIndex; i++) {
            ret.addIf(i, p);
        }
        return ret.toArray();
    }

    public static int[] filterIndex(final int endIndex, final IntPredicate p) {
        return filterIndex(0, endIndex, p);
    }

    public static int[] accumulateFromHead(final int[] a, final IntBinaryOperator op, final int e) {
        final int n = a.length;
        final int[] ret = new int[n + 1];
        ret[0] = e;
        for (int i = 0; i < n; i++) {
            ret[i + 1] = op.applyAsInt(ret[i], a[i]);
        }
        return ret;
    }

    public static int[] accumulateFromTail(final int[] a, final IntBinaryOperator op, final int e) {
        final int n = a.length;
        final int[] ret = new int[n + 1];
        ret[n] = e;
        for (int i = n - 1; i >= 0; i--) {
            ret[i] = op.applyAsInt(ret[i + 1], a[i]);
        }
        return ret;
    }
}

@FunctionalInterface
interface LongComparator {
    public int compare(long i, long j);

    public default boolean eq(final long i, final long j) {
        return compare(i, j) == 0;
    }

    public default boolean ne(final long i, final long j) {
        return compare(i, j) != 0;
    }

    public default boolean gt(final long i, final long j) {
        return compare(i, j) > 0;
    }

    public default boolean ge(final long i, final long j) {
        return compare(i, j) >= 0;
    }

    public default boolean lt(final long i, final long j) {
        return compare(i, j) < 0;
    }

    public default boolean le(final long i, final long j) {
        return compare(i, j) <= 0;
    }
}


final class ComparativeMergeSort {
    private static int INSERTION_SORT_THRESHOLD = 60;

    public static void sort(final int[] a, final IntComparator comparator) {
        sort(a, 0, a.length, comparator);
    }

    public static void sort(final int[] a, final int begin, final int end, final IntComparator comparator) {
        for (int i = begin;;) {
            final int j = i + INSERTION_SORT_THRESHOLD;
            if (j < end) {
                ComparativeInsertionSort.sort(a, i, j, comparator);
            } else {
                ComparativeInsertionSort.sort(a, i, end, comparator);
                break;
            }
            i = j;
        }
        final int len = end - begin;
        final int[] work = new int[len];
        for (int block = INSERTION_SORT_THRESHOLD; block <= len; block <<= 1) {
            final int twoBlocks = block << 1;
            for (int from = begin, max = end - block; from < max; from += twoBlocks) {
                final int mid = from + block;
                final int to = Math.min(from + twoBlocks, end);
                System.arraycopy(a, from, work, 0, block);
                for (int i = from, wi = 0, ti = mid;; i++) {
                    if (ti == to) {
                        System.arraycopy(work, wi, a, i, block - wi);
                        break;
                    } else if (comparator.gt(work[wi], a[ti])) {
                        a[i] = a[ti++];
                    } else {
                        a[i] = work[wi++];
                        if (wi == block) {
                            break;
                        }
                    }
                }
            }
        }
    }

    public static void sort(final long[] a, final LongComparator comparator) {
        sort(a, 0, a.length, comparator);
    }

    public static void sort(final long[] a, final int begin, final int end, final LongComparator comparator) {
        for (int i = begin;;) {
            final int j = i + INSERTION_SORT_THRESHOLD;
            if (j < end) {
                ComparativeInsertionSort.sort(a, i, j, comparator);
            } else {
                ComparativeInsertionSort.sort(a, i, end, comparator);
                break;
            }
            i = j;
        }
        final int len = end - begin;
        final long[] work = new long[len];
        for (int block = INSERTION_SORT_THRESHOLD; block <= len; block <<= 1) {
            final int twoBlocks = block << 1;
            for (int from = begin, max = end - block; from < max; from += twoBlocks) {
                final int mid = from + block;
                final int to = Math.min(from + twoBlocks, end);
                System.arraycopy(a, from, work, 0, block);
                for (int i = from, wi = 0, ti = mid;; i++) {
                    if (ti == to) {
                        System.arraycopy(work, wi, a, i, block - wi);
                        break;
                    } else if (comparator.gt(work[wi], a[ti])) {
                        a[i] = a[ti++];
                    } else {
                        a[i] = work[wi++];
                        if (wi == block) {
                            break;
                        }
                    }
                }
            }
        }
    }
}


/**
 * @author https://atcoder.jp/users/suisen
 */
final class In {
    public static final FastScanner fsc = new FastScanner();

    public static int ni() {
        return fsc.nextInt();
    }

    public static int ni(final IntUnaryOperator f) {
        return f.applyAsInt(fsc.nextInt());
    }

    public static int[] ni(final int n) {
        final int[] a = new int[n];
        Arrays.setAll(a, i -> fsc.nextInt());
        return a;
    }

    public static int[] ni(final int n, final IntUnaryOperator f) {
        final int[] a = new int[n];
        Arrays.setAll(a, i -> ni(f));
        return a;
    }

    public static int[][] ni(final int n, final int m) {
        final int[][] a = new int[n][m];
        Arrays.setAll(a, i -> ni(m));
        return a;
    }

    public static int[][] ni(final int n, final int m, final IntUnaryOperator f) {
        final int[][] a = new int[n][m];
        Arrays.setAll(a, i -> ni(m, f));
        return a;
    }

    public static long nl() {
        return fsc.nextLong();
    }

    public static long nl(final LongUnaryOperator f) {
        return f.applyAsLong(fsc.nextLong());
    }

    public static long[] nl(final int n) {
        final long[] a = new long[n];
        Arrays.setAll(a, i -> fsc.nextLong());
        return a;
    }

    public static long[] nl(final int n, final LongUnaryOperator f) {
        final long[] a = new long[n];
        Arrays.setAll(a, i -> nl(f));
        return a;
    }

    public static long[][] nl(final int n, final int m) {
        final long[][] a = new long[n][m];
        Arrays.setAll(a, i -> nl(m));
        return a;
    }

    public static long[][] nl(final int n, final int m, final LongUnaryOperator f) {
        final long[][] a = new long[n][m];
        Arrays.setAll(a, i -> nl(m, f));
        return a;
    }

    public static char[] nc() {
        return fsc.next().toCharArray();
    }

    public static char[][] nc(final int n, final int m) {
        final char[][] c = new char[n][m];
        Arrays.setAll(c, i -> nc());
        return c;
    }

    public static double nd() {
        return fsc.nextDouble();
    }

    public static double nd(final DoubleUnaryOperator f) {
        return f.applyAsDouble(fsc.nextDouble());
    }

    public static double[] nd(final int n) {
        final double[] a = new double[n];
        Arrays.setAll(a, i -> fsc.nextDouble());
        return a;
    }

    public static double[] nd(final int n, final DoubleUnaryOperator f) {
        final double[] a = new double[n];
        Arrays.setAll(a, i -> nd(f));
        return a;
    }

    public static double[][] nd(final int n, final int m) {
        final double[][] a = new double[n][m];
        Arrays.setAll(a, i -> nd(m));
        return a;
    }

    public static double[][] nd(final int n, final int m, final DoubleUnaryOperator f) {
        final double[][] a = new double[n][m];
        Arrays.setAll(a, i -> nd(m, f));
        return a;
    }

    public static String ns() {
        return fsc.next();
    }

    public static String[] ns(final int n) {
        final String[] s = new String[n];
        Arrays.setAll(s, i -> ns());
        return s;
    }

    public static boolean[][] grid(final int h, final int w, final char trueCharacter) {
        final boolean[][] grid = new boolean[h][w];
        for (int i = 0; i < h; i++) {
            final char[] s = fsc.next().toCharArray();
            for (int j = 0; j < w; j++) {
                grid[i][j] = s[j] == trueCharacter;
            }
        }
        return grid;
    }
}


final class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;

    private boolean hasNextByte() {
        if (ptr < buflen) {
            return true;
        } else {
            ptr = 0;
            try {
                buflen = in.read(buffer);
            } catch (final IOException e) {
                e.printStackTrace();
            }
            if (buflen <= 0) {
                return false;
            }
        }
        return true;
    }

    private int readByte() {
        if (hasNextByte()) {
            return buffer[ptr++];
        } else {
            return -1;
        }
    }

    private static boolean isPrintableChar(final int c) {
        return 33 <= c && c <= 126;
    }

    public boolean hasNext() {
        while (hasNextByte() && !isPrintableChar(buffer[ptr])) {
            ptr++;
        }
        return hasNextByte();
    }

    public String next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        final StringBuilder sb = new StringBuilder();
        int b = readByte();
        while (isPrintableChar(b)) {
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }

    public long nextLong() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        if (b < '0' || '9' < b) {
            throw new NumberFormatException();
        }
        while (true) {
            if ('0' <= b && b <= '9') {
                n *= 10;
                n += b - '0';
            } else if (b == -1 || !isPrintableChar(b)) {
                return minus ? -n : n;
            } else {
                throw new NumberFormatException();
            }
            b = readByte();
        }
    }

    public int nextInt() {
        final long nl = nextLong();
        if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) {
            throw new NumberFormatException();
        }
        return (int) nl;
    }

    public double nextDouble() {
        return Double.parseDouble(next());
    }
}


/**
 * @author https://atcoder.jp/users/suisen
 * 
 * 1. DESTRUCTIVE methods for int arrays.
 * 2. methods that receives arrays and return some results (except for int arrays).
 */
final class IntArrays {

    private IntArrays(){}

    public static void swap(final int[] a, final int u, final int v) {
        final int tmp = a[u];
        a[u] = a[v];
        a[v] = tmp;
    }

    public static void reverse(final int[] a, final int begin, final int end) {
        for (int i = begin; i < begin + (end - begin) / 2; i++) {
            swap(a, i, begin + end - i - 1);
        }
    }

    public static void reverse(final int[] a) {
        reverse(a, 0, a.length);
    }

    public static void sortDescending(final int[] a) {
        Arrays.sort(a);
        reverse(a);
    }

    public static int reduce(final int[] a, final IntBinaryOperator op) {
        int ret = a[0];
        for (int i = 1; i < a.length; i++) {
            ret = op.applyAsInt(ret, a[i]);
        }
        return ret;
    }

    public static void map(final int[] a, final IntUnaryOperator op) {
        Arrays.setAll(a, i -> op.applyAsInt(a[i]));
    }

    public static void filter(final int[] src, final int[] dst, final IntPredicate p) {
        int idx = 0;
        for (final int e : src) {
            if (p.test(e)) {
                dst[idx++] = e;
            }
        }
    }

    public static void filterIndex(final int[] dst, final int beginIndex, final int endIndex, final IntPredicate p) {
        for (int i = beginIndex, idx = 0; i < endIndex; i++) {
            if (p.test(i)) {
                dst[idx++] = i;
            }
        }
    }

    public static void filterIndex(final int dst[], final int endIndex, final IntPredicate p) {
        filterIndex(dst, 0, endIndex, p);
    }

    public static void accumulate(final int[] a, final IntBinaryOperator op) {
        for (int i = 1; i < a.length; i++) {
            a[i] = op.applyAsInt(a[i - 1], a[i]);
        }
    }

    public static void accumulate(final int[] a) {
        for (int i = 1; i < a.length; i++) {
            a[i] += a[i - 1];
        }
    }

    public static int unique(int[] a) {
        final HashSet<Integer> set = new HashSet<>();
        for (final int e : a) {
            set.add(e);
        }
        final int m = set.size();
        final int[] b = new int[m];
        int index = 0;
        for (int i = 0; i < a.length; i++) {
            if (set.contains(a[i])) {
                b[index++] = a[i];
                set.remove(a[i]);
            }
        }
        a = b;
        return m;
    }

    public static void permute(int[] a, int[] p) {
        int n = p.length;
        boolean[] settled = new boolean[n];
        for (int i = 0; i < n; i++) {
            for (int j = i; !settled[j]; j = p[j]) {
                if (p[j] == i) {
                    settled[j] = true;
                    break;
                }
                swap(a, j, p[j]);
                settled[j] = true;
            }
        }
    }

    public static void transpose(int[][] a) {
        final int n = a.length;
        final int m = a[0].length;
        final int[][] ret = new int[m][n];
        for (int j = 0; j < m; j++) {
            for (int i = 0; i < n; i++) {
                ret[j][i] = a[i][j];
            }
        }
        a = ret;
    }

    public static int compare(final int[] a, final int[] b) {
        for (int i = 0; i < a.length; i++) {
            if (i >= b.length) {
                return -1;
            } else if (a[i] > b[i]) {
                return 1;
            } else if (a[i] < b[i]) {
                return -1;
            }
        }
        if (a.length < b.length) {
            return 1;
        } else {
            return 0;
        }
    }

    public static boolean equals(final int[] a, final int[] b) {
        return compare(a, b) == 0;
    }

    public static String join(final int[] a, final String sep) {
        final StringBuilder sb = new StringBuilder();
        for (int i = 0; i < a.length; i++) {
            sb.append(a[i]);
            if (i < a.length - 1) {
                sb.append(sep);
            }
        }
        return sb.toString();
    }

    public static String joinWithPrefixAndSuffix(final int[] a, final IntFunction<String> idxToPre,
            final IntFunction<String> idxToSuf, final String sep) {
        final StringBuilder sb = new StringBuilder();
        for (int i = 0; i < a.length; i++) {
            sb.append(idxToPre.apply(i)).append(a[i]).append(idxToSuf.apply(i));
            if (i < a.length - 1) {
                sb.append(sep);
            }
        }
        return sb.toString();
    }
}

@FunctionalInterface
interface IntComparator {
    public int compare(int i, int j);

    public default boolean eq(final int i, final int j) {
        return compare(i, j) == 0;
    }

    public default boolean ne(final int i, final int j) {
        return compare(i, j) != 0;
    }

    public default boolean gt(final int i, final int j) {
        return compare(i, j) > 0;
    }

    public default boolean ge(final int i, final int j) {
        return compare(i, j) >= 0;
    }

    public default boolean lt(final int i, final int j) {
        return compare(i, j) < 0;
    }

    public default boolean le(final int i, final int j) {
        return compare(i, j) <= 0;
    }
}

final class DependentSort {
    public static void sort(int[] a, Object... dependentArrays) {
        sort(a, false, dependentArrays);
    }

    public static void sortDescending(int[] a, Object... dependentArrays) {
        sort(a, true, dependentArrays);
    }

    private static void sort(int[] a, boolean descending, Object... dependentArrays) {
        int n = a.length;
        int[] p;
        if (descending) {
            p = IndexSort.sortDescending(a);
            RadixSort.sortDescending(a);
        } else {
            p = IndexSort.sort(a);
            RadixSort.sort(a);
        }
        boolean[] settled = new boolean[n];
        boolean ok = true;
        for (Object obj : dependentArrays) {
            if (obj instanceof int[]) {
                int[] arr = (int[]) obj;
                for (int i = 0; i < n; i++) {
                    for (int j = i; ok ^ settled[j]; j = p[j]) {
                        if (p[j] == i) {
                            settled[j] = !settled[j];
                            break;
                        }
                        int tmp = arr[j];
                        arr[j] = arr[p[j]];
                        arr[p[j]] = tmp;
                        settled[j] = !settled[j];
                    }
                }
            } else if (obj instanceof long[]) {
                long[] arr = (long[]) obj;
                for (int i = 0; i < n; i++) {
                    for (int j = i; ok ^ settled[j]; j = p[j]) {
                        if (p[j] == i) {
                            settled[j] = !settled[j];
                            break;
                        }
                        long tmp = arr[j];
                        arr[j] = arr[p[j]];
                        arr[p[j]] = tmp;
                        settled[j] = !settled[j];
                    }
                }
            } else {
                throw new UnsupportedOperationException("dependent objects musst be int[] or long[] type.");
            }
            ok = !ok;
        }
    }

    public static void sort(long[] a, Object... dependentArrays) {
        sort(a, false, dependentArrays);
    }

    public static void sortDescending(long[] a, Object... dependentArrays) {
        sort(a, true, dependentArrays);
    }

    private static void sort(long[] a, boolean descending, Object... dependentArrays) {
        int n = a.length;
        int[] p;
        if (descending) {
            p = IndexSort.sortDescending(a);
            RadixSort.sortDescending(a);
        } else {
            p = IndexSort.sort(a);
            RadixSort.sort(a);
        }
        boolean[] settled = new boolean[n];
        boolean ok = true;
        for (Object obj : dependentArrays) {
            if (obj instanceof int[]) {
                int[] arr = (int[]) obj;
                for (int i = 0; i < n; i++) {
                    for (int j = i; ok ^ settled[j]; j = p[j]) {
                        if (p[j] == i) {
                            settled[j] = !settled[j];
                            break;
                        }
                        int tmp = arr[j];
                        arr[j] = arr[p[j]];
                        arr[p[j]] = tmp;
                        settled[j] = !settled[j];
                    }
                }
            } else if (obj instanceof long[]) {
                long[] arr = (long[]) obj;
                for (int i = 0; i < n; i++) {
                    for (int j = i; ok ^ settled[j]; j = p[j]) {
                        if (p[j] == i) {
                            settled[j] = !settled[j];
                            break;
                        }
                        long tmp = arr[j];
                        arr[j] = arr[p[j]];
                        arr[p[j]] = tmp;
                        settled[j] = !settled[j];
                    }
                }
            } else {
                throw new UnsupportedOperationException("dependent objects musst be int[] or long[] type.");
            }
            ok = !ok;
        }
    }
}


final class IndexSort {
    public static int[] sort(final int[] a) {
        final int[] index = new int[a.length];
        Arrays.setAll(index, IntUnaryOperator.identity());
        ComparativeMergeSort.sort(index, (i, j) -> a[i] - a[j]);
        return index;
    }

    public static int[] sortDescending(final int[] a) {
        final int[] index = new int[a.length];
        Arrays.setAll(index, IntUnaryOperator.identity());
        ComparativeMergeSort.sort(index, (i, j) -> a[j] - a[i]);
        return index;
    }

    public static int[] sort(final long[] a) {
        final int[] index = new int[a.length];
        Arrays.setAll(index, IntUnaryOperator.identity());
        ComparativeMergeSort.sort(index, (i, j) -> Long.compare(a[i], a[j]));
        return index;
    }

    public static int[] sortDescending(final long[] a) {
        final int[] index = new int[a.length];
        Arrays.setAll(index, IntUnaryOperator.identity());
        ComparativeMergeSort.sort(index, (i, j) -> Long.compare(a[j], a[i]));
        return index;
    }
}


final class ComparativeInsertionSort {
    public static void sort(final int[] a, final int from, final int to, final IntComparator comparator) {
        for (int i = from + 1; i < to; i++) {
            final int tmp = a[i];
            if (comparator.gt(a[i - 1], tmp)) {
                int j = i;
                do {
                    a[j] = a[j - 1];
                    j--;
                } while (j > from && comparator.gt(a[j - 1], tmp));
                a[j] = tmp;
            }
        }
    }

    public static void sort(final long[] a, final int from, final int to, final LongComparator comparator) {
        for (int i = from + 1; i < to; i++) {
            final long tmp = a[i];
            if (comparator.gt(a[i - 1], tmp)) {
                int j = i;
                do {
                    a[j] = a[j - 1];
                    j--;
                } while (j > from && comparator.gt(a[j - 1], tmp));
                a[j] = tmp;
            }
        }
    }
}


/**
 * @author https://atcoder.jp/users/suisen
 * 
 * Queue for int type.
 */
final class IntQueue implements Iterable<Integer> {
    private static final int DEFAULT_SIZE = 64;

    private int[] q;
    private int head = 0;
    private int tail = 0;

    public IntQueue(final int capacity) {
        this.q = new int[capacity];
    }

    public IntQueue() {
        this(DEFAULT_SIZE);
    }

    public int peek() {
        if (head == tail) throw new NoSuchElementException("No Elements.");
        return q[head];
    }

    public int getFromHead(int index) {
        if (head + index >= tail || index < 0) throw new NoSuchElementException("Index out of bounds.");
        return q[head + index];
    }

    public int getFromTail(int index) {
        if (head + index >= tail || index < 0) throw new NoSuchElementException("Index out of bounds.");
        return q[tail - 1 - index];
    }

    public void add(final int v) {
        if (tail == q.length) grow();
        q[tail++] = v;
    }

    public void add(final int... vals) {
        for (int v : vals) add(v);
    }

    public int poll() {
        if (head == tail) throw new NoSuchElementException("No Elements.");
        return q[head++];
    }

    public int size() {
        return tail - head;
    }

    private void grow() {
        final int[] grown = new int[q.length << 1];
        final int len = size();
        System.arraycopy(q, head, grown, 0, len);
        q = grown;
        tail = len;
        head = 0;
    }

    public PrimitiveIterator.OfInt iterator() {
        return new IntQueueIterator();
    }

    private class IntQueueIterator implements PrimitiveIterator.OfInt {
        private int i = head;

        public boolean hasNext() {
            return i < tail;
        }

        public int nextInt() {
            return q[i++];
        }
    }
}
