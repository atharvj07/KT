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
        private void solve(InputReader inp, PrintWriter out) {
            int n = inp.nextInt();
            ArrayList<Integer>[] tree = new ArrayList[n];
            for (int i = 0; i < n; i++) tree[i] = new ArrayList<>();
            for (int i = 0; i < n - 1; i++) {
                int x = inp.nextInt() - 1, y = inp.nextInt() - 1;
                tree[x].add(y);
                tree[y].add(x);
            }
            int[] topo = topologicalSort(tree);
            long[][] dp = new long[n][2];
            long MOD = 1000000007;
            for (int node: topo) {
                long white = 1;
                long black = 1;
                for (int child: tree[node]) {
                    if (dp[child][0] == 0) continue;
                    white = (white * (dp[child][0] + dp[child][1])) % MOD;
                    black = (black * dp[child][0]) % MOD;
                }
                dp[node][0] = white;
                dp[node][1] = black;
            }
            out.print((dp[topo[n-1]][0] + dp[topo[n-1]][1]) % MOD);
        }

        private static int[] topologicalSort(ArrayList<Integer>[] graph) {
            int n = graph.length;
            int[] in_degree = new int[n];
            for (int i = 0; i < n; i++) {
                for (int to: graph[i]) in_degree[to]++;
            }
            int[] res = new int[n];
            int j = 0;
            for (int i = 0; i < n; i++) {
                if (in_degree[i] == 1) res[j++] = i;
            }
            for (int i = 0; i < j; i++) {
                for (int to: graph[res[i]]) {
                    if (--in_degree[to] == 1) res[j++] = to;
                }
            }
            return res;
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


