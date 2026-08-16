import java.io.*;
import java.util.*;

public class Main {
    private FastScanner in;
    private PrintWriter out;

    final int mod = (int) 1e9 + 7;

    ArrayList<Integer>[] g;


    long[][] go(int v) {
        long[][] dp = new long[3][1];
        dp[0][0] = 1;
        for (int to : g[v]) {
            long[][] child = go(to);
            int maxK = child[0].length;
            long[][] ndp = new long[3][dp[0].length + maxK];
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < dp[i].length; j++) {
                    long cur = dp[i][j];
                    if (cur == 0) {
                        continue;
                    }
                    for (int i2 = 0; i2 < 2; i2++) {
                        for (int j2 = 0; j2 < child[i2].length; j2++) {
                            long chWays = child[i2][j2];
                            if (chWays == 0) {
                                continue;
                            }
                            int nextI = i + i2;
                            if (nextI >= 3) {
                                continue;
                            }
                            int nextJ = j + j2;
                            ndp[nextI][nextJ] = (int) ((ndp[nextI][nextJ] + cur * chWays) % mod);
                        }
                    }
                }
            }
            dp = ndp;
        }
        long[][] res = new long[2][dp[0].length + 1];
        for (int j = 0; j < dp[0].length; j++) {
            {
                long cur0 = dp[0][j];
                res[0][j] += cur0;
                if (res[0][j] >= mod) {
                    res[0][j] -= mod;
                }
                res[1][j + 1] += cur0;
                if (res[1][j + 1] >= mod) {
                    res[1][j + 1] -= mod;
                }
            }
            {
                res[0][j] += dp[1][j] + dp[1][j];
                while (res[0][j] >= mod) {
                    res[0][j] -= mod;
                }
                res[1][j + 1] += dp[1][j];
                if (res[1][j + 1] >= mod) {
                    res[1][j + 1] -= mod;
                }
            }
            {
                res[0][j] += dp[2][j] + dp[2][j];
                while (res[0][j] >= mod) {
                    res[0][j] -= mod;
                }
            }
        }
        return res;
    }

    private void solve() {
        int n = in.nextInt();
        g = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            g[i] = new ArrayList<>();
        }
        for (int i = 1; i < n; i++) {
            g[in.nextInt() - 1].add(i);
        }
        long[][] go = go(0);
        long[] fact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i < fact.length; i++) {
            fact[i] = fact[i - 1] * i % mod;
        }
        long result = 0;
        for (int i = 0; i < go[0].length; i++) {
            if (go[0][i] == 0) {
                continue;
            }
            long ways = go[0][i] * fact[n - i] % mod;
            if (i % 2 == 1) {
                ways = mod - ways;
            }
            result += ways;
        }
        out.println(result % mod);
    }

    private void run() {
        try {
            in = new FastScanner(new File("CF17_Exhibition_A.in"));
            out = new PrintWriter(new File("CF17_Exhibition_A.out"));

            solve();

            out.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private void runIO() {
        in = new FastScanner(System.in);
        out = new PrintWriter(System.out);

        solve();

        out.close();
    }

    private class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(File f) {
            try {
                br = new BufferedReader(new FileReader(f));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        FastScanner(InputStream f) {
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