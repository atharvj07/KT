import java.util.*;
import java.io.*;
import java.lang.*;

public class Solution {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter out = new PrintWriter(System.out);
    StringTokenizer st = new StringTokenizer("");

    String next() {
        if (!st.hasMoreTokens()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (Exception e) {

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

    public static void main(String[] args) {
        new Solution().solve();
    }

    int gcd(int a, int b) {
        if (a == 0)
            return b;
        return gcd(b % a, a);
    }

    void solve() {
        int t = 1;
        t = nextInt();
        for (int tt = 0; tt < t; tt++) {
            int n = nextInt();
            out.println(100 / gcd(n, 100));
        }
        out.close();
    }
}
