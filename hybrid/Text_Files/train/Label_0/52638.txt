import java.io.*;
import java.util.*;

public class Main {
    private FastScanner in;
    private PrintWriter out;

    private void solve() {
        int n = in.nextInt();
        int m = in.nextInt();
        boolean[][] g = new boolean[n][n];
        for (int i = 0; i < m; i++) {
            int fr = in.nextInt() - 1;
            int to = in.nextInt() - 1;
            g[fr][to] = true;
        }
        final int mod = (int) 1e9 + 7;
        int[] pow2 = new int[1000];
        pow2[0] = 1;
        for (int i = 1; i < pow2.length; i++) {
            pow2[i] = pow2[i - 1] * 2 % mod;
        }
        if (g[0][1]) {
            out.println(pow2[m]);
            return;
        }
        int[] edgesInside = new int[1 << n];
        for (int mask = 0; mask < 1 << n; mask++) {
            int edges = 0;
            for (int i = 0; i < n; i++) {
                if (((1 << i) & mask) != 0) {
                    for (int j = i + 1; j < n; j++) {
                        if (((1 << j) & mask) != 0) {
                            if (g[i][j])
                                edges++;
                        }
                    }
                }
            }
            edgesInside[mask] = edges;
        }
        int[] canReachAll = new int[1 << n];
        for (int mask = 0; mask < 1 << n; mask++) {
            int xx = (mask & 3);
            if (xx == 0 || xx == 3) {
                continue;
            }
            int root = (xx == 1 ? 0 : 1);
            int edges = edgesInside[mask];
            canReachAll[mask] = pow2[edges];
            for (int cant = mask; cant > 0; cant = (cant - 1) & mask) {
                if ((cant & (1 << root)) != 0) {
                    continue;
                }
                int inside = edgesInside[cant];
                long ways = pow2[inside];
                int can = mask ^ cant;
                ways = ways * canReachAll[can] % mod;
                canReachAll[mask] -= ways;
                if (canReachAll[mask] < 0)
                    canReachAll[mask] += mod;
            }
        }
        long result = pow2[m];
        for (int canFrom0 = 0; canFrom0 < 1 << n; canFrom0++) {
            if ((canFrom0 & 1) == 0) {
                continue;
            }
            long ways = canReachAll[canFrom0];
            int notMask = ((1 << n) - 1) ^ canFrom0;
            for (int canFrom1 = notMask; canFrom1 > 0; canFrom1 = (canFrom1 - 1) & notMask) {
                if ((canFrom1 & 2) == 0) {
                    continue;
                }
                if (edgesInside[canFrom0] + edgesInside[canFrom1] != edgesInside[canFrom0 | canFrom1]) {
                    continue;
                }

                long nowWays = canReachAll[canFrom1] * ways % mod;
                int otherMask = notMask ^ canFrom1;
                nowWays = nowWays * pow2[edgesInside[otherMask]] % mod;
                result -= nowWays;
            }
        }
        result %= mod;
        result += mod;
        out.println(result % mod);
    }

    private void run() {
        try {
            in = new FastScanner(new File("AtCoderRelayI.in"));
            out = new PrintWriter(new File("AtCoderRelayI.out"));

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