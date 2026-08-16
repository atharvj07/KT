import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.EnumSet;
import java.util.HashMap;
import java.util.NoSuchElementException;
import java.util.function.IntUnaryOperator;
import java.util.function.LongBinaryOperator;
import java.util.function.LongUnaryOperator;


public class Main {
    public static void main(String[] args) throws Exception {
        Field f = System.out.getClass().getDeclaredField("autoFlush");
        f.setAccessible(true);
        f.set(System.out, false);
        execute(System.in, System.out);
    }

    public static void execute(InputStream in, OutputStream out) {
        ExtendedScanner s = new ExtendedScanner(System.in);
        Out o = new Out(System.out);
        solve(s, o);
        o.flush();
        o.close();
    }

    public static ModuloArithmetic ma = new ModuloArithmetic(Const.MOD7);

    public static void solve(ExtendedScanner sc, Out out) {
        int t = sc.nextInt();
        long[] eb = new long[16];
        long[] ob = new long[16];
        for (int i = 0; i < 16; i++) {
            eb[i] = answer(2 * i);
            ob[i] = answer(2 * i + 1);
        }
        long[][] ea = new long[16][16];
        long[][] oa = new long[16][16];
        for (int i = 0; i < 16; i++) {
            ea[i][0] = 1;
            oa[i][0] = 1;
            for (int j = 1; j < 16; j++) {
                ea[i][j] = ma.mul(ea[i][j - 1], 2 * i);
                oa[i][j] = ma.mul(oa[i][j - 1], 2 * i + 1);
            }
        }
        ea = inverse(ea);
        oa = inverse(oa);
        long[] ex = new long[16];
        long[] ox = new long[16];
        for (int i = 0; i < 16; i++) {
            for (int j = 0; j < 16; j++) {
                ex[i] += ma.mul(ea[i][j], eb[j]);
                ox[i] += ma.mul(oa[i][j], ob[j]);
            }
            ex[i] = ma.mod(ex[i]);
            ox[i] = ma.mod(ox[i]);
        }
        while (t --> 0) {
            long n = sc.nextLong();
            long p = 1;
            long ans = 0;
            for (int i = 0; i < 16; i++) {
                ans += ma.mul(p, (n & 1) == 0 ? ex[i] : ox[i]);
                p = ma.mul(p, n);
            }
            ans = ma.mod(ans);
            out.write(ans).write('\n');
        }
    }

    public static long answer(long n) {
        long ans = 0;
        for (long a = 0; a <= n; a++) {
            long fa = f(a);
            for (long b = 0; a + b <= n; b++) {
                long fb = f(b);
                for (long c = 0; a + b + c <= n; c++) {
                    long fc = f(c);
                    for (long d = 0; a + b + c + d <= n; d++) {
                        long fd = f(d);
                        for (long eb = 0; a + b + c + d + eb <= n; eb++) {
                            long fe = f(eb);
                            ans += ma.prod(fa, fb, fc, fd, fe);
                            ans = ma.mod(ans);
                        }
                    }
                }
            }
        }
        return ans;
    }

    public static long f(long i) {
        long m = i / 2;
        if ((i & 1) == 0) {
            return ma.mul(m, m + 1);
        } else {
            return ma.mul(m + 1, m + 1);
        }
    }

    public static long[][] inverse(long[][] a) {
        long[][] b = new long[16][16];
        for (int i = 0; i < 16; i++) {
            b[i][i] = 1;
        }
        for (int i = 0; i < 16; i++) {
            long iv = ma.inv(a[i][i]);
            for (int k = i; k < 16; k++) {
                a[i][k] = ma.mul(a[i][k], iv);
            }
            for (int k = 0; k < 16; k++) {
                b[i][k] = ma.mul(b[i][k], iv);
            }
            for (int j = i + 1; j < 16; j++) {
                long x = a[j][i];
                for (int k = i; k < 16; k++) {
                    a[j][k] -= ma.mul(x, a[i][k]);
                    a[j][k] = ma.mod(a[j][k]);
                }
                for (int k = 0; k < 16; k++) {
                    b[j][k] -= ma.mul(x, b[i][k]);
                    b[j][k] = ma.mod(b[j][k]);
                }
            }
        }
        for (int i = 16 - 1; i >= 0; i--) {
            for (int j = i - 1; j >= 0; j--) {
                long x = a[j][i];
                for (int k = 0; k < 16; k++) {
                    b[j][k] -= ma.mul(x, b[i][k]);
                    b[j][k] = ma.mod(b[j][k]);
                }
                a[j][i] -= x;
            }
        }
        return b;
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


/**
 * @author https://atcoder.jp/users/suisen
 */
final class ExtendedScanner extends BasicScanner {
    public ExtendedScanner(InputStream in) {super(in);}
    public int[] ints(final int n) {
        final int[] a = new int[n];
        Arrays.setAll(a, $ -> nextInt());
        return a;
    }
    public int[] ints(final int n, final IntUnaryOperator f) {
        final int[] a = new int[n];
        Arrays.setAll(a, $ -> f.applyAsInt(nextInt()));
        return a;
    }
    public int[][] ints(final int n, final int m) {
        final int[][] a = new int[n][];
        Arrays.setAll(a, $ -> ints(m));
        return a;
    }
    public int[][] ints(final int n, final int m, final IntUnaryOperator f) {
        final int[][] a = new int[n][];
        Arrays.setAll(a, $ -> ints(m, f));
        return a;
    }
    public long[] longs(final int n) {
        final long[] a = new long[n];
        Arrays.setAll(a, $ -> nextLong());
        return a;
    }
    public long[] longs(final int n, final LongUnaryOperator f) {
        final long[] a = new long[n];
        Arrays.setAll(a, $ -> f.applyAsLong(nextLong()));
        return a;
    }
    public long[][] longs(final int n, final int m) {
        final long[][] a = new long[n][];
        Arrays.setAll(a, $ -> longs(m));
        return a;
    }
    public long[][] longs(final int n, final int m, final LongUnaryOperator f) {
        final long[][] a = new long[n][];
        Arrays.setAll(a, $ -> longs(m, f));
        return a;
    }
    public char[][] charArrays(final int n) {
        final char[][] c = new char[n][];
        Arrays.setAll(c, $ -> nextChars());
        return c;
    }
    public char[][] charArrays(final int n, final int m) {
        final char[][] c = new char[n][];
        Arrays.setAll(c, $ -> nextChars(m));
        return c;
    }
    public double[] doubles(final int n) {
        final double[] a = new double[n];
        Arrays.setAll(a, $ -> nextDouble());
        return a;
    }
    public double[][] doubles(final int n, final int m) {
        final double[][] a = new double[n][];
        Arrays.setAll(a, $ -> doubles(m));
        return a;
    }
    public String[] strings(final int n) {
        final String[] s = new String[n];
        Arrays.setAll(s, $ -> next());
        return s;
    }
    public String[] strings(final int n, final int m) {
        final String[] s = new String[n];
        Arrays.setAll(s, $ -> next(m));
        return s;
    }
    public boolean[][] grid(final int h, final int w, final char trueCharacter) {
        final boolean[][] grid = new boolean[h][w];
        for (int i = 0; i < h; i++) {
            final char[] s = nextChars(w);
            for (int j = 0; j < w; j++) grid[i][j] = s[j] == trueCharacter;
        }
        return grid;
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



class LongField extends LongRing {
    public LongField(final LongAbelianGroup addition, final LongMonoid multiplication) {
        super(addition, multiplication);
        multiplication.requireProperties(EnumSet.of(Property.COMMUTATIVE));
    }
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


class LongRing extends LongSemiRing {
    private final LongUnaryOperator additiveInverse;
    public LongRing(final LongAbelianGroup addition, final LongMonoid multiplication) {
        super(addition, multiplication);
        this.additiveInverse = addition::inverse;
    }
    public final long additiveInverse(final long t) {return additiveInverse.applyAsLong(t);}
}


class BasicScanner {
    private final InputStream in;
    private final byte[] buf = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;
    public BasicScanner(InputStream in) {this.in = in;}
    private boolean hasNextByte() {
        if (ptr < buflen) return true;
        ptr = 0;
        try {buflen = in.read(buf);}
        catch (final IOException e) {e.printStackTrace();}
        return buflen > 0;
    }
    private int readByte() {return hasNextByte() ? buf[ptr++] : -1;}
    public boolean hasNext() {
        while (hasNextByte() && !(33 <= buf[ptr] && buf[ptr] <= 126)) ptr++;
        return hasNextByte();
    }
    private StringBuilder nextSequence() {
        if (!hasNext()) throw new NoSuchElementException();
        final StringBuilder sb = new StringBuilder();
        int b = readByte();
        while (33 <= b && b <= 126) {sb.appendCodePoint(b); b = readByte();}
        return sb;
    }
    public char nextChar() {
        return (char) readByte();
    }
    public String next() {
        return nextSequence().toString();
    }
    public String next(int len) {
        return new String(nextChars(len));
    }
    public char[] nextChars() {
        final StringBuilder sb = nextSequence();
        int l = sb.length();
        char[] dst = new char[l];
        sb.getChars(0, l, dst, 0);
        return dst;
    }
    public char[] nextChars(int len) {
        if (!hasNext()) throw new NoSuchElementException();
        char[] s = new char[len];
        int i = 0;
        int b = readByte();
        while (33 <= b && b <= 126 && i < len) {s[i++] = (char) b; b = readByte();}
        if (i != len) throw new NoSuchElementException(String.format("length %d is longer than the sequence.", len));
        return s;
    }
    public long nextLong() {
        if (!hasNext()) throw new NoSuchElementException();
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {minus = true; b = readByte();}
        if (b < '0' || '9' < b) throw new NumberFormatException();
        while (true) {
            if ('0' <= b && b <= '9') n = n * 10 + b - '0';
            else if (b == -1 || !(33 <= b && b <= 126)) return minus ? -n : n;
            else throw new NumberFormatException();
            b = readByte();
        }
    }
    public int nextInt() {return Math.toIntExact(nextLong());}
    public double nextDouble() {return Double.parseDouble(next());}
}


class Out {
    private final OutputStream out;
    private byte[] buf = new byte[1024];
    private int ptr = 0;
    private static final int AUTO_FLUSH_THRETHOLD = 1 << 17;

    public Out(OutputStream out) {
        this.out = out;
    }

    public void flush() {
        try {
            out.write(buf, 0, ptr);
            out.flush();
            ptr = 0;
        } catch (IOException e) {e.printStackTrace();}
    }

    public void close() {
        try {out.close();} catch (IOException e) {e.printStackTrace();}
    }

    public Out write(Object o) {
        return write(o.toString());
    }

    public Out write(String s) {
        try {
            Field strValueField = s.getClass().getDeclaredField("value");
            strValueField.setAccessible(true);
            byte[] b = (byte[]) strValueField.get(s);
            int l = s.length();
            if (l > AUTO_FLUSH_THRETHOLD) {
                flush();
                int i = 0;
                while (i + AUTO_FLUSH_THRETHOLD < l) {
                    out.write(b, i, AUTO_FLUSH_THRETHOLD);
                    out.flush();
                    i += AUTO_FLUSH_THRETHOLD;
                }
                ensureCapacity(l - i);
                System.arraycopy(b, i, buf, 0, l - i);
                ptr = l - i;
            } else {
                ensureCapacity(ptr + l);
                System.arraycopy(b, 0, buf, ptr, l);
                ptr += l;
            }
        } catch (Exception e) {e.printStackTrace();}
        return this;
    }

    public Out write(char[] c) {
        int l = c.length;
        if (l > AUTO_FLUSH_THRETHOLD) {
            flush();
            ensureCapacity(AUTO_FLUSH_THRETHOLD);
            int i = 0;
            while (i + AUTO_FLUSH_THRETHOLD < l) {
                for (int j = 0; j < AUTO_FLUSH_THRETHOLD; j++) {
                    buf[ptr++] = (byte) c[i + j];
                }
                flush();
                i += AUTO_FLUSH_THRETHOLD;
            }
            for (; i < l; i++) {
                buf[ptr++] = (byte) c[i];
            }
        } else {
            ensureCapacity(ptr + l);
            for (char ch : c) buf[ptr++] = (byte) ch;
        }
        return this;
    }

    public Out write(char c) {
        ensureCapacity(ptr + 1);
        buf[ptr++] = (byte) c;
        return this;
    }

    public Out write(byte b) {
        ensureCapacity(ptr + 1);
        buf[ptr++] = b;
        return this;
    }

    public Out write(int x) {
        if (x == 0) {
            ensureCapacity(ptr + 1);
            buf[ptr++] = '0';
            return this;
        }
        int d = stringSize(x);
        ensureCapacity(ptr + d);
        if (x < 0) {
            buf[ptr++] = '-';
            x = -x;
            d--;
        }
        int j = ptr + d; 
        while (x > 0) {
            buf[--j] = (byte) ('0' + (x % 10));
            x /= 10;
        }
        ptr += d;
        return this;
    }

    public Out write(long x) {
        if (x == 0) {
            ensureCapacity(ptr + 1);
            buf[ptr++] = '0';
            return this;
        }
        int d = stringSize(x);
        ensureCapacity(ptr + d);
        if (x < 0) {
            buf[ptr++] = '-';
            x = -x;
            d--;
        }
        int j = ptr + d; 
        while (x > 0) {
            buf[--j] = (byte) ('0' + (x % 10));
            x /= 10;
        }
        ptr += d;
        return this;
    }

    public Out write(double d) {
        return write(Double.toString(d));
    }

    private void ensureCapacity(int cap) {
        if (cap > AUTO_FLUSH_THRETHOLD) {
            flush();
        }
        if (cap >= buf.length) {
            int newLength = buf.length;
            while (newLength < cap) newLength <<= 1;
            byte[] newBuf = new byte[newLength];
            System.arraycopy(buf, 0, newBuf, 0, buf.length);
            buf = newBuf;
        }
    }
    private static int stringSize(long x) {
        int d = 1;
        if (x >= 0) {d = 0; x = -x;}
        long p = -10;
        for (int i = 1; i < 19; i++, p *= 10) if (x > p) return i + d;
        return 19 + d;
    }
    private static int stringSize(int x) {
        int d = 1;
        if (x >= 0) {d = 0; x = -x;}
        int p = -10;
        for (int i = 1; i < 10; i++, p *= 10) if (x > p) return i + d;
        return 10 + d;
    }
}

enum Property {ANNIHILATED_BY_ZERO, ASSOCIATIVE, CANCELLATIVE, COMMUTATIVE, DISTRIBUTIVE, IDEMPOTENT;}


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



class LongAbelianGroup extends LongGroup {
    public LongAbelianGroup(final LongBinaryOperator operator, final long e, final LongUnaryOperator inverse) {
        super(operator, e, inverse);
        addProperties(Property.COMMUTATIVE);
    }
}

interface LongUnital {long identityElement();}



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
