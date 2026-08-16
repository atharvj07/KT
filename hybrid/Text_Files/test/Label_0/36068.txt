import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * @author Don Li
 */
public class CirclingRoundTreasures {
    
    int INF = (int) 1e7;
    
    int[] dx = new int[]{-1, 0, 0, 1};
    int[] dy = new int[]{0, -1, 1, 0};
    
    void solve() {
        int n = in.nextInt(), m = in.nextInt();
        char[][] s = new char[n][];
        for (int i = 0; i < n; i++) s[i] = in.nextToken().toCharArray();
        
        int t = 0, b = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (s[i][j] >= '1' && s[i][j] <= '8') t++;
                else if (s[i][j] == 'B') b++;
            }
        }
        
        int[] v = new int[t + b];
        for (int i = 0; i < t; i++) v[i] = in.nextInt();
        
        int sx = -1, sy = -1;
        int[] X = new int[t + b], Y = new int[t + b];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (s[i][j] >= '1' && s[i][j] <= '8') {
                    int id = s[i][j] - '1';
                    X[id] = i;
                    Y[id] = j;
                } else if (s[i][j] == 'B') {
                    X[t] = i;
                    Y[t] = j;
                    v[t] = -INF;
                    t++;
                } else if (s[i][j] == 'S') {
                    sx = i;
                    sy = j;
                }
            }
        }
        
        int[] cost = new int[1 << t];
        for (int i = 0; i < 1 << t; i++) {
            for (int j = 0; j < t; j++) {
                if ((i & (1 << j)) > 0) cost[i] += v[j];
            }
        }
        
        int[][][] dp = new int[n][m][1 << t];
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) Arrays.fill(dp[i][j], INF);
        
        int ans = 0;
        Queue<int[]> qu = new LinkedList<>();
        qu.offer(new int[]{sx, sy, 0});
        dp[sx][sy][0] = 0;
        while (!qu.isEmpty()) {
            int[] a = qu.poll();
            int x = a[0], y = a[1], mask = a[2];
            if (x == sx && y == sy) {
                ans = Math.max(ans, cost[mask] - dp[x][y][mask]);
            }
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && (s[nx][ny] == '.' || s[nx][ny] == 'S')) {
                    int nmask = mask;
                    for (int j = 0; j < t; j++) {
                        if (cross(x, y, nx, ny, X[j], Y[j])) nmask ^= 1 << j;
                    }
                    if (dp[nx][ny][nmask] > dp[x][y][mask] + 1) {
                        dp[nx][ny][nmask] = dp[x][y][mask] + 1;
                        qu.offer(new int[]{nx, ny, nmask});
                    }
                }
            }
        }
        out.println(ans);
    }
    
    boolean cross(int x1, int y1, int x2, int y2, int x, int y) {
        return x == x1 && y < y1 && x == x2 + 1 && y < y2 || x == x2 && y < y2 && x == x1 + 1 && y < y1;
    }
    
    public static void main(String[] args) {
        in = new FastScanner(new BufferedReader(new InputStreamReader(System.in)));
        out = new PrintWriter(System.out);
        new CirclingRoundTreasures().solve();
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
