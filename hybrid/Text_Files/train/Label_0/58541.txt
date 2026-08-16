import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * @author Don Li
 */
public class XorTask {
    
    int N = 1 << 20;
    int MOD = (int) 1e9 + 7;
    
    boolean[] in_set = new boolean[N];
    List<Integer> set = new ArrayList<>();
    
    void solve() {
        int n = in.nextInt(), m = in.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = in.nextInt();
        int[] l = new int[m], x = new int[m];
        for (int i = 0; i < m; i++) {
            l[i] = in.nextInt();
            x[i] = in.nextInt();
        }
        
        int[] cnt = new int[n + 1];
        for (int i = 0; i < m; i++) {
            cnt[l[i]]++;
        }
        int[][][] grp = new int[n + 1][][];
        for (int i = 0; i <= n; i++) grp[i] = new int[cnt[i]][];
        for (int i = 0; i < m; i++) {
            grp[l[i]][--cnt[l[i]]] = new int[]{x[i], i};
        }
        
        int[] res = new int[m];
        set.add(0);
        in_set[0] = true;
        int ans = 1;
        for (int i = 0; i < n; i++) {
            if (in_set[a[i]]) {
                ans = ans * 2 % MOD;
            } else {
                int sz = set.size();
                for (int j = 0; j < sz; j++) {
                    int v = set.get(j) ^ a[i];
                    set.add(v);
                    in_set[v] = true;
                }
            }
            for (int[] t : grp[i + 1]) {
                if (in_set[t[0]]) res[t[1]] = ans;
            }
        }
        
        for (int i = 0; i < m; i++) {
            out.println(res[i]);
        }
    }
    
    public static void main(String[] args) {
        in = new FastScanner(new BufferedReader(new InputStreamReader(System.in)));
        out = new PrintWriter(System.out);
        new XorTask().solve();
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
