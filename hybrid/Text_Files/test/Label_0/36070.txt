import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

/**
 * @author Don Li
 */
public class DestructionTree3 {
    
    int N = (int) 2e5 + 10;
    
    int n;
    int[][] G;
    int[] sz = new int[N], par = new int[N], even = new int[N];
    
    void solve() {
        n = in.nextInt();
        
        if (n % 2 == 0) {
            out.println("NO");
            return;
        }
        
        int[] fr = new int[n - 1], to = new int[n - 1];
        for (int i = 0, j = 0; i < n; i++) {
            int p = in.nextInt() - 1;
            if (p != -1) {
                fr[j] = p;
                to[j++] = i;
            }
        }
        G = build_graph(n, fr, to);
        
        dfs(0, -1);
        
        int[] q = new int[n]; boolean[] inq = new boolean[n];
        int qh = 0, qt = 0;
        for (int i = 0; i < n; i++) {
            if (even[i] == 0) {
                q[qt++] = i;
                inq[i] = true;
            }
        }
        while (qh < qt) {
            int u = q[qh++];
            for (int v : G[u]) {
                if (inq[v]) continue;
                int comp_sz = u == par[v] ? n - sz[v] : sz[u];
                if (comp_sz % 2 == 0) even[v]--;
                if (even[v] == 0) {
                    q[qt++] = v;
                    inq[v] = true;
                }
            }
        }
    
        out.println("YES");
        for (int u : q) out.println(u + 1);
    }
    
    void dfs(int u, int p) {
        sz[u] = 1;
        par[u] = p;
        for (int v : G[u]) {
            if (v != p) {
                dfs(v, u);
                if (sz[v] % 2 == 0) even[u]++;
                sz[u] += sz[v];
            }
        }
        if (p != -1 && (n - sz[u]) % 2 == 0) even[u]++;
    }
    
    int[][] build_graph(int n, int[] from, int[] to) {
        int[][] G = new int[n][];
        int[] cnt = new int[n];
        for (int i = 0; i < from.length; i++) {
            cnt[from[i]]++;
            cnt[to[i]]++;
        }
        for (int i = 0; i < n; i++) G[i] = new int[cnt[i]];
        for (int i = 0; i < from.length; i++) {
            G[from[i]][--cnt[from[i]]] = to[i];
            G[to[i]][--cnt[to[i]]] = from[i];
        }
        return G;
    }
    
    public static void main(String[] args) {
        in = new FastScanner(new BufferedReader(new InputStreamReader(System.in)));
        out = new PrintWriter(System.out);
        new DestructionTree3().solve();
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
