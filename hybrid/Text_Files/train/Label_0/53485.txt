import java.io.InputStream;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.function.IntUnaryOperator;
import java.util.function.LongUnaryOperator;


public class Main {
    static final long mod = Const.MOD998244353;
    static final ModArithmetic ma = ModArithmetic.of(mod);
    static final ModPolynomialFactory mpf = ModPolynomialFactory.of((int) mod);
    public static void main(String[] args) throws Exception {
        ExtendedScanner sc = new ExtendedScanner();
        FastPrintStream pw = new FastPrintStream();
        solve(sc, pw);
        sc.close();
        pw.flush();
        pw.close();
    }

    public static void solve(ExtendedScanner sc, FastPrintStream pw) {
        final int hmax = 100000;
        final int n = sc.nextInt();

        long[] fac = ma.factorial(2 * n);
        long[] ifac = ma.factorialInv(2 * n);
        long[] ipow = new long[2 * n + 1];
        ipow[2 * n] = ma.inv(ma.pow(2, 2 * n));
        for (int i = 2 * n; i > 0; i--) {
            ipow[i - 1] = ma.add(ipow[i], ipow[i]);
        }
        long[] tab = new long[n + 1];
        for (int i = 0; i <= n; i++) {
            tab[i] = ma.mul(fac[2 * i], ifac[i], ipow[i]);
        }

        int[] c = new int[hmax];
        for (int i = 0; i < 2 * n; i++) {
            c[sc.nextInt() - 1]++;
        }

        int pmax = 0;
        
        for (int e : c) {
            pmax += e / 2;
        }

        PriorityQueue<ModPolynomialFactory.ModPolynomial> pq = new PriorityQueue<>((f, g) -> f.N - g.N);
        for (int i = 0; i < hmax; i++) {
            if (c[i] == 0) continue;
            int k = c[i];
            long[] g = new long[k / 2 + 1];
            for (int j = 0; j <= k / 2; j++) {
                g[j] = ma.mul(fac[k], ipow[j], ifac[j], ifac[k - 2 * j]);
            }
            pq.add(mpf.create(g));
        }

        while (pq.size() >= 2) {
            var f = pq.poll();
            var g = pq.poll();
            pq.add(f.mul(g));
        }

        long[] coefs = pq.poll().getCoefs();

        long ans = 0;
        
        for (int i = 0; i <= pmax; i++) {
            long cmb = ma.mul(coefs[i], tab[n - i]);
            if ((i & 1) == 0) {
                ans += cmb;
            } else {
                ans -= cmb;
            }
        }

        pw.println(ma.mod(ans));
    }
}

/**
 * @author https://atcoder.jp/users/suisen
 */
class FastScanner implements AutoCloseable {
    private final java.io.InputStream in;
    private final byte[] buf = new byte[1 << 13];
    private int ptr = 0;
    private int buflen = 0;

    public FastScanner(java.io.InputStream in) {
        this.in = in;
    }

    public FastScanner() {
        this(System.in);
    }

    private boolean hasNextByte() {
        if (ptr < buflen) return true;
        ptr = 0;
        try {
            buflen = in.read(buf);
        } catch (java.io.IOException e) {
            throw new RuntimeException(e);
        }
        return buflen > 0;
    }

    private int readByte() {
        return hasNextByte() ? buf[ptr++] : -1;
    }

    public boolean hasNext() {
        while (hasNextByte() && !(32 < buf[ptr] && buf[ptr] < 127)) ptr++;
        return hasNextByte();
    }

    private StringBuilder nextSequence() {
        if (!hasNext()) throw new java.util.NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        for (int b = readByte(); 32 < b && b < 127; b = readByte()) {
            sb.appendCodePoint(b);
        }
        return sb;
    }

    public String next() {
        return nextSequence().toString();
    }

    public String next(int len) {
        return new String(nextChars(len));
    }

    public char nextChar() {
        if (!hasNextByte()) throw new java.util.NoSuchElementException();
        return (char) readByte();
    }

    public char[] nextChars() {
        StringBuilder sb = nextSequence();
        int l = sb.length();
        char[] dst = new char[l];
        sb.getChars(0, l, dst, 0);
        return dst;
    }
    public char[] nextChars(int len) {
        if (!hasNext()) throw new java.util.NoSuchElementException();
        char[] s = new char[len];
        int i = 0;
        int b = readByte();
        while (32 < b && b < 127 && i < len) {
            s[i++] = (char) b; b = readByte();
        }
        if (i != len) {
            throw new java.util.NoSuchElementException(
                String.format("Next token has smaller length than expected.", len)
            );
        }
        return s;
    }
    public long nextLong() {
        if (!hasNext()) throw new java.util.NoSuchElementException();
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        if (b < '0' || '9' < b) throw new NumberFormatException();
        while (true) {
            if ('0' <= b && b <= '9') {
                n = n * 10 + b - '0';
            } else if (b == -1 || !(32 < b && b < 127)) {
                return minus ? -n : n;
            } else throw new NumberFormatException();
            b = readByte();
        }
    }
    public int nextInt() {
        return Math.toIntExact(nextLong());
    }
    public double nextDouble() {
        return Double.parseDouble(next());
    }
    public void close() {
        try {
            in.close();
        } catch (java.io.IOException e) {
            throw new RuntimeException(e);
        }
    }
}


/**
 * @author https://atcoder.jp/users/suisen
 */
final class ExtendedScanner extends FastScanner {
    public ExtendedScanner() {super();}
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
}


class ModPolynomialFactory {
    public final long MOD;
    public final Convolution cnv;
    public final ModArithmetic ma;

    private ModPolynomialFactory(int mod, boolean isNTTPrime) {
        this.MOD = mod;
        this.cnv = isNTTPrime ? Convolution.ofNTTPrime(mod) : Convolution.of(mod);
        this.ma = ModArithmetic.of(mod);
    }

    public static ModPolynomialFactory of(int mod) {
        return new ModPolynomialFactory(mod, false);
    }

    public static ModPolynomialFactory ofNTTPrime(int mod) {
        return new ModPolynomialFactory(mod, true);
    }

    public ModPolynomial create(long[] c, int n) {
        return new ModPolynomial(c, n);
    }

    public ModPolynomial create(long[] c) {
        return new ModPolynomial(c);
    }

    public ModPolynomial cut(ModPolynomial f, int maxDegInclusive) {
        long[] c = new long[maxDegInclusive + 1];
        System.arraycopy(f.C, 0, c, 0, Math.min(f.N, maxDegInclusive + 1));
        return new ModPolynomial(c);
    }

    public ModPolynomial add(ModPolynomial f, ModPolynomial g) {
        long[] hc = new long[Math.max(f.N, g.N)];
        System.arraycopy(f.C, 0, hc, 0, f.N);
        for (int i = 0; i < g.N; i++) {
            hc[i] = hc[i] + g.C[i];
        }
        return new ModPolynomial(hc);
    }

    public ModPolynomial sub(ModPolynomial f, ModPolynomial g) {
        long[] hc = new long[Math.max(f.N, g.N)];
        System.arraycopy(f.C, 0, hc, 0, f.N);
        for (int i = 0; i < g.N; i++) {
            hc[i] = hc[i] - g.C[i];
        }
        return new ModPolynomial(hc);
    }

    public ModPolynomial mul(ModPolynomial f, long a) {
        a = ma.mod(a);
        long[] c = new long[f.N];
        for (int i = 0; i < f.N; i++) c[i] = ma.mul(a, f.C[i]);
        return new ModPolynomial(c);
    }

    public ModPolynomial mul(ModPolynomial f, ModPolynomial g) {
        return new ModPolynomial(cnv.convolution(f.C, g.C));
    }

    public ModPolynomial mul(ModPolynomial f, ModPolynomial g, int maxDegInclusive) {
        return new ModPolynomial(cnv.convolution(f.C, g.C), maxDegInclusive);
    }

    public ModPolynomial div(ModPolynomial f, ModPolynomial g, int maxDegInclusive) {
        return mul(f, inv(g, maxDegInclusive), maxDegInclusive);
    }

    public ModPolynomial inv(ModPolynomial f, int maxDegInclusive) {
        int k = 1;
        ModPolynomial inv = new ModPolynomial(new long[]{ma.inv(f.C[0])});
        while (k < maxDegInclusive + 1) {
            k <<= 1;
            inv = inv.mul(2).sub(inv.mul(inv, k).mul(cut(f, k), k));
        }
        return cut(inv, maxDegInclusive);
    }

    public ModPolynomial differentiate(ModPolynomial f) {
        long[] c = new long[f.N - 1];
        for (int i = 1; i < f.N; i++) c[i - 1] = ma.mul(f.C[i], i);
        return new ModPolynomial(c);
    }

    public ModPolynomial integrate(ModPolynomial f) {
        long[] c = new long[f.N + 1];
        long[] invs = ma.rangeInv(f.N + 1);
        for (int i = 1; i <= f.N; i++) c[i] = ma.mul(f.C[i - 1], invs[i]);
        return new ModPolynomial(c);
    }
    
    public ModPolynomial log(ModPolynomial f, int maxDegInclusive) {
        return integrate(mul(differentiate(f), inv(f, maxDegInclusive), maxDegInclusive - 1));
    }
    
    public ModPolynomial exp(ModPolynomial f, int maxDegInclusive) {
        ModPolynomial g = new ModPolynomial(new long[]{1});
        int k = 1;
        while (k < maxDegInclusive + 1) {
            k <<= 1;
            ModPolynomial tmp = sub(cut(f, k), log(g, k));
            tmp.C[0] = ma.add(tmp.C[0], 1);
            g = mul(g, tmp, k);
        }
        return cut(g, maxDegInclusive);
    }

    public ModPolynomial pow(ModPolynomial f, long k, int maxDegInclusive) {
        int t0 = 0;
        while (t0 < f.N && f.C[t0] == 0) t0++;
        if ((long) t0 * k >= f.N) return new ModPolynomial(new long[]{0});
        ModPolynomial g = new ModPolynomial(java.util.Arrays.copyOfRange(f.C, t0, f.N));
        long base = g.C[0];
        g = g.mul(ma.inv(base));
        ModPolynomial h = exp(log(g, maxDegInclusive).mul(k), maxDegInclusive).mul(ma.pow(base, k));
        long[] c = new long[maxDegInclusive + 1];
        System.arraycopy(h.C, 0, c, (int) (t0 * k), (int) (maxDegInclusive + 1 - t0 * k));
        return new ModPolynomial(c);
    }

    public ModPolynomial sqrt(ModPolynomial f, int maxDegInclusive) {
        int i = 0;
        while (i < f.N && f.C[i] == 0) i++;
        if (i == f.N) return new ModPolynomial(new long[]{0});
        if ((i & 1) == 1) return null;
        java.util.OptionalLong ops = ma.sqrt(f.C[i]);
        if (ops.isEmpty()) return null;
        long s = ops.getAsLong();
        ModPolynomial g = new ModPolynomial(java.util.Arrays.copyOfRange(f.C, i, f.N));
        g = mul(exp(mul(log(mul(g, ma.inv(g.C[0])), maxDegInclusive), ma.inv(2)), maxDegInclusive), s);
        long[] sqrt = new long[i / 2 + g.N];
        System.arraycopy(g.C, 0, sqrt, i / 2, g.N);
        return new ModPolynomial(sqrt, maxDegInclusive);
    }

    // public static long[] lagrangePolynomial(long[] x, long[] y, NTT ntt) {
    // long mod = ntt.MOD;
    // int m = x.length;
    // int n = 1; while (n < m) n <<= 1;
    // long[][] seg = new long[n << 1][];
    // for (int k = 0; k < m; k++) {
    // seg[n + k] = new long[]{-x[k], 1};
    // }
    // for (int k = m; k < n; k++) {
    // seg[n + k] = new long[]{1};
    // }
    // for (int k = n - 1; k > 0; k--) {
    // seg[k] = ntt.convolution(seg[k << 1 | 0], seg[k << 1 | 1]);
    // }
    // long[] l = seg[1];
    // seg = null;
    // int d = l.length - 1;
    // for (int i = 0; i < d; i++) {
    // l[i] = (l[i + 1] * (i + 1)) % mod;
    // }
    // l[d] = 0;
    // }

    public class ModPolynomial implements ArithmeticOperations<ModPolynomial> {
        public final int N;
        final long[] C;
        ModPolynomial(long[] c, int n) {
            this.N = n + 1;
            this.C = new long[N];
            int l = Math.min(N, c.length);
            for (int i = 0; i < l; i++) {
                C[i] = ma.mod(c[i]);
            }
        }
        ModPolynomial(long[] c) {
            int n = c.length - 1;
            while (n > 0 && c[n] == 0) n--;
            this.N = n + 1;
            this.C = new long[N];
            for (int i = 0; i < N; i++) C[i] = ma.mod(c[i]);
        }
        public long apply(long x) {
            long ret = C[N - 1];
            for (int i = N - 2; i >= 0; i--) ret = ma.mod(ret * x + C[i]);
            return ret;
        }
        public ModPolynomial add(ModPolynomial f) {return ModPolynomialFactory.this.add(this, f);}
        public ModPolynomial sub(ModPolynomial f) {return ModPolynomialFactory.this.sub(this, f);}
        public ModPolynomial mul(ModPolynomial f) {return ModPolynomialFactory.this.mul(this, f);}
        public ModPolynomial mul(ModPolynomial f, int maxDegInclusive) {
            return ModPolynomialFactory.this.mul(this, f, maxDegInclusive);
        }
        public ModPolynomial mul(long a)          {return ModPolynomialFactory.this.mul(this, a);}
        public ModPolynomial div(ModPolynomial f) {
            return ModPolynomialFactory.this.div(this, f, f.N);
        }
        public ModPolynomial div(ModPolynomial f, int maxDegInclusive) {
            return ModPolynomialFactory.this.div(this, f, maxDegInclusive);
        }
        public ModPolynomial inv(int maxDegInclusive) {
            return ModPolynomialFactory.this.inv(this, maxDegInclusive);
        }
        public ModPolynomial differentiate()      {return ModPolynomialFactory.this.differentiate(this);}
        public ModPolynomial integrate    ()      {return ModPolynomialFactory.this.integrate(this);}
        public ModPolynomial log(int maxDegInclusive) {return ModPolynomialFactory.this.log(this, maxDegInclusive);}
        public ModPolynomial exp(int maxDegInclusive) {return ModPolynomialFactory.this.exp(this, maxDegInclusive);}
        public ModPolynomial pow(long n, int maxDegInclusive) {
            return ModPolynomialFactory.this.pow(this, n, maxDegInclusive);
        }
        public ModPolynomial sqrt(int maxDegInclusive) {
            return ModPolynomialFactory.this.sqrt(this, maxDegInclusive);
        }
        public long   getCoef(int deg) {return C[deg];}
        public long[] getCoefs()       {return C;}
    }
}

/**
 * @author https://atcoder.jp/users/suisen
 */
class FastPrintStream implements AutoCloseable {
    private static final int BUF_SIZE = 1 << 13;
    private final byte[] buf = new byte[BUF_SIZE];
    private int ptr = 0;
    private final java.lang.reflect.Field strField;
    private final java.nio.charset.CharsetEncoder encoder;

    private java.io.OutputStream out;

    public FastPrintStream(java.io.OutputStream out) {
        this.out = out;
        java.lang.reflect.Field f;
        try {
            f = java.lang.String.class.getDeclaredField("value");
            f.setAccessible(true);
        } catch (NoSuchFieldException | SecurityException e) {
            f = null;
        }
        this.strField = f;
        this.encoder = java.nio.charset.StandardCharsets.US_ASCII.newEncoder();
    }

    public FastPrintStream(java.io.File file) throws java.io.IOException {
        this(new java.io.FileOutputStream(file));
    }

    public FastPrintStream(java.lang.String filename) throws java.io.IOException {
        this(new java.io.File(filename));
    }

    public FastPrintStream() {
        this(System.out);
        try {
            java.lang.reflect.Field f = java.io.PrintStream.class.getDeclaredField("autoFlush");
            f.setAccessible(true);
            f.set(System.out, false);
        } catch (IllegalAccessException | IllegalArgumentException | NoSuchFieldException e) {
            // ignore
        }
    }

    public FastPrintStream println() {
        if (ptr == BUF_SIZE) internalFlush();
        buf[ptr++] = (byte) '\n';
        return this;
    }

    public FastPrintStream println(java.lang.Object o) {
        return print(o).println();
    }

    public FastPrintStream println(java.lang.String s) {
        return print(s).println();
    }

    public FastPrintStream println(char[] s) {
        return print(s).println();
    }

    public FastPrintStream println(char c) {
        return print(c).println();
    }

    public FastPrintStream println(int x) {
        return print(x).println();
    }

    public FastPrintStream println(long x) {
        return print(x).println();
    }

    public FastPrintStream println(double d, int precision) {
        return print(d, precision).println();
    }

    private FastPrintStream print(byte[] bytes) {
        int n = bytes.length;
        if (ptr + n > BUF_SIZE) {
            internalFlush();
            try {
                out.write(bytes);
            } catch (java.io.IOException e) {
                throw new RuntimeException();
            }
        } else {
            System.arraycopy(bytes, 0, buf, ptr, n);
            ptr += n;
        }
        return this;
    }

    public FastPrintStream print(java.lang.Object o) {
        return print(o.toString());
    }

    public FastPrintStream print(java.lang.String s) {
        if (strField == null) {
            return print(s.getBytes());
        } else {
            try {
                Object value = strField.get(s);
                if (value instanceof byte[]) {
                    return print((byte[]) value);
                } else {
                    return print((char[]) value);
                }
            } catch (IllegalAccessException e) {
                return print(s.getBytes());
            }
        }
    }

    public FastPrintStream print(char[] s) {
        try {
            return print(encoder.encode(java.nio.CharBuffer.wrap(s)).array());
        } catch (java.nio.charset.CharacterCodingException e) {
            byte[] bytes = new byte[s.length];
            for (int i = 0; i < s.length; i++) {
                bytes[i] = (byte) s[i];
            }
            return print(bytes);
        }
    }

    public FastPrintStream print(char c) {
        if (ptr == BUF_SIZE) internalFlush();
        buf[ptr++] = (byte) c;
        return this;
    }

    public FastPrintStream print(int x) {
        if (x == 0) {
            if (ptr == BUF_SIZE) internalFlush();
            buf[ptr++] = '0';
            return this;
        }
        int d = len(x);
        if (ptr + d > BUF_SIZE) internalFlush();
        if (x < 0) {
            buf[ptr++] = '-';
            x = -x;
            d--;
        }
        int j = ptr += d; 
        while (x > 0) {
            buf[--j] = (byte) ('0' + (x % 10));
            x /= 10;
        }
        return this;
    }

    public FastPrintStream print(long x) {
        if (x == 0) {
            if (ptr == BUF_SIZE) internalFlush();
            buf[ptr++] = '0';
            return this;
        }
        int d = len(x);
        if (ptr + d > BUF_SIZE) internalFlush();
        if (x < 0) {
            buf[ptr++] = '-';
            x = -x;
            d--;
        }
        int j = ptr += d; 
        while (x > 0) {
            buf[--j] = (byte) ('0' + (x % 10));
            x /= 10;
        }
        return this;
    }

    public FastPrintStream print(double d, int precision) {
        if (d < 0) {
            print('-');
            d = -d;
        }
        d += Math.pow(10, -precision) / 2;
        print((long) d).print('.');
        d -= (long) d;
        for(int i = 0; i < precision; i++){
            d *= 10;
            print((int) d);
            d -= (int) d;
        }
        return this;
    }

    private void internalFlush() {
        try {
            out.write(buf, 0, ptr);
            ptr = 0;
        } catch (java.io.IOException e) {
            throw new RuntimeException(e);
        }
    }

    public void flush() {
        try {
            out.write(buf, 0, ptr);
            out.flush();
            ptr = 0;
        } catch (java.io.IOException e) {
            throw new RuntimeException(e);
        }
    }

    public void close() {
        try {
            out.close();
        } catch (java.io.IOException e) {
            throw new RuntimeException(e);
        }
    }

    private static int len(int x) {
        int d = 1;
        if (x >= 0) {d = 0; x = -x;}
        int p = -10;
        for (int i = 1; i < 10; i++, p *= 10) if (x > p) return i + d;
        return 10 + d;
    }

    private static int len(long x) {
        int d = 1;
        if (x >= 0) {d = 0; x = -x;}
        long p = -10;
        for (int i = 1; i < 19; i++, p *= 10) if (x > p) return i + d;
        return 19 + d;
    }
}

interface ArithmeticOperations<T> {
    public T add(T t);
    public T sub(T t);
    public T mul(T t);
    public T div(T t);
}

/**
 * @author https://atcoder.jp/users/suisen
 */
final class MathUtil {
    private MathUtil(){}
    public static java.util.ArrayList<Integer> primeList(int n) {
        java.util.ArrayList<Integer> primes = new java.util.ArrayList<>();
        int[] div = osak(n);
        for (int i = 2; i <= n; i++) {
            if (div[i] == i) primes.add(i);
        }
        return primes;
    }
    public static int[] osak(int n) {
        if (n <= 0) throw new AssertionError();
        int[] div = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            if ((i & 1) != 0) {
                div[i] = i;
            } else {
                div[i] = 2;
            }
        }
        for (int i = 3; i <= n; i += 2) {
            if (div[i] == i) {
                if ((long) i * i > n) continue;
                for (int j = i * i; j <= n; j += i << 1) {
                    div[j] = i;
                }
            }
        }
        return div;
    }
    public static java.util.HashMap<Long, Integer> factorize(long n) {
        java.util.HashMap<Long, Integer> factors = new java.util.HashMap<>();
        for (long p = 2; p * p <= n; p++) {
            int q = 0;
            while (n % p == 0) {
                n /= p;
                q++;
            }
            if (q > 0) factors.put(p, q);
        }
        if (n > 1) factors.put(n, 1);
        return factors;
    }
    public static java.util.ArrayList<Long> divisors(long n) {
        java.util.ArrayList<Long> div = new java.util.ArrayList<>();
        for (long i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                div.add(i);
                long j = n / i;
                if (i != j) div.add(j);
            }
        }
        return div;
    }
    private static java.util.HashMap<Long, Integer> mergeFactor(java.util.HashMap<Long, Integer> fac1, java.util.HashMap<Long, Integer> fac2) {
        if (fac1.size() < fac2.size()) {
            return mergeFactor(fac2, fac1);
        }
        for (java.util.Map.Entry<Long, Integer> e : fac2.entrySet()) {
            long prime = e.getKey();
            int num = e.getValue();
            if (fac1.containsKey(prime)) {
                fac1.put(prime, Math.max(fac1.get(prime), num));
            } else {
                fac1.put(prime, num);
            }
        }
        return fac1;
    }
    public static java.util.HashMap<Long, Integer> factorizedLCM(long a, long b) {
        return mergeFactor(factorize(a), factorize(b));
    }
    public static java.util.HashMap<Long, Integer> factorizedLCM(long... xs) {
        java.util.HashMap<Long, Integer> lcm = new java.util.HashMap<>();
        for (long x : xs) lcm = mergeFactor(lcm, factorize(x));
        return lcm;
    }
    public static long lcm(long a, long b) {
        return (a / gcd(a, b)) * b;
    }
    public static long gcd(long a, long b) {
        a = Math.abs(a);
        b = Math.abs(b);
        if (a < b) {
            long tmp = a; a = b; b = tmp;
        }
        if (b == 0) return a;
        if (a == 0) return b;
        for (long r = a % b; r != 0; r = a % b) {
            a = b; b = r;
        }
        return b;
    }
    public static long gcd(long... xs) {
        long gcd = 0;
        for (long x : xs) gcd = gcd(gcd, x);
        return gcd;
    }
    /**
     * Return one of the solutions to {@code ax+by=gcd(a, b)}.
     * 
     * @return {@code x}, {@code y}, {@code gcd(a, b)}.
     * @param a a of ax+by=gcd(a, b).
     * @param b b of ax+by=gcd(a, b).
     */
    public static long[] extGCD(long a, long b) {
        long s = a, sx = 1, sy = 0; // ax + by = s
        long t = b, tx = 0, ty = 1; // ax + by = t
        for (long tmp, u, ux, uy; s % t != 0;) {
            // u: ax + by = s % t
            tmp = s / t;
            u  = s  - t  * tmp; s  = t ; t  = u ;
            ux = sx - tx * tmp; sx = tx; tx = ux;
            uy = sy - ty * tmp; sy = ty; ty = uy;
        }
        return new long[]{tx, ty, a * tx + b * ty};
    }
    public static long inv(long a, long MOD) {
        long b = MOD;
        long u = 1, v = 0;
        while (b > 0) {
            long t = a / b;
            a -= t * b;
            long tmp1 = a; a = b; b = tmp1;
            u -= t * v;
            long tmp2 = u; u = v; v = tmp2;
        }
        u %= MOD;
        return u < 0 ? u + MOD : u;
    }
    /**
     * @return pair(g, x) s.t. g = gcd(a, b), xa = g (mod b), 0 <= x < b/g
     */
    public static long[] gcdInv(long a, long mod) {
        if ((a %= mod) < 0) a += mod;
        if (a == 0) return new long[]{mod, 0};
        long s = mod, t = a;
        long m0 = 0, m1 = 1;
        while (t > 0) {
            long u = s / t;
            s -= t * u;
            m0 -= m1 * u;
            long tmp;
            tmp = s; s = t; t = tmp;
            tmp = m0; m0 = m1; m1 = tmp;
        }
        if (m0 < 0) m0 += mod / s;
        return new long[]{s, m0};
    }
    public static long pow(long a, long b, long mod) {
        if (mod == 1) return 0;
        if ((a %= mod) < 0) a += mod;
        long pow = 1;
        for (long p = a, c = 1; b > 0;) {
            long lsb = b & -b;
            while (lsb != c) {
                c <<= 1;
                p = (p * p) % mod;
            }
            pow = (pow * p) % mod;
            b ^= lsb;
        }
        return pow;
    }
    public static java.util.OptionalLong sqrt(long a, long p) {
        if ((a %= p) < 0) a += p;
        if (a == 0) return java.util.OptionalLong.of(0);
        if (a == 1) return java.util.OptionalLong.of(1);
        if (pow(a, (p - 1) >> 1, p) != 1) return java.util.OptionalLong.empty();
        if ((p & 3) == 3) {
            return java.util.OptionalLong.of(pow(a, (p + 1) >> 2, p));
        }
        if ((p & 7) == 5) {
            if (pow(a, (p - 1) >> 2, p) == 1) {
                return java.util.OptionalLong.of(pow(a, (p + 3) >> 3, p));
            } else {
                return java.util.OptionalLong.of(pow(2, (p - 1) >> 2, p) * pow(a, (p + 3) >> 3, p) % p);
            }
        }
        long S = 0;
        long Q = p - 1;
        while ((Q & 1) == 0) {
            ++S;
            Q >>= 1;
        }
        long z = 1;
        while (pow(z, (p - 1) >> 1, p) != p - 1) ++z;
        long c = pow(z, Q, p);
        long R = pow(a, (Q + 1) / 2, p);
        long t = pow(a, Q, p);
        long M = S;
        while (t != 1) {
            long cur = t;
            int i;
            for (i = 1; i < M; i++) {
                cur = cur * cur % p;
                if (cur == 1) break;
            }
            long b = pow(c, 1l << (M - i - 1), p);
            R = R * b % p;
            t = t * b % p * b % p;
            c = b * b % p;
            M = i;
        }
        return java.util.OptionalLong.of(R);
    }
    public static long eulerPhi(long n) {
        for (long p : factorize(n).keySet()) {
            n = (n / p) * (p - 1);
        }
        return n;
    }
    public static long comb(long n, long r) {
        if (n < r) return 0;
        r = Math.min(r, n - r);
        long res = 1; for (long d = 1; d <= r; d++) {res *= n--; res /= d;}
        return res;
    }
    public static long ceilSqrt(long n) {
        long l = -1, r = n;
        while (r - l > 1) {
            long m = (r + l) >> 1;
            if (m * m >= n) r = m;
            else l = m;
        }
        return r;
    }
    public static long floorSqrt(long n) {
        long l = 0, r = n + 1;
        while (r - l > 1) {
            long m = (r + l) >> 1;
            if (m * m > n) r = m;
            else l = m;
        }
        return l;
    }
    public static long[] crt(long[] r, long[] m){
        if (r.length != m.length) {
            throw new AssertionError("Different length.");
        }
        int n = r.length;
        long r0 = 0, m0 = 1;
        for(int i=0; i<n; i++){
            if (m[i] < 1) {
                throw new AssertionError();
            }
            long m1 = m[i];
            long r1 = r[i] % m1;
            if (r1 < 0) r1 += m1;
            if (m0 < m1){
                long tmp;
                tmp = r0; r0 = r1; r1 = tmp;
                tmp = m0; m0 = m1; m1 = tmp;
            }
            if (m0 % m1 == 0){
                if (r0 % m1 != r1) return new long[]{0, 0};
                continue;
            }
            long[] gi = gcdInv(m0, m1);
            long g = gi[0], im = gi[1];
            long u1 = m1 / g;
            if((r1 - r0) % g != 0) return new long[]{0, 0};
            long x = (r1 - r0) / g % u1 * im % u1;
            r0 += x * m0;
            m0 *= u1;
            if (r0 < 0) r0 += m0;
        } 
        return new long[]{r0, m0};
    }
    public static long garner(long[] c, long[] mods) {
        int n = c.length + 1;
        long[] cnst = new long[n];
        long[] coef = new long[n];
        java.util.Arrays.fill(coef, 1);
        for (int i = 0; i < n - 1; i++) {
            long m1 = mods[i];
            long v = (c[i] - cnst[i] + m1) % m1;
            v = v * pow(coef[i], m1 - 2, m1) % m1;

            for (int j = i + 1; j < n; j++) {
                long m2 = mods[j];
                cnst[j] = (cnst[j] + coef[j] * v) % m2;
                coef[j] = (coef[j] * m1) % m2;
            }
        }
        return cnst[n - 1];
    }
    public static long floorSum(long n, long m, long a, long b){
        long ans = 0;
        if(a >= m){
            ans += (n - 1) * n * (a / m) / 2;
            a %= m;
        }
        if(b >= m){
            ans += n * (b / m);
            b %= m;
        }
        long ymax = (a * n + b) / m;
        long xmax = ymax * m - b;
        if (ymax == 0) return ans;
        ans += (n - (xmax + a - 1) / a) * ymax;
        ans += floorSum(ymax, a, m, (a - xmax % a) % a);
        return ans;
    }
    /**
     * @param m prime
     */
    public static int primitiveRoot(int m) {
        if (m == 2) return 1;
        if (m == 167772161) return 3;
        if (m == 469762049) return 3;
        if (m == 754974721) return 11;
        if (m == 998244353) return 3;
        int[] divs = new int[20];
        divs[0] = 2;
        int cnt = 1;
        int x = (m - 1) / 2;
        while (x % 2 == 0) x /= 2;
        for (int i = 3; (long) i * i <= x; i += 2) {
            if (x % i == 0) {
                divs[cnt++] = i;
                while (x % i == 0) x /= i;
            }
        }
        if (x > 1) {
            divs[cnt++] = x;
        }
        for (int g = 2; ; g++) {
            boolean ok = true;
            for (int i = 0; i < cnt; i++) {
                if (pow(g, (m - 1) / divs[i], m) == 1) {
                    ok = false;
                    break;
                }
            }
            if (ok) return g;
        }
    }
    
}

class Const {
    public static final long   LINF   = 1l << 59;
    public static final int    IINF   = (1  << 30) - 1;
    public static final double DINF   = 1e150;
    
    public static final double SMALL  = 1e-12;
    public static final double MEDIUM = 1e-9;
    public static final double LARGE  = 1e-6;

    public static final long MOD1000000007 = 1000000007;
    public static final long MOD998244353  = 998244353 ;
    public static final long MOD754974721  = 754974721 ;
    public static final long MOD167772161  = 167772161 ;
    public static final long MOD469762049  = 469762049 ;

    public static final int[] dx8 = {1, 0, -1, 0, 1, -1, -1, 1};
    public static final int[] dy8 = {0, 1, 0, -1, 1, 1, -1, -1};
    public static final int[] dx4 = {1, 0, -1, 0};
    public static final int[] dy4 = {0, 1, 0, -1};
}


interface Convolution {
    static final int THRESHOLD_NAIVE_CONVOLUTION = 150;
    public static final Convolution C_167772161 = new Convolution167772161();
    public static final Convolution C_469762049 = new Convolution469762049();
    public static final Convolution C_754974721 = new Convolution754974721();
    public static final Convolution C_998244353 = new Convolution998244353();

    public long[] convolution(long[] a, long[] b);

    public static Convolution of(int mod) {
        if (mod == 998244353) {
            return C_998244353;
        } else if (mod == 167772161) {
            return C_167772161;
        } else if (mod == 469762049) {
            return C_469762049;
        } else if (mod == 754974721) {
            return C_754974721;
        } else {
            return new ConvolutionAnyMod(mod);
        }
    }

    public static Convolution ofNTTPrime(int mod) {
        if (mod == 998244353) {
            return C_998244353;
        } else if (mod == 167772161) {
            return C_167772161;
        } else if (mod == 469762049) {
            return C_469762049;
        } else if (mod == 754974721) {
            return C_754974721;
        } else {
            return new ConvolutionNTTPrime(mod);
        }
    }

    public static long[] convolutionNaive(long[] a, long[] b, int mod) {
        int n = a.length;
        int m = b.length;
        int k = n + m - 1;
        long[] ret = new long[k];
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
            ret[i + j] += a[i] * b[j] % mod;
        }
        for (int i = 0; i < k; i++) {
            ret[i] %= mod;
        }
        return ret;
    }

    private static int ceilPow2(int n) {
        int x = 0;
        while ((1L << x) < n) x++;
        return x;
    }

    /**
     * Pre-calculation for NTT.
     *
     * @param mod NTT Prime.
     * @param g   Primitive root of mod.
     * @return Pre-calculation table.
     */
    private static long[] sumE(int mod, int g) {
        long[] sum_e = new long[30];
        long[] es = new long[30];
        long[] ies = new long[30];
        int cnt2 = Integer.numberOfTrailingZeros(mod - 1);
        long e = MathUtil.pow(g, (mod - 1) >> cnt2, mod);
        long ie = MathUtil.pow(e, mod - 2, mod);
        for (int i = cnt2; i >= 2; i--) {
            es[i - 2] = e;
            ies[i - 2] = ie;
            e = e * e % mod;
            ie = ie * ie % mod;
        }
        long now = 1;
        for (int i = 0; i < cnt2 - 2; i++) {
            sum_e[i] = es[i] * now % mod;
            now = now * ies[i] % mod;
        }
        return sum_e;
    }

    /**
     * Pre-calculation for inverse NTT.
     *
     * @param mod Mod.
     * @param g   Primitive root of mod.
     * @return Pre-calculation table.
     */
    private static long[] sumIE(int mod, int g) {
        long[] sum_ie = new long[30];
        long[] es = new long[30];
        long[] ies = new long[30];

        int cnt2 = Integer.numberOfTrailingZeros(mod - 1);
        long e = MathUtil.pow(g, (mod - 1) >> cnt2, mod);
        long ie = MathUtil.pow(e, mod - 2, mod);
        for (int i = cnt2; i >= 2; i--) {
            es[i - 2] = e;
            ies[i - 2] = ie;
            e = e * e % mod;
            ie = ie * ie % mod;
        }
        long now = 1;
        for (int i = 0; i < cnt2 - 2; i++) {
            sum_ie[i] = ies[i] * now % mod;
            now = now * es[i] % mod;
        }
        return sum_ie;
    }

    static final class Convolution754974721 implements Convolution {
        private static final int PRIMITIVE_ROOT = 11;
        private static final int NTT_PRIME = 754974721;
        @Override
        public long[] convolution(long[] a, long[] b) {
            int n = a.length;
            int m = b.length;
            if (n == 0 || m == 0) return new long[0];
            if (Math.max(n, m) <= THRESHOLD_NAIVE_CONVOLUTION) {
                int k = n + m - 1;
                long[] ret = new long[k];
                for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
                    ret[i + j] += a[i] * b[j] % NTT_PRIME;
                }
                for (int i = 0; i < k; i++) {
                    ret[i] %= NTT_PRIME;
                }
                return ret;
            }

            int z = 1 << ceilPow2(n + m - 1);
            {
                long[] na = new long[z];
                long[] nb = new long[z];
                System.arraycopy(a, 0, na, 0, n);
                System.arraycopy(b, 0, nb, 0, m);
                a = na;
                b = nb;
            }
            long[] sume = sumE(NTT_PRIME, PRIMITIVE_ROOT);
            long[] sumie = sumIE(NTT_PRIME, PRIMITIVE_ROOT);
    
            butterfly(a, sume);
            butterfly(b, sume);
            for (int i = 0; i < z; i++) {
                a[i] = a[i] * b[i] % NTT_PRIME;
            }
            butterflyInv(a, sumie);
            a = java.util.Arrays.copyOf(a, n + m - 1);
    
            long iz = MathUtil.pow(z, NTT_PRIME - 2, NTT_PRIME);
            for (int i = 0; i < n + m - 1; i++) a[i] = a[i] * iz % NTT_PRIME;
            return a;
        }
        private void butterfly(long[] a, long[] sumE) {
            int h = ceilPow2(a.length);
            for (int ph = 1; ph <= h; ph++) {
                int w = 1 << (ph - 1), p = 1 << (h - ph);
                long now = 1;
                for (int s = 0; s < w; s++) {
                    int offset = s << (h - ph + 1);
                    for (int i = 0; i < p; i++) {
                        long l = a[i + offset];
                        long r = a[i + offset + p] * now % NTT_PRIME;
                        a[i + offset] = (l + r) % NTT_PRIME;
                        a[i + offset + p] = (l - r + NTT_PRIME) % NTT_PRIME;
                    }
                    int x = Integer.numberOfTrailingZeros(~s);
                    now = now * sumE[x] % NTT_PRIME;
                }
            }
        }
        private void butterflyInv(long[] a, long[] sumIE) {
            int h = ceilPow2(a.length);
            for (int ph = h; ph >= 1; ph--) {
                int w = 1 << (ph - 1), p = 1 << (h - ph);
                long inow = 1;
                for (int s = 0; s < w; s++) {
                    int offset = s << (h - ph + 1);
                    for (int i = 0; i < p; i++) {
                        long l = a[i + offset];
                        long r = a[i + offset + p];
                        a[i + offset] = (l + r) % NTT_PRIME;
                        a[i + offset + p] = (NTT_PRIME + l - r) * inow % NTT_PRIME;
                    }
                    int x = Integer.numberOfTrailingZeros(~s);
                    inow = inow * sumIE[x] % NTT_PRIME;
                }
            }
        }
    }
    static final class Convolution167772161 implements Convolution {
        private static final int PRIMITIVE_ROOT = 3;
        private static final int NTT_PRIME = 167772161;
        public long[] convolution(long[] a, long[] b) {
            int n = a.length;
            int m = b.length;
            if (n == 0 || m == 0) return new long[0];
            if (Math.max(n, m) <= THRESHOLD_NAIVE_CONVOLUTION) {
                int k = n + m - 1;
                long[] ret = new long[k];
                for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
                    ret[i + j] += a[i] * b[j] % NTT_PRIME;
                }
                for (int i = 0; i < k; i++) {
                    ret[i] %= NTT_PRIME;
                }
                return ret;
            }

            int z = 1 << ceilPow2(n + m - 1);
            {
                long[] na = new long[z];
                long[] nb = new long[z];
                System.arraycopy(a, 0, na, 0, n);
                System.arraycopy(b, 0, nb, 0, m);
                a = na;
                b = nb;
            }
            long[] sume = sumE(NTT_PRIME, PRIMITIVE_ROOT);
            long[] sumie = sumIE(NTT_PRIME, PRIMITIVE_ROOT);
    
            butterfly(a, sume);
            butterfly(b, sume);
            for (int i = 0; i < z; i++) {
                a[i] = a[i] * b[i] % NTT_PRIME;
            }
            butterflyInv(a, sumie);
            a = java.util.Arrays.copyOf(a, n + m - 1);
    
            long iz = MathUtil.pow(z, NTT_PRIME - 2, NTT_PRIME);
            for (int i = 0; i < n + m - 1; i++) a[i] = a[i] * iz % NTT_PRIME;
            return a;
        }
        private void butterfly(long[] a, long[] sumE) {
            int h = ceilPow2(a.length);
            for (int ph = 1; ph <= h; ph++) {
                int w = 1 << (ph - 1), p = 1 << (h - ph);
                long now = 1;
                for (int s = 0; s < w; s++) {
                    int offset = s << (h - ph + 1);
                    for (int i = 0; i < p; i++) {
                        long l = a[i + offset];
                        long r = a[i + offset + p] * now % NTT_PRIME;
                        a[i + offset] = (l + r) % NTT_PRIME;
                        a[i + offset + p] = (l - r + NTT_PRIME) % NTT_PRIME;
                    }
                    int x = Integer.numberOfTrailingZeros(~s);
                    now = now * sumE[x] % NTT_PRIME;
                }
            }
        }
        private void butterflyInv(long[] a, long[] sumIE) {
            int h = ceilPow2(a.length);
            for (int ph = h; ph >= 1; ph--) {
                int w = 1 << (ph - 1), p = 1 << (h - ph);
                long inow = 1;
                for (int s = 0; s < w; s++) {
                    int offset = s << (h - ph + 1);
                    for (int i = 0; i < p; i++) {
                        long l = a[i + offset];
                        long r = a[i + offset + p];
                        a[i + offset] = (l + r) % NTT_PRIME;
                        a[i + offset + p] = (NTT_PRIME + l - r) * inow % NTT_PRIME;
                    }
                    int x = Integer.numberOfTrailingZeros(~s);
                    inow = inow * sumIE[x] % NTT_PRIME;
                }
            }
        }
    }
    static final class Convolution469762049 implements Convolution {
        private static final int PRIMITIVE_ROOT = 3;
        private static final int NTT_PRIME = 469762049;
        public long[] convolution(long[] a, long[] b) {
            int n = a.length;
            int m = b.length;
            if (n == 0 || m == 0) return new long[0];
            if (Math.max(n, m) <= THRESHOLD_NAIVE_CONVOLUTION) {
                int k = n + m - 1;
                long[] ret = new long[k];
                for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
                    ret[i + j] += a[i] * b[j] % NTT_PRIME;
                }
                for (int i = 0; i < k; i++) {
                    ret[i] %= NTT_PRIME;
                }
                return ret;
            }

            int z = 1 << ceilPow2(n + m - 1);
            {
                long[] na = new long[z];
                long[] nb = new long[z];
                System.arraycopy(a, 0, na, 0, n);
                System.arraycopy(b, 0, nb, 0, m);
                a = na;
                b = nb;
            }
            long[] sume = sumE(NTT_PRIME, PRIMITIVE_ROOT);
            long[] sumie = sumIE(NTT_PRIME, PRIMITIVE_ROOT);
    
            butterfly(a, sume);
            butterfly(b, sume);
            for (int i = 0; i < z; i++) {
                a[i] = a[i] * b[i] % NTT_PRIME;
            }
            butterflyInv(a, sumie);
            a = java.util.Arrays.copyOf(a, n + m - 1);
    
            long iz = MathUtil.pow(z, NTT_PRIME - 2, NTT_PRIME);
            for (int i = 0; i < n + m - 1; i++) a[i] = a[i] * iz % NTT_PRIME;
            return a;
        }
        private void butterfly(long[] a, long[] sumE) {
            int h = ceilPow2(a.length);
            for (int ph = 1; ph <= h; ph++) {
                int w = 1 << (ph - 1), p = 1 << (h - ph);
                long now = 1;
                for (int s = 0; s < w; s++) {
                    int offset = s << (h - ph + 1);
                    for (int i = 0; i < p; i++) {
                        long l = a[i + offset];
                        long r = a[i + offset + p] * now % NTT_PRIME;
                        a[i + offset] = (l + r) % NTT_PRIME;
                        a[i + offset + p] = (l - r + NTT_PRIME) % NTT_PRIME;
                    }
                    int x = Integer.numberOfTrailingZeros(~s);
                    now = now * sumE[x] % NTT_PRIME;
                }
            }
        }
        private void butterflyInv(long[] a, long[] sumIE) {
            int h = ceilPow2(a.length);
            for (int ph = h; ph >= 1; ph--) {
                int w = 1 << (ph - 1), p = 1 << (h - ph);
                long inow = 1;
                for (int s = 0; s < w; s++) {
                    int offset = s << (h - ph + 1);
                    for (int i = 0; i < p; i++) {
                        long l = a[i + offset];
                        long r = a[i + offset + p];
                        a[i + offset] = (l + r) % NTT_PRIME;
                        a[i + offset + p] = (NTT_PRIME + l - r) * inow % NTT_PRIME;
                    }
                    int x = Integer.numberOfTrailingZeros(~s);
                    inow = inow * sumIE[x] % NTT_PRIME;
                }
            }
        }
    }
    static class Convolution998244353 implements Convolution {
        private static final int PRIMITIVE_ROOT = 3;
        private static final int NTT_PRIME = 998244353;
        public long[] convolution(long[] a, long[] b) {
            int n = a.length;
            int m = b.length;
            if (n == 0 || m == 0) return new long[0];
            if (Math.max(n, m) <= THRESHOLD_NAIVE_CONVOLUTION) {
                int k = n + m - 1;
                long[] ret = new long[k];
                for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
                    ret[i + j] += a[i] * b[j] % NTT_PRIME;
                }
                for (int i = 0; i < k; i++) {
                    ret[i] %= NTT_PRIME;
                }
                return ret;
            }

            int z = 1 << ceilPow2(n + m - 1);
            {
                long[] na = new long[z];
                long[] nb = new long[z];
                System.arraycopy(a, 0, na, 0, n);
                System.arraycopy(b, 0, nb, 0, m);
                a = na;
                b = nb;
            }
            long[] sume = sumE(NTT_PRIME, PRIMITIVE_ROOT);
            long[] sumie = sumIE(NTT_PRIME, PRIMITIVE_ROOT);
    
            butterfly(a, sume);
            butterfly(b, sume);
            for (int i = 0; i < z; i++) {
                a[i] = a[i] * b[i] % NTT_PRIME;
            }
            butterflyInv(a, sumie);
            a = java.util.Arrays.copyOf(a, n + m - 1);
    
            long iz = MathUtil.pow(z, NTT_PRIME - 2, NTT_PRIME);
            for (int i = 0; i < n + m - 1; i++) a[i] = a[i] * iz % NTT_PRIME;
            return a;
        }
        private void butterfly(long[] a, long[] sumE) {
            int h = ceilPow2(a.length);
            for (int ph = 1; ph <= h; ph++) {
                int w = 1 << (ph - 1), p = 1 << (h - ph);
                long now = 1;
                for (int s = 0; s < w; s++) {
                    int offset = s << (h - ph + 1);
                    for (int i = 0; i < p; i++) {
                        long l = a[i + offset];
                        long r = a[i + offset + p] * now % NTT_PRIME;
                        a[i + offset] = (l + r) % NTT_PRIME;
                        a[i + offset + p] = (l - r + NTT_PRIME) % NTT_PRIME;
                    }
                    int x = Integer.numberOfTrailingZeros(~s);
                    now = now * sumE[x] % NTT_PRIME;
                }
            }
        }
        private void butterflyInv(long[] a, long[] sumIE) {
            int h = ceilPow2(a.length);
            for (int ph = h; ph >= 1; ph--) {
                int w = 1 << (ph - 1), p = 1 << (h - ph);
                long inow = 1;
                for (int s = 0; s < w; s++) {
                    int offset = s << (h - ph + 1);
                    for (int i = 0; i < p; i++) {
                        long l = a[i + offset];
                        long r = a[i + offset + p];
                        a[i + offset] = (l + r) % NTT_PRIME;
                        a[i + offset + p] = (NTT_PRIME + l - r) * inow % NTT_PRIME;
                    }
                    int x = Integer.numberOfTrailingZeros(~s);
                    inow = inow * sumIE[x] % NTT_PRIME;
                }
            }
        }
    }
    static final class ConvolutionAnyMod implements Convolution {
        private final int MOD;
        private ConvolutionAnyMod(int mod) {
            this.MOD = mod;
        }
        public long[] convolution(long[] a, long[] b) {
            int n = a.length;
            int m = b.length;
            if (n == 0 || m == 0) return new long[0];
            if (Math.max(n, m) <= THRESHOLD_NAIVE_CONVOLUTION) {
                int k = n + m - 1;
                long[] ret = new long[k];
                for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
                    ret[i + j] += a[i] * b[j] % MOD;
                }
                for (int i = 0; i < k; i++) {
                    ret[i] %= MOD;
                }
                return ret;
            }
    
            int mod1 = 754974721;
            int mod2 = 167772161;
            int mod3 = 469762049;
    
            long[] c1 = C_754974721.convolution(a, b);
            long[] c2 = C_167772161.convolution(a, b);
            long[] c3 = C_469762049.convolution(a, b);
    
            int retSize = c1.length;
            long[] ret = new long[retSize];
            long[] mods = {mod1, mod2, mod3, MOD};
            for (int i = 0; i < retSize; ++i) {
                ret[i] = MathUtil.garner(new long[]{c1[i], c2[i], c3[i]}, mods);
            }
            return ret;
        }
    }
    static final class ConvolutionNTTPrime implements Convolution {
        private final int NTT_PRIME;
        private final int PRIMITIVE_ROOT;
        private ConvolutionNTTPrime(int mod) {
            this.NTT_PRIME = mod;
            this.PRIMITIVE_ROOT = MathUtil.primitiveRoot(mod);
        }
        public long[] convolution(long[] a, long[] b) {
            int n = a.length;
            int m = b.length;
            if (n == 0 || m == 0) return new long[0];
            if (Math.max(n, m) <= THRESHOLD_NAIVE_CONVOLUTION) {
                int k = n + m - 1;
                long[] ret = new long[k];
                for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
                    ret[i + j] += a[i] * b[j] % NTT_PRIME;
                }
                for (int i = 0; i < k; i++) {
                    ret[i] %= NTT_PRIME;
                }
                return ret;
            }
    
            int z = 1 << ceilPow2(n + m - 1);
            {
                long[] na = new long[z];
                long[] nb = new long[z];
                System.arraycopy(a, 0, na, 0, n);
                System.arraycopy(b, 0, nb, 0, m);
                a = na;
                b = nb;
            }

            long[] sume = sumE(NTT_PRIME, PRIMITIVE_ROOT);
            long[] sumie = sumIE(NTT_PRIME, PRIMITIVE_ROOT);
    
            butterfly(a, sume);
            butterfly(b, sume);
            for (int i = 0; i < z; i++) {
                a[i] = a[i] * b[i] % NTT_PRIME;
            }
            butterflyInv(a, sumie);
            a = java.util.Arrays.copyOf(a, n + m - 1);
    
            long iz = MathUtil.pow(z, NTT_PRIME - 2, NTT_PRIME);
            for (int i = 0; i < n + m - 1; i++) a[i] = a[i] * iz % NTT_PRIME;
            return a;
        }
        private void butterflyInv(long[] a, long[] sumIE) {
            int n = a.length;
            int h = ceilPow2(n);

            for (int ph = h; ph >= 1; ph--) {
                int w = 1 << (ph - 1), p = 1 << (h - ph);
                long inow = 1;
                for (int s = 0; s < w; s++) {
                    int offset = s << (h - ph + 1);
                    for (int i = 0; i < p; i++) {
                        long l = a[i + offset];
                        long r = a[i + offset + p];
                        a[i + offset] = (l + r) % NTT_PRIME;
                        a[i + offset + p] = (NTT_PRIME + l - r) * inow % NTT_PRIME;
                    }
                    int x = Integer.numberOfTrailingZeros(~s);
                    inow = inow * sumIE[x] % NTT_PRIME;
                }
            }
        }
        private void butterfly(long[] a, long[] sumE) {
            int n = a.length;
            int h = ceilPow2(n);

            for (int ph = 1; ph <= h; ph++) {
                int w = 1 << (ph - 1), p = 1 << (h - ph);
                long now = 1;
                for (int s = 0; s < w; s++) {
                    int offset = s << (h - ph + 1);
                    for (int i = 0; i < p; i++) {
                        long l = a[i + offset];
                        long r = a[i + offset + p] * now % NTT_PRIME;
                        a[i + offset] = (l + r) % NTT_PRIME;
                        a[i + offset + p] = (l - r + NTT_PRIME) % NTT_PRIME;
                    }
                    int x = Integer.numberOfTrailingZeros(~s);
                    now = now * sumE[x] % NTT_PRIME;
                }
            }
        }
    }
}


/**
 * @author https://atcoder.jp/users/suisen
 */
interface ModArithmetic {
    public static ModArithmetic of(long mod) {
        if (mod <= 0) {
            throw new IllegalArgumentException("Negative mod");
        } else if (mod == 1) {
            return new ModArithmetic1();
        } else if (mod == 2) {
            return new ModArithmetic2();
        } else if (mod == 1000000007) {
            return new ModArithmetic1000000007();
        } else if (mod == 998244353) {
            return new ModArithmetic998244353();
        } else {
            return new ModArithmeticDynamic(mod);
            // return new ModArithmeticBarrett(mod);
        }
    }
    public long getMod();
    public long mod(long a);
    public long add(long a, long b);
    public long sub(long a, long b);
    public long mul(long a, long b);
    public long inv(long a);
    public long pow(long a, long b);
    public default long add(long a, long b, long c) {
        return add(a, add(b, c));
    }
    public default long add(long a, long b, long c, long d) {
        return add(a, add(b, add(c, d)));
    }
    public default long add(long a, long b, long c, long d, long e) {
        return add(a, add(b, add(c, add(d, e))));
    }
    public default long add(long a, long b, long c, long d, long e, long f) {
        return add(a, add(b, add(c, add(d, add(e, f)))));
    }
    public default long add(long a, long b, long c, long d, long e, long f, long g) {
        return add(a, add(b, add(c, add(d, add(e, add(f, g))))));
    }
    public default long add(long a, long b, long c, long d, long e, long f, long g, long h) {
        return add(a, add(b, add(c, add(d, add(e, add(f, add(g, h)))))));
    }
    public default long add(long... xs) {
        long s = 0;
        for (long x : xs) s += x;
        return mod(s);
    }
    public default long mul(long a, long b, long c) {
        return mul(a, mul(b, c));
    }
    public default long mul(long a, long b, long c, long d) {
        return mul(a, mul(b, mul(c, d)));
    }
    public default long mul(long a, long b, long c, long d, long e) {
        return mul(a, mul(b, mul(c, mul(d, e))));
    }
    public default long mul(long a, long b, long c, long d, long e, long f) {
        return mul(a, mul(b, mul(c, mul(d, mul(e, f)))));
    }
    public default long mul(long a, long b, long c, long d, long e, long f, long g) {
        return mul(a, mul(b, mul(c, mul(d, mul(e, mul(f, g))))));
    }
    public default long mul(long a, long b, long c, long d, long e, long f, long g, long h) {
        return mul(a, mul(b, mul(c, mul(d, mul(e, mul(f, mul(g, h)))))));
    }
    public default long mul(long... xs) {
        long s = 1;
        for (long x : xs) s = mul(s, x);
        return s;
    }
    public default long div(long a, long b) {
        return mul(a, inv(b));
    }
    public default java.util.OptionalLong sqrt(long a) {
        a = mod(a);
        if (a == 0) return java.util.OptionalLong.of(0);
        if (a == 1) return java.util.OptionalLong.of(1);
        long p = getMod();
        if (pow(a, (p - 1) >> 1) != 1) return java.util.OptionalLong.empty();
        if ((p & 3) == 3) {
            return java.util.OptionalLong.of(pow(a, (p + 1) >> 2));
        }
        if ((p & 7) == 5) {
            if (pow(a, (p - 1) >> 2) == 1) {
                return java.util.OptionalLong.of(pow(a, (p + 3) >> 3));
            } else {
                return java.util.OptionalLong.of(mul(pow(2, (p - 1) >> 2), pow(a, (p + 3) >> 3)));
            }
        }
        long S = 0;
        long Q = p - 1;
        while ((Q & 1) == 0) {
            ++S;
            Q >>= 1;
        }
        long z = 1;
        while (pow(z, (p - 1) >> 1) != p - 1) ++z;
        long c = pow(z, Q);
        long R = pow(a, (Q + 1) / 2);
        long t = pow(a, Q);
        long M = S;
        while (t != 1) {
            long cur = t;
            int i;
            for (i = 1; i < M; i++) {
                cur = mul(cur, cur);
                if (cur == 1) break;
            }
            long b = pow(c, 1l << (M - i - 1));
            R = mul(R, b);
            t = mul(t, b, b);
            c = mul(b, b);
            M = i;
        }
        return java.util.OptionalLong.of(R);
    }

    /** array operations */

    public default long[] rangeInv(int n) {
        final long MOD = getMod();
        if (n >= MOD) throw new ArithmeticException("divide by zero");
        long[] invs = new long[n + 1];
        invs[1] = 1;
        for (int i = 2; i <= n; i++) {
            long q = MOD - MOD / i;
            long r = invs[(int) (MOD % i)];
            invs[i] = mul(q, r);
        }
        return invs;
    }
    public default long[] arrayInv(long[] a) {
        int n = a.length;
        long[] dp = new long[n + 1];
        long[] pd = new long[n + 1];
        dp[0] = pd[n] = 1;
        for (int i = 0; i < n; i++) dp[i + 1] = mul(dp[i], a[i    ]);
        for (int i = n; i > 0; i--) pd[i - 1] = mul(pd[i], a[i - 1]);
        long inv = inv(dp[n]);
        long[] invs = new long[n];
        for (int i = 0; i < n; i++) {
            long lr = mul(dp[i], pd[i + 1]);
            invs[i] = mul(lr, inv);
        }
        return invs;
    }
    public default long[] factorial(int n) {
        long[] ret = new long[n + 1];
        ret[0] = 1;
        for (int i = 1; i <= n; i++) ret[i] = mul(ret[i - 1], i);
        return ret;
    }
    public default long[] factorialInv(int n) {
        long facN = 1;
        for (int i = 2; i <= n; i++) facN = mul(facN, i);
        long[] invs = new long[n + 1];
        invs[n] = inv(facN);
        for (int i = n; i > 0; i--) invs[i - 1] = mul(invs[i], i);
        return invs;
    }
    public default long[] rangePower(long a, int n) {
        a = mod(a);
        long[] pows = new long[n + 1];
        pows[0] = 1;
        for (int i = 1; i <= n; i++) pows[i] = mul(pows[i - 1], a);
        return pows;
    }

    /** combinatric operations */

    public default long[][] combTable(int n) {
        long[][] comb = new long[n + 1][];
        for (int i = 0; i <= n; i++) {
            comb[i] = new long[i + 1];
            comb[i][0] = comb[i][i] = 1;
            for (int j = 1; j < i; j++) {
                comb[i][j] = add(comb[i - 1][j - 1], comb[i - 1][j]);
            }
        }
        return comb;
    }
    public default long comb(int n, int r, long[] factorial, long[] invFactorial) {
        if (r < 0 || r > n) return 0;
        long inv = mul(invFactorial[r], invFactorial[n - r]);
        return mul(factorial[n], inv);
    }
    public default long naiveComb(long n, long r) {
        if (r < 0 || r > n) return 0;
        r = Math.min(r, n - r);
        if (r == 0) return 1;
        long res = 1;
        long[] invs = rangeInv(Math.toIntExact(r));
        for (int d = 1; d <= r; d++) {
            res = mul(res, n--, invs[d]);
        }
        return res;
    }
    public default long perm(int n, int r, long[] factorial, long[] invFactorial) {
        if (r < 0 || r > n) return 0;
        return mul(factorial[n], invFactorial[n - r]);
    }
    public default long naivePerm(long n, long r) {
        if (r < 0 || r > n) return 0;
        long res = 1;
        for (long i = n - r + 1; i <= n; i++) res = mul(res, i);
        return res;
    }
    static final class ModArithmetic1 implements ModArithmetic {
        @Override public long getMod() {return 1;}
        @Override public long mod(long a) {return 0;}
        @Override public long add(long a, long b) {return 0;}
        @Override public long sub(long a, long b) {return 0;}
        @Override public long mul(long a, long b) {return 0;}
        @Override public long inv(long a) {return 0;}
        @Override public long pow(long a, long b) {return 0;}
        @Override public long[] rangeInv(int n) {return new long[n + 1];}
        @Override public long[] arrayInv(long[] a) {return new long[a.length];}
        @Override public long[] factorial(int n) {return new long[n + 1];}
        @Override public long[] factorialInv(int n) {return new long[n + 1];}
        @Override public long[] rangePower(long a, int n) {return new long[n + 1];}
        @Override public long[][] combTable(int n) {return new long[n + 1][n + 1];}
        @Override public long comb(int n, int r, long[] factorial, long[] invFactorial) {return 0;}
        @Override public long naiveComb(long n, long r) {return 0;}
        @Override public long perm(int n, int r, long[] factorial, long[] invFactorial) {return 0;}
        @Override public long naivePerm(long n, long r) {return 0;}
    }
    static final class ModArithmetic2 implements ModArithmetic {
        @Override public long getMod() {return 2;}
        @Override public long mod(long a) {return a & 1;}
        @Override public long add(long a, long b) {return (a ^ b) & 1;}
        @Override public long sub(long a, long b) {return (a ^ b) & 1;}
        @Override public long mul(long a, long b) {return (a & b) & 1;}
        @Override public long inv(long a) {
            if ((a & 1) == 1) return 1;
            throw new ArithmeticException("divide by zero");
        }
        @Override public long pow(long a, long b) {
            if (b == 0 || (a & 1) == 1) return 1;
            return 0;
        }
    }
    static final class ModArithmetic1000000007 implements ModArithmetic {
        private static final long MOD = Const.MOD1000000007;
        @Override public long getMod() {return MOD;}
        @Override public long mod(long a) {return (a %= MOD) < 0 ? a + MOD : a;}
        @Override public long add(long a, long b) {
            long s = a + b;
            return s >= MOD ? s - MOD : s;
        }
        @Override public long sub(long a, long b) {
            long s = a - b;
            return s < 0 ? s + MOD : s;
        }
        @Override public long mul(long a, long b) {
            return (a * b) % MOD;
        }
        @Override public long inv(long a) {
            a = mod(a);
            long b = MOD;
            long u = 1, v = 0;
            while (b >= 1) {
                long t = a / b;
                a -= t * b;
                long tmp1 = a; a = b; b = tmp1;
                u -= t * v;
                long tmp2 = u; u = v; v = tmp2;
            }
            // if (a != 1) throw new ArithmeticException("divide by zero");
            return mod(u);
        }
        @Override public long pow(long a, long b) {
            a = mod(a);
            long pow = 1;
            for (long p = a, c = 1; b > 0;) {
                long lsb = b & -b;
                while (lsb != c) {
                    c <<= 1;
                    p = (p * p) % MOD;
                }
                pow = (pow * p) % MOD;
                b ^= lsb;
            }
            return pow;
        }
    }
    static final class ModArithmetic998244353 implements ModArithmetic {
        private static final long MOD = Const.MOD998244353;
        @Override public long getMod() {return MOD;}
        @Override public long mod(long a) {return (a %= MOD) < 0 ? a + MOD : a;}
        @Override public long add(long a, long b) {
            long s = a + b;
            return s >= MOD ? s - MOD : s;
        }
        @Override public long sub(long a, long b) {
            long s = a - b;
            return s < 0 ? s + MOD : s;
        }
        @Override public long mul(long a, long b) {
            return (a * b) % MOD;
        }
        @Override public long inv(long a) {
            a = mod(a);
            long b = MOD;
            long u = 1, v = 0;
            while (b >= 1) {
                long t = a / b;
                a -= t * b;
                long tmp1 = a; a = b; b = tmp1;
                u -= t * v;
                long tmp2 = u; u = v; v = tmp2;
            }
            // if (a != 1) throw new ArithmeticException("divide by zero");
            return mod(u);
        }
        @Override public long pow(long a, long b) {
            a = mod(a);
            long pow = 1;
            for (long p = a, c = 1; b > 0;) {
                long lsb = b & -b;
                while (lsb != c) {
                    c <<= 1;
                    p = (p * p) % MOD;
                }
                pow = (pow * p) % MOD;
                b ^= lsb;
            }
            return pow;
        }
    }
    static class ModArithmeticDynamic implements ModArithmetic {
        final long MOD;
        private ModArithmeticDynamic(long mod) {
            this.MOD = mod;
        }
        @Override public long getMod() {
            return MOD;
        }
        @Override public long mod(long a) {
            return (a %= MOD) < 0 ? a + MOD : a;
        }
        @Override public long add(long a, long b) {
            long s = a + b;
            return s >= MOD ? s - MOD : s;
        }
        @Override public long sub(long a, long b) {
            long s = a - b;
            return s < 0 ? s + MOD : s;
        }
        @Override public long mul(long a, long b) {
            return (a * b) % MOD;
        }
        @Override public long inv(long a) {
            a = mod(a);
            long b = MOD;
            long u = 1, v = 0;
            while (b >= 1) {
                long t = a / b;
                a -= t * b;
                long tmp1 = a; a = b; b = tmp1;
                u -= t * v;
                long tmp2 = u; u = v; v = tmp2;
            }
            // if (a != 1) throw new ArithmeticException("divide by zero");
            return mod(u);
        }
        @Override public long pow(long a, long b) {
            a = mod(a);
            long pow = 1;
            for (long p = a, c = 1; b > 0;) {
                long lsb = b & -b;
                while (lsb != c) {
                    c <<= 1;
                    p = mul(p, p);
                }
                pow = mul(pow, p);
                b ^= lsb;
            }
            return pow;
        }
    }
    static final class ModArithmeticBarrett extends ModArithmeticDynamic {
        private static final long mask = 0xffff_ffffl;
        private final long mh;
        private final long ml;
        private ModArithmeticBarrett(long mod) {
            super(mod);
            long a = (1l << 32) / mod, b = (1l << 32) % mod;
            long m = a * a * mod + 2 * a * b + (b * b) / mod;
            this.mh = m >>> 32;
            this.ml = m & mask;
        }
        private long reduce(long x) {
            long z = (x & mask) * ml;
            z = (x & mask) * mh + (x >>> 32) * ml + (z >>> 32);
            z = (x >>> 32) * mh + (z >>> 32);
            x -= z * MOD;
            return (int) (x < MOD ? x : x - MOD);
        }
        @Override public long mul(long a, long b) {
            return reduce(a * b);
        }
    }
}
