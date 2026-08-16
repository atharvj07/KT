import java.util.*;
import java.io.*;

public class WaterTree implements Runnable {
    static ArrayList<Integer>[] graph;
    public static void main(String[] args) throws Exception {
        Thread thread = new Thread(null, new WaterTree(), "spargeltarzan", 1L<< 29);
        thread.start();
        thread.join();
    }
    public void run() {
        try {solve();} catch (Exception e) {
            System.err.println(e);
        }
    }
    public void solve() throws Exception {
        FastScanner scanner = new FastScanner();
        PrintWriter out = new PrintWriter(System.out, false);
        int n = scanner.nextInt();
        graph = new ArrayList[n];
        for(int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for(int i = 1; i < n; i++) {
            int a = scanner.nextInt()-1;
            int b = scanner.nextInt()-1;
            graph[a].add(b); graph[b].add(a);
        }
        inval = new int[n];
        parent = new int[n];
        sz = new int[n];
        cnt = 0;
        dfsOrder(0,0);
        graph = null;
        SegTree sg = new SegTree(n);
        int q = scanner.nextInt();
        sg.update(1, 0, n-1,2 * q, 0, n-1);
        for(int Q = 1; Q <= q; Q++) {
            int type = scanner.nextInt();
            int v = scanner.nextInt()-1;
            if (type == 1) {
                //fill operation
                int val = sg.query(1, inval[v], inval[v] + sz[v], 0, n-1);
                if (val == 2 * q && v != 0) {
                    sg.update(1,inval[parent[v]], inval[parent[v]], 2 * q, 0, n-1);
                }
                sg.update(1,inval[v], inval[v] + sz[v], Q, 0, n-1);
            } else if (type == 2) {
                //empty operation
                sg.update(1,inval[v],inval[v], 2*q,0, n-1);
            } else {
                int val = sg.query(1, inval[v], inval[v] + sz[v], 0, n-1);
                if (val == 2*q) out.println(0);
                else out.println(1);
            }
        }
        out.flush();
    }
    static int[] inval, sz;
    static int[] parent;
    static int cnt;
    static void dfsOrder(int cur, int p) {
        inval[cur] = cnt++;
        parent[cur] = p;
        for(int edge: graph[cur]) {
            if (edge == p) continue;
            dfsOrder(edge, cur);
            sz[cur] += sz[edge] + 1;
        }
    }
    static class SegTree {
        int[] max, delta;
        public SegTree(int ss) {
            max = new int[4 * ss+1];
            delta = new int[4 * ss+1];
        }
        public int query(int cur, int l, int r, int lo, int hi) {
            if (l > hi || r < lo) return -1;
            if (r >= hi && l<=lo) {
                if (delta[cur] != 0) return delta[cur];
                return max[cur];
            }
            prop(cur);
            int mid = (hi + lo)/2;
            int left = query(cur*2, l, r, lo, mid);
            int right = query(cur*2 + 1, l,r,mid + 1, hi);
            update(cur);
            if (left >= right) return left;
            return right;
        }
        void prop(int cur) {
            if (delta[cur] > 0) {
                delta[cur * 2] = delta[cur];
                delta[cur * 2 + 1] = delta[cur];
                delta[cur] = 0;
            }
        }
        void update(int cur) {
            int temp = delta[cur*2] != 0 ? delta[cur*2] : max[cur*2];
            int t2 = delta[cur*2+1] != 0 ? delta[cur*2+1] : max[cur*2+1];
            max[cur] = temp;
            if (t2 > max[cur]) max[cur] = t2;
        }
        void update(int cur, int l, int r, int amt, int lo, int hi) {
            if (l > hi || r < lo) {
                return;
            }
            if (r >= hi && l <= lo) {
                delta[cur] = amt;
                return;
            }
            prop(cur);
            int mid = (hi + lo)/2;
            update(cur*2, l, r, amt, lo, mid);
            update(cur*2 + 1, l, r, amt, mid + 1, hi);
            update(cur);
        }
        
    }
    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;
        
        public FastScanner(Reader in) {
            br = new BufferedReader(in);
        }
        
        public FastScanner() {
            this(new InputStreamReader(System.in));
        }
        
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        
        int nextInt() {
            return Integer.parseInt(next());
        }
        
        long nextLong() {
            return Long.parseLong(next());
        }
        
        double nextDouble() {
            return Double.parseDouble(next());
        }
        
        String readNextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
