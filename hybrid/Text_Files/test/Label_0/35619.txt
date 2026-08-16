import java.io.*;
import java.util.*;

class Main {
    static Scanner scanner = new Scanner();
    static long inf = 0x7fffffffffL;

    public static void main(String[]$) throws IOException {
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        long p = scanner.nextInt();
        Edge[] edges = new Edge[m];
        for (int i = 0; i < m; i++) {
            int a = scanner.nextInt() - 1;
            int b = scanner.nextInt() - 1;
            long c = scanner.nextLong();
            edges[i] = new Edge(a, b, p - c);
        }
        long[] d = new long[n];
        Arrays.fill(d, inf);
        d[0] = 0;
        Set<Integer> loop = new HashSet<>();

        for (int i = 1; i <= 2 * n; i++) {
            for (int j = 0; j < m; j++) {
                if (d[edges[j].to] > d[edges[j].from] + edges[j].cost) {
                    d[edges[j].to] = d[edges[j].from] + edges[j].cost;
                    if (i >= n) {
                        loop.add(edges[j].from);
                        loop.add(edges[j].to);
                    }
                }
            }
        }

        if (loop.contains(n - 1)) {
            System.out.println(-1);
        } else {
            System.out.println(Math.max(0, -d[n - 1]));
        }
    }

    static class Edge implements Comparable<Edge> {
        int from;
        int to;
        long cost;

        Edge(int from, int to, long cost) {
            this.from = from;
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge o) {
            return Long.compare(this.cost, o.cost);
        }

        @Override
        public String toString() {
            return String.format("[%s, %s, %s]", from, to, cost);
        }
    }

    static class Scanner {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in), 32768);
        StringTokenizer tokenizer;

        String next() throws IOException {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                tokenizer = new StringTokenizer(reader.readLine());
            }
            return tokenizer.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }
    }
}