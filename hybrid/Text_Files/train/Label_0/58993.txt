import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Pradyumn Agrawal coderbond007
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastReader in = new FastReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        HashMap<String, Integer> hm = new HashMap<>();
        ArrayList<Pair> result = new ArrayList<>();
        ArrayList<ArrayList<Integer>> g = new ArrayList<>();
        boolean[] was;

        public void solve(int testNumber, FastReader in, PrintWriter out) {
            int n = in.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = getId(in.next().toLowerCase());
            }
            int t = in.nextInt();
            for (int i = 0; i < t; i++) {
                int s = getId(in.next().toLowerCase());
                int toId = getId(in.next().toLowerCase());
                g.get(toId).add(s);
            }
            Pair2[] all = new Pair2[hm.size()];
            for (int i = 0; i < hm.size(); i++) {
                all[i] = new Pair2(i, result.get(i));
            }
            Arrays.sort(all);
            was = new boolean[hm.size()];
            for (int i = 0; i < all.length; i++) {
                go(all[i].pos, all[i].p);
            }

            long resLen = 0;
            int cntR = 0;
            for (int i = 0; i < n; i++) {
                Pair another = result.get(a[i]);
                resLen += another.y;
                cntR += another.x;
            }
            out.println(cntR + " " + resLen);
        }

        Pair gen(String s) {
            Pair p = new Pair(0, s.length());
            for (int i = 0; i < s.length(); i++)
                if (s.charAt(i) == 'r') {
                    p.x++;
                }
            return p;
        }

        int getId(String s) {
            Integer x = hm.get(s);
            if (x != null)
                return x;
            hm.put(s, hm.size());
            result.add(gen(s));
            g.add(new ArrayList<Integer>());
            return hm.size() - 1;
        }

        void go(int v, Pair p) {
            if (was[v])
                return;
            was[v] = true;
            result.set(v, p);
            for (int to : g.get(v)) {
                go(to, p);
            }
        }

        class Pair implements Comparable<Pair> {
            int x;
            int y;

            public Pair(int x, int y) {
                super();
                this.x = x;
                this.y = y;
            }


            public int compareTo(Pair o) {
                if (x != o.x)
                    return Integer.compare(x, o.x);
                return Integer.compare(y, o.y);
            }


            public String toString() {
                return "Pair [x=" + x + ", y=" + y + "]";
            }

        }

        class Pair2 implements Comparable<Pair2> {
            int pos;
            Pair p;

            public Pair2(int pos, Pair p) {
                super();
                this.pos = pos;
                this.p = p;
            }


            public int compareTo(Pair2 o) {
                return p.compareTo(o.p);
            }


            public String toString() {
                return "Pair2 [pos=" + pos + ", p=" + p + "]";
            }

        }

    }

    static class FastReader {
        private InputStream stream;
        private byte[] buf = new byte[8192];
        private int curChar;
        private int pnumChars;
        private FastReader.SpaceCharFilter filter;

        public FastReader(InputStream stream) {
            this.stream = stream;
        }

        private int pread() {
            if (pnumChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= pnumChars) {
                curChar = 0;
                try {
                    pnumChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (pnumChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }

        public String next() {
            return nextString();
        }

        public int nextInt() {
            int c = pread();
            while (isSpaceChar(c))
                c = pread();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = pread();
            }
            int res = 0;
            do {
                if (c == ',') {
                    c = pread();
                }
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = pread();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public String nextString() {
            int c = pread();
            while (isSpaceChar(c))
                c = pread();
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = pread();
            } while (!isSpaceChar(c));
            return res.toString();
        }

        private boolean isSpaceChar(int c) {
            if (filter != null) {
                return filter.isSpaceChar(c);
            }
            return isWhitespace(c);
        }

        private static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        private interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);

        }

    }
}

