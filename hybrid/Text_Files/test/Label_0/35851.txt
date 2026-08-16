// package arc.arc101;

import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.*;

public class Main {
    static long __startTime = System.currentTimeMillis();

    static int INF = 1000000010;
    static int MOD = 1000000007;

    public static void main(String[] args) {
        InputReader in = new InputReader(System.in);
        PrintWriter out = new PrintWriter(System.out);

        int n = in.nextInt();
        int m = in.nextInt();

        int[] robots = new int[n];
        for (int i = 0; i < n ; i++) {
            robots[i] = in.nextInt();
        }
        TreeSet<Integer> holes = new TreeSet<>();
        for (int i = 0; i < m ; i++) {
            holes.add(in.nextInt());
        }
        holes.add(INF);
        holes.add(-INF);

        List<int[]> ranges = new ArrayList<>();
        for (int i = 0; i < n ; i++) {
            int L = holes.lower(robots[i]);
            int R = holes.higher(robots[i]);
            if (L == -INF || R == INF) {
                continue;
            }
            int dl = Math.abs(L - robots[i]);
            int dr = Math.abs(R - robots[i]);
            ranges.add(new int[]{dl, dr});
        }
        n = ranges.size();

        Collections.sort(ranges, (u, v) -> u[0] == v[0] ? v[1] - u[1] : u[0] - v[0]);
        int[][] wn = new int[ranges.size()][2];
        for (int i = 0; i < n ; i++) {
            wn[i] = ranges.get(i);
        }
        out.println(ways(wn));
        out.flush();
    }

    private static long ways(int[][] d) {
        Set<Integer> yset = new HashSet<>();
        for (int i = 0; i < d.length ; i++) {
            yset.add(d[i][1]);
        }
        yset.add(0);
        List<Integer> y = new ArrayList<>(yset);
        Collections.sort(y);
        Map<Integer,Integer> ymap = new HashMap<>();
        for (int i = 0; i < y.size() ; i++) {
            ymap.put(y.get(i), i);
        }
        for (int i = 0; i < d.length ; i++) {
            d[i][1] = ymap.get(d[i][1]);
        }


        int n = d.length;
        FenwickTree bit = new FenwickTree(n+10);

        long total = 0;
        for (int i = 0; i < n ; ) {
            int j = i;
            while (j < n && d[j][0] == d[i][0]) {
                j++;
            }
            int last = n+10;
            for (int k = i ; k < j ; k++) {
                if (last != d[k][1]) {
                    long add = bit.range(1, d[k][1]) + 1;
                    total += add;
                    bit.add(d[k][1]+1, add);
                    last = d[k][1];
                }
            }
            total %= MOD;
            i = j;
        }
        return (total + 1) % MOD;
    }


    public static class FenwickTree {
        long N;
        long[] data;

        public FenwickTree(int n) {
            N = n;
            data = new long[n + 1];
        }

        /**
         * Computes value of [1, i].
         * <p>
         * O(logn)
         *
         * @param i
         * @return
         */
        public long sum(int i) {
            long s = 0;
            while (i > 0) {
                s += data[i];
                i -= i & (-i);
            }
            return s % MOD;
        }

        /**
         * Computes value of [i, j].
         * <p>
         * O(logn)
         *
         * @param i
         * @param j
         * @return
         */
        public long range(int i, int j) {
            return (sum(j) - sum(i - 1) + MOD) % MOD;
        }

        /**
         * Sets value x into i-th position.
         * <p>
         * O(logn)
         *
         * @param i
         * @param x
         */
        public void set(int i, long x) {
            add(i, x - range(i, i));
        }

        /**
         * Adds value x into i-th position.
         * <p>
         * O(logn)
         *
         * @param i
         * @param x
         */
        public void add(int i, long x) {
            x %= MOD;
            while (i <= N) {
                data[i] += x;
                data[i] %= MOD;
                i += i & (-i);
            }
        }
    }

    private static void printTime(String label) {
        debug(label, System.currentTimeMillis() - __startTime);
    }

    private static void debug(Object... o) {
        System.err.println(Arrays.deepToString(o));
    }

    public static class InputReader {
        private static final int BUFFER_LENGTH = 1 << 12;
        private InputStream stream;
        private byte[] buf = new byte[BUFFER_LENGTH];
        private int curChar;
        private int numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        private int next() {
            if (numChars == -1) {
                throw new InputMismatchException();
            }
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

        public char nextChar() {
            return (char) skipWhileSpace();
        }

        public String nextToken() {
            int c = skipWhileSpace();
            StringBuilder res = new StringBuilder();
            do {
                res.append((char) c);
                c = next();
            } while (!isSpaceChar(c));
            return res.toString();
        }

        public int nextInt() {
            return (int) nextLong();
        }

        public long nextLong() {
            int c = skipWhileSpace();
            long sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = next();
            }
            long res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = next();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public double nextDouble() {
            return Double.valueOf(nextToken());
        }

        int skipWhileSpace() {
            int c = next();
            while (isSpaceChar(c)) {
                c = next();
            }
            return c;
        }

        boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }
    }
}