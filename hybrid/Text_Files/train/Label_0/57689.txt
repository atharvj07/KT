/*
Keep solving problems.
*/

import java.util.*;
import java.io.*;

public class CFA {
    BufferedReader br;
    PrintWriter out;
    StringTokenizer st;
    boolean eof;
    final long MOD = 1000L * 1000L * 1000L + 7;
    int[] dx = {0, -1, 0, 1};
    int[] dy = {1, 0, -1, 0};

    void solve() throws IOException {
        int n = nextInt();
        long[] arr = nextLongArr(n);
        long[] pref = new long[1 + n];
        int cnt = 0;
        Map<Long, Integer> hm = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            pref[i] = pref[i - 1] + arr[i - 1];
            hm.put(pref[i], hm.getOrDefault(pref[i], 0) + 1);
        }
        for (Map.Entry<Long, Integer> entry : hm.entrySet()) {
            cnt = Math.max(cnt, entry.getValue());
        }

        out(n - cnt);
    }

    void shuffle(int[] a) {
        int n = a.length;
        for(int i = 0; i < n; i++) {
            int r = i + (int) (Math.random() * (n - i));
            int tmp = a[i];
            a[i] = a[r];
            a[r] = tmp;
        }
    }

    long gcd(long a, long b) {
        while(a != 0 && b != 0) {
            long c = b;
            b = a % b;
            a = c;
        }
        return a + b;
    }

    private void outln(Object o) {
        out.println(o);
    }
    private void out(Object o) {
        out.print(o);
    }
    public CFA() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        solve();
        out.close();
    }
    public static void main(String[] args) throws IOException {
        new CFA();
    }

    public long[] nextLongArr(int n) throws IOException{
        long[] res = new long[n];
        for(int i = 0; i < n; i++)
            res[i] = nextLong();
        return res;
    }
    public int[] nextIntArr(int n) throws IOException {
        int[] res = new int[n];
        for(int i = 0; i < n; i++)
            res[i] = nextInt();
        return res;
    }
    public String nextToken() {
        while (st == null || !st.hasMoreTokens()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (Exception e) {
                eof = true;
                return null;
            }
        }
        return st.nextToken();
    }
    public String nextString() {
        try {
            return br.readLine();
        } catch (IOException e) {
            eof = true;
            return null;
        }
    }
    public int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }
    public long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }
    public double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }
}

