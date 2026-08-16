import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.stream.IntStream;
import java.util.function.IntPredicate;
import java.util.TreeSet;
import java.util.ArrayList;
import java.util.AbstractCollection;
import java.io.OutputStreamWriter;
import java.io.OutputStream;
import java.io.IOException;
import java.io.UncheckedIOException;
import java.util.List;
import java.util.stream.Stream;
import java.io.Closeable;
import java.io.Writer;
import java.util.Comparator;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) throws Exception {
        Thread thread = new Thread(null, new TaskAdapter(), "", 1 << 29);
        thread.start();
        thread.join();
    }

    static class TaskAdapter implements Runnable {
        @Override
        public void run() {
            InputStream inputStream = System.in;
            OutputStream outputStream = System.out;
            FastInput in = new FastInput(inputStream);
            FastOutput out = new FastOutput(outputStream);
            DChoosingSubtreeIsFun solver = new DChoosingSubtreeIsFun();
            solver.solve(1, in, out);
            out.close();
        }
    }

    static class DChoosingSubtreeIsFun {
        public void solve(int testNumber, FastInput in, FastOutput out) {
            int n = in.ri();
            int k = in.ri();
            List<UndirectedEdge>[] g = Graph.createGraph(n);
            for (int i = 0; i < n - 1; i++) {
                Graph.addUndirectedEdge(g, in.ri() - 1, in.ri() - 1);
            }
            MinSpanningGraphOnTree msg = new MinSpanningGraphOnTree(n);
            msg.init(g);
            int[] r = new int[n];
            for (int i = 0; i < n; i++) {
                r[i] = i > 0 ? r[i - 1] : -1;
                while (r[i] + 1 < n && msg.minSpanningGraph() <= k) {
                    r[i]++;
                    msg.add(r[i]);
                }
                if (msg.minSpanningGraph() <= k) {
                    r[i] = n;
                }
                msg.remove(i);
            }
            int ans = 0;
            for (int i = 0; i < n; i++) {
                ans = Math.max(ans, r[i] - i);
            }
            out.println(ans);
        }

    }

    static class Log2 {
        public static int floorLog(int x) {
            if (x <= 0) {
                throw new IllegalArgumentException();
            }
            return 31 - Integer.numberOfLeadingZeros(x);
        }

    }

    static class LcaOnTree {
        int[] parent;
        int[] preOrder;
        int[] i;
        int[] head;
        int[] a;
        int time;

        void dfs1(List<? extends DirectedEdge>[] tree, int u, int p) {
            parent[u] = p;
            i[u] = preOrder[u] = time++;
            for (DirectedEdge e : tree[u]) {
                int v = e.to;
                if (v == p) continue;
                dfs1(tree, v, u);
                if (Integer.lowestOneBit(i[u]) < Integer.lowestOneBit(i[v])) {
                    i[u] = i[v];
                }
            }
            head[i[u]] = u;
        }

        void dfs2(List<? extends DirectedEdge>[] tree, int u, int p, int up) {
            a[u] = up | Integer.lowestOneBit(i[u]);
            for (DirectedEdge e : tree[u]) {
                int v = e.to;
                if (v == p) continue;
                dfs2(tree, v, u, a[u]);
            }
        }

        public void init(List<? extends DirectedEdge>[] tree, int root) {
            init(tree, i -> i == root);
        }

        public void init(List<? extends DirectedEdge>[] tree, IntPredicate isRoot) {
            time = 0;
            for (int i = 0; i < tree.length; i++) {
                if (isRoot.test(i)) {
                    dfs1(tree, i, -1);
                    dfs2(tree, i, -1, 0);
                }
            }
        }

        public LcaOnTree(int n) {
            preOrder = new int[n];
            i = new int[n];
            head = new int[n];
            a = new int[n];
            parent = new int[n];
        }

        public LcaOnTree(List<? extends DirectedEdge>[] tree, IntPredicate isRoot) {
            this(tree.length);
            init(tree, isRoot);
        }

        public LcaOnTree(List<? extends DirectedEdge>[] tree, int root) {
            this(tree, i -> i == root);
        }

        private int enterIntoStrip(int x, int hz) {
            if (Integer.lowestOneBit(i[x]) == hz)
                return x;
            int hw = 1 << Log2.floorLog(a[x] & (hz - 1));
            return parent[head[i[x] & -hw | hw]];
        }

        public int lca(int x, int y) {
            int hb = i[x] == i[y] ? Integer.lowestOneBit(i[x]) : (1 << Log2.floorLog(i[x] ^ i[y]));
            int hz = Integer.lowestOneBit(a[x] & a[y] & -hb);
            int ex = enterIntoStrip(x, hz);
            int ey = enterIntoStrip(y, hz);
            return preOrder[ex] < preOrder[ey] ? ex : ey;
        }

    }

    static class Graph {
        public static UndirectedEdge addUndirectedEdge(List<UndirectedEdge>[] g, int s, int t) {
            UndirectedEdge toT = new UndirectedEdge(t);
            UndirectedEdge toS = new UndirectedEdge(s);
            toT.rev = toS;
            toS.rev = toT;
            g[s].add(toT);
            g[t].add(toS);
            return toT;
        }

        public static List[] createGraph(int n) {
            return IntStream.range(0, n).mapToObj(i -> new ArrayList<>()).toArray(i -> new List[i]);
        }

    }

    static class UndirectedEdge extends DirectedEdge {
        public UndirectedEdge rev;

        public UndirectedEdge(int to) {
            super(to);
        }

        public String toString() {
            return String.format("%d<->%d", Math.min(rev.to, to), Math.max(rev.to, to));
        }

    }

    static class MinSpanningGraphOnTree {
        private List<? extends DirectedEdge>[] g;
        private int[] depth;
        private LcaOnTree lca;
        private int[] index2dfn;
        private int[] dfn2index;
        private int order;
        private TreeSet<Integer> S = new TreeSet<>(Comparator.comparingInt(x -> index2dfn[x]));
        private int size;

        void dfs(int root, int p) {
            index2dfn[root] = order++;
            dfn2index[index2dfn[root]] = root;
            depth[root] = p == -1 ? 0 : depth[p] + 1;
            for (DirectedEdge e : g[root]) {
                if (e.to == p) {
                    continue;
                }
                dfs(e.to, root);
            }
        }

        public int dist(int a, int b) {
            int c = lca.lca(a, b);
            return depth[a] + depth[b] - depth[c] * 2;
        }

        public MinSpanningGraphOnTree(int n) {
            depth = new int[n];
            index2dfn = new int[n];
            dfn2index = new int[n];
            lca = new LcaOnTree(n);
        }

        public void init(List<? extends DirectedEdge>[] g) {
            this.g = g;
            lca.init(g, 0);
            order = 0;
            dfs(0, -1);
            clear();
        }

        public void clear() {
            S.clear();
            size = 0;
        }

        public void add(int v) {
            assert !S.contains(v);
            Integer floor = S.floor(v);
            Integer ceil = S.ceiling(v);
            if (floor != null) {
                size += dist(floor, v);
            }
            if (ceil != null) {
                size += dist(ceil, v);
            }
            if (floor != null && ceil != null) {
                size -= dist(floor, ceil);
            }
            S.add(v);
        }

        public void remove(int v) {
            assert S.contains(v);
            S.remove(v);
            Integer floor = S.floor(v);
            Integer ceil = S.ceiling(v);
            if (floor != null) {
                size -= dist(floor, v);
            }
            if (ceil != null) {
                size -= dist(ceil, v);
            }
            if (floor != null && ceil != null) {
                size += dist(floor, ceil);
            }
        }

        public int size() {
            return S.size();
        }

        public int minSpanningGraph() {
            if (size() == 0) {
                return 0;
            }
            int ans = size + dist(S.first(), S.last());
            assert ans % 2 == 0;
            return ans / 2 + 1;
        }

        public String toString() {
            return S.toString() + "=" + minSpanningGraph();
        }

    }

    static class FastOutput implements AutoCloseable, Closeable, Appendable {
        private static final int THRESHOLD = 32 << 10;
        private final Writer os;
        private StringBuilder cache = new StringBuilder(THRESHOLD * 2);

        public FastOutput append(CharSequence csq) {
            cache.append(csq);
            return this;
        }

        public FastOutput append(CharSequence csq, int start, int end) {
            cache.append(csq, start, end);
            return this;
        }

        private void afterWrite() {
            if (cache.length() < THRESHOLD) {
                return;
            }
            flush();
        }

        public FastOutput(Writer os) {
            this.os = os;
        }

        public FastOutput(OutputStream os) {
            this(new OutputStreamWriter(os));
        }

        public FastOutput append(char c) {
            cache.append(c);
            afterWrite();
            return this;
        }

        public FastOutput append(int c) {
            cache.append(c);
            afterWrite();
            return this;
        }

        public FastOutput println(int c) {
            return append(c).println();
        }

        public FastOutput println() {
            return append('\n');
        }

        public FastOutput flush() {
            try {
//            boolean success = false;
//            if (stringBuilderValueField != null) {
//                try {
//                    char[] value = (char[]) stringBuilderValueField.get(cache);
//                    os.write(value, 0, cache.length());
//                    success = true;
//                } catch (Exception e) {
//                }
//            }
//            if (!success) {
                os.append(cache);
//            }
                os.flush();
                cache.setLength(0);
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
            return this;
        }

        public void close() {
            flush();
            try {
                os.close();
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        }

        public String toString() {
            return cache.toString();
        }

    }

    static class DirectedEdge {
        public int to;

        public DirectedEdge(int to) {
            this.to = to;
        }

        public String toString() {
            return "->" + to;
        }

    }

    static class FastInput {
        private final InputStream is;
        private byte[] buf = new byte[1 << 13];
        private int bufLen;
        private int bufOffset;
        private int next;

        public FastInput(InputStream is) {
            this.is = is;
        }

        private int read() {
            while (bufLen == bufOffset) {
                bufOffset = 0;
                try {
                    bufLen = is.read(buf);
                } catch (IOException e) {
                    bufLen = -1;
                }
                if (bufLen == -1) {
                    return -1;
                }
            }
            return buf[bufOffset++];
        }

        public void skipBlank() {
            while (next >= 0 && next <= 32) {
                next = read();
            }
        }

        public int ri() {
            return readInt();
        }

        public int readInt() {
            int sign = 1;

            skipBlank();
            if (next == '+' || next == '-') {
                sign = next == '+' ? 1 : -1;
                next = read();
            }

            int val = 0;
            if (sign == 1) {
                while (next >= '0' && next <= '9') {
                    val = val * 10 + next - '0';
                    next = read();
                }
            } else {
                while (next >= '0' && next <= '9') {
                    val = val * 10 - next + '0';
                    next = read();
                }
            }

            return val;
        }

    }
}

