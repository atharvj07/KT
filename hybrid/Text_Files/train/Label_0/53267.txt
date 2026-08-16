import java.util.*;
import java.io.*;

public class Main {

    static FastReader sc;
    static PrintWriter out;
    static int mod = 1000000007;

    public static void main(String[] args) throws IOException {
        if (System.getProperty("ONLINE_JUDGE") == null) {
            File f1 = new File("input.txt");
            File f2 = new File("output.txt");
            Reader r = new FileReader(f1);
            sc = new FastReader(r);
            out = new PrintWriter(f2);
            double prev = System.currentTimeMillis();
            solve(sc, out);
            out.println("\n\nExecuted in : " + ((System.currentTimeMillis() - prev) / 1e3) + " ms");
        } else {
            sc = new FastReader(new InputStreamReader(System.in));
            out = new PrintWriter(System.out);
            solve(sc, out);
        }
        out.flush();
        out.close();
    }

    static void solve(FastReader sc, PrintWriter out) {
        int t = sc.nextInt();
        StringBuffer ans = new StringBuffer("");
        while (t-- > 0) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            int res = Integer.MIN_VALUE, cnt = 1;
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
                if (i > 0 && arr[i] == arr[i - 1])
                    cnt++;
                else {
                    res = Math.max(res, cnt);
                    cnt = 1;
                }
            }
            res = Math.max(res, cnt);
            cnt = 1;
            ans.append(res + "\n");
        }
        out.println(ans);
    }

    public static boolean isPowerTwo(long n) {
        return (n & n - 1) == 0;
    }

    static void sieve(boolean[] prime, int n) { // Sieve Of Eratosthenes
        for (int i = 1; i <= n; i++) {
            prime[i] = true;
        }
        for (int i = 2; i * i <= n; i++) {
            if (prime[i]) {
                for (int j = 2; i * j <= n; j++) {
                    prime[i * j] = false;
                }
            }
        }
    }

    static void fillGraph(ArrayList<ArrayList<Integer>> adj, FastReader sc) {
        int n = sc.nextInt(), m = sc.nextInt();
        for (int i = 0; i < n + 1; i++) {
            adj.add(new ArrayList<Integer>());
        }
        for (int i = 1; i <= m; i++) {
            int x = sc.nextInt(), y = sc.nextInt();
            adj.get(x).add(y);
            adj.get(y).add(x);
        }
    }

    static void dfs(ArrayList<ArrayList<Integer>> adj, boolean[] visited, int v, PrintWriter out) {
        visited[v] = true;
        out.print(v + " ");
        for (Integer i : adj.get(v)) {
            if (!visited[i])
                dfs(adj, visited, i, out);
        }
    }

    static void bfs(ArrayList<ArrayList<Integer>> adj, int V, int s, PrintWriter out) {
        boolean[] visited = new boolean[V];
        Queue<Integer> q = new LinkedList<>();
        visited[s] = true;
        q.add(s);
        while (!q.isEmpty()) {
            s = q.poll();
            out.print(s + " ");
            for (Integer i : adj.get(s)) {
                if (!visited[i]) {
                    visited[i] = true;
                    q.add(i);
                }
            }
        }
    }

    int fib(int n) { // n-th Fibonacci Number
        int a = 0, b = 1, c, i;
        if (n == 0)
            return a;
        for (i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }

    static long nCr(int n, int r) { // Combinations
        if (n < r)
            return 0;
        if (r > n - r) { // because nCr(n, r) == nCr(n, n - r)
            r = n - r;
        }
        long ans = 1L;
        for (int i = 0; i < r; i++) {
            ans *= (n - i);
            ans /= (i + 1);
        }
        return ans;
    }

    static long catalan(int n) { // n-th Catalan Number
        long c = nCr(2 * n, n);
        return c / (n + 1);
    }

    static class Pair implements Comparable<Pair> { // Pair Class
        long x;
        long y;

        Pair(long x, long y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Pair o) {
            return (int) (this.x - o.x);
        }
    }

    static class Trip<E, T, Z> { // Triplet Class
        E x;
        T y;
        Z z;

        Trip(E x, T y, Z z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        public boolean equals(Trip<E, T, Z> o) {
            if (o instanceof Trip) {
                Trip<E, T, Z> t = o;
                return t.x == x && t.y == y && t.z == z;
            }
            return false;
        }

        public int hashCode() {
            return Integer.valueOf((int) x).hashCode() * 62 + Integer.valueOf((int) y).hashCode() * 31
                    + Integer.valueOf((int) z).hashCode();
        }
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader(Reader r) {
            br = new BufferedReader(r);
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
}