import java.io.*;
import java.util.*;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.IntFunction;

public class Main {

    static int N, D;
    static int[] A;

    public static void main(String[] args) {
        FastScanner sc = new FastScanner(System.in);
        N = sc.nextInt();
        D = sc.nextInt();
        A = sc.nextIntArray(N);

        System.out.println(solve());
    }

    static City INF = new City(-1, Long.MAX_VALUE);

    static long solve() {
        // 解説のやりかた
        // 各都市の左右一つを選んでクラスカル法
        BinaryOperator<City> merge = (a, b) -> a.cost < b.cost ? a : b;
        RangeGetObj<City> lseg = new RangeGetObj<>(N, INF, merge, City[]::new);
        for (int i = 0; i < N; i++) {
            long cost = (long)D * (N-i-1) + A[i];
            lseg.update(i, new City(i, cost));
        }
        RangeGetObj<City> rseg = new RangeGetObj<>(N, INF, merge, City[]::new);
        for (int i = 0; i < N; i++) {
            long cost = (long)D * i + A[i];
            rseg.update(i, new City(i, cost));
        }

        PriorityQueue<Road> q = new PriorityQueue<>(Comparator.comparingLong(r -> r.cost));

        // Aが大きいもの順に実行
        //   Aより小さいもの、という制限がついている
        int[][] B = new int[N][2];
        for (int i = 0; i < N; i++) {
            B[i][0] = i;
            B[i][1] = A[i];
        }
        Arrays.sort(B, Comparator.comparingInt(b -> -b[1]));
        for (int bi = 0; bi < N; bi++) {
            int i = B[bi][0];
            int a = B[bi][1];

            City lc = lseg.query(0, i);
            if( lc != INF ) {
                q.add( new Road(i, lc.i, cost(i, lc.i)) );
            }
            City rc = rseg.query(i+1, N);
            if( rc != INF ) {
                q.add( new Road(i, rc.i, cost(i, rc.i)) );
            }

            lseg.update(i, INF);
            rseg.update(i, INF);
        }

        UnionFind uf = new UnionFind(N);

        int cnt = 0;
        long ans = 0;
        while(true) {
            Road road = q.poll();
            if( !uf.isSame(road.from, road.to) ) {
                uf.unite(road.from, road.to);
                ans += road.cost;
                cnt++;

                if( cnt == N-1 ) {
                    break;
                }
            }
        }
        return ans;
    }

    static long cost(int a, int b) {
        return (long)A[a] + A[b] + (long)Math.abs(a-b) * D;
    }

    static class City {
        int i;
        long cost;

        public City(int i, long cost) {
            this.i = i;
            this.cost = cost;
        }

        public String toString() {
            return "City(" + i + ", " + cost + ")";
        }
    }

    static class Road {
        int from, to;
        long cost;

        public Road(int from, int to, long cost) {
            this.from = from;
            this.to = to;
            this.cost = cost;
        }
    }

    static class RangeGetObj<A> {

        int size;
        A[] tree;
        A identity;
        BinaryOperator<A> merge;

        RangeGetObj(int size, A identity, BinaryOperator<A> merge, IntFunction<A[]> mkArr) {
            this.size = 1;
            while( this.size < size ) this.size *= 2;
            this.tree = mkArr.apply(this.size*2);
            this.identity = identity;
            this.merge = merge;
            Arrays.fill(tree, identity);
        }

        void update(int idx, A a) {
            idx += size;
            tree[idx] = a;

            while(idx > 0) {
                idx /= 2;
                tree[idx] = merge.apply(tree[idx*2], tree[idx*2+1]);
            }
        }

        // [from, to)
        A query(int from, int to) {
            return _query(from, to, 1, 0, size);
        }

        private A _query(int from, int to, int idx, int l, int r) {
            if (r <= from || to <= l) return identity;

            if (from <= l && r <= to) {
                return tree[idx];

            } else {
                int mid = (l+r)/2;
                A vl = _query(from, to, idx*2, l, mid);
                A vr = _query(from, to, idx*2+1, mid, r);
                return merge.apply(vl, vr);
            }
        }

        A get(int idx) {
            return tree[idx+size];
        }
    }

    static class UnionFind {

        private final int[] parent;
        private final int[] rank;

        public UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }

        public int root(int i) {
            if( parent[i] == i ) {
                return i;
            } else {
                return parent[i] = root(parent[i]);
            }
        }

        public int unite(int i, int j) {
            int ri = root(i);
            int rj = root(j);
            if( ri == rj ) return ri;

            if( rank[ri] < rank[rj] ) {
                parent[ri] = rj;
                return rj;

            } else {
                parent[rj] = ri;
                if( rank[ri] == rank[rj] ) {
                    rank[ri]++;
                }
                return ri;
            }
        }

        public boolean isSame(int a, int b) {
            return root(a) == root(b);
        }
    }

    @SuppressWarnings("unused")
    static class FastScanner {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

        FastScanner(InputStream in) {
            reader = new BufferedReader(new InputStreamReader(in));
            tokenizer = null;
        }

        String next() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        String nextLine() {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    return reader.readLine();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken("\n");
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        int[] nextIntArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt();
            return a;
        }

        int[] nextIntArray(int n, int delta) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt() + delta;
            return a;
        }

        long[] nextLongArray(int n) {
            long[] a = new long[n];
            for (int i = 0; i < n; i++)
                a[i] = nextLong();
            return a;
        }
    }

    static <A> void writeLines(A[] as, Function<A, String> f) {
        PrintWriter pw = new PrintWriter(System.out);
        for (A a : as) {
            pw.println(f.apply(a));
        }
        pw.flush();
    }

    static void writeLines(int[] as) {
        PrintWriter pw = new PrintWriter(System.out);
        for (int a : as) pw.println(a);
        pw.flush();
    }

    static void writeLines(long[] as) {
        PrintWriter pw = new PrintWriter(System.out);
        for (long a : as) pw.println(a);
        pw.flush();
    }

    static int max(int... as) {
        int max = Integer.MIN_VALUE;
        for (int a : as) max = Math.max(a, max);
        return max;
    }

    static int min(int... as) {
        int min = Integer.MAX_VALUE;
        for (int a : as) min = Math.min(a, min);
        return min;
    }

    static void debug(Object... args) {
        StringJoiner j = new StringJoiner(" ");
        for (Object arg : args) {
            if (arg instanceof int[]) j.add(Arrays.toString((int[]) arg));
            else if (arg instanceof long[]) j.add(Arrays.toString((long[]) arg));
            else if (arg instanceof double[]) j.add(Arrays.toString((double[]) arg));
            else if (arg instanceof Object[]) j.add(Arrays.toString((Object[]) arg));
            else j.add(arg.toString());
        }
        System.err.println(j.toString());
    }
}
