import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Objects;
import java.util.stream.Collectors;

public class Main {
    static final class Edge {
        final int src;
        final int dest;
        final long weight;
        Edge(int src, int dest, long weight) {
            if (src < 0 || dest < 0) {
                throw new IllegalArgumentException();
            }
            this.src = src;
            this.dest = dest;
            this.weight = weight;
        }
        Edge reverse() {
            return new Edge(dest, src, weight);
        }
        static List<Edge> newEdges(int[] oneBasedSrc,
                                   int[] oneBasedDest,
                                   int[] weight,
                                   boolean directedGraph) {
            if (oneBasedSrc.length != oneBasedDest.length
                || (weight != null && oneBasedSrc.length != weight.length)) {
                throw new IllegalArgumentException();
            }
            List<Edge> result = new ArrayList<>(oneBasedSrc.length
                                                * (directedGraph ? 1 : 2));
            for (int i = 0; i < oneBasedDest.length; i++) {
                Edge e = new Edge(oneBasedSrc[i] - 1,
                                  oneBasedDest[i] - 1,
                                  weight == null ? 1 : weight[i]);
                result.add(e);
                if (!directedGraph) {
                    result.add(e.reverse());
                }
            }
            return result;
        }
        @Override
        public int hashCode() {
            return Objects.hash(dest, src, weight);
        }
        @Override
        public boolean equals(Object obj) {
            if (this == obj) {
                return true;
            }
            if (obj == null) {
                return false;
            }
            if (!(obj instanceof Edge)) {
                return false;
            }
            Edge other = (Edge)obj;
            return dest == other.dest
                   && src == other.src
                   && weight == other.weight;
        }
        @Override
        public String toString() {
            return "Edge [src="
                   + src
                   + ", dest="
                   + dest
                   + ", weight="
                   + weight
                   + "]";
        }
    }
    static final class WarshallFloyd {
        static final class Result {
            private final long[][] distance;
            private final int[][] next;
            private Result(long[][] distance, int[][] next) {
                this.distance = distance;
                this.next = next;
            }
            long distance(int src, int dest) {
                return distance[src][dest];
            }
            int next(int src, int dest) {
                return next[src][dest];
            }
            List<Integer> path(int src, int dest) {
                List<Integer> path = new ArrayList<>();
                path.add(src);
                for (int n = next(src, dest); n != -1; n = next(n, dest)) {
                    path.add(n);
                }
                return path;
            }
        }
        private static boolean isShorterPath(long[][] distance,
                                             int k,
                                             int i,
                                             int j) {
            return distance[i][k] != Long.MAX_VALUE
                   && distance[k][j] != Long.MAX_VALUE
                   && distance[i][j] > distance[i][k] + distance[k][j];
        }
        static Result exec(int vertexNumber, List<Edge> edges) {
            int n = vertexNumber;
            long[][] distance = new long[n][n];
            int[][] next = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    distance[i][j] = i == j ? 0 : Long.MAX_VALUE;
                    next[i][j] = -1;
                }
            }
            for (Edge edge : edges) {
                distance[edge.src][edge.dest] = edge.weight;
                next[edge.src][edge.dest] = edge.dest;
            }
            for (int k = 0; k < n; k++) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (isShorterPath(distance, k, i, j)) {
                            distance[i][j] = distance[i][k] + distance[k][j];
                            next[i][j] = next[i][k];
                        }
                    }
                }
            }
            return new Result(distance, next);
        }
    }
    static void solve(MyScanner in, MyWriter out) {
        int n = in.nextInt();
        int m = in.nextInt();
        int l = in.nextInt();
        int[] a = new int[m];
        int[] b = new int[m];
        int[] c = new int[m];
        in.nextVerticalIntArrays(a, b, c);
        List<Edge> edges = Edge.newEdges(a, b, c, false)
                               .stream()
                               .filter(e -> e.weight <= l)
                               .collect(Collectors.toList());
        WarshallFloyd.Result r = WarshallFloyd.exec(n, edges);
        List<Edge> oneWeightEdges = new ArrayList<>();
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (r.distance(i, j) <= l) {
                    Edge e = new Edge(i, j, 1);
                    oneWeightEdges.add(e);
                    oneWeightEdges.add(e.reverse());
                }
            }
        }
        WarshallFloyd.Result ans = WarshallFloyd.exec(n, oneWeightEdges);
        int q = in.nextInt();
        for (int i = 0; i < q; i++) {
            int s = in.nextInt() - 1;
            int t = in.nextInt() - 1;
            long dist = ans.distance(s, t);
            if (dist == Long.MAX_VALUE) {
                out.println(-1);
            } else {
                out.println(dist - 1);
            }
        }
    }

    public static void main(String[] args) {
        MyWriter w = new MyWriter(System.out);
        solve(new MyScanner(System.in), w);
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
        private static boolean isPrintableCharExceptSpace(int c) {
            return 33 <= c && c <= 126;
        }
        String next() {
            int c = readByte();
            while (!(c == -1 || isPrintableCharExceptSpace(c))) {
                c = readByte();
            }
            if (c == -1) {
                throw new NoSuchElementException();
            }
            StringBuilder b = new StringBuilder();
            do {
                b.appendCodePoint(c);
                c = readByte();
            } while (c != -1 && isPrintableCharExceptSpace(c));
            return b.toString();
        }
        long nextLong() {
            int c = readByte();
            while (!(c == -1 || isPrintableCharExceptSpace(c))) {
                c = readByte();
            }
            if (c == -1) {
                throw new NoSuchElementException();
            }
            boolean minus = false;
            if (c == '-') {
                minus = true;
                c = readByte();
            }
            long result = 0L;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                result = result * 10L + (c - '0');
                c = readByte();
            } while (c != -1 && isPrintableCharExceptSpace(c));
            return minus ? -result : result;
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
        private static boolean allSameLength(int[] a, int[] b, int[]... c) {
            if (a.length != b.length) {
                return false;
            }
            for (int[] element : c) {
                if (a.length != element.length) {
                    return false;
                }
            }
            return true;
        }
        private static boolean allSameLength(char[] a, char[] b, char[]... c) {
            if (a.length != b.length) {
                return false;
            }
            for (char[] element : c) {
                if (a.length != element.length) {
                    return false;
                }
            }
            return true;
        }
        void nextVerticalIntArrays(int[] a, int[] b, int[]... c) {
            if (!allSameLength(a, b, c)) {
                throw new IllegalArgumentException();
            }
            for (int i = 0; i < a.length; i++) {
                a[i] = nextInt();
                b[i] = nextInt();
                for (int[] d : c) {
                    d[i] = nextInt();
                }
            }
        }
        long[] nextLongArray(int n) {
            long[] result = new long[n];
            for (int i = 0; i < n; i++) {
                result[i] = nextLong();
            }
            return result;
        }
        char nextChar() {
            int c = readByte();
            while (!(c == -1 || isPrintableCharExceptSpace(c))) {
                c = readByte();
            }
            if (c == -1) {
                throw new NoSuchElementException();
            }
            return (char)c;
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
        void nextVerticalCharArrays(char[] a, char[] b, char[]... c) {
            if (!allSameLength(a, b, c)) {
                throw new IllegalArgumentException();
            }
            for (int i = 0; i < a.length; i++) {
                a[i] = nextChar();
                b[i] = nextChar();
                for (char[] d : c) {
                    d[i] = nextChar();
                }
            }
        }
    }
    static final class MyWriter extends PrintWriter {
        MyWriter(OutputStream out) {
            super(out);
        }
        void joinAndPrintln(int[] x) {
            joinAndPrintln(x, " ");
        }
        void joinAndPrintln(int[] x, String delimiter) {
            StringBuilder b = new StringBuilder();
            if (x.length > 0) {
                b.append(x[0]);
                for (int i = 1; i < x.length; i++) {
                    b.append(delimiter).append(x[i]);
                }
            }
            println(b.toString());
        }
        void joinAndPrintln(long[] x) {
            joinAndPrintln(x, " ");
        }
        void joinAndPrintln(long[] x, String delimiter) {
            StringBuilder b = new StringBuilder();
            if (x.length > 0) {
                b.append(x[0]);
                for (int i = 1; i < x.length; i++) {
                    b.append(delimiter).append(x[i]);
                }
            }
            println(b.toString());
        }
        void joinAndPrintln(Iterable<?> iterable) {
            joinAndPrintln(iterable, " ");
        }
        void joinAndPrintln(Iterable<?> iterable, String delimiter) {
            StringBuilder b = new StringBuilder();
            for (Iterator<?> i = iterable.iterator(); i.hasNext();) {
                b.append(i.next());
                while (i.hasNext()) {
                    b.append(delimiter).append(i.next());
                }
            }
            println(b.toString());
        }
    }
}
