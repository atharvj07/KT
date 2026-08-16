//Created by Aminul on 11/16/2020.

import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class C {
    private static final long MOD = 998244353;

    public static void main(String[] args) throws Exception {
        InputReader in = new InputReader(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        int n = in.nextInt(), m = in.nextInt();
        ArrayDeque<Edge> graph[] = genDQ(n + 1);
        ArrayDeque<Edge> revGraph[] = genDQ(n + 1);
        for (int i = 0; i < m; i++) {
            int u = in.nextInt(), v = in.nextInt();
            graph[u].addLast(new Edge(v, 0, 0));
            revGraph[v].addLast(new Edge(u, 0, 0));
        }

        pw.println(dijkstra(1, n, graph, revGraph));
        pw.close();
    }

    static <T> ArrayDeque<T>[] genDQ(int n) {
        ArrayDeque<T> list[] = new ArrayDeque[n];
        for (int i = 0; i < n; i++) list[i] = new ArrayDeque<T>();
        return list;
    }

    static long dijkstra(int source, int n, ArrayDeque<Edge> graph[], ArrayDeque<Edge> revGraph[]) {
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        ArrayDeque<Edge> vis[][] = new ArrayDeque[n + 1][2];
        for (int i = 0; i < vis.length; i++) {
            vis[i][0] = new ArrayDeque<>();
            vis[i][1] = new ArrayDeque<>();
        }

        HashSet<Long> done = new HashSet<>();
        pq.add(new Edge(source, 0, 0));
        //vis[source][0].addLast(new Edge(source, 0, 0));

        while (!pq.isEmpty()) {
            Edge pop = pq.poll();
            int u = pop.vertex, m = pop.moves, k = pop.pow;
            if (!done.add(pop.getHash()) || !isValid(vis[u][k & 1], pop)) continue;
            vis[u][k & 1].addLast(pop);

            if (u == n) {
                return (m + bigMod(2, k, MOD) - 1) % MOD;
            }

            ArrayDeque<Edge> g[] = (k % 2) == 0 ? graph : revGraph;

            Edge trans = pop.trans();
            if (!done.contains(trans.getHash()) && isValid(vis[trans.vertex][trans.pow & 1], trans)) {
                pq.add(trans);
            }

            for (Edge e : g[u]) {
                Edge moved = pop.move(e.vertex);
                if (!done.contains(moved.getHash()) && isValid(vis[moved.vertex][moved.pow & 1], moved)) {
                    pq.add(moved);
                }
            }
        }

        return -1; // never reaches here //
    }

    static boolean isValid(ArrayDeque<Edge> list, Edge edge) {
        for (Edge e : list) {
            if (e.pow < edge.pow && e.compareTo(edge) <= 0) {
                return false;
            }
        }
        return true;
    }

    static long bigMod(long a, long p, long m) { // returns (a^p) % m
        long res = 1 % m, x = a % m;
        while (p > 0) {
            if ((p & 1) > 0) res = (res * x) % m;
            x = (x * x) % m;
            p >>= 1;
        }
        return res;
    }

    static class Edge implements Comparable<Edge> {
        int vertex, moves, pow;

        public Edge(int v, int m, int k) {
            this.vertex = v;
            this.moves = m;
            this.pow = k;
        }

        Edge move(int v) {
            return new Edge(v, this.moves + 1, this.pow);
        }

        Edge trans() {
            return new Edge(this.vertex, this.moves, this.pow + 1);
        }

        long getHash() {
            return ((long) vertex << 31) | pow;
        }

        public int compareTo(Edge o) {
            if (pow == o.pow) {
                return Integer.compare(moves, o.moves);
            } else if (max(pow, o.pow) <= 60) {
                return Long.compare(moves + (1l << pow), o.moves + (1l << o.pow));
            } else {
                return Integer.compare(pow, o.pow);
            }
        }

        @Override
        public String toString() {
            return "Edge{" +
                    "vertex=" + vertex +
                    ", moves=" + moves +
                    ", pow=" + pow +
                    '}';
        }
    }

    static void debug(Object... obj) {
        System.err.println(Arrays.deepToString(obj));
    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
            tokenizer = null;
        }

        public String next() throws Exception {
            while (tokenizer == null || !tokenizer.hasMoreTokens())
                tokenizer = new StringTokenizer(reader.readLine());
            return tokenizer.nextToken();
        }

        public int nextInt() throws Exception {
            return Integer.parseInt(next());
        }
    }
}