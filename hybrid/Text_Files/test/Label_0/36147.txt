import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        G1NaBlokiUproshennayaVersiya solver = new G1NaBlokiUproshennayaVersiya();
        solver.solve(1, in, out);
        out.close();
    }

    static class G1NaBlokiUproshennayaVersiya {
        int[] cnt;

        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            in.nextInt();
            int[] a = new int[n];
            int m = 0;
            for (int i = 0; i < n; i++) {
                a[i] = in.nextInt() - 1;
                m = Math.max(m, a[i] + 1);
            }
            cnt = new int[m];
            for (int i = 0; i < n; i++) {
                cnt[a[i]]++;
            }
            DSU dsu = new DSU(m);

            int[] s = new int[n];
            int sp = -1;
            boolean[] onStack = new boolean[m];
            for (int i = 0; i < n; i++) {
                int v = dsu.get(a[i]);
                if (sp == -1 || !onStack[v]) {
                    sp++;
                    s[sp] = v;
                    onStack[v] = true;
                } else {
                    while (dsu.get(s[sp]) != dsu.get(v)) {
                        dsu.unite(s[sp], v);
                        sp--;
                    }
                    v = dsu.get(v);
                    onStack[v] = true;
                }
            }

            int[] max = new int[m];
            for (int i = 0; i < n; i++) {
                int v = dsu.get(a[i]);
                max[v] = Math.max(max[v], cnt[a[i]]);
            }

            int ans = n;
            for (int i = 0; i < m; i++) {
                ans -= max[i];
            }
            out.println(ans);
        }

        class DSU {
            int n;
            int[] p;
            int[] r;

            public DSU(int n) {
                this.n = n;
                p = new int[n];
                r = new int[n];
                for (int i = 0; i < n; i++) {
                    p[i] = i;
                }
            }

            int get(int v) {
                if (p[v] != v) {
                    p[v] = get(p[v]);
                }
                return p[v];
            }

            void unite(int x, int y) {
                x = get(x);
                y = get(y);
                if (r[x] == r[y]) {
                    r[x]++;
                }
                if (r[x] > r[y]) {
                    p[y] = x;
                } else {
                    p[x] = y;
                }
            }

        }

    }
}

