import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.Comparator;
import java.util.Collections;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        CNearestVectors solver = new CNearestVectors();
        solver.solve(1, in, out);
        out.close();
    }

    static class CNearestVectors {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            ArrayList<Point> up = new ArrayList<>();
            ArrayList<Point> lw = new ArrayList<>();
            Point ref = new Point(1, 0);
            for (int i = 0; i < n; i++) {
                Point P = new Point(in.nextInt(), in.nextInt());
                P.ind = i + 1;
                long cr = ref.cross(P);
                long dt = ref.dot(P);
                if (cr == 0 && dt >= 0) {
                    up.add(P);
                } else if (cr == 0 && dt < 0) {
                    lw.add(P);
                } else if (cr > 0) {
                    up.add(P);
                } else if (cr < 0) {
                    lw.add(P);
                }
            }
            Collections.sort(up, new Comparator<Point>() {

                public int compare(Point o1, Point o2) {
                    return o2.ccw(o1);
                }
            });
            Collections.sort(lw, new Comparator<Point>() {

                public int compare(Point o1, Point o2) {
                    return o2.ccw(o1);
                }
            });
            ArrayList<Point> All = new ArrayList<>();
            for (Point ele : up) {
                All.add(ele);
            }
            for (Point ele : lw) {
                All.add(ele);
            }

            int i1 = 0;
            int i2 = 1;
            BigInteger mina = BigInteger.valueOf(-100);
            BigInteger minb = BigInteger.valueOf(1);
            for (int i = 0; i < n; i++) {

                BigInteger x1 = (BigInteger.valueOf(All.get(i).x));
                BigInteger y1 = BigInteger.valueOf(All.get(i).y);
                BigInteger x2 = BigInteger.valueOf(All.get((i + 1) % n).x);
                BigInteger y2 = BigInteger.valueOf(All.get((i + 1) % n).y);
                BigInteger dot = x1.multiply(x2).add(y1.multiply(y2));
                int s = (dot.compareTo(BigInteger.valueOf(0)) < 0) ? -1 : 1;
                BigInteger numer = dot.multiply(dot).multiply(BigInteger.valueOf(s));
                BigInteger denom = BigInteger.valueOf(All.get((i + 1) % n).abs()).multiply(BigInteger.valueOf(All.get(i).abs()));

                if (comp(numer, denom, mina, minb)) {
                    mina = numer;
                    minb = denom;
                    i2 = All.get((i + 1) % n).ind;
                    i1 = All.get(i).ind;
                }
            }

            out.println(i1 + " " + i2);
        }

        boolean comp(BigInteger a1, BigInteger b1, BigInteger a2, BigInteger b2) {
            return (a1.multiply(b2).subtract(a2.multiply(b1)).compareTo((BigInteger.valueOf(0))) > 0);
        }

        class Point {
            long x;
            long y;
            int ind;

            Point(long x1, long y1) {
                x = x1;
                y = y1;
            }

            long dot(Point a) {
                return x * a.x + y * a.y;
            }

            long cross(Point a) {
                return x * a.y - y * a.x;
            }

            long abs() {
                return dot(this);
            }

            int ccw(Point a) {
                return (int) Math.signum(cross(a));
            }

        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int read() {
            if (numChars == -1)
                throw new InputMismatchException();
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public int nextInt() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        private boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

    }
}

