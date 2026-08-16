import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.util.PriorityQueue;
import java.util.AbstractQueue;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.AbstractCollection;
import java.util.stream.Stream;
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
        DManhattanMaxMatching solver = new DManhattanMaxMatching();
        solver.solve(1, in, out);
        out.close();
    }

    static class DManhattanMaxMatching {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.nextInt();
            List<DManhattanMaxMatching.Edge>[] graph = Stream.generate(ArrayList::new).limit(2 * n + 10).toArray(List[]::new);
            int sum = 0;
            for (int i = 1; i <= n; i++) {
                int x = in.nextInt(), y = in.nextInt(), f = in.nextInt();
                sum += f;
                DManhattanMaxMatching.MinCostFlow.addEdge(graph, 0, i, f, 0);
                DManhattanMaxMatching.MinCostFlow.addEdge(graph, i, n + 1, 100, x + y);
                DManhattanMaxMatching.MinCostFlow.addEdge(graph, i, n + 2, 100, x - y);
                DManhattanMaxMatching.MinCostFlow.addEdge(graph, i, n + 3, 100, -x + y);
                DManhattanMaxMatching.MinCostFlow.addEdge(graph, i, n + 4, 100, -x - y);
            }

            for (int i = 1; i <= n; i++) {
                int x = in.nextInt(), y = in.nextInt(), f = in.nextInt();
                DManhattanMaxMatching.MinCostFlow.addEdge(graph, n + 4 + i, 2 * n + 5, f, 0);
                DManhattanMaxMatching.MinCostFlow.addEdge(graph, n + 1, n + 4 + i, 100, -x - y);
                DManhattanMaxMatching.MinCostFlow.addEdge(graph, n + 2, n + 4 + i, 100, -x + y);
                DManhattanMaxMatching.MinCostFlow.addEdge(graph, n + 3, n + 4 + i, 100, x - y);
                DManhattanMaxMatching.MinCostFlow.addEdge(graph, n + 4, n + 4 + i, 100, x + y);
            }

            long flowCost = DManhattanMaxMatching.MinCostFlow.minCostFlow(graph, 0, 2 * n + 5, Long.MAX_VALUE)[1];
            out.println(DManhattanMaxMatching.MinCostFlow.MAX * sum * 4 - flowCost);
        }

        static class Edge {
            int to;
            int rev;
            long f;
            long cap;
            long cost;

            Edge(int to, long cap, long cost, int rev) {
                this.to = to;
                this.cap = cap;
                this.cost = cost;
                this.rev = rev;
            }

        }

        static class MinCostFlow {
            static final long MAX = 1L << 32;

            public static void addEdge(List<DManhattanMaxMatching.Edge>[] graph, int s, int t, long cap, long cost) {
                cost = MAX - cost;
                graph[s].add(new DManhattanMaxMatching.Edge(t, cap, cost, graph[t].size()));
                graph[t].add(new DManhattanMaxMatching.Edge(s, 0, -cost, graph[s].size() - 1));
            }

            public static long[] minCostFlow(List<DManhattanMaxMatching.Edge>[] graph, int s, int t, long maxf) {
                int n = graph.length;
                long[] prio = new long[n];
                long[] curflow = new long[n];
                int[] prevedge = new int[n];
                int[] prevnode = new int[n];
                long[] pot = new long[n];
                long flow = 0;
                long flowCost = 0;
                int mask = (1 << 20) - 1;
//            bellmanFord(graph, s, pot);
                while (flow < maxf) {
                    PriorityQueue<Long> q = new PriorityQueue<>();
                    q.add((long) s);
                    Arrays.fill(prio, Long.MAX_VALUE);
                    prio[s] = 0;
                    boolean[] finished = new boolean[n];
                    curflow[s] = Long.MAX_VALUE;
                    while (!finished[t] && !q.isEmpty()) {
                        long cur = q.remove();
                        int u = (int) (cur & mask);
                        long priou = (cur >>> 20);
                        if (priou != prio[u])
                            continue;
                        finished[u] = true;
                        for (int i = 0; i < graph[u].size(); i++) {
                            DManhattanMaxMatching.Edge e = graph[u].get(i);
                            if (e.f >= e.cap)
                                continue;
                            int v = e.to;
                            long nprio = prio[u] + e.cost + pot[u] - pot[v];
                            if (prio[v] > nprio) {
                                prio[v] = nprio;
                                q.add(((long) nprio << 20) + v);
                                prevnode[v] = u;
                                prevedge[v] = i;
                                curflow[v] = Math.min(curflow[u], e.cap - e.f);
                            }
                        }
                    }
                    if (prio[t] == Long.MAX_VALUE)
                        break;
                    for (int i = 0; i < n; i++)
                        if (finished[i])
                            pot[i] += prio[i] - prio[t];
                    long df = Math.min(curflow[t], maxf - flow);
                    flow += df;
                    for (int v = t; v != s; v = prevnode[v]) {
                        DManhattanMaxMatching.Edge e = graph[prevnode[v]].get(prevedge[v]);
                        e.f += df;
                        graph[v].get(e.rev).f -= df;
                        flowCost += df * e.cost;
                    }
                }

                return new long[]{flow, flowCost};
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

        public void println(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                if (i != 0) {
                    writer.print(' ');
                }
                writer.print(objects[i]);
            }
            writer.print('\n');
        }

        public void close() {
            writer.close();
        }

    }
}

