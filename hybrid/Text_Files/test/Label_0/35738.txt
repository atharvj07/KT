import java.awt.Point;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.NavigableSet;
import java.util.NoSuchElementException;
import java.util.TreeSet;

public class Main {
    int LINE = -1;
    int UNDONE = 0;
    int DONE = 1;
    int[] dx = {-1, 0, 1, 0};
    int[] dy = {0, -1, 0, 1};
    void solve(MyScanner in, MyWriter out) {
        int n = in.nextInt();
        int m = in.nextInt();
        long[][] abc = in.nextVerticalLongArrays(3, n);
        long[] a = abc[0];
        long[] b = abc[1];
        long[] c = abc[2];
        long[][] def = in.nextVerticalLongArrays(3, m);
        long[] d = def[0];
        long[] e = def[1];
        long[] f = def[2];

        var xSet = new TreeSet<Long>();
        var ySet = new TreeSet<Long>();
        xSet.add(0L);
        ySet.add(0L);
        for (int i = 0; i < n; i++) {
            xSet.add(a[i]);
            xSet.add(b[i]);
            ySet.add(c[i]);
        }
        for (int i = 0; i < m; i++) {
            xSet.add(d[i]);
            ySet.add(e[i]);
            ySet.add(f[i]);
        }
        var x = new Compress(xSet);
        var y = new Compress(ySet);
        var map = new int[xSet.size() * 2][ySet.size() * 2];
        for (int i = 0; i < n; i++) {
            int from = x.indexOf(a[i]) * 2;
            int to = x.indexOf(b[i]) * 2;
            int cIndex = y.indexOf(c[i]) * 2;
            for (int j = from; j <= to; j++) {
                map[j][cIndex] = LINE;
            }
        }
        for (int i = 0; i < m; i++) {
            int dIndex = x.indexOf(d[i]) * 2;
            int from = y.indexOf(e[i]) * 2;
            int to = y.indexOf(f[i]) * 2;
            for (int j = from; j <= to; j++) {
                map[dIndex][j] = LINE;
            }
        }
        var queue = new ArrayDeque<Point>();
        int zeroX = x.indexOf(0) * 2;
        int zeroY = y.indexOf(0) * 2;
        queue.offer(new Point(zeroX, zeroY));
        map[zeroX][zeroY] = DONE;
        while (!queue.isEmpty()) {
            Point p = queue.poll();
            for (int i = 0; i < dx.length; i++) {
                int nextX = p.x + dx[i];
                int nextY = p.y + dy[i];
                if (nextX < 0 || nextX >= map.length)
                    continue;
                if (nextY < 0 || nextY >= map[0].length)
                    continue;
                if (map[nextX][nextY] != UNDONE)
                    continue;
                map[nextX][nextY] = DONE;
                queue.offer(new Point(nextX, nextY));
            }
        }
        long answer = 0;
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                if (map[i][j] != DONE)
                    continue;
                if (i == 0
                    || i == map.length - 1
                    || j == 0
                    || j == map[i].length - 1) {
                    out.println("INF");
                    return;
                }
                if (i % 2 == 0 || j % 2 == 0)
                    continue;
                long xLength = x.valueOf(i / 2 + 1) - x.valueOf(i / 2);
                long yLength = y.valueOf(j / 2 + 1) - y.valueOf(j / 2);
                answer += xLength * yLength;
            }
        }
        out.println(answer);
    }
    static final class Compress {
        final Map<Long, Integer> valueToIndex;
        final List<Long> indexToValue;
        Compress(NavigableSet<Long> values) {
            valueToIndex = new HashMap<>(values.size());
            indexToValue = new ArrayList<>(values.size());
            Iterator<Long> iterator = values.iterator();
            for (int i = 0; iterator.hasNext(); i++) {
                long value = iterator.next();
                valueToIndex.put(value, i);
                indexToValue.add(value);
            }
        }
        int indexOf(long value) {
            return valueToIndex.get(value);
        }
        long valueOf(int index) {
            return indexToValue.get(index);
        }
    }
    public static void main(String[] args) {
        MyWriter w = new MyWriter(System.out);
        new Main().solve(new MyScanner(System.in), w);
        w.flush();
    }
    static final class MyScanner {
        static final int BUFFER_SIZE = 8192;
        private final InputStream in;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int point;
        private int readLength;

        MyScanner(InputStream in) {
            this.in = in;
        }
        private int readByte() {
            if (point < readLength) {
                int result = buffer[point];
                point += 1;
                return result;
            }
            try {
                readLength = in.read(buffer);
            } catch (IOException e) {
                throw new AssertionError(null, e);
            }
            if (readLength == -1) {
                return -1;
            }
            point = 1;
            return buffer[0];
        }
        private static boolean isVisibleChar(int c) {
            return 33 <= c && c <= 126;
        }
        char nextChar() {
            int c = readByte();
            while (!(c == -1 || isVisibleChar(c))) {
                c = readByte();
            }
            if (c == -1) {
                throw new NoSuchElementException();
            }
            return (char)c;
        }
        String next() {
            return next(16);
        }
        String next(int n) {
            int c = readByte();
            while (!(c == -1 || isVisibleChar(c))) {
                c = readByte();
            }
            if (c == -1) {
                throw new NoSuchElementException();
            }
            StringBuilder b = new StringBuilder(n);
            do {
                b.append((char)c);
                c = readByte();
            } while (c != -1 && isVisibleChar(c));
            return b.toString();
        }
        long nextLong() {
            int c = readByte();
            while (!(c == -1 || isVisibleChar(c))) {
                c = readByte();
            }
            if (c == -1) {
                throw new NoSuchElementException();
            }
            boolean minus = false;
            long limit = -Long.MAX_VALUE;
            if (c == '-') {
                minus = true;
                limit = Long.MIN_VALUE;
                c = readByte();
            }
            long n = 0L;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                if (n < limit / 10L) {
                    throw new InputMismatchException();
                }
                n *= 10L;
                int digit = c - '0';
                if (n < limit + digit) {
                    throw new InputMismatchException();
                }
                n -= digit;
                c = readByte();
            } while (c != -1 && isVisibleChar(c));
            return minus ? n : -n;
        }
        int nextInt() {
            long n = nextLong();
            if (n < Integer.MIN_VALUE || n > Integer.MAX_VALUE) {
                throw new InputMismatchException();
            }
            return (int)n;
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        int[] nextIntArray(int n) {
            int[] result = new int[n];
            for (int i = 0; i < n; i++) {
                result[i] = nextInt();
            }
            return result;
        }
        long[] nextLongArray(int n) {
            long[] result = new long[n];
            for (int i = 0; i < n; i++) {
                result[i] = nextLong();
            }
            return result;
        }
        char[] nextCharArray(int n) {
            char[] result = new char[n];
            for (int i = 0; i < n; i++) {
                result[i] = nextChar();
            }
            return result;
        }
        char[][] next2dCharArray(int n, int m) {
            char[][] result = new char[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    result[i][j] = nextChar();
                }
            }
            return result;
        }
        int[][] nextVerticalIntArrays(int arrayCount, int arrayLength) {
            int[][] result = new int[arrayCount][arrayLength];
            for (int i = 0; i < arrayLength; i++) {
                for (int j = 0; j < arrayCount; j++) {
                    result[j][i] = nextInt();
                }
            }
            return result;
        }
        long[][] nextVerticalLongArrays(int arrayCount, int arrayLength) {
            long[][] result = new long[arrayCount][arrayLength];
            for (int i = 0; i < arrayLength; i++) {
                for (int j = 0; j < arrayCount; j++) {
                    result[j][i] = nextLong();
                }
            }
            return result;
        }
        char[][] nextVerticalCharArrays(int arrayCount, int arrayLength) {
            char[][] result = new char[arrayCount][arrayLength];
            for (int i = 0; i < arrayLength; i++) {
                for (int j = 0; j < arrayCount; j++) {
                    result[j][i] = nextChar();
                }
            }
            return result;
        }
    }
    static final class MyWriter extends PrintWriter {
        MyWriter(OutputStream out) {
            super(out);
        }
        void println(int[] x) {
            println(x, " ");
        }
        void println(int[] x, String delimiter) {
            if (x.length > 0) {
                print(x[0]);
                for (int i = 1; i < x.length; i++) {
                    print(delimiter);
                    print(x[i]);
                }
            }
            println();
        }
        void println(long[] x) {
            println(x, " ");
        }
        void println(long[] x, String delimiter) {
            if (x.length > 0) {
                print(x[0]);
                for (int i = 1; i < x.length; i++) {
                    print(delimiter);
                    print(x[i]);
                }
            }
            println();
        }
        void println(Iterable<?> iterable) {
            println(iterable, " ");
        }
        void println(Iterable<?> iterable, String delimiter) {
            Iterator<?> i = iterable.iterator();
            if (i.hasNext()) {
                print(i.next());
                while (i.hasNext()) {
                    print(delimiter);
                    print(i.next());
                }
            }
            println();
        }
        void printLines(int[] x) {
            println(x, System.lineSeparator());
        }
        void printLines(long[] x) {
            println(x, System.lineSeparator());
        }
        void printLines(Iterable<?> iterable) {
            println(iterable, System.lineSeparator());
        }
    }
}
