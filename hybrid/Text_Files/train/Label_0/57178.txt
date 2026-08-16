import java.util.*;
import java.io.PrintWriter;
public class Main{

    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[][] arr = new int[n][2];

    long MOD = 998244353;

    public static void main(String[] args){
        new Main().run();
    }

    void run() {
        for (int i=0; i<n; i++) {
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
        }
        Arrays.sort(arr, (a, b) -> (a[0] - b[0]));
        SegTree st = new SegTree(n);

        int[] maxIdx = new int[n];
        for (int i=n-1; 0<=i; i--) {
            int idx = upperbound(i, n, arr[i][0]+arr[i][1]-1);
            maxIdx[i] = Math.max(i, st.query(i+1, idx));
            st.update(i, maxIdx[i]);
        }
        long[] dp = new long[n+1];
        dp[n] = 1;
        for (int i=n-1; 0<=i; i--) {
            dp[i] += dp[i+1] + dp[maxIdx[i]+1];
            dp[i] %= MOD;
        }
        System.out.println(dp[0]);
    }

    int upperbound(int l, int r, int d) {
        while (r - l > 1) {
            int mid = (r + l) / 2;
            if (arr[mid][0] > d) {
                r = mid;
            } else {
                l = mid;
            }
        }
        return r;
    }

    class SegTree {
        int n = 1;
        int[] val;

        public SegTree(int n) {
            while (this.n < n) this.n *= 2;
            val = new int[2*this.n-1];
        }

        void update(int k, int v) {
            k += n - 1;
            val[k] = v;
            while (k > 0) {
                k = (k - 1) / 2;
                val[k] = Math.max(val[2*k+1], val[2*k+2]);
            }
        }

        int query(int a, int b) {
            return query(0, n, a, b, 0);
        }

        int query(int l, int r, int a, int b, int k) {
            if (r<=a || b<=l) return Integer.MIN_VALUE;
            if (a<=l && r<=b) return val[k];
            else {
                int vl = query(l, (l+r)/2, a, b, 2*k+1);
                int vr = query((l+r)/2, r, a, b, 2*k+2);
                return Math.max(vl, vr);
            }

        }
    }
}
