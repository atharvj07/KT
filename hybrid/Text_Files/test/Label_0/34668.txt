import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

/**
 * @author Don Li
 */
public class Madness {
    
    int N = 100 + 10;
    
    int n;
    int[][][] G;
    
    boolean[] vis = new boolean[N];
    
    int[][] dir = new int[N][2];
    double[] dist = new double[N];
    
    void solve() {
        n = in.nextInt();
        int[] fr = new int[n - 1], to = new int[n - 1], ids = new int[n - 1];
        for (int i = 0; i < n - 1; i++) {
            fr[i] = in.nextInt() - 1;
            to[i] = in.nextInt() - 1;
            ids[i] = i;
        }
        G = build_graph(n, fr, to, ids);
        
        dfs(0, 0);
        
        out.println(n - 1);
        for (int i = 0; i < n - 1; i++) {
            out.printf("%d %d %d %d %f%n", 1, i + 1, dir[i][0] + 1, dir[i][1] + 1, dist[i]);
        }
    }
    
    void dfs(int u, double time) {
        vis[u] = true;
        int deg = G[u].length;
        double slot = 2.0 / deg, cur = time;
        for (int[] p : G[u]) {
            int v = p[0], id = p[1];
            if (vis[v]) continue;
            double nxt = cur + slot;
            if (nxt >= 2.0) nxt -= 2.0;
            double toV;
            if (nxt <= 1.0) {
                dir[id][0] = v;
                dir[id][1] = u;
                dist[id] = 1.0 - nxt;
                toV = nxt + 1.0;
            } else {
                dir[id][0] = u;
                dir[id][1] = v;
                dist[id] = 2.0 - nxt;
                toV = nxt - 1.0;
            }
            dfs(v, toV);
            cur = nxt;
        }
    }
    
    int[][][] build_graph(int n, int[] from, int[] to, int[] weight) {
        int[][][] G = new int[n][][];
        int[] cnt = new int[n];
        for (int i = 0; i < from.length; i++) {
            cnt[from[i]]++;
            cnt[to[i]]++;
        }
        for (int i = 0; i < n; i++) G[i] = new int[cnt[i]][];
        for (int i = 0; i < from.length; i++) {
            G[from[i]][--cnt[from[i]]] = new int[]{to[i], weight[i]};
            G[to[i]][--cnt[to[i]]] = new int[]{from[i], weight[i]};
        }
        return G;
    }
    
    public static void main(String[] args) {
        in = new FastScanner(new BufferedReader(new InputStreamReader(System.in)));
        out = new PrintWriter(System.out);
        new Madness().solve();
        out.close();
    }
    
    static FastScanner in;
    static PrintWriter out;
    
    static class FastScanner {
        BufferedReader in;
        StringTokenizer st;
        
        public FastScanner(BufferedReader in) {
            this.in = in;
        }
        
        public String nextToken() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(in.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        
        public int nextInt() {
            return Integer.parseInt(nextToken());
        }
        
        public long nextLong() {
            return Long.parseLong(nextToken());
        }
        
        public double nextDouble() {
            return Double.parseDouble(nextToken());
        }
    }
}
