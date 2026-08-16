import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.List;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.Reader;
import java.io.InputStreamReader;
import java.io.InputStream;
import java.util.ArrayList;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        MyInput in = new MyInput(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskE solver = new TaskE();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskE {
        final int mod = (int) 1e9 + 7;

        public void solve(int testNumber, MyInput in, PrintWriter out) {
            int n = in.nextInt();
            Graph g = new Graph(n);
            for (int i = 0; i < n - 1; i++) {
                int x = in.nextInt() - 1;
                int y = in.nextInt() - 1;
                g.addEdge(x, y, 0, i);
                g.addEdge(y, x, 0, i);
            }
            Tree t = g.dfsTree(0);
            int[] order = t.inversedDfsOrder();
            long[][] dp = new long[n][];
            for (int v : order) {
                long[] cur = new long[2];
                cur[1] = 1;
                for (Edge e : t.edges(v)) {
                    long[] next = new long[cur.length + dp[e.to].length - 1];
                    for (int x = 0; x < cur.length; x++) {
                        for (int y = 0; y < dp[e.to].length; y++) {
                            // 頂点vを含む連結成分がx+y個のときの場合の数
                            next[x + y] = (next[x + y] + cur[x] * dp[e.to][y]) % mod;
                        }
                    }
                    cur = next;
                }
                long c = 1;
                for (int i = 2; i < cur.length; i += 2) {
                    c = c * (i - 1) % mod;
                    cur[0] = (cur[0] - c * cur[i] % mod + mod) % mod;
                }
                dp[v] = cur;
            }
            out.println((mod - dp[0][0]) % mod);
        }

        class Edge {
            public final int edgeId;
            public final int to;
            public long cost;

            public Edge(int to, long cost, int edgeId) {
                this.to = to;
                this.cost = cost;
                this.edgeId = edgeId;
            }


            public String toString() {
                return String.format("[Edge id=%d, to=%d, cost=%d]", edgeId, to, cost);
            }

        }

        class Vertex {
            public final int id;
            public final List<Edge> edges = new ArrayList<>();

            public Vertex(final int id) {
                this.id = id;
            }

            public void addEdge(Edge e) {
                edges.add(e);
            }

        }

        class Tree {
            int V;
            int root;
            Vertex[] vertex;
            int[] dfsOrder;

            public Tree(int V, int root) {
                this.V = V;
                this.root = root;
                vertex = new Vertex[V];
                for (int i = 0; i < V; i++) vertex[i] = new Vertex(i);
            }

            public void addEdge(int s, Edge e) {
                vertex[s].addEdge(e);
            }

            public List<Edge> edges(int v) {
                return vertex[v].edges;
            }

            public int[] dfsOrder() {
                if (dfsOrder == null) {
                    dfsOrder = new int[V];
                    int[] st = new int[V];
                    int sp = 0, len = 0;
                    boolean[] vis = new boolean[V];

                    vis[root] = true;
                    st[sp++] = root;
                    while (sp > 0) {
                        int v = st[--sp];
                        dfsOrder[len++] = v;
                        for (Edge e : vertex[v].edges)
                            if (!vis[e.to]) {
                                vis[e.to] = true;
                                st[sp++] = e.to;
                            }
                    }
                }
                return dfsOrder;
            }

            public int[] inversedDfsOrder() {
                return TaskE.ArrayAlgorithms.reverse(dfsOrder());
            }

        }

        class Graph {
            int V;
            int E;
            Vertex[] vertex;

            public Graph(int V) {
                this.V = V;
                this.E = 0;
                vertex = new Vertex[V];
                for (int i = 0; i < V; i++) vertex[i] = new Vertex(i);
            }

            public void addEdge(int s, int t, long c, int edgeId) {
                vertex[s].addEdge(new Edge(t, c, edgeId));
            }

            public Tree dfsTree(int r) {
                Tree tree = new Tree(V, r);
                int[] st = new int[V];
                int sp = 0;
                boolean[] vis = new boolean[V];

                vis[r] = true;
                st[sp++] = r;
                while (sp > 0) {
                    int v = st[--sp];
                    for (Edge e : vertex[v].edges)
                        if (!vis[e.to]) {
                            vis[e.to] = true;
                            st[sp++] = e.to;
                            tree.addEdge(v, e);
                        }
                }
                return tree;
            }

        }

        static class ArrayAlgorithms {
            public static int[] reverse(int[] ary) {
                int V = ary.length;
                for (int i = 0; i < V / 2; i++) {
                    int t = ary[i];
                    ary[i] = ary[V - 1 - i];
                    ary[V - 1 - i] = t;
                }
                return ary;
            }

        }

    }

    static class MyInput {
        private final BufferedReader in;
        private static int pos;
        private static int readLen;
        private static final char[] buffer = new char[1024 * 8];
        private static char[] str = new char[500 * 8 * 2];
        private static boolean[] isDigit = new boolean[256];
        private static boolean[] isSpace = new boolean[256];
        private static boolean[] isLineSep = new boolean[256];

        static {
            for (int i = 0; i < 10; i++) {
                isDigit['0' + i] = true;
            }
            isDigit['-'] = true;
            isSpace[' '] = isSpace['\r'] = isSpace['\n'] = isSpace['\t'] = true;
            isLineSep['\r'] = isLineSep['\n'] = true;
        }

        public MyInput(InputStream is) {
            in = new BufferedReader(new InputStreamReader(is));
        }

        public int read() {
            if (pos >= readLen) {
                pos = 0;
                try {
                    readLen = in.read(buffer);
                } catch (IOException e) {
                    throw new RuntimeException();
                }
                if (readLen <= 0) {
                    throw new MyInput.EndOfFileRuntimeException();
                }
            }
            return buffer[pos++];
        }

        public int nextInt() {
            int len = 0;
            str[len++] = nextChar();
            len = reads(len, isSpace);
            int i = 0;
            int ret = 0;
            if (str[0] == '-') {
                i = 1;
            }
            for (; i < len; i++) ret = ret * 10 + str[i] - '0';
            if (str[0] == '-') {
                ret = -ret;
            }
            return ret;
        }

        public char nextChar() {
            while (true) {
                final int c = read();
                if (!isSpace[c]) {
                    return (char) c;
                }
            }
        }

        int reads(int len, boolean[] accept) {
            try {
                while (true) {
                    final int c = read();
                    if (accept[c]) {
                        break;
                    }
                    if (str.length == len) {
                        char[] rep = new char[str.length * 3 / 2];
                        System.arraycopy(str, 0, rep, 0, str.length);
                        str = rep;
                    }
                    str[len++] = (char) c;
                }
            } catch (MyInput.EndOfFileRuntimeException e) {
            }
            return len;
        }

        static class EndOfFileRuntimeException extends RuntimeException {
        }

    }
}

