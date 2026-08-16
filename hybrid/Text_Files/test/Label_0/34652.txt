import java.lang.*;
import java.util.*;
import java.io.*;

public class Main {
    static FastScanner in = new FastScanner();

    static void solve() {
        int n = in.nextInt();
        int[] pre = new int[n];
        int val = 0;
        for (int i = 0; i < n; ++i) {
            int x = in.nextInt();
            pre[i] = (i == 0 ? 0 : pre[i - 1]) ^ x;
        }

        boolean good = (pre[n - 1] == 0);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                good = good | (pre[i] == (pre[j] ^ pre[i]) && pre[i] == (pre[n - 1] ^ pre[j]));
            }
        }
        System.out.println(good ? "YES" : "NO");
    }

    public static void main(String[] args) {
        int T = in.nextInt();
        while (T-- > 0)
            solve();
    }

    static class Pair<X, Y> {
        X x;
        Y y;

        public Pair(X x, Y y) {
            this.x = x;
            this.y = y;
        }
    }
}

class FastScanner {
    BufferedReader br;
    StringTokenizer st;

    public FastScanner() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
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

    String nextLine() {
        String str = "";
        try {
            str = br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return str;
    }
}
