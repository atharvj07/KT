import java.io.*;
import java.time.temporal.TemporalAmount;
import java.util.*;
import java.util.function.Consumer;

public class Solution {


    static MyScanner sc;
    private static PrintWriter out;
    static long M2 = 1_000_000_000L + 9;
    private static HashMap<Long, Long>[] mods;

    public static void main(String[] s) throws Exception {
        StringBuilder stringBuilder = new StringBuilder();
//
//        stringBuilder.append("1 25 20 30 80");


        if (stringBuilder.length() == 0) {
            sc = new MyScanner(System.in);
        } else {
            sc = new MyScanner(new BufferedReader(new StringReader(stringBuilder.toString())));
        }

        out = new PrintWriter(new OutputStreamWriter(System.out));

        initData();
        solve();
        out.flush();
    }

    private static void initData() {
//        fillPows();
//        mods = new HashMap[1001];
//        for (int i = 0; i < mods.length; i++) {
//            mods[i] = new HashMap<>();
//        }
    }


    private static void solve() throws IOException {
        int n = sc.nextInt();
        int[] r = sc.na(n);
        boolean[] vx = new boolean[1000001];
        for (int i : r) {
            vx[i] = true;
        }
        int gcd = r[0];
        for (int k : r) {
            gcd = (int) gcd(gcd, k);
        }

        int[] res = new int[r.length + r.length - 1];
        Arrays.fill(res, gcd);
        for (int t = 0; t < n; t++) {
            res[2 * t ] = r[t];
        }

        for (int t = 0; t < res.length; t++) {
            int gc = res[t];
            for (int l = t + 1; l < res.length; l++) {
                gc = (int) gcd(gc, res[l]);
                if (!vx[gc]) {
                    out.println(-1);
                    return;
                }
            }
        }
        out.println(res.length);
        for (int i : res) {
            out.print(i + " ");
        }
    }

    private static int[][] pows = new int[1001][1001];

    private static void fillPows() {
        pows[2][0] = 1;
        pows[2][1] = 2;
        pows[2][2] = 1;
        for (int i = 3; i < pows.length; i++) {
            pows[i][0] = 1;
            pows[i][i] = 1;
            for (int j = 1; j < i; j++) {
                pows[i][j] = pows[i - 1][j - 1] + pows[i - 1][j];
                pows[i][j] %= M2;
            }
        }
    }


    private static long sumOfPow(long to, int pow) {
        if (to == 1) {
            return 1;
        }

        Long vl = null;
        if (to < 1000) {
            vl = mods[pow].get(to);
        }

        if (vl != null) {
            return vl;
        }
        if (pow == 1) {
            long tx = to % M2;
            tx *= tx + 1;
            vl = tx % M2;
        } else {
            vl = sumOfPow1(to, pow) + sumOfPow2(to, pow);
            vl %= M2;
        }
        if (to < 1000) {
            mods[pow].put(to, vl);
        }

        return vl;
    }

    private static long sumOfPow1(long to, int pow) {
        return (pow(2, pow, M2) * sumOfPow(to / 2, pow)) % M2;
    }


    private static long sumOfPow2(long to, int pow) {
        if (to % 2 == 0) {
            return sumOfPow2(to - 1, pow);
        }
        if (to == 1) {
            return 1;
        }

        long sum = to / 2 + 1;
        sum %= M2;
        sum += sumOfPow1(to, pow);
        sum %= M2;
        for (int i = 1; i < pow; i++) {
            sum += (pows[pow][i] * sumOfPow1(to, pow - i)) % M2;
            sum %= M2;
        }

        return sum;
    }


    private static final class LogTreePar {

        private final int[] levels;
        private final int[][] parents;

        public LogTreePar(int n) {
            levels = new int[n];
            parents = new int[n][19];
            Arrays.fill(levels, -1);
            for (int[] x : parents) {
                Arrays.fill(x, -1);
            }
        }

        public boolean ispar(int f, int l) {
            if (levels[f] >= levels[l]) return false;
            int diff = levels[l] - levels[f];
            return up(l, diff) == f;
        }

        private int up(int item, int diff) {
            int r = 0;
            while (diff > 0 && item >= 0) {
                if (isset(diff, r)) {
                    diff ^= 1 << r;
                    item = parents[item][r];
                }
                r++;
            }
            return item;
        }


        public void add(int item, int parent) {
            parents[item][0] = parent;
            clt(item);
        }


        protected void clt(int item) {
            levels[item] = levels[parents[item][0]] + 1;
            for (int l = 1; l < 19; l++) {
                if (parents[item][l - 1] == -1) break;
                parents[item][l] = parents[parents[item][l - 1]][l - 1];
            }
        }

        public int lca(int f, int l) {
            if (levels[f] > levels[l]) {
                return lca(l, f);
            }
            return lca1(f, up(l, levels[l] - levels[f]));
        }

        private int lca1(int f1, int f2) {
            for (int r = 18; r >= 0 && f1 != f2; r--) {
                if (parents[f1][r] != parents[f2][r]) {
                    f1 = parents[f1][r];
                    f2 = parents[f2][r];
                }
            }
            return f1 == f2 ? f1 : parents[f1][0];
        }
    }


    private static class P {
        private boolean b;
        private final int ind;
        private final int parent;

        public P(int i, boolean b, int par) {
            this.ind = i;
            this.b = b;
            this.parent = par;

        }
    }

    private static void dfs(int start, int[][] neig, Consumer<int[]> onAdd, Consumer<int[]> onRemove) {
        ArrayList<P> toVisit = new ArrayList<P>(3000);
        toVisit.add(new P(start, true, -1));
        boolean[] vis = new boolean[neig.length];
        vis[start] = true;
        int[] level = new int[neig.length];
        while (toVisit.size() > 0) {
            P ppr = toVisit.remove(toVisit.size() - 1);
            if (!ppr.b) {
                onRemove.accept(new int[]{ppr.ind, level[ppr.ind], ppr.parent});
                continue;
            }
            ppr.b = false;
            int i = ppr.ind;
            toVisit.add(ppr);
            onAdd.accept(new int[]{ppr.ind, level[ppr.ind], ppr.parent});
            for (int kk : neig[i]) {
                if (!vis[kk]) {
                    vis[kk] = true;
                    level[kk] = level[i] + 1;
                    toVisit.add(new P(kk, true, i));
                }
            }
        }


    }


    private static int[][] tr(int n) {
        int[][] x = new int[2][n - 1];
        for (int i = 0; i < n - 1; i++) {
            x[0][i] = sc.nextInt() - 1;
            x[1][i] = sc.nextInt() - 1;
        }
        return pn(x, n);
    }

    private static int[][] pn(int[][] x, int n) {
        int[] ct = new int[n];
        int[][] res = new int[n][];
        for (int v : x[0]) {
            ct[v]++;
        }
        for (int v : x[1]) {
            ct[v]++;
        }
        for (int l = 0; l < n; l++) {
            res[l] = new int[ct[l]];
        }
        for (int i = 0; i < x[0].length; i++) {
            res[x[0][i]][--ct[x[0][i]]] = x[1][i];
            res[x[1][i]][--ct[x[1][i]]] = x[0][i];
        }
        return res;
    }


    private static boolean isset(long i, int k) {
        return (i & (1 << k)) > 0;
    }

    private static void solveT() throws IOException {
        int t = sc.nextInt();
        while (t-- > 0) {
            solve();
        }
    }


    private static long gcd(long l, long l1) {
        if (l > l1) return gcd(l1, l);
        if (l == 0) return l1;
        return gcd(l1 % l, l);
    }

    private static long pow(long a, long b, long m) {
        if (b == 0) return 1;
        if (b == 1) return a;
        long pp = pow(a, b / 2, m);
        pp *= pp;
        pp %= m;
        return (pp * (b % 2 == 0 ? 1 : a)) % m;
    }


    static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        MyScanner(BufferedReader br) {
            this.br = br;
        }

        public MyScanner(InputStream in) {
            this(new BufferedReader(new InputStreamReader(in)));
        }

        void findToken() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }

        String next() {
            findToken();
            return st.nextToken();
        }

        Integer[] nab(int n) {
            Integer[] k = new Integer[n];
            for (int i = 0; i < n; i++) {
                k[i] = sc.fi();
            }
            return k;
        }

        int[] na(int n) {
            int[] k = new int[n];
            for (int i = 0; i < n; i++) {
                k[i] = sc.fi();
            }
            return k;
        }

        long[] nl(int n) {
            long[] k = new long[n];
            for (int i = 0; i < n; i++) {
                k[i] = sc.nextLong();
            }
            return k;
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        int fi() {
            String t = next();
            int cur = 0;
            boolean n = t.charAt(0) == '-';
            for (int a = n ? 1 : 0; a < t.length(); a++) {
                cur = cur * 10 + t.charAt(a) - '0';
            }
            return n ? -cur : cur;
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }
    }


}