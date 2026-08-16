import java.io.*;
import java.util.*;

public class E {

    BufferedReader in;
    StringTokenizer st;
    PrintWriter out;

    String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(in.readLine());
        return st.nextToken();
    }

    int nextInt() throws Exception {
        return Integer.parseInt(next());
    }

    long nextLong() throws Exception {
        return Long.parseLong(next());
    }

    double nextDouble() throws Exception {
        return Double.parseDouble(next());
    }

    void solve() throws Exception {
        int n = nextInt();
        int m = nextInt();

        int[] Q = new int[m];
        int[] W = new int[m];

        int[] d1q = new int[2 * n];
        int[] d2q = new int[2 * n];
        int[] hq = new int[n];
        int[] vq = new int[n];

        int[] d1w = new int[2 * n];
        int[] d2w = new int[2 * n];
        int[] hw = new int[n];
        int[] vw = new int[n];

        for (int i = 0; i < n; i++) {
            hw[i] = Integer.MIN_VALUE;
            vw[i] = Integer.MIN_VALUE;
            hq[i] = Integer.MAX_VALUE;
            vq[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < 2 * n; i++) {
            d1w[i] = Integer.MIN_VALUE;
            d2w[i] = Integer.MIN_VALUE;
            d1q[i] = Integer.MAX_VALUE;
            d2q[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < m; i++) {
            int q = nextInt() - 1;
            Q[i] = q;
            int w = nextInt() - 1;
            W[i] = w;

            hq[q] = Math.min(hq[q], w);
            vq[w] = Math.min(vq[w], q);
            hw[q] = Math.max(hw[q], w);
            vw[w] = Math.max(vw[w], q);

            int d1n = q - w + n - 1;
            int d2n = w + q;
            d1q[d1n] = Math.min(d1q[d1n], w);
            d2q[d2n] = Math.min(d2q[d2n], w);
            d1w[d1n] = Math.max(d1w[d1n], w);
            d2w[d2n] = Math.max(d2w[d2n], w);
        }
        int[] tot = new int[9];
        for (int i = 0; i < 9; i++)
            tot[i] = 0;

        for (int i = 0; i < m; i++) {
            int ans = 8;
            int q = Q[i];
            int w = W[i];
            if (hq[q] == w)
                ans--;
            if (vq[w] == q)
                ans--;
            if (hw[q] == w)
                ans--;
            if (vw[w] == q)
                ans--;

            int d1n = q - w + n - 1;
            int d2n = w + q;
            if (d1q[d1n] == w)
                ans--;
            if (d2q[d2n] == w)
                ans--;
            if (d1w[d1n] == w)
                ans--;
            if (d2w[d2n] == w)
                ans--;
            tot[ans]++;
        //  out.print(ans);
        }
        
        for (int i = 0; i < 9; i++)
            out.print(tot[i] + " ");
    }

    void run() {
        try {
            Locale.setDefault(Locale.US);
            in = new BufferedReader(new InputStreamReader((System.in)));
            out = new PrintWriter(System.out);

            solve();
            out.close();
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    public static void main(String[] args) {
        new E().run();

    }

}
