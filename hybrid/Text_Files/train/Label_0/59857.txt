import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.Random;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
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
        int[] firstEdge;
        int numEdges;
        int[] nextEdge;
        int[] edgeSrc;
        int[] edgeDst;
        int[] firstChild;
        int[] nextSibling;
        boolean[] was;
        int[] ans;
        int maxParts;
        int[] order;
        int[] parent;
        int[] maxPath;

        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            int n = in.nextInt();
            initGraph(n, n - 1);
            for (int i = 0; i < n - 1; i++) {
                int a = in.nextInt() - 1;
                int b = in.nextInt() - 1;
                addEdge(a, b);
                addEdge(b, a);
            }

            boolean stress = false;
//        boolean stress = true;
            if (stress) {
                n = 100000;
                initGraph(n, n - 1);
                Random random = new Random(0);
                for (int i = 0; i < n - 1; i++) {
                    int a = i + 1;
//                int b = random.nextInt(i + 1);
                    int b = i;
                    addEdge(a, b);
                    addEdge(b, a);
                }
            }

            was = new boolean[n + 1];
            ans = new int[n + 1];
            maxPath = new int[n];

            bfs(n);

            int mode = 0;
            switch (mode) {
                case 0:
                    solveRec(n);
                    break;
                case 1:
                    solveBinarySteps(n);
                    break;
                case 2:
                    solveSync(n);
                    break;
            }

            for (int i = 1; i <= n; i++) {
                out.println(ans[i]);
            }
        }

        private void initGraph(int n, int m) {
            firstEdge = new int[n];
            Arrays.fill(firstEdge, -1);
            numEdges = 0;
            nextEdge = new int[2 * m];
            edgeSrc = new int[2 * m];
            edgeDst = new int[2 * m];
        }

        private void addEdge(int a, int b) {
            int e = numEdges++;
            nextEdge[e] = firstEdge[a];
            firstEdge[a] = e;
            edgeSrc[e] = a;
            edgeDst[e] = b;
        }

        private void solveRec(int n) {
            rec(1, n, solve(1), solve(n));
        }

        private void solveBinarySteps(int n) {
            int k = 1;
            while (k <= n) {
                int s = 1;
                int l = k;
                int r = l;
                int vl = solve(k);
                while (r < n) {
                    r = Math.min(n, l + s);
                    int vr = solve(r);
                    if (vl != vr) {
                        break;
                    }
                    s *= 2;
                }

                while (l < n && s > 0) {
                    r = Math.min(n, l + s);
                    int vr = solve(r);
                    if (vl != vr) {
                        s /= 2;
                    } else {
                        l = r;
                    }
                }

                while (k <= l) {
                    ans[k] = vl;
                    ++k;
                }
            }
        }

        private void solveSync(int n) {
            int S = 100;
            int[] syncV = new int[S + 1];
            int[] syncX = new int[S + 1];
            for (int i = 0; i < S; i++) {
                int x = (int) ((long) i * n / S);
                if (x < 1) {
                    x = 1;
                }
                if (x > n) {
                    x = n;
                }
                syncV[i] = solve(x);
                syncX[i] = x;
            }
            syncV[S] = -1;
            syncX[S] = n;

            int syncPtr = 0;
            int k = 1;
            while (k <= n) {
                int l = k;
                int vl = solve(l);
                while (syncV[syncPtr] >= vl) {
                    ++syncPtr;
                }
                int r = syncX[syncPtr] + 1;

                while (r - l > 1) {
                    int m = (l + r) / 2;
                    int vm = solve(m);
                    if (vl == vm) {
                        l = m;
                    } else {
                        r = m;
                    }
                }

                while (k < r) {
                    ans[k] = vl;
                    ++k;
                }
            }
        }

        private void rec(int l, int r, int vl, int vr) {
            if (vl == vr) {
                for (int i = l; i <= r; i++) {
                    was[i] = true;
                    ans[i] = vl;
                }
                return;
            }
            int m = (l + r) / 2;
            if (m != r) {
                rec(l, m, vl, solve(m));
            }
            if (m != l) {
                rec(m, r, solve(m), vr);
            }
        }

        private void bfs(int n) {
            order = new int[n];
            parent = new int[n];
            order[0] = 0;
            Arrays.fill(parent, -1);
            parent[0] = -2;
            int qt = 0;
            int qh = 1;
            firstChild = new int[n];
            nextSibling = new int[n];
            Arrays.fill(firstChild, -1);
            Arrays.fill(nextSibling, -1);
            while (qt < qh) {
                int v = order[qt++];
                for (int e = firstEdge[v]; e >= 0; e = nextEdge[e]) {
                    int u = edgeDst[e];
                    if (parent[u] == -1) {
                        parent[u] = v;
                        order[qh++] = u;

                        nextSibling[u] = firstChild[v];
                        firstChild[v] = u;
                    }
                }
            }
        }

        private int solve(int k) {
            if (was[k]) {
                return ans[k];
            }
            was[k] = true;
            maxParts = 0;

            for (int i = order.length - 1; i >= 0; i--) {
                int v = order[i];

                int max1 = 0;
                int max2 = 0;
//            for (int e = firstEdge[v]; e >= 0; e = nextEdge[e]) {
//                int u = edgeDst[e];
//                if (u == parent[v]) {
//                    continue;
//                }
                for (int u = firstChild[v]; u >= 0; u = nextSibling[u]) {
                    int c = maxPath[u];
                    if (max1 < c) {
                        max2 = max1;
                        max1 = c;
                    } else if (max2 < c) {
                        max2 = c;
                    }
                }
                int res = max1 + 1;
                if (max1 + max2 + 1 >= k) {
                    ++maxParts;
                    res = 0;
                }
                maxPath[v] = res;
            }

            ans[k] = maxParts;
            return ans[k];
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

