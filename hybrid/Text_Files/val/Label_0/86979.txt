import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

/**
 * @author Don Li
 */
public class WrapAround3 {
    
    int N = 41;
    
    int n, m;
    char[] s;
    
    int[] f;
    List<Integer>[][] prev = new List[N][2];
    int[][] next = new int[N][2];
    
    long[][] dp = new long[N][N];
    long[][] ep = new long[N][N];
    
    void solve() {
        n = in.nextInt();
        s = in.nextToken().toCharArray();
        m = s.length;
        
        f = fail(s);
        
        for (int i = 0; i < N; i++) for (int j = 0; j < 2; j++) prev[i][j] = new ArrayList<>();
        for (int i = 0; i <= m; i++) {
            for (int x = 0; x <= 1; x++) {
                int j = getNext(i, (char) (x + '0'));
                prev[j][x].add(i);
                next[i][x] = j;
            }
        }
        
        long ans = 0;
        for (int i = 0; i < N; i++) Arrays.fill(dp[i], -1);
        for (int i = 0; i < N; i++) Arrays.fill(ep[i], -1);
        for (int i = 0; i <= m; i++) {
            for (int pos = 0; pos < n; pos++) {
                ans += f(pos + 1, i) * g(n - pos - 1, i);
            }
        }
        out.println(ans);
    }
    
    long f(int n, int cur) {
        if (n == 0) return cur == m ? 1 : 0;
        if (dp[n][cur] >= 0) return dp[n][cur];
        long res = 0;
        for (int i = 0; i <= 1; i++) {
            int nxt = next[cur][i];
            if (n - 1 > 0 && nxt == m) continue; 
            res += f(n - 1, nxt);
        }
        return dp[n][cur] = res;
    }
    
    long g(int n, int cur) {
        if (n == 0) return cur == m ? 1 : 0;
        if (ep[n][cur] >= 0) return ep[n][cur];
        long res = 0;
        for (int i = 0; i <= 1; i++) {
            for (int nxt : prev[cur][i]) {
                res += g(n - 1, nxt);
            }
        }
        return ep[n][cur] = res;
    }
    
    int getNext(int now, char x) {
        if (now == m) now = f[now];
        while (now > 0 && s[now] != x) now = f[now];
        return s[now] == x ? now + 1 : 0;
    }
    
    int[] fail(char[] s) {
        int n = s.length;
        int[] f = new int[n + 1];
        f[0] = f[1] = 0;
        for (int i = 2; i <= n; i++) {
            int j = f[i - 1];
            while (j > 0 && s[j] != s[i - 1]) j = f[j];
            f[i] = s[j] == s[i - 1] ? j + 1 : 0;
        }
        return f;
    }
    
    public static void main(String[] args) {
        in = new FastScanner(new BufferedReader(new InputStreamReader(System.in)));
        out = new PrintWriter(System.out);
        new WrapAround3().solve();
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
