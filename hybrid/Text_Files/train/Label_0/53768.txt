import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        C_Shift solver = new C_Shift();
        solver.solve(1, in, out);
        out.close();
    }

    static class C_Shift {
        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            final int MOD = 998244353;
            char[] s = in.next().toCharArray();
            int[] a = extractBlocksOfOnes(s);
            int n = a.length;
            int k = in.nextInt();
            k = Math.min(k, s.length);
            int[][] d = new int[k + 1][k + 1];
            int[][] nd = new int[k + 1][k + 1];
            d[0][k] = 1;
            for (int i = n - 1; i >= 0; i--) {
                for (int[] arr : nd) {
                    Arrays.fill(arr, 0);
                }
                for (int inHand = 0; inHand <= k; inHand++) {
                    for (int liberties = 0; liberties <= k; liberties++) {
                        if (d[inHand][liberties] == 0) {
                            continue;
                        }
                        for (int leaveHere = Math.max(0, a[i] - liberties); leaveHere <= a[i] + inHand; leaveHere++) {
                            int nInHand = inHand + a[i] - leaveHere;
                            int nLiberties = liberties - Math.max(0, nInHand - inHand);
                            nd[nInHand][nLiberties] += d[inHand][liberties];
                            if (nd[nInHand][nLiberties] >= MOD) {
                                nd[nInHand][nLiberties] -= MOD;
                            }
                        }
                    }
                }
                int[][] t = d;
                d = nd;
                nd = t;
            }
            int ans = 0;
            for (int liberties = 0; liberties <= k; liberties++) {
                ans += d[0][liberties];
                if (ans >= MOD) {
                    ans -= MOD;
                }
            }
            out.println(ans);
        }

        private int[] extractBlocksOfOnes(char[] s) {
            List<Integer> blocks = new ArrayList<>();
            int last = 0;
            for (int i = 0; i <= s.length; i++) {
                if (i == s.length || s[i] == '0') {
                    blocks.add(last);
                    last = 0;
                } else {
                    ++last;
                }
            }
            int[] ret = new int[blocks.size()];
            for (int i = 0; i < ret.length; i++) {
                ret[i] = blocks.get(i);
            }
            return ret;
        }

    }

    static class FastScanner {
        private BufferedReader in;
        private StringTokenizer st;

        public FastScanner(InputStream stream) {
            in = new BufferedReader(new InputStreamReader(stream));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(in.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

