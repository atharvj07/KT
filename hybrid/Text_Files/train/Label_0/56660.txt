import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

/**
 * @author Don Li
 */
public class Tournament {
    
    int N = (int) 5e4 + 10;
    int M = 10;
    int INF = (int) 1e9 + 100;
    
    int n, m;
    
    int id = 0;
    int[] sz = new int[N];
    int[][] min = new int[N][M], max = new int[N][M];
    
    void solve() {
        n = in.nextInt(); m = in.nextInt();
        int[][] s = new int[n][m];
    
        TreeSet<Node>[] minSet = new TreeSet[m], maxSet = new TreeSet[m];
        for (int i = 0; i < m; i++) {
            minSet[i] = new TreeSet<>(Comparator.comparingInt(a -> a.val));
            maxSet[i] = new TreeSet<>(Comparator.comparingInt(a -> a.val));
        }
        for (int i = 0; i < n; i++) {
            Node lose = null, win = null;
            for (int j = 0; j < m; j++) {
                s[i][j] = in.nextInt();
                Node hi = maxSet[j].higher(new Node(-1, s[i][j]));
                if (hi != null) {
                    if (lose == null || max[lose.id][0] > max[hi.id][0]) lose = hi;
                }
                Node lo = minSet[j].lower(new Node(-1, s[i][j]));
                if (lo != null) {
                    if (win == null || min[win.id][0] < min[lo.id][0]) win = lo;
                }
            }
            
            if (lose == null || win == null || min[lose.id][0] > min[win.id][0]) {
                sz[id] = 1;
                for (int j = 0; j < m; j++) {
                    min[id][j] = max[id][j] = s[i][j];
                    minSet[j].add(new Node(id, min[id][j]));
                    maxSet[j].add(new Node(id, max[id][j]));
                }
                id++;
            } else {
                int fr = lose.id, to = win.id;
                Set<Integer> del = new HashSet<>();
                for (Node node : minSet[0].subSet(new Node(fr, min[fr][0]), true, new Node(to, min[to][0]), true)) {
                    del.add(node.id);
                }
                for (int x : del) {
                    for (int j = 0; j < m; j++) {
                        minSet[j].remove(new Node(x, min[x][j]));
                        maxSet[j].remove(new Node(x, max[x][j]));
                    }
                }
                sz[id] = 1;
                for (int x : del) sz[id] += sz[x];
                for (int j = 0; j < m; j++) {
                    min[id][j] = Math.min(min[fr][j], s[i][j]);
                    max[id][j] = Math.max(max[to][j], s[i][j]);
                    minSet[j].add(new Node(id, min[id][j]));
                    maxSet[j].add(new Node(id, max[id][j]));
                }
                id++;
            }
            
            int first = minSet[0].lower(new Node(-1, INF)).id;
            out.println(sz[first]);
        }
    }
    
    static class Node {
        int id;
        int val;
        
        Node(int id, int val) {
            this.id = id;
            this.val = val;
        }
    }
    
    
    public static void main(String[] args) {
        in = new FastScanner(new BufferedReader(new InputStreamReader(System.in)));
        out = new PrintWriter(System.out);
        new Tournament().solve();
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
