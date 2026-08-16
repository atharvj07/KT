import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader in;
    static PrintWriter out;
    static StringTokenizer tok;

    void solve() throws IOException {
        int N = ni();
        int W = ni();

        ArrayList<Integer> vlist = new ArrayList<>();
        ArrayList<Integer> wlist = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int v = ni();
            int w = ni();
            int m = ni();
            int p = 1;
            int tv = v;
            int tw = w;
            while (true) {
                if (m > p) {
                    m -= p;
                } else {
                    vlist.add(m * v);
                    wlist.add(m * w);
                    break;
                }
                vlist.add(tv);
                wlist.add(tw);
                tv *= 2;
                tw *= 2;
                p *= 2;
            }
        }

        int n = vlist.size();

        int[][] dp = new int[n + 1][W + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= W; j++) {
                if (j < wlist.get(i)) {
                    dp[i + 1][j] = dp[i][j];
                } else {
                    dp[i + 1][j] = Math.max(dp[i][j], dp[i][j - wlist.get(i)] + vlist.get(i));
                }
            }
        }

        out.println(dp[n][W]);
    }

    String ns() throws IOException {
        while (!tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine(), " ");
        }
        return tok.nextToken();
    }

    int ni() throws IOException {
        return Integer.parseInt(ns());
    }

    long nl() throws IOException {
        return Long.parseLong(ns());
    }

    double nd() throws IOException {
        return Double.parseDouble(ns());
    }

    String[] nsa(int n) throws IOException {
        String[] res = new String[n];
        for (int i = 0; i < n; i++) {
            res[i] = ns();
        }
        return res;
    }

    int[] nia(int n) throws IOException {
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = ni();
        }
        return res;
    }

    long[] nla(int n) throws IOException {
        long[] res = new long[n];
        for (int i = 0; i < n; i++) {
            res[i] = nl();
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        tok = new StringTokenizer("");
        Main main = new Main();
        main.solve();
        out.close();
    }
}