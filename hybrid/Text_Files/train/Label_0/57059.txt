import java.util.*;
import java.io.*;

public class Main {

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

        public float nextFloat() {
            return Float.parseFloat(next());
        }

        public double nextDouble() {
            return Float.parseFloat(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }
    }

    static InputReader sc;
    static PrintWriter pw;

    static long[] sums;
    static long[] dp;

    public static void main(String[] args) throws Exception {
        sc = new InputReader(System.in);
        pw = new PrintWriter(System.out);

        Thread t=new Thread(null, null, "", 1<<28) {
            public void run() {
                int n = sc.nextInt();
                int[][] grid = new int[n][n];

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        grid[i][j] = sc.nextInt();
                    }
                }

                sums = new long[1 << n];
                for (int i = 0; i < 1 << n; i++) {
                    for (int j = 0; j < n; j++) {
                        if ((i & (1 << j)) != 0) {
                            for (int k = j + 1; k < n; k++) {
                                if ((i & (1 << k)) != 0) {
                                    sums[i] += grid[j][k];
                                }
                            }
                        }
                    }
                }

                dp = new long[1 << n];
                for (int i = 1; i < (1 << n); i++) {
                    dp[i] = Long.MIN_VALUE;
                }

                for (int i = 0; i < 1 << n; i++) {
                    ArrayList<Integer> arrayList = new ArrayList<>();
                    for (int j = 0; j < n; j++) {
                        if (((1 << j) & i) == 0) {
                            arrayList.add(j);
                        }
                    }

                    rec(0, arrayList, dp[i], i, 0);
                }

                pw.println(dp[(1 << n) - 1]);

                pw.close();
            }
        };
        t.start();
        t.join();
    }


    static void rec(int i, ArrayList<Integer> not_taken, long score_so_far, int mask, int group) {
        // i - the value we are considering to add from not_taken
        // not taken is the array of values not in the current mask
        //
        if (i == not_taken.size()) {
            // base case
            dp[mask] = Math.max(dp[mask], score_so_far + sums[group]);
            return;
        }

        rec(i+1, not_taken, score_so_far, mask, group);
        rec(i+1, not_taken, score_so_far, mask ^ (1 << not_taken.get(i)), group ^ (1 << not_taken.get(i))); // group is the exact group that is used
    }
}


