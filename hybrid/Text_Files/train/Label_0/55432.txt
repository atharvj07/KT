import java.io.*;
import java.util.*;

public class Test {

    static int readInt() {
        int ans = 0;
        boolean neg = false;
        try {
            boolean start = false;
            for (int c = 0; (c = System.in.read()) != -1; ) {
                if (c == '-') {
                    start = true;
                    neg = true;
                    continue;
                } else if (c >= '0' && c <= '9') {
                    start = true;
                    ans = ans * 10 + c - '0';
                } else if (start) break;
            }
        } catch (IOException e) {
        }
        return neg ? -ans : ans;
    }

    static long readLong() {
        long ans = 0;
        boolean neg = false;
        try {
            boolean start = false;
            for (int c = 0; (c = System.in.read()) != -1; ) {
                if (c == '-') {
                    start = true;
                    neg = true;
                    continue;
                } else if (c >= '0' && c <= '9') {
                    start = true;
                    ans = ans * 10 + c - '0';
                } else if (start) break;
            }
        } catch (IOException e) {
        }
        return neg ? -ans : ans;
    }

    static String readString() {
        StringBuilder b = new StringBuilder();
        try {
            boolean start = false;
            for (int c = 0; (c = System.in.read()) != -1; ) {
                if (c >= '0' && c <= '9') {
                    start = true;
                    b.append((char) (c));
                } else if (start) break;
            }
        } catch (IOException e) {
        }
        return b.toString().trim();
    }

    static PrintWriter writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    void start() {
        int n = readInt(), m = readInt(), k = readInt();
        int[] from = new int[m], to = new int[m];
        int[] q = new int[n];
        Set<Integer>[] g = new Set[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new HashSet<>();
        for (int i = 0; i < m; i++) {
            int u = readInt(), v = readInt();
            g[u].add(v);
            g[v].add(u);
            from[i] = u;
            to[i] = v;
        }
        TreeSet<Integer> f = new TreeSet<>();
        int a = 0, b = 0;
        for (int i = 1; i <= n; i++)
            if (g[i].size() < k) q[b++] = i;
            else f.add(i);
        while (a < b) {
            int u = q[a++];
            for (int v : g[u]) {
                g[v].remove(u);
                if (g[v].size() == k - 1) {
                    f.remove(v);
                    q[b++] = v;
                }
            }
            g[u].clear();
        }
        int[] ans = new int[m];
        for (int i = m - 1; i >= 0; i--) {
            ans[i] = f.size();
            a = 0;
            b = 0;
            int u = from[i], v = to[i];
            for (int x : new int[]{u, v}) {
                g[x].remove(x == u ? v : u);
                if (g[x].size() == k - 1) {
                    f.remove(x);
                    q[b++] = x;
                }
            }
            while (a < b) {
                u = q[a++];
                for (int x : g[u]) {
                    g[x].remove(u);
                    if (g[x].size() == k - 1) {
                        f.remove(x);
                        q[b++] = x;
                    }
                }
                g[u].clear();
            }
        }
        for (int i = 0; i < m; i++) writer.println(ans[i]);
    }

    public static void main(String[] args) {
        Test te = new Test();
        te.start();
        writer.flush();
    }
}
