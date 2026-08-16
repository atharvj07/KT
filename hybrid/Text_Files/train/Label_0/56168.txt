import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader inp = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Solver solver = new Solver();
        solver.solve(inp, out);
        out.close();
    }

    private static class Solver {

        int[] a;
        int min = Integer.MAX_VALUE;
        boolean[] dp;
        boolean[] set;

        private boolean win(int k) {
            Stack<Integer> solve = new Stack<>();
            solve.add(k);

            while (!solve.isEmpty()) {
                int k2 = solve.peek();
                if (set[k2]) {
                    solve.pop();
                    continue;
                }

                boolean win = true;
                boolean skip = false;
                for (int i: a) {
                    if (k2 - i >= 0 && !set[k2 - i]) {
                        skip = true;
                        solve.add(k2 - i);
                    } else if (k2 - i >= 0) {
                        win &= dp[k2 - i];
                    }
                }
                if (!skip) {
                    solve.pop();
                    set[k2] = true;
                    dp[k2] = !win;
                }
            }
            return dp[k];
        }

        private void solve(InputReader inp, PrintWriter out) {
            int n = inp.nextInt(), k = inp.nextInt();
            a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = inp.nextInt();
                min = Math.min(min, a[i]);
            }
            dp = new boolean[k+1];
            set = new boolean[k+1];
            out.print(win(k) ? "First" : "Second");
        }
    }

    static class InputReader {
        BufferedReader reader;
        StringTokenizer tokenizer;

        InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        String next() {
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
        public long nextLong() {
            return Long.parseLong(next());
        }
        public double nextDouble() {
            return Double.parseDouble(next());
        }
    }
}

