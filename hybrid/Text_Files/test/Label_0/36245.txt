import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.Objects;

public class Main {
    public static void main(String[] args) {
        FastScanner fsc = new FastScanner();
        int n = fsc.nextInt();
        LightComplex[] c = new LightComplex[n];
        for (int i = 0; i < n; i++) {
            long x = fsc.nextLong();
            long y = fsc.nextLong();
            c[i] = new LightComplex(x, y);
        }
        LightComplex.argsort(c);
        double ans = 0;
        for (int i = 0; i < n; i++) {
            LightComplex z = LightComplex.ZERO;
            for (int j = i, k = j; j < n + i; j++, k = j % n) {
                if (c[i].t <= c[k].t && c[k].t < c[i].t + Math.PI) {
                    z = z.add(c[k]);
                } else if (c[i].t <= c[k].t + 2. * Math.PI && c[k].t + 2. * Math.PI < c[i].t + Math.PI) {
                    z = z.add(c[k]);
                }
                ans = Math.max(ans, z.r);
            }
        }
        System.out.println(ans);
    }
}


class FastScanner {
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
            } catch (IOException e) {
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

    private static boolean isPrintableChar(int c) {
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
        StringBuilder sb = new StringBuilder();
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
        long nl = nextLong();
        if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) {
            throw new NumberFormatException();
        }
        return (int) nl;
    }

    public double nextDouble() {
        return Double.parseDouble(next());
    }
}


class LightComplex {
    public static final LightComplex ZERO = new LightComplex(0, 0, 0, 0);
    public static final LightComplex ONE = new LightComplex(1, 0);
    public static final LightComplex I = new LightComplex(0, 1);

    public long x;
    public long y;
    public double r;
    public double t;

    public LightComplex(long x, long y) {
        this(x, y, Math.sqrt(x * x + y * y), Math.atan2(y, x));
    }

    private LightComplex(long x, long y, double r, double t) {
        this.x = x;
        this.y = y;
        this.r = r;
        this.t = t;
    }

    public LightComplex add(LightComplex c) {
        return new LightComplex(x + c.x, y + c.y);
    }

    public static void argsort(LightComplex[] c) {
        Arrays.sort(c, (u, v) -> Double.compare(u.t, v.t));
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        } else if (!(o instanceof LightComplex)) {
            return false;
        } else {
            LightComplex c = (LightComplex) o;
            return x == c.x && y == c.y && r == c.r && t == c.t;
        }
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y, r, t);
    }

    @Override
    public String toString() {
        return "(x, y) = (" + x + ", " + y + "). (r, t) = (" + r + ", " + t + ").";
    }
}
