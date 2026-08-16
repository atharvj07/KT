import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

/**
 * @author Don Li
 */
public class LipshitzSequence {

    void solve() {
        int n = in.nextInt(), Q = in.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) A[i] = in.nextInt();

        // D[i] = the Lipschitz constant for [i,i+1]
        long[] D = new long[n - 1];
        for (int i = 0; i < n - 1; i++) D[i] = Math.abs(A[i + 1] - A[i]);

        // a[i] = the index of leftmost element in D that is less than D[i]
        int[] a = new int[n - 1];
        a[0] = 0;
        for (int i = 1; i < n - 1; i++) {
            if (D[i] <= D[i - 1]) {
                a[i] = i;
            } else {
                int j = a[i - 1];
                while (j > 0 && D[i] > D[j - 1]) j = a[j - 1];
                a[i] = j;
            }
        }

        // b[i] = the index of rightmost element in D that is less than or equal to D[i]
        int[] b = new int[n - 1];
        b[n - 2] = n - 2;
        for (int i = n - 3; i >= 0; i--) {
            if (D[i] < D[i + 1]) {
                b[i] = i;
            } else {
                int j = b[i + 1];
                while (j < n - 2 && D[i] >= D[j + 1]) j = b[j + 1];
                b[i] = j;
            }
        }

        for (int q = 0; q < Q; q++) {
            int l = in.nextInt() - 1, r = (in.nextInt() - 1) - 1;
            long res = 0;
            // for each D[i]
            for (int i = l; i <= r; i++) {
                // count num of subarrays that choose D[i] as the Lipschitz constant
                long times = (long) (i - Math.max(l, a[i]) + 1) * (Math.min(r, b[i]) - i + 1);
                res += D[i] * times;
            }
            out.println(res);
        }
    }

    public static void main(String[] args) {
        in = new FastScanner(new BufferedReader(new InputStreamReader(System.in)));
        out = new PrintWriter(System.out);
        new LipshitzSequence().solve();
        out.close();
    }

    static FastScanner in;
    static PrintWriter out;

    static class FastScanner {
        BufferedReader in;
        StringTokenizer st;

        public FastScanner(BufferedReader in) {
            this.in = in;
        }

        public String nextToken() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(in.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(nextToken());
        }

        public long nextLong() {
            return Long.parseLong(nextToken());
        }

        public double nextDouble() {
            return Double.parseDouble(nextToken());
        }
    }
}
