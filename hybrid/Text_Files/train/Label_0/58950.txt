import java.awt.Point;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.InputMismatchException;

public class R227_2_D {
    static ArrayList<Integer>[] graph;
    static int[] right, left;
    static boolean vis[];

    public static boolean dfs(int node) {
        if (vis[node])
            return false;
        vis[node] = true;
        for (int i = 0; i < graph[node].size(); i++) {
            int tmp = graph[node].get(i);
            if (right[tmp] == -1) {
                left[node] = tmp;
                right[tmp] = node;
                return true;
            }
        }
        for (int i = 0; i < graph[node].size(); i++) {
            int tmp = graph[node].get(i);
            if (dfs(right[tmp])) {
                left[node] = tmp;
                right[tmp] = node;
                return true;
            }
        }
        return false;
    }

    public static int getMaxMatch() {
        Arrays.fill(left, -1);
        Arrays.fill(right, -1);
        boolean done = false;
        while (!done) {
            done = true;
            Arrays.fill(vis, false);
            for (int i = 0; i < graph.length; i++) {
                if (left[i] == -1 && dfs(i)) {
                    done = false;
                }
            }
        }
        int res = 0;
        for (int i = 0; i < left.length; i++) {
            res += (left[i] != -1 ? 1 : 0);
        }
        return res;
    }

    public static void main(String[] args) {
        InputReader in = new InputReader(System.in);
        PrintWriter out = new PrintWriter(System.out);
        int V = in.readInt();
        int E = in.readInt();
        Point[] edges = new Point[E];
        for (int i = 0; i < edges.length; i++) {
            edges[i] = new Point(in.readInt() - 1, in.readInt() - 1);
        }
        int best = Integer.MAX_VALUE;
        for (int k = 0; k < V; k++) {
            int n = V - 1;
            graph = new ArrayList[n];
            left = new int[n];
            vis = new boolean[n];
            right = new int[n];
            for (int i = 0; i < graph.length; i++) {
                graph[i] = new ArrayList<Integer>();
            }
            int center = 0;
            for (int i = 0; i < E; i++) {
                if (edges[i].x == k || edges[i].y == k) {
                    center++;
                    continue;
                }
                int src = edges[i].x > k ? edges[i].x - 1 : edges[i].x;
                int dst = edges[i].y > k ? edges[i].y - 1 : edges[i].y;
                graph[src].add(dst);
            }
            int matching = getMaxMatch();
            int addToCenterEdges = 2 * V - 1 - center;
            int removed = E - center - matching;
            int added = n - matching;
            best = Math.min(best, added + removed + addToCenterEdges);
        }
        System.out.println(best);
    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1000];
        private int curChar, numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        private int read() {
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

        public int readInt() {
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

        public long readLong() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            long res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public String readString() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            StringBuffer res = new StringBuffer();
            do {
                res.appendCodePoint(c);
                c = read();
            } while (!isSpaceChar(c));
            return res.toString();
        }

        private boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        private String readLine0() {
            StringBuffer buf = new StringBuffer();
            int c = read();
            while (c != '\n' && c != -1) {
                buf.appendCodePoint(c);
                c = read();
            }
            return buf.toString();
        }

        public String readLine() {
            String s = readLine0();
            while (s.trim().length() == 0)
                s = readLine0();
            return s;
        }

        public String readLine(boolean ignoreEmptyLines) {
            if (ignoreEmptyLines)
                return readLine();
            else
                return readLine0();
        }

        public char readCharacter() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            return (char) c;
        }

        public double readDouble() {
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
                    return res * Math.pow(10, readInt());
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            }
            if (c == '.') {
                c = read();
                double m = 1;
                while (!isSpaceChar(c)) {
                    if (c == 'e' || c == 'E')
                        return res * Math.pow(10, readInt());
                    if (c < '0' || c > '9')
                        throw new InputMismatchException();
                    m /= 10;
                    res += (c - '0') * m;
                    c = read();
                }
            }
            return res * sgn;
        }
    }
}
