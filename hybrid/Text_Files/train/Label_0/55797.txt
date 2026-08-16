import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.lang.reflect.Array;
import java.util.function.BiFunction;
import java.util.function.Supplier;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.Map;
import java.util.function.IntFunction;
import java.io.PrintWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Nikita Mikhailov
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        EKompaniya solver = new EKompaniya();
        solver.solve(1, in, out);
        out.close();
    }

    static class EKompaniya {
        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            int n = in.readInt();
            int q = in.readInt();

            TreeGraph tree = new TreeGraph(n);
            for (int i = 1; i < n; i++) {
                tree.addEdgeBi(i, in.readInt() - 1);
            }

            TreeLcm lcm = new TreeLcm(tree, 0);

            IRmq<IntPair> segForFirst = new SegmentTree<>(n, Utils::minObj);
            IRmq<IntPair> segForLast = new SegmentTree<>(n, Utils::maxObj);

            int[] depth = lcm.depth;
            int[] firstInOrder = lcm.first;


            for (int i = 0; i < n; i++) {
                segForFirst.set(i, new IntPair(firstInOrder[i], i));
                segForLast.set(i, new IntPair(firstInOrder[i], i));
            }

            for (int i = 0; i < q; i++) {
                int from = in.readInt() - 1;
                int to = in.readInt() - 1;

                if (to - from == 1) {
                    if (depth[from] >= depth[to]) {
                        out.println((to + 1) + " " + depth[from]);
                    } else {
                        out.println((from + 1) + " " + depth[to]);
                    }

                    continue;
                }

                IntPair first = segForFirst.get(from, to);
                IntPair last = segForLast.get(from, to);

                // remove 1
                segForFirst.set(first.y(), new IntPair(Integer.MAX_VALUE, first.y()));
                segForLast.set(last.y(), new IntPair(0, last.y()));


                IntPair firstWithoutFirst = segForFirst.get(from, to);
                IntPair lastWithoutLast = segForLast.get(from, to);

                segForFirst.set(first.y(), first);
                segForLast.set(last.y(), last);


                int lcm1 = lcm.getLcm(firstWithoutFirst.y(), last.y());
                int lcm2 = lcm.getLcm(first.y(), lastWithoutLast.y());

                if (depth[lcm1] >= depth[lcm2]) {
                    out.println((first.y() + 1) + " " + depth[lcm1]);
                } else {
                    out.println((last.y() + 1) + " " + depth[lcm2]);
                }
            }
        }

    }

    static final class Utils {
        private Utils() {
        }

        public static <T extends Comparable<T>> T maxObj(T a, T b) {
            return a.compareTo(b) < 0 ? b : a;
        }

        public static <T extends Comparable<T>> T minObj(T a, T b) {
            return a.compareTo(b) <= 0 ? a : b;
        }

        public static <T> T[] makeArrayInd(int n, IntFunction<T> creator) {
            if (n > 0) {
                T first = creator.apply(0);
                T[] res = (T[]) Array.newInstance(first.getClass(), n);
                res[0] = first;

                for (int i = 1; i < n; i++) {
                    res[i] = creator.apply(i);
                }

                return res;
            } else {
                return null;
            }
        }

        public static <T> T[] makeArray(int n, Supplier<T> creator) {
            return makeArrayInd(n, value -> creator.get());
        }

    }

    static class GraphDfs {
        private TreeGraph graph;
        private Map<Class, GraphDfs.DfsMetric> metrics;

        public GraphDfs(TreeGraph graph, int startNode, GraphDfs.DfsMetric... requiredMetrics) {

            this.metrics = Stream.of(requiredMetrics).collect(Collectors.toMap(Object::getClass, o -> o));

            this.graph = graph;

            metrics.values().forEach(dfsMetric -> dfsMetric.init(graph.n));

            this.dfs(startNode, -1);
        }

        private void dfs(int node, int from) {
            metrics.values().forEach(dfsMetric -> dfsMetric.onEnter(node, from, true));


            for (int target : graph.edges[node]) {
                if (target != from) {
                    dfs(target, node);
                    metrics.values().forEach(dfsMetric -> dfsMetric.onEnter(node, target, false));
                }
            }

            metrics.values().forEach(dfsMetric -> dfsMetric.onLeave(node, from));
        }

        public <T extends GraphDfs.DfsMetric> T metric(Class<T> c) {
            return (T) metrics.get(c);
        }

        public ArrayList<Integer> order() {
            return metric(GraphDfs.OrderMetric.class).order;
        }

        public int[] depth() {
            return metric(GraphDfs.DepthMetric.class).depth;
        }

        public interface DfsMetric {
            void init(int size);

            void onEnter(int node, int from, boolean firstTime);

            void onLeave(int node, int to);

        }

        public static class DepthMetric implements GraphDfs.DfsMetric {
            public int[] depth;

            public void init(int size) {
                depth = new int[size];
                Arrays.fill(depth, -1);
            }

            public void onEnter(int node, int from, boolean firstTime) {
                if (firstTime) {
                    depth[node] = from == -1 ? 0 : depth[from] + 1;
                }
            }

            public void onLeave(int node, int to) {
            }

        }

        public static class OrderMetric implements GraphDfs.DfsMetric {
            public ArrayList<Integer> order;

            public void init(int size) {
                order = new ArrayList<>(size * 2);
            }

            public void onEnter(int node, int from, boolean firstTime) {
                order.add(node);
            }

            public void onLeave(int node, int to) {
            }

        }

    }

    static class Pair<K, V> {
        private final K key;
        private final V value;

        public Pair(K k, V v) {
            key = k;
            value = v;
        }

        public Pair(Pair<? extends K, ? extends V> entry) {
            this(entry.getKey(), entry.getValue());
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }

        public K getFirst() {
            return key;
        }

        public V getSecond() {
            return value;
        }

        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (!(o instanceof Pair)) {
                return false;
            } else {
                Pair<?, ?> oP = (Pair<?, ?>) o;
                return (key == null ?
                        oP.key == null :
                        key.equals(oP.key)) &&
                        (value == null ?
                                oP.value == null :
                                value.equals(oP.value));
            }
        }

        public int hashCode() {
            int result = key == null ? 0 : key.hashCode();

            final int h = value == null ? 0 : value.hashCode();
            result = 37 * result + h ^ (h >>> 16);

            return result;
        }

        public String toString() {
            return "[" + getKey() + ", " + getValue() + "]";
        }

    }

    static class SegmentTree<T> implements IRmq<T> {
        private Object[] arr;
        private int n;
        private BiFunction<T, T, T> ops;
        private boolean hadQueries = false;

        public SegmentTree(int size, BiFunction<T, T, T> ops) {
            this.ops = ops;
            int len = 1;
            while (len < size) {
                len *= 2;
            }
            this.n = len;

            arr = new Object[2 * n + 1];
        }

        private T refreshTree(int pos) {
            if (pos >= n) {
                return (T) arr[pos];
            }

            T sum = doSum(refreshTree(pos * 2), refreshTree(pos * 2 + 1));
            arr[pos] = sum;
            return sum;
        }

        public void set(int pos, T value) {
            pos += n;
            arr[pos] = value;

            // Don't refresh tree yet
            if (!hadQueries) {
                return;
            }

            pos /= 2;

            while (pos >= 1) {
                arr[pos] = doSum((T) arr[2 * pos], (T) arr[2 * pos + 1]);
                pos /= 2;
            }
        }

        public T get(int from, int to) {
            if (!hadQueries) {
                hadQueries = true;
                refreshTree(1);
            }
            return get(1, 0, n - 1, from, to);
        }

        private T doSum(T a, T b) {
            if (a == null) {
                return b;
            }
            if (b == null) {
                return a;
            }
            return ops.apply(a, b);
        }

        private T get(int subTreeRoot, int subTreeFrom, int subTreeTo, int from, int to) {
            if (from == subTreeFrom && to == subTreeTo)
                return (T) arr[subTreeRoot];

            int middle = (subTreeFrom + subTreeTo) / 2;

            if (to <= middle) {
                return get(subTreeRoot * 2, subTreeFrom, middle, from, to);
            }

            if (from > middle) {
                return get(subTreeRoot * 2 + 1, middle + 1, subTreeTo, from, to);
            }

            T leftSum = get(subTreeRoot * 2, subTreeFrom, middle, from, middle);
            T rightSum = get(subTreeRoot * 2 + 1, middle + 1, subTreeTo, middle + 1, to);

            return ops.apply(leftSum, rightSum);
        }

    }

    static class TreeGraph {
        protected int n;
        protected ArrayList<Integer>[] edges;

        public TreeGraph(int n) {
            this.n = n;
            this.edges = Utils.makeArray(n, ArrayList::new);
        }

        public void addEdge(int from, int to) {
            edges[from].add(to);
        }

        public void addEdgeBi(int a, int b) {
            addEdge(a, b);
            addEdge(b, a);
        }

    }

    static class IntPair extends Pair<Integer, Integer> implements Comparable<IntPair> {
        public IntPair(Integer integer, Integer integer2) {
            super(integer, integer2);
        }

        public IntPair(Pair<? extends Integer, ? extends Integer> entry) {
            super(entry);
        }

        public Integer x() {
            return getFirst();
        }

        public Integer y() {
            return getSecond();
        }

        public int compareTo(IntPair o) {
            if (x().equals(o.x())) {
                return y().compareTo(o.y());
            }
            return x().compareTo(o.x());
        }

    }

    static interface IRmq<T> {
        void set(int index, T value);

        T get(int from, int to);

    }

    static class FastScanner {
        private StringTokenizer st;
        private BufferedReader in;

        public FastScanner(final InputStream in) {
            this.in = new BufferedReader(new InputStreamReader(in));
        }

        public String readToken() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(in.readLine());
                } catch (final IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        public int readInt() {
            return Integer.parseInt(readToken());
        }

    }

    static class TreeLcm {
        private TreeGraph graph;
        private int root;
        private SegmentTree<IntPair> seg;
        public int[] first;
        public int[] depth;
        public ArrayList<Integer> order;

        public TreeLcm(TreeGraph graph, int root) {
            this.graph = graph;
            this.root = root;

            this.lcm();
        }

        private void lcm() {
            GraphDfs dfs = new GraphDfs(graph, root, new GraphDfs.OrderMetric(), new GraphDfs.DepthMetric());

            depth = dfs.depth();
            order = dfs.order();

            first = new int[graph.n];
            Arrays.fill(first, -1);

            for (int i = 0; i < order.size(); i++) {
                int node = order.get(i);

                if (first[node] == -1) {
                    first[node] = i;
                }
            }

            seg = new SegmentTree<>(order.size(), Utils::minObj);

            for (int i = 0; i < order.size(); i++) {
                seg.set(i, new IntPair(depth[order.get(i)], order.get(i)));
            }
        }

        public int getLcm(int a, int b) {
            int from = Math.min(first[a], first[b]);
            int to = Math.max(first[a], first[b]);

            return seg.get(from, to).y();
        }

    }
}

