import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    FastScanner in;
    PrintWriter out;

    void solve() {
        char[] s = in.next().toCharArray();
        int n = s.length;
        // used chars; cnt0; cnt1
        boolean[][][] dp = new boolean[n + 1][n + 1][n + 1];
        dp[0][0][0] = true;
        for (int used = 0; used <= n; used++) {
            for (int cnt0 = n; cnt0 >= 0; cnt0--) {
                for (int cnt1 = n; cnt1 >= 0; cnt1--) {
                    if (!dp[used][cnt0][cnt1]) {
                        continue;
                    }
                    if (used + 2 <= n) {
                        int f1 = s[used] - '0';
                        int f2 = s[used + 1] - '0';
                        if (f1 == 0 || f2 == 0) {
                            dp[used + 2][cnt0 + 1][cnt1] = true;
                        }
                        if (f1 == 1 || f2 == 1) {
                            dp[used + 2][cnt0][cnt1 + 1] = true;
                        }
                    }
                    if (used + 1 <= n) {
                        int f1 = s[used] - '0';

                        dp[used + 1][cnt0][cnt1] = true;
                        if (f1 == 0) {
                            if (cnt0 > 0) {
                                dp[used + 1][cnt0][cnt1] = true;
                            }
                            if (cnt1 > 0) {
                                dp[used + 1][cnt0 + 1][cnt1 - 1] = true;
                            }
                        } else {
                            if (cnt1 > 0) {
                                dp[used + 1][cnt0][cnt1] = true;
                            }
                            if (cnt0 > 0) {
                                dp[used + 1][cnt0 - 1][cnt1 + 1] = true;
                            }
                        }
                    }
                    if (cnt0 > 0) {
                        dp[used][cnt0 - 1][cnt1] = true;
                    }
                    if (cnt1 > 0) {
                        dp[used][cnt0][cnt1 - 1] = true;
                    }
                }
            }
        }
        // {need0, need1}
        int[][] ways = new int[n + 1][n + 1];
        ways[0][0] = 1;
        int res = 0;
        int[][] nways = new int[n + 1][n + 1];
        for (int len = 1; len <= n; len++) {
            for (int i = 0; i < nways.length; i++) {
                Arrays.fill(nways[i], 0);
            }
            for (int need0 = 0; need0 < ways.length; need0++) {
                for (int need1 = 0; need1 < ways[need0].length; need1++) {
                    int c = ways[need0][need1];
                    if (c == 0) {
                        continue;
                    }
                    {
                        // 0
                        int sufLen = len - need0 - need1;
                        int used = n - sufLen;
                        if (s[used] == '0') {
                            nways[need0][need1] = add(nways[need0][need1], c);
                        } else {
                            nways[need0 + 1][need1] = add(nways[need0 + 1][need1], c);
                        }
                    }
                    {
                        // 1
                        int sufLen = len - need0 - need1;
                        int used = n - sufLen;
                        if (s[used] == '1') {
                            nways[need0][need1] = add(nways[need0][need1], c);
                        } else {
                            nways[need0][need1 + 1] = add(nways[need0][need1 + 1], c);
                        }
                    }
                }
            }
            int[][] tmp = ways;
            ways = nways;
            nways = tmp;
            for (int need0 = 0; need0 < ways.length; need0++) {
                for (int need1 = 0; need1 < ways[need0].length; need1++) {
                    if (ways[need0][need1] == 0) {
                        continue;
                    }
                    int sufLen = len - need0 - need1;
                    int used = n - sufLen;
                    if (dp[used][need0][need1]) {
                        res = add(res, ways[need0][need1]);
//                        System.err.println("len = " + len + ", res = " + res);
                    }
                }
            }
        }
        out.println(res);
    }

    final int mod = 998244353;

    int mul(int x, int y) {
        return (int) ((x * 1L * y) % mod);
    }

    int add(int x, int y) {
        x += y;
        return x >= mod ? (x - mod) : x;
    }

    void run() {
        try {
            in = new FastScanner(new File("Main.in"));
            out = new PrintWriter(new File("Main.out"));

            solve();

            out.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    void runIO() {

        in = new FastScanner(System.in);
        out = new PrintWriter(System.out);

        solve();
        out.close();
    }

    class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner(File f) {
            try {
                br = new BufferedReader(new FileReader(f));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        public FastScanner(InputStream f) {
            br = new BufferedReader(new InputStreamReader(f));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                String s = null;
                try {
                    s = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (s == null)
                    return null;
                st = new StringTokenizer(s);
            }
            return st.nextToken();
        }

        boolean hasMoreTokens() {
            while (st == null || !st.hasMoreTokens()) {
                String s = null;
                try {
                    s = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (s == null)
                    return false;
                st = new StringTokenizer(s);
            }
            return true;
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }
    }

    public static void main(String[] args) {
        new Main().runIO();
    }
}