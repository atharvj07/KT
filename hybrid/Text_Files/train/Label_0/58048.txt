import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.util.Collections;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author AlexFetisov
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskE_CyclingCity solver = new TaskE_CyclingCity();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskE_CyclingCity {
        int n;
        int m;
        boolean[] used;
        int[] tIn;
        int[] fUp;
        int timer;
        boolean[] isCut;
        List<Integer>[] g;
        List<Integer> stack;
        int curColor = 0;
        int[] decompressVertexId;
        HashSet<Edge> edgesOnCycle;
        int T;
        boolean[] u;
        int[] parent;
        int[] color;
        List<Integer> cycle;
        int[] compressVertexId;
        Graph G;

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            n = in.nextInt();
            m = in.nextInt();
            g = new List[n];
            for (int i = 0; i < n; ++i) {
                g[i] = new ArrayList<Integer>();
            }
            for (int i = 0; i < m; ++i) {
                int a = in.nextInt() - 1;
                int b = in.nextInt() - 1;
                g[a].add(b);
                g[b].add(a);
            }
            tIn = new int[n];
            fUp = new int[n];
            used = new boolean[n];
            isCut = new boolean[n];
            timer = 0;
            stack = new ArrayList<Integer>();
            compressVertexId = new int[n];
            cycle = new ArrayList<Integer>();
            color = new int[n];
            parent = new int[n];
            decompressVertexId = new int[n];
            u = new boolean[n];

            for (int i = 0; i < n; ++i) {
                if (!used[i]) {
                    dfs(i);
                }
            }

            out.println("NO");
        }

        int dfs(int v) {
            // System.err.println("DFS run: " + v);
            used[v] = true;
            tIn[v] = fUp[v] = timer++;
            int size = 1;
            for (int to : g[v]) {
                if (!used[to]) {
                    int toSz = dfs(to);
                    if (fUp[to] >= tIn[v]) {
                        stack.add(v);
//                    System.err.println("v - to => " + v + " " + to + " toSZ: " + toSz);
                        if (processComponent(toSz + 1)) {
                            System.exit(0);
                        }
                    } else {
                        size += toSz;
                    }
                    fUp[v] = Math.min(fUp[v], fUp[to]);
                } else {
                    fUp[v] = Math.min(fUp[v], tIn[to]);
                }
            }
            stack.add(v);
            return size;
        }

        private boolean processComponent(int cnt) {
            List<Integer> component = new ArrayList<Integer>();
            while (cnt-- > 0) {
                component.add(stack.get(stack.size() - 1));
                stack.remove(stack.size() - 1);
            }
            Collections.reverse(component);

//        System.err.println("Comonent! " + component.size());
//        System.err.println(ArrayUtils.toString(component));
            if (component.size() <= 3) {
                return false;
            }
            ++curColor;
            for (int i = 0; i < component.size(); ++i) {
                compressVertexId[component.get(i)] = i;
                decompressVertexId[i] = component.get(i);
                color[component.get(i)] = curColor;
                u[i] = false;
            }
            List<Integer> a = new ArrayList<Integer>();
            List<Integer> b = new ArrayList<Integer>();
            for (int v : component) {
                for (int to : g[v]) {
                    if (v < to) {
                        if (color[to] == curColor) {
                            a.add(compressVertexId[v]);
                            b.add(compressVertexId[to]);
                        }
                    }
                }
            }
            for (int i = 0; i < component.size(); ++i) {
                color[component.get(i)] = 0;
            }
            G = new Graph();
            G.initGraph(component.size(), a.size());
            for (int i = 0; i < a.size(); ++i) {
                G.addEdge(a.get(i), b.get(i));
            }
            cycle.clear();
            for (int i = 0; i < component.size(); ++i) {
                color[i] = 0;
                u[i] = false;
            }
            getCycle(0);
            for (int i = 0; i < component.size(); ++i) {
                color[i] = 0;
                u[i] = false;
            }
            edgesOnCycle = new HashSet<Edge>();
            int p = cycle.get(cycle.size() - 1);
            for (int v : cycle) {
                color[v] = 1;
                edgesOnCycle.add(new Edge(p, v));
                p = v;
            }
            for (int v : cycle) {
                color[v] = 0;
                if (dfs2(v, -1)) {
                    System.out.println("YES");
                    outPath();
                    outCycle(v, T, 1);
                    outCycle(v, T, -1);
                    return true;
                }
                color[v] = 1;
            }
            return false;
        }

        private void outCycle(int start, int end, int delta) {
            int i = 0;
            for (; i < cycle.size(); ++i) {
                if (cycle.get(i) == start) {
                    break;
                }
            }
            List<Integer> path = new ArrayList<Integer>();
            for (; ; i += delta) {
                i += cycle.size();
                i %= cycle.size();
                path.add(1 + decompressVertexId[cycle.get(i)]);
                if (cycle.get(i) == end) {
                    break;
                }
            }
            System.out.print(path.size());
            for (int x : path) {
                System.out.print(" " + x);
            }
            System.out.println();
        }

        private void outPath() {
            List<Integer> path = new ArrayList<Integer>();
            int cur = T;
            while (cur != -1) {
                path.add(cur);
                cur = parent[cur];
            }
            Collections.reverse(path);
            System.out.print(path.size());
            for (int i : path) {
                System.out.print(" " + (decompressVertexId[i] + 1));
            }
            System.out.println();
        }

        boolean dfs2(int v, int p) {
            parent[v] = p;
            if (color[v] == 1) {
                T = v;
                return true;
            }
            u[v] = true;
            for (int ei = G.first[v]; ei != -1; ei = G.next[ei]) {
                int to = G.to[ei];
                if (!u[to]) {
                    if (edgesOnCycle.contains(new Edge(to, v))) {
                        continue;
                    }
                    if (dfs2(to, v)) {
                        return true;
                    }
                }
            }
            return false;
        }

        private void getCycle(int v) {
            int last = dfsCycle(v, -1, v);
            while (last != v) {
                cycle.add(last);
                last = parent[last];
            }
            cycle.add(v);
        }

        private int dfsCycle(int v, int p, int start) {
            parent[v] = p;
            color[v] = 1;
            for (int ei = G.first[v]; ei != -1; ei = G.next[ei]) {
                int to = G.to[ei];
                if (to == start && p != start) {
                    return v;
                }
                if (to != p && color[to] == 0) {
                    int res = dfsCycle(to, v, start);
                    if (res != -1) {
                        return res;
                    }
                }
            }
            return -1;
        }

        class Edge {
            int a;
            int b;

            public Edge(int a, int b) {
                if (a > b) {
                    int t = a;
                    a = b;
                    b = t;
                }
                this.a = a;
                this.b = b;
            }


            public boolean equals(Object o) {
                if (this == o) return true;
                if (o == null || getClass() != o.getClass()) return false;

                Edge edge = (Edge) o;

                if (a != edge.a) return false;
                return b == edge.b;

            }


            public int hashCode() {
                int result = a;
                result = 31 * result + b;
                return result;
            }

        }

    }

    static class Graph {
        public int[] from;
        public int[] to;
        public int[] first;
        public int[] next;
        public int nVertex;
        public int nEdges;
        public int curEdge;

        public Graph() {
        }

        public void initGraph(int n, int m) {
            curEdge = 0;
            nVertex = n;
            nEdges = m;
            from = new int[m * 2];
            to = new int[m * 2];
            first = new int[n];
            next = new int[m * 2];
            Arrays.fill(first, -1);
        }

        public void addEdge(int a, int b) {
            next[curEdge] = first[a];
            first[a] = curEdge;
            to[curEdge] = b;
            from[curEdge] = a;
            ++curEdge;

            next[curEdge] = first[b];
            first[b] = curEdge;
            to[curEdge] = a;
            from[curEdge] = b;
            ++curEdge;
        }

    }

    static class InputReader {
        private BufferedReader reader;
        private StringTokenizer stt;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
        }

        public String nextLine() {
            try {
                return reader.readLine();
            } catch (IOException e) {
                return null;
            }
        }

        public String nextString() {
            while (stt == null || !stt.hasMoreTokens()) {
                stt = new StringTokenizer(nextLine());
            }
            return stt.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(nextString());
        }

    }
}

