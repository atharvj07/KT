import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.TreeSet;

/**
 * @author Don Li
 */
public class RatingsRealityShows2 {
    void solve() {
        int n = in.nextInt();
        long a = in.nextInt(), b = in.nextInt(), c = in.nextInt(), d = in.nextInt();
        int start = in.nextInt(), len = in.nextInt();
        int[] t = new int[n], q = new int[n];
        for (int i = 0; i < n; i++) {
            t[i] = in.nextInt();
            q[i] = in.nextInt();
        }
        
        long[] rating1 = new long[n + 1];
        long[] rating2 = new long[n + 1];
        for (int i = 0; i < n; i++) {
            rating1[i + 1] = rating1[i] + (q[i] > 0 ? a : -b);
            rating2[i + 1] = rating2[i] + (q[i] > 0 ? c : -d);
        }
        
        int[] begins = new int[n + 1];
        begins[0] = 0;
        for (int i = 0; i < n; i++) begins[i + 1] = t[i] + 1;
        
        int ql = 0, qr = 0;
        TreeSet<Integer> set = new TreeSet<>((i, j) -> {
            if (rating2[i + 1] != rating2[j + 1]) return Long.compare(rating2[i + 1], rating2[j + 1]);
            return Integer.compare(i, j);
        });
        for (int l : begins) {
            int r = l + len;
            while (ql < qr && t[ql] < l) {
                set.remove(ql);
                ql++;
            }
            while (qr < n && t[qr] < r && t[qr] >= l) {
                set.add(qr);
                qr++;
            }
            if (start + rating1[ql] < 0) {
                out.println(-1);
                return;
            }
            if (set.isEmpty() || start + rating2[set.first() + 1] - rating2[ql] + rating1[ql] >= 0) {
                out.println(l);
                return;
            }
        }
        out.println(-1);
    }
    
    public static void main(String[] args) {
        in = new FastScanner(new BufferedReader(new InputStreamReader(System.in)));
        out = new PrintWriter(System.out);
        new RatingsRealityShows2().solve();
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
