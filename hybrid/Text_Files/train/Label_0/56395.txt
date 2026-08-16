import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Writer;
import java.io.BufferedReader;
import java.util.Comparator;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Arthur Gazizov [2oo7] - Kazan FU
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        FastPrinter out = new FastPrinter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        public static int cmpIndex(Func a, Func b) {
            return Integer.compare(-a.index, -b.index);
        }

        public static int cmpOne(Func a, Func b) {
            if (MathUtils.equals(a.x, 1)) {
                int cmp = Double.compare(a.x, b.x);
                return MathUtils.equals(cmp, 0) ? cmpIndex(a, b) : cmp;
            }
            if (MathUtils.equals(b.x, 1)) {
                int cmp = Double.compare(a.x, b.x);
                return MathUtils.equals(cmp, 0) ? cmpIndex(a, b) : cmp;
            }
            return 0;
        }

        public static int cmp(Func a, Func b) {
            int test = cmpOne(a, b);
            if (test != 0) return test;
            if ((a.x - 1) * (b.x - 1) < 0) {
                return Double.compare(a.x, b.x);
            } else {
                return MathUtils.equals(a.get(), b.get()) ? cmpIndex(a, b) : Double.compare(a.get(), b.get());
            }
        }

        public static int compare01(Func a, Func b) {
            return -compare10(b, a);
        }

        public static int compare10(Func a, Func b) {
            int test = cmpOne(a, b);
            if (test != 0) return test;
            if ((a.x - 1) * (b.x - 1) < 0) return Double.compare(a.x, b.x);
            if (a.x > 1) {
                if (b.x > 1) {
                    if (MathUtils.equals(Math.log(Math.log(b.x)) + Math.log(b.y * b.z), Math.log(Math.log(a.x)) + a.z * Math.log(a.y))) {
                        return cmpIndex(a, b);
                    } else {
                        double valueOfA = Math.log(Math.log(a.x)) + Math.log(a.y * a.z);
                        double valueOfB = b.get();
                        return Double.compare(valueOfA, valueOfB);
                    }
                }
            } else {
                double valueOfA = Math.log(-Math.log(a.x)) + Math.log(a.z * a.y);
                double valueOfB = b.get();
                if (MathUtils.equals(valueOfA, valueOfB)) {
                    return cmpIndex(a, b);
                } else {
                    return Double.compare(valueOfB, valueOfA);
                }
            }
            return 0;
        }

        public void solve(int testNumber, FastScanner in, FastPrinter out) {
            double x = in.nextDouble();
            double y = in.nextDouble();
            double z = in.nextDouble();
            Func[] funcs = new Func[12];
            funcs[0] = new Func(x, y, z, 0, 0);
            funcs[1] = new Func(x, z, y, 0, 1);
            funcs[2] = new Func(x, y, z, 1, 2);
            funcs[3] = new Func(x, z, y, 1, 3);
            funcs[4] = new Func(y, x, z, 0, 4);
            funcs[5] = new Func(y, z, x, 0, 5);
            funcs[6] = new Func(y, x, z, 1, 6);
            funcs[7] = new Func(y, z, x, 1, 7);
            funcs[8] = new Func(z, x, y, 0, 8);
            funcs[9] = new Func(z, y, x, 0, 9);
            funcs[10] = new Func(z, x, y, 1, 10);
            funcs[11] = new Func(z, y, x, 1, 11);
            int size = 12;
            Comparator<Func> fuck = new Comparator<Func>() {

                public int compare(Func a, Func b) {
                    if (a.type == 1) {
                        return b.type == 1 ? cmp(a, b) : compare10(a, b);
                    } else {
                        return b.type == 1 ? compare01(a, b) : cmp(a, b);
                    }
                }
            };
            Func exe = funcs[0];
            for (int i = 1; i < 12; i++) {
                int compare = fuck.compare(exe, funcs[i]);
                int tttp = fuck.compare(exe, funcs[i]);
                if (compare == -1) {
                    exe = funcs[i];
                }
            }
            String ans = "";
            switch (exe.index) {
                case 0:
                    ans = "x^y^z";
                    break;
                case 1:
                    ans = "x^z^y";
                    break;
                case 2:
                    ans = "(x^y)^z";
                    break;
                case 3:
                    ans = "(x^z)^y";
                    break;
                case 4:
                    ans = "y^x^z";
                    break;
                case 5:
                    ans = "y^z^x";
                    break;
                case 6:
                    ans = "(y^x)^z";
                    break;
                case 7:
                    ans = "(y^z)^x";
                    break;
                case 8:
                    ans = "z^x^y";
                    break;
                case 9:
                    ans = "z^y^x";
                    break;
                case 10:
                    ans = "(z^x)^y";
                    break;
                case 11:
                    ans = "(z^y)^x";
                    break;
            }
            out.print(ans);
        }

    }

    static class Func {
        public double x;
        public double y;
        public double z;
        public int type;
        public int index;

        public Func(double x, double y, double z, int type, int index) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.type = type;
            this.index = index;
        }

        public double get() {
            return type == 0 ? Math.log(Math.abs(Math.log(x))) + z * Math.log(y) : Math.log(x) * y * z;
        }

    }

    static class FastScanner extends BufferedReader {
        boolean isEOF;

        public FastScanner(InputStream is) {
            super(new InputStreamReader(is));
        }

        public FastScanner(InputStreamReader inputStreamReader) {
            super(inputStreamReader);
        }

        public int read() {
            try {
                int ret = super.read();
                if (isEOF && ret < 0) {
                    throw new InputMismatchException();
                }
                isEOF = ret == -1;
                return ret;
            } catch (IOException e) {
                throw new InputMismatchException();
            }
        }

        public static boolean isWhiteSpace(int c) {
            return c >= -1 && c <= 32;
        }

        public static boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public int nextInt() {
            int c = read();
            while (isWhiteSpace(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int ret = 0;
            while (!isWhiteSpace(c)) {
                if (c < '0' || c > '9') {
                    throw new NumberFormatException("digit expected " + (char) c
                            + " found");
                }
                ret = ret * 10 + c - '0';
                c = read();
            }
            return ret * sgn;
        }

        public double nextDouble() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            double res = 0;
            while (!isSpaceChar(c) && c != '.') {
                if (c == 'e' || c == 'E')
                    return res * Math.pow(10, nextInt());
                if (c < '0' || c > '9')
                    throw new NumberFormatException("digit expected " + (char) c
                            + " found");
                res *= 10;
                res += c - '0';
                c = read();
            }
            if (c == '.') {
                c = read();
                double m = 1;
                while (!isSpaceChar(c)) {
                    if (c == 'e' || c == 'E')
                        return res * Math.pow(10, nextInt());
                    if (c < '0' || c > '9')
                        throw new UnknownError();
                    m /= 10;
                    res += (c - '0') * m;
                    c = read();
                }
            }
            return res * sgn;
        }

        public String readLine() {
            try {
                return super.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return null;
        }

    }

    static class FastPrinter extends PrintWriter {
        public FastPrinter(Writer writer) {
            super(writer);
        }

        public FastPrinter(OutputStream out) {
            super(out);
        }

        public void close() {
            super.close();
        }

    }

    static class MathUtils<T> {
        public static final double EPS = 1e-9;

        public static final double abs(double value) {
            return value >= 0 ? value : -value;
        }

        public static final boolean equals(double a, double b) {
            return abs(a - b) < EPS;
        }

    }
}
