import java.io.*;
import java.util.*;

public class FTask {
    private static final String QUICK_ANSWER = "NO";
    private final MyReader in;
    private final StringBuilder out;
    private final int n;
    private final int m;
    private final int k;
    private final int q;
    private final Graph g;
    private final int[] a;
    private final int[] b;
    private final long[] res;
    private HashSet<Integer>[] qs;
    private int[] root;
    private long[] weight;

    public FTask(BufferedReader in, StringBuilder out) {
        this.in = new MyReader(in);
        this.out = out;
        n = nextInt();
        m = nextInt();
        k = nextInt();
        q = nextInt();
        g = Graph.builder().setN(n).setM(m).setWithWeights(true).build(this.in);
        a = new int[q];
        b = new int[q];
        res = new long[q];
        for (int i = 0; i < q; i++) {
            a[i] = nextInt() - 1;
            b[i] = nextInt() - 1;
        }
    }

    int getRoot(int i) {
        int curr = i;
        while (root[curr] != curr) curr = root[curr];
        while (i != curr) {
            int tmp = i;
            i = root[i];
            root[tmp] = curr;
        }
        return curr;
    }

    void union(int n1, int n2, long level) {
        n1 = getRoot(n1);
        n2 = getRoot(n2);
        if (n1 == n2) return;
        if (qs[n1] == null) {
            root[n1] = n2;
            return;
        }
        if (qs[n2] == null) {
            root[n2] = n1;
            return;
        }
        if(qs[n1].size() < qs[n2].size()) {
            union(n2, n1, level);
            return;
        }

        for(int i : qs[n2]){
            int other = getRoot(a[i]) == n2 ? getRoot(b[i]) : getRoot(a[i]);
            if(other == n1) {
                res[i] = level;
                qs[n1].remove(i);
            } else {
                qs[n1].add(i);
            }
        }
        qs[n2] = null;
        root[n2] = n1;
    }

    public void solve() throws QuickAnswer {
        long[] d = getDist();
        weight = new long[g.edgeFrom.length];
        for (int i = 0; i < g.edgeFrom.length; i++) {
            weight[i] = g.edgeWeight[i] + d[g.edgeFrom[i]] + d[g.edgeTo[i]];
        }
        Integer[] order = new Integer[g.edgeFrom.length];
        for (int i = 0; i < order.length; i++) {
            order[i] = i;
        }
        Arrays.sort(order, Comparator.comparingLong(i -> weight[i]));
        qs = new HashSet[g.n];
        root = new int[g.n];
        for (int i = 0; i < g.n; i++) {
            root[i] = i;
        }
        for (int i = 0; i < q; i++) {
            if (qs[a[i]] == null) qs[a[i]] = new HashSet<>();
            qs[a[i]].add(i);
            if (qs[b[i]] == null) qs[b[i]] = new HashSet<>();
            qs[b[i]].add(i);
        }
        for (int pos : order) {
            union(g.edgeFrom[pos], g.edgeTo[pos], weight[pos]);
        }
        for (long i : res) {
            println(i);
        }
    }

    long[] getDist() {
        long[] res = new long[n];
        Arrays.fill(res, -1);
        PriorityQueue<Long> queue = new PriorityQueue<>();
        long N = n;
        for (int i = 0; i < k; i++) {
            queue.add((long) i);
        }
        while (!queue.isEmpty()) {
            Long key = queue.poll();
            int node = (int) (key % N);
            if (res[node] >= 0) continue;
            long dist = key / N;
            res[node] = dist;
            int[] neighbors = g.neighbors[node];
            int[] pathWeight = g.pathWeights[node];
            for (int i = 0; i < neighbors.length; i++) {
                int neighbor = neighbors[i];
                if (res[neighbor] >= 0) continue;
                queue.add((dist + pathWeight[i]) * N + neighbor);
            }
        }
        return res;
    }


    // Common functions

    static class MyReader{
        private final BufferedReader in;
        private StringTokenizer tokenizer;

        public MyReader(BufferedReader in) {
            this.in = in;
            try {
                tokenizer = new StringTokenizer(in.readLine());
            } catch (IOException e) {
            }
        }

        String nextToken(){
            try {
                while (!tokenizer.hasMoreTokens()) tokenizer = new StringTokenizer(in.readLine());
            } catch (Exception e){

            }
            return tokenizer.nextToken();
        }

        int nextInt(){
            return Integer.parseInt(nextToken());
        }
        long nextLong(){
            return Long.parseLong(nextToken());
        }
        String nextLine() {
            try {
                return in.readLine();
            } catch (IOException e) {
                return "";
            }
        }


    }

    void quickAnswer(String answer) throws QuickAnswer {
        throw new QuickAnswer(answer);
    }

    void quickAnswer() throws QuickAnswer {
        quickAnswer(QUICK_ANSWER);
    }


    static class QuickAnswer extends Exception {
        private String answer;

        public QuickAnswer(String answer) {
            this.answer = answer;
        }
    }

    void print(Object... args) {
        String prefix = "";
        for (Object arg : args) {
            out.append(prefix);
            out.append(arg);
            prefix = " ";
        }
    }

    void println(Object... args) {
        print(args);
        out.append("\n");
    }

    void printsp(Object... args) {
        print(args);
        out.append(" ");
    }

    int nextInt() {
        return in.nextInt();
    }

    long nextLong() {
        return in.nextLong();
    }

    String nextString() {
        return in.nextLine();
    }

    int[] nextInts(int count) {
        int[] res = new int[count];
        for (int i = 0; i < count; ++i) {
            res[i] = nextInt();
        }
        return res;
    }

    int[][] nextInts(int count, int n) {
        int[][] res = new int[n][count];
        for (int i = 0; i < count; ++i) {
            for (int j = 0; j < n; j++) {
                res[j][i] = nextInt();
            }
        }
        return res;
    }

    long[] nextLongs(int count) {
        long[] res = new long[count];
        for (int i = 0; i < count; ++i) {
            res[i] = nextLong();
        }
        return res;
    }

    long[][] nextLongs(int count, int n) {
        long[][] res = new long[n][count];
        for (int i = 0; i < count; ++i) {
            for (int j = 0; j < n; j++) {
                res[j][i] = nextLong();
            }
        }
        return res;
    }

    public static void main(String[] args) {
        doMain(System.in, System.out);
    }

    static void doMain(InputStream inStream, PrintStream outStream) {
        BufferedReader in = new BufferedReader(new InputStreamReader(inStream));
        StringBuilder totalOut = new StringBuilder();
        int count = 1;
        //count = in.nextInt();
        while (count-- > 0) {
            try {
                StringBuilder out = new StringBuilder();
                new FTask(in, out).solve();
                totalOut.append(out.toString());
            } catch (QuickAnswer e) {
                totalOut.append(e.answer);
            }
            if (count > 0) {
                totalOut.append("\n");
            }
        }
        outStream.print(totalOut.toString());
    }

    static class Graph {
        final int n;
        final int[][] neighbors;
        final int[][] pathWeights;
        final int[] color;
        final int[] edgeFrom;
        final int[] edgeTo;
        final int[] edgeWeight;

        static Builder builder() {
            return new Builder();
        }

        static class Builder {
            int adjustIndex = -1;
            boolean withWeights = false;
            int n = -1;
            int m = -1;

            Builder setAdjustIndex(int adjustIndex) {
                this.adjustIndex = adjustIndex;
                return this;
            }

            Builder setWithWeights(boolean withWeights) {
                this.withWeights = withWeights;
                return this;
            }

            Builder setN(int n) {
                this.n = n;
                return this;
            }

            Builder setM(int m) {
                this.m = m;
                return this;
            }

            Graph build(MyReader in) {
                return new Graph(
                        in,
                        n == -1 ? in.nextInt() : n,
                        m == -1 ? in.nextInt() : m,
                        adjustIndex,
                        withWeights);
            }
        }

        Graph(MyReader in, int n, int m, int adjustIndex, boolean withWeights) {
            this.n = n;
            this.color = new int[n];
            int[] cnt = new int[n];
            edgeFrom = new int[m];
            edgeTo = new int[m];
            edgeWeight = new int[m];
            for (int i = 0; i < m; ++i) {
                int x = in.nextInt() + adjustIndex;
                int y = in.nextInt() + adjustIndex;
                edgeFrom[i] = x;
                edgeTo[i] = y;
                edgeWeight[i] = withWeights ? in.nextInt() : 1;
                cnt[x]++;
                cnt[y]++;
            }
            this.neighbors = new int[n][];
            this.pathWeights = new int[n][];
            for (int i = 0; i < n; i++) {
                neighbors[i] = new int[cnt[i]];
                pathWeights[i] = new int[cnt[i]];
            }
            for (int i = 0; i < m; ++i) {
                int from = edgeFrom[i];
                int to = edgeTo[i];
                neighbors[from][--cnt[from]] = to;
                pathWeights[from][cnt[from]] = edgeWeight[i];
                neighbors[to][--cnt[to]] = from;
                pathWeights[to][cnt[to]] = edgeWeight[i];
            }
        }
    }
}

