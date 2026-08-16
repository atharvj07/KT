import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.Stack;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;
import java.util.Vector;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        TaskH solver = new TaskH();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskH {
        int[] size;
        boolean[] is_leaf;

        int dfs(List<Integer>[] graph, int s, int p) {
            size[s] = 0;
            int num_child = 0;
            for (int v : graph[s]) {
                if (v != p) {
                    size[s] += dfs(graph, v, s);
                    num_child++;
                }
            }
            if (num_child == 0) {
                size[s]++;
                is_leaf[s] = true;
            }
            return size[s];
        }

        int centroid(List<Integer>[] graph, int s, int p, int n) {
            for (int v : graph[s]) if (v != p && 2 * size[v] > n && !is_leaf[v]) return centroid(graph, v, s, n);
            return s;
        }

        void getComponents(List<Integer>[] graph, List<Integer> record, int s, int p, int donotgohere) {
            int num_child = 0;
            for (int v : graph[s]) {
                if (v != p && v != donotgohere) {
                    getComponents(graph, record, v, s, donotgohere);
                    num_child++;
                }
            }
            if (num_child == 0) record.add(s);
        }

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.nextInt(), m = in.nextInt();
            List<Integer>[] graph = Stream.generate(ArrayList::new).limit(n).toArray(List[]::new);
            for (int i = 0; i < m; i++) {
                int u = in.nextInt(), v = in.nextInt();
                u--;
                v--;
                graph[u].add(v);
                graph[v].add(u);
            }
            TaskH.Biconnectivity utility = new TaskH.Biconnectivity();
            List<List<Integer>> components = utility.biconnectivity(graph);
            List<Integer>[] tree = utility.ebcTree(graph, components);
            int tree_n = components.size();

            if (tree_n == 1) {
                out.println(0);
            } else if (tree_n == 2 && n != 2) {
                out.println(1);
                out.println(components.get(0).get(0) + 1, components.get(1).get(0) + 1);
            } else if (tree_n == 2 && n == 2) {
                out.println(-1);
            } else {
                size = new int[tree_n];
                is_leaf = new boolean[tree_n];
                int root = 0;

                List<Integer> a = new ArrayList<>();
                List<Integer> b = new ArrayList<>();
                for (int j = 0; j < tree_n; j++) if (tree[j].size() > 1) root = j;
                dfs(tree, root, -1);
                int centroid = centroid(tree, root, -1, size[root]);
                List<List<Integer>> leaf_sets = new ArrayList<>();
                int num_leaves = 0;
                int[] set_sizes = new int[n];
                int[] pos = new int[n];
                int cnt = 0;
                for (int v : tree[centroid]) {
                    List<Integer> leaves = new ArrayList<>();
                    getComponents(tree, leaves, v, -1, centroid);
                    leaf_sets.add(leaves);
                    num_leaves += leaves.size();
                    set_sizes[cnt++] = leaves.size();
                }
                for (; num_leaves > 0; ) {
                    int ind_2 = 0, ind_1 = 0, mx_1 = 0, mx_2 = 0;
                    for (int j = 0; j < cnt; j++) {
                        if (set_sizes[j] > mx_1) {
                            ind_2 = ind_1;
                            mx_2 = mx_1;
                            mx_1 = set_sizes[j];
                            ind_1 = j;
                        } else if (set_sizes[j] > mx_2) {
                            mx_2 = set_sizes[j];
                            ind_2 = j;
                        }
                    }
                    a.add(leaf_sets.get(ind_1).get(pos[ind_1]++));
                    set_sizes[ind_1]--;
                    if (num_leaves == 1) {
                        for (int j = 0; j < cnt; j++)
                            if (j != ind_1) {
                                b.add(leaf_sets.get(j).get(0));
                                break;
                            }
                    } else {
                        b.add(leaf_sets.get(ind_2).get(pos[ind_2]++));
                        set_sizes[ind_2]--;
                    }
                    num_leaves -= 2;
                }
                if (n == 2) {
                    out.println(-1);
                } else {
                    out.println(a.size());
                    for (int i = 0; i < a.size(); i++)
                        out.println(components.get(a.get(i)).get(0) + 1, components.get(b.get(i)).get(0) + 1);
                }
            }
        }

        static class Biconnectivity {
            List<Integer>[] graph;
            boolean[] visited;
            Stack<Integer> stack;
            int time;
            int[] tin;
            int[] lowlink;
            List<List<Integer>> edgeBiconnectedComponents;
            List<Integer> cutPoints;
            List<String> bridges;

            public List<List<Integer>> biconnectivity(List<Integer>[] graph) {
                int n = graph.length;
                this.graph = graph;
                visited = new boolean[n];
                stack = new Stack<>();
                time = 0;
                tin = new int[n];
                lowlink = new int[n];
                edgeBiconnectedComponents = new ArrayList<>();
                cutPoints = new ArrayList<>();
                bridges = new ArrayList<>();

                for (int u = 0; u < n; u++)
                    if (!visited[u])
                        dfs(u, -1);

                return edgeBiconnectedComponents;
            }

            void dfs(int u, int p) {
                visited[u] = true;
                lowlink[u] = tin[u] = time++;
                stack.add(u);
                int children = 0;
                boolean cutPoint = false;
                for (int v : graph[u]) {
                    if (v == p)
                        continue;
                    if (visited[v]) {
                        lowlink[u] = Math.min(lowlink[u], tin[v]); // or lowlink[u] = Math.min(lowlink[u], lowlink[v]);
                    } else {
                        dfs(v, u);
                        lowlink[u] = Math.min(lowlink[u], lowlink[v]);
                        cutPoint |= tin[u] <= lowlink[v];
                        if (tin[u] < lowlink[v]) // or if (lowlink[v] == tin[v])
                            bridges.add("(" + u + "," + v + ")");
                        ++children;
                    }
                }
                if (p == -1)
                    cutPoint = children >= 2;
                if (cutPoint)
                    cutPoints.add(u);
                if (tin[u] == lowlink[u]) {
                    List<Integer> component = new ArrayList<>();
                    while (true) {
                        int x = stack.pop();
                        component.add(x);
                        if (x == u)
                            break;
                    }
                    edgeBiconnectedComponents.add(component);
                }
            }

            public List<Integer>[] ebcTree(List<Integer>[] graph, List<List<Integer>> components) {
                int[] comp = new int[graph.length];
                for (int i = 0; i < components.size(); i++)
                    for (int u : components.get(i))
                        comp[u] = i;
                List<Integer>[] g = Stream.generate(ArrayList::new).limit(components.size()).toArray(List[]::new);
                for (int u = 0; u < graph.length; u++)
                    for (int v : graph[u])
                        if (comp[u] != comp[v])
                            g[comp[u]].add(comp[v]);
                return g;
            }

        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private InputReader.SpaceCharFilter filter;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int read() {
            if (numChars == -1) throw new InputMismatchException();
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0) return -1;
            }
            return buf[curChar++];
        }

        public int nextInt() {
            int c = read();
            while (isSpaceChar(c)) c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public boolean isSpaceChar(int c) {
            if (filter != null)
                return filter.isSpaceChar(c);
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public interface SpaceCharFilter {
            boolean isSpaceChar(int ch);

        }

    }

    static class OutputWriter {
        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }

        public void print(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                if (i != 0) {
                    writer.print(' ');
                }
                writer.print(objects[i]);
            }
        }

        public void println(Object... objects) {
            print(objects);
            writer.println();
        }

        public void close() {
            writer.close();
        }

        public void println(int i) {
            writer.println(i);
        }

    }
}

