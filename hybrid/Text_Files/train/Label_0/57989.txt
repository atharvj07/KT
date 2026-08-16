import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeSet;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Bat-Orgil
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        static int mod = 1000000007;
        static int n;
        static int d;
        static int[] a;
        static ArrayList<Integer>[] G;
        static boolean[] vis;
        static int root;
        static TreeSet<Integer>[] sets;

        static long dfs(int node) {//number of ways when node is max
            vis[node] = true;
            long val = 1;
            for (int child : G[node]) {
                if (!vis[child] && a[child] <= a[root] && a[child] >= (a[root] - d) && !sets[child].contains(root)) {
                    val = (val * (dfs(child) + 1)) % mod;
                    if (a[root] == a[child]) {
                        sets[root].add(child);
                    }
                }
            }
            return val;
        }

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            d = in.nextInt();
            n = in.nextInt();
            a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = in.nextInt();
            }
            G = new ArrayList[n];
            sets = new TreeSet[n];

            for (int i = 0; i < n; i++) {
                G[i] = new ArrayList();
                sets[i] = new TreeSet();
            }
            for (int i = 0; i < (n - 1); i++) {
                int a = in.nextInt() - 1;
                int b = in.nextInt() - 1;
                G[a].add(b);
                G[b].add(a);
            }
            vis = new boolean[n];
            long ways = 0;
            for (int i = 0; i < n; i++) {
                Arrays.fill(vis, false);
                root = i;
                ways = (ways + dfs(i)) % mod;
                //System.out.println("Ways at i=" + i + " and ways=" + ways);
            }
            out.println(ways);
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

