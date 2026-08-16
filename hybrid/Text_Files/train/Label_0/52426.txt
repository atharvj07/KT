import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.StringTokenizer;
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
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        int[] treeSt;
        int[] treeDec;

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            int repDur = in.nextInt();
            int st = in.nextInt();
            int dec = in.nextInt();
            int q = in.nextInt();
            treeSt = build(n);
            treeDec = build(n);
            while (q > 0) {
                q--;
                int t = in.nextInt();
                if (t == 1) {
                    int d = in.nextInt();
                    int ord = in.nextInt();
                    update(treeSt, d, ord, st);
                    update(treeDec, d, ord, dec);
                } else {
                    int f = in.nextInt();
                    int sumBefore = sum(true, 1, f - 1);
                    int sumAfter = sum(false, f + repDur, n);
                    int ans = sumBefore + sumAfter;
                    out.println(ans);
                }
            }
        }

        int sum(boolean fl, int s, int f) {
            if (s > f)
                return 0;
            else {
                if (fl)
                    return queryDec(1, s, f, 1, treeSt.length / 2);
                else
                    return querySt(1, s, f, 1, treeSt.length / 2);
            }
        }

        int[] build(int n) {
            int sz = 1;
            while (sz < n) {
                sz *= 2;
            }
            if (sz == 1)
                sz = 2;
            return new int[2 * sz];
        }

        void update(int[] tree, int day, int val, int max) {
            day--;
            int sz = tree.length;
            int node = sz / 2 + day;
            tree[node] += val;
            tree[node] = Math.min(tree[node], max);
            node /= 2;
            while (node > 0) {
                tree[node] = tree[2 * node] + tree[2 * node + 1];
                node /= 2;
            }
        }

        int querySt(int v, int ql, int qr, int l, int r) {
            if (ql == l && qr == r)
                return treeSt[v];
            else {
                int m = (l + r) / 2;
                int sl = 0, sr = 0;
                if (ql <= m)
                    sl += querySt(2 * v, ql, Math.min(m, qr), l, m);
                if (qr >= m + 1)
                    sr += querySt(2 * v + 1, Math.max(ql, m + 1), qr, m + 1, r);
                return sl + sr;
            }
        }

        int queryDec(int v, int ql, int qr, int l, int r) {
            if (ql == l && qr == r)
                return treeDec[v];
            else {
                int m = (l + r) / 2;
                int sl = 0, sr = 0;
                if (ql <= m)
                    sl += queryDec(2 * v, ql, Math.min(m, qr), l, m);
                if (qr >= m + 1)
                    sr += queryDec(2 * v + 1, Math.max(ql, m + 1), qr, m + 1, r);
                return sl + sr;
            }
        }

    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

