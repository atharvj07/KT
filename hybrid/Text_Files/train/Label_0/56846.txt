import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author beginner1010
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskC solver = new TaskC();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskC {
        final int INF = 1 << 29;
        int n;
        int m;
        Integer[] firstIndex;
        int[][][] coveredMask;
        int[][][] cost;
        int[][] dp;

        int two(int x) {
            return 1 << x;
        }

        boolean contain(int mask, int x) {
            return (mask & two(x)) > 0;
        }

        int rec(int posChar, int mask) {
            if (mask == two(n) - 1)
                return 0;
            if (posChar == m) {
                return INF;
            }

            int res = dp[posChar][mask];
            if (res != -1)
                return res;

            res = rec(posChar + 1, mask);
            Integer idx = firstIndex[mask];
            res = Math.min(res,
                    rec(0, mask | coveredMask[0][idx][posChar]) + cost[0][idx][posChar]);
            res = Math.min(res,
                    rec(0, mask | coveredMask[1][idx][posChar]) + cost[1][idx][posChar]);

            return dp[posChar][mask] = res;
        }

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            this.n = in.nextInt();
            this.m = in.nextInt();

            firstIndex = new Integer[two(n)];
            for (int i = 0; i < two(n); i++) {
                firstIndex[i] = -1;
                for (int j = 0; j < n; j++) {
                    if (contain(i, j) == false) {
                        firstIndex[i] = j;
                        break;
                    }
                }
            }

            coveredMask = new int[2][n][m];
            cost = new int[2][n][m];

            ArrayList<String> bag = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                String s = in.next();
                bag.add(s);
            }

            int[][] A = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    A[i][j] = in.nextInt();
                }
            }

            for (int i = 0; i < n; i++) {
                for (int k = 0; k < m; k++) {
                    int max = 0;
                    for (int j = 0; j < n; j++) {
                        if (bag.get(i).charAt(k) == bag.get(j).charAt(k)) {
                            coveredMask[0][i][k] |= two(j);
                            cost[0][i][k] += A[j][k];
                            max = Math.max(max, A[j][k]);
                        }
                    }
                    cost[0][i][k] -= max;
                    coveredMask[1][i][k] |= two(i);
                    cost[1][i][k] = A[i][k];
                }
            }

            dp = new int[m][two(n)];
            for (int[] one : dp) {
                Arrays.fill(one, -1);
            }
            int ans = rec(0, 0);
            out.println(ans);
            return;
        }

    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

