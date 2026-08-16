import java.io.*;
import java.util.*;

public class Solution {


    static MyScanner sc;
    private static PrintWriter out;
    static long M2 = 1_000_000_000L + 7;

    private static HashMap<Long, Long>[] mods;

    public static void main(String[] s) throws Exception {
        StringBuilder stringBuilder = new StringBuilder();


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


    }


    private static void solve() {
        int n = sc.nextInt();
        long time = sc.nextLong();

        int[][] data = new int[n][4];
        ArrayList<Integer>[] torem = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            torem[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            data[i][0] = sc.nextInt();
            data[i][1] = sc.nextInt();
            data[i][2] = i + 1;
        }
        Arrays.sort(data, (l1, l2) -> l1[1] - l2[1]);
        for (int i = 0; i < n; i++) {
            torem[data[i][0]].add(i);
        }
        long curT = 0;
        int curN = 0;
        int curIndex = -1;
        for (int f = 1; f <= n; f++) {
            int ncurn = curN;
            int ncuri = curIndex;
            for (int s : torem[f - 1]) {
                if (s <= curIndex) {
                    curT -= data[s][1];
                    ncurn--;
                }
            }


            while (ncurn != f && ncuri + 1 < n) {
                ncuri++;
                if (data[ncuri][0] >= f) {
                    ncurn++;
                    curT += data[ncuri][1];
                }
            }
            if (curT > time || ncurn < f) break;

            curN = f;
            curIndex = ncuri;
        }


        out.println(curN);
        out.println(curN);
        for (int i = 0; i <= curIndex; i++) {
            if (data[i][0] >= curN) {
                out.print(data[i][2] + " ");
            }
        }

    }

    private static boolean solve(int n, int p, int p1, int i) {
        return false;
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