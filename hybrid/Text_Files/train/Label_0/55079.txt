
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;


public class FlightsRegularCustomers2 {
    public static void main(String[] args) {
        long res = solve();
        if (res < 0) {
            System.out.println("Impossible");
        } else {
            System.out.println(res);
        }
    }

    private static long solve() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();


        Matrix matrix = new Matrix(n);
        int[][] weight = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                weight[i][j] = Integer.MAX_VALUE;
            }
        }


        Edge[] d = new Edge[m];
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt() - 1;
            int v = sc.nextInt() - 1;
            int w = sc.nextInt();
            weight[v][u] = w;
            matrix.set(v, u, true);
            d[i] = new Edge(u, v, w);
        }

        Arrays.sort(d, new Comparator<Edge>() {
            @Override
            public int compare(Edge o1, Edge o2) {
                return Integer.compare(o1.weight, o2.weight);
            }
        });

        Vector can = new Vector(n);
        can.set(0, true);

        long result = -1;
        int dprev = 0;

        Matrix matrix2 = new Matrix(n);
        Matrix id = Matrix.id(n);

        Graph graph = new Graph(n);
        for (int i = 0; i < m; i++) {
            int di = d[i].weight;
            int delta = di - dprev;

            Matrix adj = matrix2.pow(id, delta);
            can = adj.mul(can);

            matrix2.set(d[i].v, d[i].u, true);
            graph.addEdge(d[i].u, d[i].v);

            result = dist2(can, graph);
            if (result >= 0) {
                result += di;
                break;
            }
            dprev = di;
        }

        if (result < 0) {
            result = dist2(can, graph);
            if (result >= 0) {
                result += dprev;
            }
        }

        return result;
    }


    private static int dist(Vector can, Matrix matrix) {
        final int n = can.n;
        final short[][] dist = new short[n][n];
        final short inf = Short.MAX_VALUE / 10;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    dist[i][j] = 0;
                } else if (matrix.get(j, i)) {
                    dist[i][j] = 1;
                } else {
                    dist[i][j] = inf;
                }
            }
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    dist[i][j] = (short) Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
        short res = Short.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (can.get(i)) {
                res = (short) Math.min(res, dist[i][n - 1]);
            }
        }
        if (res > 1000) {
            res = -1;
        }
        return res;
    }

    private static int dist2(Vector can, Graph graph) {
        final int n = can.n;

        int[] dist = new int[n];
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < can.n; i++) {
            if (can.get(i)) {
                queue.add(i);
                dist[i] = 0;
            } else {
                dist[i] = Integer.MAX_VALUE;
            }
        }

        boolean[] visited = new boolean[n];

        while (!queue.isEmpty()) {
            Integer next = queue.poll();
            if (next == n - 1) {
                return dist[n - 1];
            }
            List<Integer> edges = graph.getEdges(next);
            for (Integer edge : edges) {
                if (!visited[edge]) {
                    queue.add(edge);
                    dist[edge] = Math.min(dist[edge], dist[next] + 1);
                    visited[edge] = true;
                }
            }
        }
        return -1;


    }


    static class Matrix {
        private int n;
        private int hSize;
        private long[][] mat;

        public Matrix(int n) {
            this.n = n;
            this.hSize = (n + 63) / 64;
            this.mat = new long[n][hSize];
        }

        public Matrix(Matrix matrix) {
            this(matrix.n);
            long[][] other = matrix.mat;
            for (int i = 0; i < other.length; i++) {
                for (int j = 0; j < other[i].length; j++) {
                    mat[i][j] = other[i][j];
                }
            }
        }

        public static Matrix id(int n) {
            Matrix res = new Matrix(n);
            for (int i = 0; i < n; i++) {
                res.set(i, i, true);
            }
            return res;
        }

        public void set(int u, int v, boolean val) {
            if (u >= n || v >= n) {
                throw new ArrayIndexOutOfBoundsException("index: " + v);
            }
            if (val) {
                mat[u][v >> 6] |= 1L << (v & 63);
            } else {
                mat[u][v >> 6] &= ~(1L << (v & 63));
            }
        }

        public boolean get(int u, int v) {
            if (u >= n || v >= n) {
                throw new ArrayIndexOutOfBoundsException("index: " + v);
            }

//            return (mat[u][v >> 6] & 1L << v % 64) != 0;
            return (mat[u][v >> 6] & 1L << (v & 63)) != 0;
        }

        public Matrix mul(Matrix other) {
            Matrix temp = new Matrix(n);
            Matrix res = new Matrix(n);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    temp.set(i, j, other.get(j, i));
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    boolean scalarProduct = false;
                    for (int k = 0; k < hSize; k++) {
                        scalarProduct |= (mat[i][k] & temp.mat[j][k]) != 0;
                    }
                    res.set(i, j, scalarProduct);
                }
            }
            return res;
        }


//        public void mulInPlace(Matrix other) {
//            Matrix temp = new Matrix(n);
//            for (int i = 0; i < n; i++) {
//                for (int j = 0; j < n; j++) {
//                    temp.set(i, j, other.get(j, i));
//                }
//            }
//            for (int i = 0; i < n; i++) {
//                for (int j = 0; j < n; j++) {
//                    boolean scalarProduct = false;
//                    for (int k = 0; k < hSize; k++) {
//                        scalarProduct |= (mat[i][k] & temp.mat[j][k]) != 0;
//                    }
//                    res.set(i, j, scalarProduct);
//                }
//            }
//        }

        public Vector mul(Vector other) {
            Vector res = new Vector(n);
            for (int i = 0; i < n; i++) {
                boolean scalarProduct = false;
                for (int k = 0; k < hSize; k++) {
                    scalarProduct |= (mat[i][k] & other.vec[k]) != 0;
                }
                res.set(i, scalarProduct);
            }
            return res;
        }

        public Matrix pow(int p) {
            return pow(null, p);
        }

        public Matrix pow(Matrix id, int p) {
            if (id == null) {
                id = id(n);
            }
            Matrix res = id;
            Matrix pow = new Matrix(this);
            while (p > 0) {
                if ((p & 1) != 0) {
                    res = res.mul(pow);
                }
                pow = pow.mul(pow);
                p >>= 1;
            }
            return res;
        }


        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.append("Matrix{n=").append(n).append("}\n");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (get(i, j)) {
                        sb.append("1");
                    } else {
                        sb.append("0");
                    }
                }
                sb.append("\n");
            }
            return sb.toString();
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Matrix)) return false;

            Matrix matrix = (Matrix) o;

            if (hSize != matrix.hSize) return false;
            if (n != matrix.n) return false;

            return Arrays.deepEquals(mat, ((Matrix) o).mat);
        }

        @Override
        public int hashCode() {
            int result = n;
            result = 31 * result + hSize;
            return result;
        }
    }

    static class Vector {
        private final int hSize;
        private int n;
        private long[] vec;

        public Vector(int n) {
            this.n = n;
            this.hSize = (n + 63) / 64;
            this.vec = new long[hSize];

        }

        public void set(int v, boolean val) {
            if (v >= n) {
                throw new ArrayIndexOutOfBoundsException("index: " + v);
            }
            if (val) {
                vec[v >> 6] |= 1L << (v & 63);
            } else {
                vec[v >> 6] &= ~(1L << (v & 63));
            }
        }

        public boolean get(int v) {
            if (v >= n) {
                throw new ArrayIndexOutOfBoundsException("index: " + v);
            }
            return (vec[v >> 6] & 1L << (v & 63)) != 0;
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.append("Vector{" + "n=").append(n).append("}\n");
            for (int i = 0; i < n; i++) {
                if (get(i)) {
                    sb.append("1");
                } else {
                    sb.append("0");
                }
            }
            return sb.toString();
        }

        public boolean isZero() {
            boolean res = true;
            for (int i = 0; i < hSize; i++) {
                res &= vec[i] == 0;
            }
            return res;
        }
    }

    public static class Graph {
        private int nodesCount;
        private GraphNode[] nodes;


        public Graph(int nodesCount) {
            this.nodesCount = nodesCount;
            nodes = new GraphNode[nodesCount + 1];
            for (int i = 0; i < nodes.length; i++) {
                nodes[i] = new GraphNode(i);
            }
        }

        public int getNodesCount() {
            return nodesCount;
        }

        public void addEdge(int u, int v) {
            nodes[u].addEdge(v);
        }

        public List<Integer> getEdges(int id) {
            return nodes[id].getEdges();
        }

        public GraphNode getNode(int id) {
            return nodes[id];
        }

        @Override
        public String toString() {
            return "Graph{" +
                    "nodesCount=" + nodesCount +
                    '}';
        }
    }


    static class GraphNode {
        List<Integer> edges = new ArrayList<>();
        int id;

        public GraphNode(int id) {
            this.id = id;
        }

        public void addEdge(Integer edge) {
            edges.add(edge);
        }

        public List<Integer> getEdges() {
            return edges;
        }
    }

    static class Edge {
        int u;
        int v;
        int weight;

        public Edge(int u, int v, int weight) {
            this.u = u;
            this.v = v;
            this.weight = weight;
        }
    }

}

