import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.EnumSet;
import java.util.HashMap;
import java.util.NoSuchElementException;
import java.util.PrimitiveIterator;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.function.IntBinaryOperator;
import java.util.function.IntFunction;
import java.util.function.IntPredicate;
import java.util.function.IntUnaryOperator;
import java.util.function.LongBinaryOperator;
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
        ModuloArithmetic ma = new ModuloArithmetic(Const.MOD7);
        int n = In.ni();
        int m = In.ni();
        long x = In.nl();
        Graph g = new Graph(n);
        Edge[] edges = new Edge[m];
        for (int i = 0; i < m; i++) {
            int u = In.ni() - 1;
            int v = In.ni() - 1;
            long w = In.nl();
            edges[i] = new Edge(u, v, w);
            g.addEdge(edges[i]);
        }
        UnionFindTree t = new UnionFindTree(n);
        PriorityQueue<Edge> pq = new PriorityQueue<>((u, v) -> Long.compare(u.cost, v.cost));
        int gt = 0;
        int eq = 0;
        int lt = 0;
        for (int i = 0; i < m; i++) {
            t.unite(edges[i].from, edges[i].to);
            for (int j = 0; j < m; j++) {
                if (i == j) continue;
                pq.add(edges[j]);
            }
            long c = edges[i].cost;
            while (pq.size() > 0) {
                Edge e = pq.poll();
                if (!t.isSame(e.from, e.to)) {
                    t.unite(e.from, e.to);
                    c += e.cost;
                }
            }
            t.reset();
            pq.clear();
            if (c > x) gt++;
            else if (c == x) eq++;
            else lt++;
        }
        long ans = eq == 0 ? 0 : lt > 0 ? ma.prod(2, ma.pow(2, gt), ma.pow(2, eq) - 1) : ma.prod(ma.pow(2, gt), ma.pow(2, eq) - 2);
        out.append(ans);
    }

    public static Edge[] kruskal(final int n, final AbstractGraph g) {
        final UnionFindTree t = new UnionFindTree(n);
        final PriorityQueue<Edge> pq = new PriorityQueue<>((u, v) -> Long.compare(u.cost, v.cost));
        for (int i = 0; i < n; i++) for (final Edge e : g.getEdges(i)) pq.add(e);
        final Edge[] ret = new Edge[n - 1];
        int index = 0;
        while (pq.size() > 0 && index < n) {
            final Edge e = pq.poll();
            if (!t.isSame(e.from, e.to)) {
                t.unite(e.from, e.to);
                ret[index++] = e;
            }
        }
        return ret;
    }
}



class LongSemiRing extends LongExtendedMagma {
    public LongSemiRing(final LongMonoid addition, final LongMonoid multiplication) {
        super(addition, multiplication, TypicalPropertySets.SEMI_RING);
        addition.requireProperties(EnumSet.of(Property.COMMUTATIVE));
    }
    public static LongSemiRing of(LongExtendedMagma m) {
        if (!m.additiveProps.containsAll(TypicalPropertySets.COMMUTATIVE_MONOID.getProperties())) {
            throw new ClassCastException("addition does not meet the conditions of commutative monoid.");
        }
        LongCommutativeMonoid add = new LongCommutativeMonoid(m::add, m.e0);
        LongMonoid mul = new LongMonoid(m::mul, m.e1);
        return new LongSemiRing(add, mul);
    }
}



class LongMonoid extends LongMagma implements LongUnital {
    public final long e;
    public LongMonoid(final LongBinaryOperator operator, final long e) {
        super(operator, TypicalPropertySets.MONOID);
        this.e = e;
    }
    @Override
    public long identityElement() {return e;}
    public static <M extends LongMagma & LongUnital> LongMonoid of(M m) {
        m.requireProperties(TypicalPropertySets.MONOID);
        return new LongMonoid(m.operator, m.identityElement());
    }
}



/**
 * @author https://atcoder.jp/users/suisen
 */
final class IntArrayList implements Iterable<Integer> {
    private int[] a;
    private int tail = 0;
    private static final int DEFAULT_SIZE = 64;
    public IntArrayList(final int capacity) {this.a = new int[Math.max(1, capacity)];}
    public IntArrayList() {this(DEFAULT_SIZE);}
    public void add(final int v) {
        if (tail == a.length) grow();
        a[tail++] = v;
    }
    public int removeLast() {return a[tail--];}
    public int get(final int i) {
        if (i >= tail) throw new IndexOutOfBoundsException("Index " + i + " out of bounds for length " + size());
        return a[i];
    }
    public void set(final int i, final int v) {
        if (i >= tail) throw new IndexOutOfBoundsException("Index " + i + " out of bounds for length " + size());
        a[i] = v;
    }
    private void grow() {
        final int[] b = new int[a.length << 1];
        System.arraycopy(a, 0, b, 0, a.length);
        a = b;
    }
    public int size() {return tail;}
    public void reverse(final int begin, final int end) {IntArrays.reverse(a, begin, end);}
    public void reverse() {IntArrays.reverse(a, 0, tail);}
    public int[] toArray() {
        final int[] ret = new int[tail];
        System.arraycopy(a, 0, ret, 0, tail);
        return ret;
    }
    public boolean addIf(final int v, final IntPredicate p) {
        if (p.test(v)) {add(v); return true;}
        return false;
    }
    public void clear() {tail = 0;}
    public PrimitiveIterator.OfInt iterator() {return new IntArrayListIterator();}
    private class IntArrayListIterator implements PrimitiveIterator.OfInt {
        private int i = 0;
        public boolean hasNext() {return i < tail;}
        public int nextInt() {return a[i++];}
    }
}



abstract class LongMagma extends PropertyHolder {
    protected final LongBinaryOperator operator;
    public LongMagma(final LongBinaryOperator operator, final EnumSet<Property> properties) {
        super(properties);
        this.operator = operator;
    }
    public LongMagma(final LongBinaryOperator operator, final TypicalPropertySets properties) {
        super(properties);
        this.operator = operator;
    }
    public final long apply(final long left, final long right) {return operator.applyAsLong(left, right);}
}



class LongField extends LongRing {
    public LongField(final LongAbelianGroup addition, final LongMonoid multiplication) {
        super(addition, multiplication);
        multiplication.requireProperties(EnumSet.of(Property.COMMUTATIVE));
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
    private int head = 0, tail = 0;
    public IntQueue(final int capacity) {this.q = new int[capacity];}
    public IntQueue() {this(DEFAULT_SIZE);}
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
    public void add(final int... vals) {for (int v : vals) add(v);}
    public int poll() {
        if (head == tail) throw new NoSuchElementException("No Elements.");
        int ret = q[head++];
        if (head == tail) head = tail = 0;
        else if (head >= 1e7) relocate();
        return ret;
    }
    private void relocate() {
        final int[] newQ = new int[q.length];
        System.arraycopy(q, head, newQ, 0, tail - head);
        q = newQ;
        tail -= head;
        head = 0;
    }
    public int size() {return tail - head;}
    public void clear() {head = tail = 0;}
    private void grow() {
        final int[] grown = new int[q.length << 1];
        final int len = size();
        System.arraycopy(q, head, grown, 0, len);
        q = grown;
        tail = len;
        head = 0;
    }
    public PrimitiveIterator.OfInt iterator() {return new IntQueueIterator();}
    private class IntQueueIterator implements PrimitiveIterator.OfInt {
        private int i = head;
        public boolean hasNext() {return i < tail;}
        public int nextInt() {return q[i++];}
    }
}


class LongRing extends LongSemiRing {
    private final LongUnaryOperator additiveInverse;
    public LongRing(final LongAbelianGroup addition, final LongMonoid multiplication) {
        super(addition, multiplication);
        this.additiveInverse = addition::inverse;
    }
    public final long additiveInverse(final long t) {return additiveInverse.applyAsLong(t);}
}


/**
 * @author https://atcoder.jp/users/suisen
 */
final class Graph extends AbstractGraph {
    public Graph(final int n) {super(n);}
    public void addEdge(final int from, final int to, final long cost) {
        final Edge e = new Edge(from, to, cost);
        super.addEdge(e);
        super.addEdge(e.reverse());
        this.m++;
    }
    public void addEdge(final int from, final int to) {this.addEdge(from, to, 1);}
    @Override
    public void addEdge(final Edge e) {
        super.addEdge(e);
        super.addEdge(e.reverse());
        this.m++;
    }
    @Override
    public boolean isBipartite() {
        final byte[] color = new byte[n];
        final IntQueue dq = new IntQueue(n);
        for (final int root : getRoots()) {
            dq.add(root);
            color[root] = 1;
        }
        while (dq.size() > 0) {
            final int now = dq.poll();
            for (final Edge e : getEdges(now)) {
                final int next = e.to;
                if (color[next] == 0) {
                    color[next] = (byte) -color[now];
                    dq.add(next);
                } else if (color[now] == color[next]) {
                    return false;
                }
            }
        }
        return true;
    }
}


final class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;
    private boolean hasNextByte() {
        if (ptr < buflen) return true;
        ptr = 0;
        try {buflen = in.read(buffer);}
        catch (final IOException e) {e.printStackTrace();}
        return buflen > 0;
    }
    private int readByte() {return hasNextByte() ? buffer[ptr++] : -1;}
    public boolean hasNext() {
        while (hasNextByte() && !(33 <= buffer[ptr] && buffer[ptr] <= 126)) ptr++;
        return hasNextByte();
    }
    public String next() {
        if (!hasNext()) throw new NoSuchElementException();
        final StringBuilder sb = new StringBuilder();
        int b = readByte();
        while (33 <= b && b <= 126) {sb.appendCodePoint(b); b = readByte();}
        return sb.toString();
    }
    public long nextLong() {
        if (!hasNext()) throw new NoSuchElementException();
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {minus = true; b = readByte();}
        if (b < '0' || '9' < b) throw new NumberFormatException();
        for (; ; b = readByte()) {
            if ('0' <= b && b <= '9') n = n * 10 + b - '0';
            else if (b == -1 || !(33 <= b && b <= 126)) return minus ? -n : n;
            else throw new NumberFormatException();
        }
    }
    public int nextInt() {return Math.toIntExact(nextLong());}
    public double nextDouble() {return Double.parseDouble(next());}
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
        final int tmp = a[u]; a[u] = a[v]; a[v] = tmp;
    }
    public static void reverse(final int[] a, final int begin, final int end) {
        for (int i = begin; i < begin + (end - begin) / 2; i++) swap(a, i, begin + end - i - 1);
    }
    public static void reverse(final int[] a) {reverse(a, 0, a.length);}
    public static void sortDescending(final int[] a) {Arrays.sort(a); reverse(a);}
    public static int reduce(final int[] a, final IntBinaryOperator op) {
        int ret = a[0]; for (int i = 1; i < a.length; i++) ret = op.applyAsInt(ret, a[i]);
        return ret;
    }
    public static void map(final int[] a, final IntUnaryOperator op) {Arrays.setAll(a, i -> op.applyAsInt(a[i]));}
    public static int filter(final int[] src, final int[] dst, final IntPredicate p) {
        int idx = 0;
        for (final int e : src) if (p.test(e)) dst[idx++] = e;
        return idx;
    }
    public static int filterIndex(final int[] dst, final int beginIndex, final int endIndex, final IntPredicate p) {
        int idx = 0;
        for (int i = beginIndex; i < endIndex; i++) if (p.test(i)) dst[idx++] = i;
        return idx;
    }
    public static int filterIndex(final int dst[], final int endIndex, final IntPredicate p) {
        return filterIndex(dst, 0, endIndex, p);
    }
    public static void accumulate(final int[] a, final IntBinaryOperator op) {
        for (int i = 1; i < a.length; i++) a[i] = op.applyAsInt(a[i - 1], a[i]);
    }
    public static void accumulate(final int[] a) {
        for (int i = 1; i < a.length; i++) a[i] += a[i - 1];
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
    public static int compare(final int[] a, final int[] b) {
        for (int i = 0; i < a.length; i++) {
            if (i >= b.length) return -1;
            if (a[i] > b[i]) return 1;
            if (a[i] < b[i]) return -1;
        }
        return a.length < b.length ? 1 : 0;
    }
    public static boolean equals(final int[] a, final int[] b) {return compare(a, b) == 0;}
    public static String join(final int[] a, final String sep) {
        final StringBuilder sb = new StringBuilder();
        for (int i = 0; i < a.length; i++) {
            sb.append(a[i]);
            if (i < a.length - 1) sb.append(sep);
        }
        return sb.toString();
    }
    public static String joinWithPrefixAndSuffix(final int[] a, final IntFunction<String> idxToPre, final IntFunction<String> idxToSuf, final String sep) {
        final StringBuilder sb = new StringBuilder();
        for (int i = 0; i < a.length; i++) {
            sb.append(idxToPre.apply(i)).append(a[i]).append(idxToSuf.apply(i));
            if (i < a.length - 1) sb.append(sep);
        }
        return sb.toString();
    }
}


/**
 * @author https://atcoder.jp/users/suisen
 */
final class UnionFindTree {
    private final int[] data;
    public UnionFindTree(final int n) {this.data = new int[n]; Arrays.fill(data, -1);}
    public int root(final int x) {return data[x] < 0 ? x : (data[x] = root(data[x]));}
    public boolean isSame(final int x, final int y) {return root(x) == root(y);}
    public boolean unite(int x, int y) {
        x = root(x); y = root(y);
        if (x == y) return false;
        if (data[x] > data[y]) {int tmp = x; x = y; y = tmp;}
        data[x] += data[y];
        data[y] = x;
        return true;
    }
    public int size(final int x) {return -data[root(x)];}
    public boolean isRoot(final int x) {return data[x] < 0;}
    public void reset() {Arrays.fill(data, -1);}
}

enum Property {ANNIHILATED_BY_ZERO, ASSOCIATIVE, CANCELLATIVE, COMMUTATIVE, DISTRIBUTIVE, IDEMPOTENT;}



class LongAbelianGroup extends LongGroup {
    public LongAbelianGroup(final LongBinaryOperator operator, final long e, final LongUnaryOperator inverse) {
        super(operator, e, inverse);
        addProperties(Property.COMMUTATIVE);
    }
}



class LongGroup extends LongMonoid implements LongInversible {
    private final LongUnaryOperator inverse;
    public LongGroup(final LongBinaryOperator operator, final long e, final LongUnaryOperator inverse) {
        super(operator, e);
        addProperties(Property.CANCELLATIVE);
        this.inverse = inverse;
    }
    @Override
    public long inverse(final long t) {return inverse.applyAsLong(t);}
}

/**
 * @author https://atcoder.jp/users/suisen
 */
class Edge {
    public final int from, to;
    public final long cost;
    public Edge(final int from, final int to, final long cost) {
        this.from = from; this.to = to; this.cost = cost;
    }
    public Edge(final int from, final int to) {this(from, to, 1);}
    public final Edge reverse() {return new Edge(to, from, cost);}
}



/**
 * @author https://atcoder.jp/users/suisen
 */
abstract class AbstractGraph {
    protected final int n;
    protected int m = 0;
    private final ArrayList<Edge>[] adj;
    private final int[] in;
    private HashMap<Integer, IntArrayList> components;
    private final UnionFindTree uft;
    @SuppressWarnings("unchecked")
    protected AbstractGraph(final int n) {
        this.n = n;
        this.in = new int[n];
        this.adj = new ArrayList[this.n];
        for (int i = 0; i < this.n; i++) this.adj[i] = new ArrayList<>();
        this.uft = new UnionFindTree(this.n);
    }
    protected void addEdge(final Edge e) {
        this.adj[e.from].add(e);
        this.in[e.to]++;
        this.uft.unite(e.from, e.to);
    }
    public final int in(final int i) {return this.in[i];}
    public final int out(final int i) {return this.adj[i].size();}
    public Edge getEdge(final int from, final int index) {return this.adj[from].get(index);}
    public final ArrayList<Edge> getEdges(final int i) {return this.adj[i];}
    public final int getV() {return this.n;}
    public final int getE() {return this.m;}
    public final int getRoot(final int i) {return uft.root(i);}
    public final HashMap<Integer, IntArrayList> getComponents() {
        generateComponentsIfAbsent();
        return this.components;
    }
    public final IntArrayList getComponent(final int i) {return getComponents().get(getRoot(i));}
    public final Set<Integer> getRoots() {return getComponents().keySet();}
    public final Collection<IntArrayList> getComponentSet() {return getComponents().values();}
    public final boolean isConnected() {return getComponents().size() == 1;}
    public final boolean isConnected(final int u, final int v) {return uft.isSame(u, v);}
    private final void generateComponentsIfAbsent() {
        if (this.components == null) {
            final HashMap<Integer, IntArrayList> components = new HashMap<>();
            for (int i = 0; i < n; i++) {
                if (!components.containsKey(getRoot(i))) components.put(getRoot(i), new IntArrayList());
                components.get(getRoot(i)).add(i);
            }
            this.components = components;
        }
    }
    abstract public boolean isBipartite();
}



/**
 * @author https://atcoder.jp/users/suisen
 */
final class ModuloArithmetic extends LongField {
    public final long MOD;
    public final LongAbelianGroup addition;
    public final LongAbelianGroup multiplication;
    /**
     * support modulo p arithmetic
     * @param p p s.t. p is a prime number.
     */
    public ModuloArithmetic(final long p) {
        super(
            new LongAbelianGroup((u, v) -> add(u, v, p), 0l, x -> -x),
            new LongAbelianGroup((u, v) -> mul(u, v, p), 1l, x -> inv(x, p)));
        this.addition = new LongAbelianGroup((u, v) -> add(u, v, p), 0l, x -> -x);
        this.multiplication = new LongAbelianGroup((u, v) -> mul(u, v, p), 1l, x -> inv(x, p));
        this.MOD = p;
    }
    /**
     * Calculate x s.t. 0 <= x < MOD /\ x = a + b mod p.
     */
    private static long add(final long a, final long b, final long mod) {
        final long s = a + b; return s < 0 ? s + mod : s >= mod ? s - mod : s;
    }
    /**
     * Calculate x s.t. 0 <= x < MOD /\ x = a * b mod p.
     */
    private static long mul(final long a, final long b, final long mod) {
        final long ret = (a * b) % mod; return ret < 0 ? ret + mod : ret;
    }
    /**
     * Calculate the value b s.t. a*b mod MOD = 1.
     */
    private static long inv(long a, final long mod) {
        long b = mod;
        long u = 1, v = 0;
        while (b >= 1) {
            final long t = a / b;
            a -= t * b;
            final long tmp1 = a; a = b; b = tmp1;
            u -= t * v;
            final long tmp2 = u; u = v; v = tmp2;
        }
        u %= mod;
        return u < 0 ? u + mod : u;
    }
    /**
     * Calculate x s.t. 0 <= x < MOD /\ x = a mod p.
     */
    public long mod(long a) {a %= MOD; return a < 0 ? a + MOD : a;}
    /**
     * Calculate x s.t. 0 <= x < MOD /\ x = a_1 + 1_2 + ... + a_k mod p.
     */
    public long sum(final long... a) {
        long ret = 0; for (final long c : a) ret += c;
        return mod(ret);
    }
    /**
     * Calculate x s.t. 0 <= x < MOD /\ x = a - b mod p.
     */
    public long sub(final long a, final long b) {
        final long s = a - b; return s < 0 ? s + MOD : s >= MOD ? s - MOD : s;
    }
    /**
     * Calculate x s.t. 0 <= x < MOD /\ x = a_1 * 1_2 * ... * a_k mod p.
     */
    public long prod(final long... a) {
        long ret = 1; for (final long c : a) ret = (ret * c) % MOD;
        return ret < 0 ? ret + MOD : ret;
    }
    /**
     * Calculate x s.t. 0 <= x < MOD /\ b * x = a mod p.
     */
    public long div(final long a, final long b) {return mul(a, inv(b));}
    /**
     * Calculate the value b s.t. a*b mod MOD = 1.
     */
    public long inv(long a) {
        long b = MOD;
        long u = 1, v = 0;
        while (b >= 1) {
            final long t = a / b;
            a -= t * b;
            final long tmp1 = a; a = b; b = tmp1;
            u -= t * v;
            final long tmp2 = u; u = v; v = tmp2;
        }
        return mod(u);
    }
    /**
     * Calculate the permutation nPr.
     */
    public long perm(final long n, final long r) {
        if (n < r) return 0;
        long ret = 1; for (long i = n; i > n - r; i--) ret = mul(ret, i);
        return ret;
    }
    public long perm(final int n, final int r, final long[] fact, final long[] ifact) {
        if (n < r) return 0;
        return mul(fact[n], ifact[n - r]);
    }
    /**
     * Calculate the combination nCr.
     */
    public long comb(long n, long r) {
        if (n < r) return 0;
        r = Math.min(r, n - r);
        n %= MOD;
        long res = 1; for (long d = 1; d <= r; d++) res = div(mul(res, n--), d);
        return res;
    }
    public long comb(final int n, final int r, final long[] fact, final long[] ifact) {
        if (n < r) return 0;
        return prod(fact[n], ifact[n - r], ifact[r]);
    }
    /**
     * Calculate a^b (mod {@code MOD}) in O(log b) time.
     */
    public long pow(final long a, final long b) {
        if (b == 0 || a == 1) return 1;
        final long half = pow(a, b >> 1);
        return (b & 1) == 0 ? mul(half, half) : prod(half, half, a);
    }
    /**
     * calculate x := log_a b mod MOD. (i.e. a^x = b mod MOD). if not exists, return
     * negative value.
     */
    public long log(final long a, final long b) {return log(a, b, getMapForLogarithm(a));}
    public long log(long a, long b, final HashMap<Long, Long> aMap) {
        a %= MOD; b %= MOD;
        final long sq = (long) (Math.sqrt(MOD) + 2);
        final long inv = pow(inv(a), sq);
        for (long p = 0, r = b; p <= sq; p++) {
            if (aMap.containsKey(r)) {
                final long res = p * sq + aMap.get(r);
                if (res > 0) return res;
            }
            r = mul(r, inv);
        }
        return -1;
    }
    public HashMap<Long, Long> getMapForLogarithm(long a) {
        a %= MOD;
        final long sq = (long) (Math.sqrt(MOD) + 2);
        final HashMap<Long, Long> map = new HashMap<>();
        for (long i = 0, ar = 1; i < sq; i++) {
            map.putIfAbsent(ar, i);
            ar = mul(ar, a);
        }
        return map;
    }
    /**
     * build factorial array from 0 to n (closed)
     */
    public long[] factorialArray(final int n) {
        final long[] fact = new long[n + 1];
        fact[0] = fact[1] = 1;
        for (int i = 1; i <= n; i++) fact[i] = mul(fact[i - 1], i);
        return fact;
    }
    public long[] inversiveFactrialArray(final long[] fact) {
        int n = fact.length - 1;
        final long[] ifact = new long[n + 1];
        ifact[n] = inv(fact[n]);
        for (int i = n - 1; i >= 0; i--) ifact[i] = mul(ifact[i + 1], i + 1);
        return ifact;
    }
    /**
     * build power array based on a from 0 to n (closed)
     * @param a base of power
     * @param n
     */
    public long[] powerArray(final long a, final int n) {
        if (a == 2) return powerArray(n);
        final long[] pow = new long[n + 1];
        pow[0] = 1; for (int i = 0; i <= n; i++) pow[i] = mul(pow[i - 1], a);
        return pow;
    }
    /**
     * build power array based on 2 from 0 to n (closed)
     * @param n
     */
    public long[] powerArray(final int n) {
        final long[] pow = new long[n + 1];
        pow[0] = 1;
        for (int i = 1; i <= n; i++) {
            pow[i] = pow[i - 1] << 1;
            if (pow[i] >= MOD) pow[i] -= MOD;
        }
        return pow;
    }
}



abstract class LongExtendedMagma extends PropertyHolder {
    public final long e0, e1;
    private final LongBinaryOperator addition, multiplication;
    protected final EnumSet<Property> additiveProps, multiplicativeProps;
    public LongExtendedMagma(LongMonoid addition, LongMonoid multiplication, EnumSet<Property> properties) {
        super(properties);
        this.addition = addition.operator;
        this.multiplication = multiplication.operator;
        this.e0 = addition.identityElement();
        this.e1 = multiplication.identityElement();
        this.additiveProps = addition.getProperties();
        this.multiplicativeProps = multiplication.getProperties();
    }
    public LongExtendedMagma(LongMonoid addition, LongMonoid multiplication, TypicalPropertySets properties) {
        this(addition, multiplication, properties.getProperties());
    }
    public final long add(long t, long u) {return addition.applyAsLong(t, u);}
    public final long mul(long t, long u) {return multiplication.applyAsLong(t, u);}
}



class LongCommutativeMonoid extends LongMonoid {
    public LongCommutativeMonoid(final LongBinaryOperator operator, final long e) {
        super(operator, e);
        addProperties(Property.COMMUTATIVE);
    }
    public static <M extends LongMagma & LongUnital> LongCommutativeMonoid of(M m) {
        m.requireProperties(TypicalPropertySets.COMMUTATIVE_MONOID.getProperties());
        return new LongCommutativeMonoid(m.operator, m.identityElement());
    }
}


/**
 * @author https://atcoder.jp/users/suisen
 */
final class In {
    public static final FastScanner fsc = new FastScanner();
    public static int ni() {return fsc.nextInt();}
    public static int[] ni(final int n) {
        final int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = fsc.nextInt();
        return a;
    }
    public static int[] ni(final int n, final IntUnaryOperator f) {
        final int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = f.applyAsInt(fsc.nextInt());
        return a;
    }
    public static int[][] ni(final int n, final int m) {
        final int[][] a = new int[n][m];
        for (int i = 0; i < n; i++) a[i] = ni(m);
        return a;
    }
    public static int[][] ni(final int n, final int m, final IntUnaryOperator f) {
        final int[][] a = new int[n][m];
        for (int i = 0; i < n; i++) a[i] = ni(m, f);
        return a;
    }
    public static long nl() {return fsc.nextLong();}
    public static long[] nl(final int n) {
        final long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = fsc.nextLong();
        return a;
    }
    public static long[] nl(final int n, final LongUnaryOperator f) {
        final long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = f.applyAsLong(fsc.nextLong());
        return a;
    }
    public static long[][] nl(final int n, final int m) {
        final long[][] a = new long[n][m];
        for (int i = 0; i < n; i++) a[i] = nl(m);
        return a;
    }
    public static long[][] nl(final int n, final int m, final LongUnaryOperator f) {
        final long[][] a = new long[n][m];
        for (int i = 0; i < n; i++) a[i] = nl(m, f);
        return a;
    }
    public static char[] nc() {return fsc.next().toCharArray();}
    public static char[][] nc(final int n) {
        final char[][] c = new char[n][];
        for (int i = 0; i < n; i++) c[i] = nc();
        return c;
    }
    public static double nd() {return fsc.nextDouble();}
    public static double[] nd(final int n) {
        final double[] a = new double[n];
        for (int i = 0; i < n; i++) a[i] = fsc.nextDouble();
        return a;
    }
    public static double[][] nd(final int n, final int m) {
        final double[][] a = new double[n][m];
        for (int i = 0; i < n; i++) a[i] = nd(m);
        return a;
    }
    public static String ns() {return fsc.next();}
    public static String[] ns(final int n) {
        final String[] s = new String[n];
        for (int i = 0; i < n; i++) s[i] = fsc.next();
        return s;
    }
    public static boolean[][] grid(final int h, final int w, final char trueCharacter) {
        final boolean[][] grid = new boolean[h][w];
        for (int i = 0; i < h; i++) {
            final char[] s = fsc.next().toCharArray();
            for (int j = 0; j < w; j++) grid[i][j] = s[j] == trueCharacter;
        }
        return grid;
    }
}


enum TypicalPropertySets {
    ABELIAN_GROUP(EnumSet.of(Property.ASSOCIATIVE, Property.CANCELLATIVE, Property.COMMUTATIVE)),
    BOUNDED_SEMI_LATTICE(EnumSet.of(Property.ASSOCIATIVE, Property.COMMUTATIVE, Property.IDEMPOTENT)),
    COMMUTATIVE_MONOID(EnumSet.of(Property.ASSOCIATIVE, Property.COMMUTATIVE)),
    GROUP(EnumSet.of(Property.ASSOCIATIVE, Property.CANCELLATIVE)),
    MONOID(EnumSet.of(Property.ASSOCIATIVE)),
    SEMI_GROUP(EnumSet.of(Property.ASSOCIATIVE)),
    SEMI_LATTICE(EnumSet.of(Property.ASSOCIATIVE, Property.IDEMPOTENT, Property.COMMUTATIVE)),
    SEMI_RING(EnumSet.of(Property.DISTRIBUTIVE, Property.ANNIHILATED_BY_ZERO)),
    RING(EnumSet.of(Property.DISTRIBUTIVE, Property.ANNIHILATED_BY_ZERO));
    private final EnumSet<Property> properties;
    private TypicalPropertySets(EnumSet<Property> properties) {this.properties = properties;}
    public final EnumSet<Property> getProperties() {return properties.clone();}
}

interface LongInversible {long inverse(long t);}

/**
 * @author https://atcoder.jp/users/suisen
 */
class Const {
    public static final long MOD7 = 1_000_000_007;
    public static final long MOD9 = 1_000_000_009;
    public static final long MOD99 = 998_244_353;

    public static final long LINF = Long.MAX_VALUE >> 2;
    public static final int IINF = Integer.MAX_VALUE >> 1;
    public static final double DINF = 1e150;

    public static final double SDELTA = 1e-12;
    public static final double DELTA = 1e-9;
    public static final double LDELTA = 1e-6;

    public static final int[] dx8 = {1, 0, -1, 0, 1, -1, -1, 1};
    public static final int[] dy8 = {0, 1, 0, -1, 1, 1, -1, -1};
    public static final int[] dx4 = {1, 0, -1, 0};
    public static final int[] dy4 = {0, 1, 0, -1};

    private Const(){}
}

interface LongUnital {long identityElement();}


abstract class PropertyHolder {
    private final EnumSet<Property> properties;
    public PropertyHolder(final EnumSet<Property> properties) {this.properties = properties;}
    public PropertyHolder(final TypicalPropertySets typicalSet) {this(typicalSet.getProperties());}
    public final EnumSet<Property> getProperties() {return properties;}
    public final void addProperties(final Property... props) {for (Property prop : props) properties.add(prop);}
    public final void addProperties(final EnumSet<Property> props) {for (Property prop : props) properties.add(prop);}
    public final void addProperties(final TypicalPropertySets props) {addProperties(props.getProperties());}
    public final boolean hasProperties(final Property... props) {
        for (final Property prop : props) if (!properties.contains(prop)) return false;
        return true;
    }
    public final boolean hasProperties(final EnumSet<Property> props) {
        for (final Property prop : props) if (!properties.contains(prop)) return false;
        return true;
    }
    public final boolean hasProperties(final TypicalPropertySets props) {return hasProperties(props.getProperties());}
    public final void requireProperties(final EnumSet<Property> props, final Property... ps) {
        final ArrayList<Property> unmet = new ArrayList<>();
        for (final Property prop : props) if (!properties.contains(prop)) unmet.add(prop);
        for (final Property prop : ps) if (!properties.contains(prop)) unmet.add(prop);
        if (unmet.size() > 0) throw new UnsatisfiedRequiredPropertiesException(unmet);
    }
    public final void requireProperties(final TypicalPropertySets props, final Property... ps) {
        requireProperties(props.getProperties(), ps);
    }
    private static final class UnsatisfiedRequiredPropertiesException extends RuntimeException {
        private static final long serialVersionUID = 1L;
        private UnsatisfiedRequiredPropertiesException(final Collection<Property> props) {
            for (final Property prop : props) System.err.println(prop.name() + "should be satisfied.");
        }
    }
}
