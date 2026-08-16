import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.List;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            int n = in.nextInt();
            int m = in.nextInt();
            int[] a = new int[m];
            int[] b = new int[m];
            int[] c = new int[m];
            int[] deg = new int[n];
            for (int i = 0; i < m; i++) {
                a[i] = in.nextInt();
                b[i] = in.nextInt();
                c[i] = in.nextInt();
                ++deg[a[i]];
            }
            Edge[][] edges = new Edge[n][];
            for (int i = 0; i < n; i++) {
                edges[i] = new Edge[deg[i]];
                deg[i] = 0;
            }
            for (int i = 0; i < m; i++) {
                Edge e = new Edge(b[i], c[i]);
                edges[a[i]][deg[a[i]]++] = e;
            }

            for (int i = 0; i < n; i++) {
                List<Edge> onlyGood = new ArrayList<>();
                for (int j = 0; j < deg[i]; j++) {
                    for (int k = 0; k < deg[i]; k++) {
                        if (k == j) {
                            continue;
                        }
                        int dist = edges[i][j].dst - edges[i][k].dst;
                        if (dist < 0) {
                            dist += n;
                        }
                        if (dist + edges[i][k].len < edges[i][j].len) {
                            edges[i][j].good = false;
                            break;
                        }
                    }
                    if (edges[i][j].good) {
                        onlyGood.add(edges[i][j]);
                    }
                }
                edges[i] = onlyGood.toArray(new Edge[0]);
                deg[i] = edges[i].length;
                Arrays.sort(edges[i], (u, v) -> (u.dst - v.dst));
            }

            long[] d = new long[n];
            boolean[] used = new boolean[n];
            final long infinity = (long) 1e18;
            for (int s = 0; s < n; s++) {
                Arrays.fill(d, infinity);
                Arrays.fill(used, false);
                d[s] = 0;
                for (int step = 0; step < n; step++) {
                    int v = -1;
                    for (int i = 0; i < n; i++) {
                        if (used[i]) {
                            continue;
                        }
                        if (v < 0 || d[v] > d[i]) {
                            v = i;
                        }
                    }
                    used[v] = true;
                    int t = (int) (d[v] % n);
                    Edge[] es = edges[v];
                    for (int e = 0; e < es.length; e++) {
                        int ne = e + 1;
                        if (ne >= es.length) {
                            ne = 0;
                        }
                        int goodFor = es[ne].dst - es[e].dst;
                        if (goodFor <= 0) {
                            goodFor += n;
                        }
                        for (int dt = 0; dt < goodFor; dt++) {
                            int u = es[e].dst + t + dt;
                            while (u >= n) {
                                u -= n;
                            }
                            long cur = d[v] + es[e].len + dt;
                            if (d[u] > cur) {
                                d[u] = cur;
                            }
                        }
                    }
                }

                for (int i = 0; i < n; i++) {
                    if (i > 0) {
                        out.print(" ");
                    }
                    out.print(d[i]);
                }
                out.println();
            }
        }

        class Edge {
            int dst;
            int len;
            boolean good;

            public Edge(int dst, int len) {
                this.dst = dst;
                this.len = len;
                this.good = true;
            }

        }

    }

    static class FastScanner {
        private BufferedReader in;
        private StringTokenizer st;

        public FastScanner(InputStream stream) {
            in = new BufferedReader(new InputStreamReader(stream));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(in.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

