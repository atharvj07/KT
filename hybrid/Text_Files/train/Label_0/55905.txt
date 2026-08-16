import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;


public class R017B {
    public void debug(Object... objects) { System.err.println(Arrays.deepToString(objects)); }
    public static final int INF = 987654321;
    public static final long LINF = 987654321987654321L;
    public static final double EPS = 1e-9;
    
    class Kruskal {
        int n;
        Node[] vs;
        List<Edge> es;
        int edge;
        int weight;
        boolean[] isAlreadySurbodinate;
        Kruskal(int n) {
            this.n = n;
            vs = new Node[n];
            for (int i = 0; i < n; i++) { vs[i] = new Node(i); }
            es = new ArrayList<Edge>();
            isAlreadySurbodinate = new boolean[n];
        }
        void addEdge(int from, int to, int weight, boolean isUndirected) { 
            es.add(new Edge(vs[from], vs[to], weight));
            if(isUndirected) { es.add(new Edge(vs[to], vs[from], weight)); } 
        }
        /**
         * Kruskalのアルゴリズム(重みの小さい辺から貪欲に取る)により
         * 無向グラフのMST(Minimum Spanning Tree: 最小全域木)をつくり、連結グラフが作れたかどうかを返す。
         * 実行後、クラスの
         * edgeに使った枝の本数
         * weightに使った枝の重みの合計
         * が入る。
         * @return 連結グラフが作れたかどうか。
         */
        boolean mst() {
            init();
            UnionFind uf = new UnionFind(n);
            for (Edge e : es) {
                if (!uf.same(e.from.id, e.to.id) && q[e.from.id] > q[e.to.id] && !isAlreadySurbodinate[e.to.id]) {
                    isAlreadySurbodinate[e.to.id] = true;
                    uf.unite(e.from.id, e.to.id);
                    e.from.es.add(e);
                    edge++;
                    weight += e.weight;
                }
            }
            return edge == n - 1;
        }
        void init() {
            Collections.sort(es);
            for (Node v : vs) { v.init(); }
            edge = 0;
            weight = 0;
        }
        
        class UnionFind {
            int[] par;
            int[] rank;
            UnionFind(int size) { this.par = new int[size]; this.rank = new int[size]; for(int i=0; i<size; i++) { par[i] = i; rank[i] = 0; } }
            // x と y の属する集合を併合
            void unite(int x, int y) { x = find(x); y = find(y); if (x == y) { return; } if (rank[x] < rank[y]) { par[x] = y; } else { par[y] = x; if(rank[x] == rank[y]) { rank[x]++; } } }
            // x と y が同じ集合に属するか否か
            boolean same(int x, int y) { return find(x) == find(y); }
            // 木の根を求める
            int find(int x) { if(par[x] == x) { return x; } else { return par[x] = find(par[x]); } }
        }
        
        class Node {
            List<Edge> es = new ArrayList<Edge>();
            int id;
            int weight;
            Node(int id) { this.id = id; }
            void init() {
                es = new ArrayList<Edge>();
                weight = 0;
            }
        }
        
        class Edge implements Comparable<Edge> {
            Node from, to;
            int weight;
            Edge(Node from, Node to, int weight) { this.from = from; this.to = to; this.weight = weight; }
            public int compareTo(Edge o) { return weight - o.weight; }
        }
    }
    
    int n, m;
    int[] q;
    Kruskal kr;
    
    public R017B() {
        Scanner scanner = new Scanner(System.in);
        this.n = scanner.nextInt();
        this.kr = new Kruskal(n);
        this.q = new int[n];
        for(int i=0; i<n; i++) { 
            q[i] = scanner.nextInt();
        }
        this.m = scanner.nextInt();
        for(int i=0; i<m; i++) {
            int a = scanner.nextInt() - 1;
            int b = scanner.nextInt() - 1;
            int c = scanner.nextInt();
            kr.addEdge(a, b, c, true);
        }
    }
    
    private void solve() {
         if(kr.mst()) { System.out.println(kr.weight); }
         else { System.out.println(-1); }
    }
    
    public static void main(String[] args) { new R017B().solve(); }
}
