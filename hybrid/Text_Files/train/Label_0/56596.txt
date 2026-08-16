import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Solution {

    BufferedReader in;
    PrintWriter out;
    StringTokenizer st;

    int[] v;
    boolean[] was;

    int end;

    void dfs(int v) {
        while (true) {
            was[v] = true;
            if (this.v[v] == -1) {
                end = v;
                break;
            } else {
                if (!was[this.v[v]])
                    v = this.v[v];
                else {
                    end = v;
                    break;
                }
            }
        }
    }

    void solve() throws IOException {
        int n = ni();
        v = new int[n];
        Arrays.fill(v, -1);
        int[] cnt = new int[n];
        for (int i = 0; i < n; ++i) {
            int a = ni() - 1;
            v[i] = a;
            cnt[a]++;
        }
        ArrayList<int[]> res = new ArrayList<int[]>();
        was = new boolean[n];
        for (int i = 0; i < n; ++i)
            if (cnt[i] == 0) {
                dfs(i);
                res.add(new int[] { i, end });
            }
        for (int i = 0; i < n; ++i)
            if (!was[i]) {
                dfs(i);
                res.add(new int[] { i, i });
            }
        if (res.size() == 1 && res.get(0)[0] == res.get(0)[1])
            out.println(0);
        else {
            out.println(res.size());
            for (int i = 0; i < res.size(); ++i) {
                int j = (i + 1) % res.size();
                out.println((res.get(i)[1] + 1) + " " + (res.get(j)[0] + 1));
            }
        }
    }

    public Solution() throws IOException {
        Locale.setDefault(Locale.US);
        in = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        solve();
        in.close();
        out.close();
    }

    String ns() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            st = new StringTokenizer(in.readLine());
        }
        return st.nextToken();
    }

    int ni() throws IOException {
        return Integer.valueOf(ns());
    }

    long nl() throws IOException {
        return Long.valueOf(ns());
    }

    double nd() throws IOException {
        return Double.valueOf(ns());
    }

    public static void main(String[] args) throws IOException {
        new Solution();
    }
}
