import java.io.BufferedReader;
// import java.io.FileInputStream;
// import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Random;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.TreeSet;

import static java.lang.Math.abs;
import static java.lang.Math.max;
import static java.lang.Math.min;
import static java.lang.Math.round;
import static java.util.Arrays.copyOf;
import static java.util.Arrays.fill;
import static java.util.Arrays.sort;
import static java.util.Collections.reverseOrder;
import static java.util.Collections.sort;
import static java.util.Comparator.comparing;

public class Main {
    FastScanner in;
    PrintWriter out;

    int n, ans = 0;
    ArrayList<Integer>[] graph;
    int[] dist;

    private void solve() throws IOException {
        n = in.nextInt();
        graph = new ArrayList[n];
        for (int i = 0; i < n; i++)
            graph[i] = new ArrayList<>();

        for (int i = 0, v, u; i < n - 1; i++) {
            v = in.nextInt() - 1;
            u = in.nextInt() - 1;
            graph[v].add(u);
            graph[u].add(v);
        }

        dist = new int[n];
        fill(dist, n + 1613);

        ans = 0;
        dist[0] = 0;
        dfs(0, -1);
        out.println(ans);
    }

    private void dfs(int v, int p) {
        for (int u : graph[v])
            if (u != p) {
                dist[u] = min(dist[u], dist[v] + 1);
                dfs(u, v);
                dist[v] = min(dist[v], dist[u] + 1);
            }
        if (dist[v] > 2) {
            ans++;
            dist[p] = 1;
            dist[v] = 2;
        }
    }

    class FastScanner {
        StringTokenizer st;
        BufferedReader br;

        FastScanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        boolean hasNext() throws IOException {
            return br.ready() || (st != null && st.hasMoreTokens());
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        String nextLine() throws IOException {
            return br.readLine();
        }

        boolean hasNextLine() throws IOException {
            return br.ready();
        }
    }

    private void run() throws IOException {
        in = new FastScanner(System.in); // new FastScanner(new FileInputStream(".in"));
        out = new PrintWriter(System.out); // new PrintWriter(new FileOutputStream(".out"));

        solve();

        out.flush();
        out.close();
    }

    public static void main(String[] args) throws IOException {
        new Main().run();
    }
}