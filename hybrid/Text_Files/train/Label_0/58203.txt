import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution {
    static final FS sc = new FS();
    static final PrintWriter pw = new PrintWriter(System.out);
    static  int alp = 20;
    static List<List<Integer>> G;
    public static void main(String[] args) {
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            char[] a = sc.next().toCharArray();
            char[] b = sc.next().toCharArray();
            G = new ArrayList<>();
            for(int i = 0;i < alp;i++) {
                G.add(new ArrayList<>());
            }
            int[] adj = new int[alp];
            for(int i = 0;i < n;i++) {
                if (a[i] != b[i]) {
                    G.get(a[i] - 'a').add(b[i] - 'a');
                    G.get(b[i] - 'a').add(a[i] - 'a');
                    adj[a[i] - 'a'] |= 1 << (b[i] - 'a');
                }
            }
            int components = 0;
            boolean[] vis = new boolean[alp];
            for (int i = 0;i < alp;i++) {
                if (!vis[i]) {
                    dfs(i, vis);
                    components++;
                }
            }
            int ans = 0;
            boolean[] dp = new boolean[1 << alp];
            dp[0] = true;
            for (int mask = 0;mask < 1 << alp;mask++) {
                if (dp[mask]) {
                    ans = Math.max(ans, Integer.bitCount(mask));
                    for (int u = 0;u < alp;u++) {
                        if ((~mask >> u & 1) == 1 && (adj[u] & mask) == 0) {
                            dp[mask | 1 << u] = true;
                        }
                    }
                }
            }
            pw.println(2 * alp - components - ans);
        }
        pw.flush();
    }

    private static void dfs(int u, boolean[] vis) {
        vis[u] = true;
        for (Integer v : G.get(u)) {
            if (!vis[v]) {
                dfs(v, vis);
            }
        }
    }

    static class FS {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        String next() {
            while(!st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch(Exception ignored) {}
            }
            return st.nextToken();
        }
        int[] nextArray(int n) {
            int[] a = new int[n];
            for(int i = 0;i < n;i++) {
                a[i] = nextInt();
            }
            return a;
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
    }
}