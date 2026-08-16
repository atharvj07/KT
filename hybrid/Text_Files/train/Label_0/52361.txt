import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.util.LinkedList;
import java.util.Comparator;
import java.util.Collections;
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
        TaskF solver = new TaskF();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskF {
        int N;
        List<Integer>[] graph;
        int[] parent;
        int[] lowest;
        int[] height;
        List<Integer> order;
        LinkedList<Integer> operations;

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            N = in.nextInt();
            graph = new List[N];
            parent = new int[N];
            lowest = new int[N];
            height = new int[N];
            for (int i = 0; i < N; i++) {
                graph[i] = new ArrayList<Integer>();
            }
            for (int i = 1; i < N; i++) {
                int p = in.nextInt();
                parent[i] = p;
                graph[p].add(i);
            }
            dfs(0);
            order = new ArrayList<>();
            operations = new LinkedList<>();
            dfs1(0);
            for (int u : order) {
                out.print(u + " ");
            }
            out.printLine();
            out.printLine(operations.size());
            for (int u : operations) {
                out.print(u + " ");
            }
            out.printLine();
        }

        public void dfs1(int u) {
            order.add(u);
            int w = -1;
            for (int v : graph[u]) {
                dfs1(v);
                if (w != -1) {
                    int node = lowest[w];
                    while (node != u) {
                        operations.addLast(v);
                        node = parent[node];
                    }
                }
                w = v;
            }
        }

        public void dfs(int u) {
            if (graph[u].size() == 0) {
                lowest[u] = u;
                height[u] = 0;
            } else {
                height[u] = -1;
                for (int v : graph[u]) {
                    dfs(v);
                    if (height[u] < height[v] + 1) {
                        height[u] = height[v] + 1;
                        lowest[u] = lowest[v];
                    }
                }
                Collections.sort(graph[u], new Comparator<Integer>() {

                    public int compare(Integer o1, Integer o2) {
                        if (height[o1] != height[o2]) {
                            return height[o1] - height[o2];
                        } else {
                            return 1;
                        }
                    }
                });
            }
        }

    }

    static class OutputWriter {
        PrintWriter writer;

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

        public void printLine(Object... objects) {
            print(objects);
            writer.println();
        }

        public void close() {
            writer.close();
        }

    }

    static class InputReader {
        BufferedReader in;
        StringTokenizer tokenizer = null;

        public InputReader(InputStream inputStream) {
            in = new BufferedReader(new InputStreamReader(inputStream));
        }

        public String next() {
            try {
                while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                    tokenizer = new StringTokenizer(in.readLine());
                }
                return tokenizer.nextToken();
            } catch (IOException e) {
                return null;
            }
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

