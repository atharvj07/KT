import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.List;
import java.util.Iterator;
import java.util.Collection;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastReader in = new FastReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskE solver = new TaskE();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskE {
        public void solve(int testNumber, FastReader in, PrintWriter out) {
            int n = in.nextInt();
            int m = in.nextInt();
            List<TaskE.Edge>[] g = new List[n];
            TaskE.Edge[] edges = new TaskE.Edge[m];
            for (int i = 0; i < n; ++i) g[i] = new ArrayList<>();
            for (int i = 0; i < m; ++i) {
                int u = in.nextInt() - 1;
                int v = in.nextInt() - 1;
                int w = in.nextInt();
                edges[i] = new TaskE.Edge(u, v, w);
                g[u].add(edges[i]);
            }

            int low = -1;
            int high = 2000_000_000;
            while (high - low > 1) {
                int mid = (high + low) >>> 1;
                if (sortTopo(g, mid) != null) {
                    high = mid;
                } else {
                    low = mid;
                }
            }

            out.print(high + " ");
            int[] ord = sortTopo(g, high);
            int[] iord = new int[n];
            for (int i = 0; i < n; ++i) {
                iord[ord[i]] = i;
            }

            List<Integer> ret = new ArrayList<>();
            for (int i = 0; i < edges.length; i++) {
                TaskE.Edge edge = edges[i];
                if (edge.weight <= high && iord[edge.cur] > iord[edge.next]) {
                    ret.add(i + 1);
                }
            }
            out.println(ret.size());
            ArrayUtils.printArray(out, ret);
        }

        public int[] sortTopo(List<TaskE.Edge>[] g, int pos) {
            int n = g.length;
            int[] indeg = new int[n];
            for (int cur = 0; cur < n; ++cur) {
                for (TaskE.Edge edge : g[cur]) {
                    if (edge.weight > pos) {
                        ++indeg[edge.next];
                    }
                }
            }

            int[] queue = new int[n];
            int sizeQ = 0;

            // sources
            for (int i = 0; i < n; ++i) {
                if (indeg[i] == 0) queue[sizeQ++] = i;
            }

            for (int ptr = 0; ptr < sizeQ; ++ptr) {
                int cur = queue[ptr];
                for (TaskE.Edge edge : g[cur]) {
                    if (edge.weight > pos)
                        if (--indeg[edge.next] == 0)
                            queue[sizeQ++] = edge.next;
                }
            }

            // loop
            for (int i = 0; i < n; ++i) {
                if (indeg[i] > 0) return null;
            }
            return queue;
        }

        static class Edge {
            int cur;
            int next;
            int weight;

            public Edge(int cur, int next, int weight) {
                this.cur = cur;
                this.next = next;
                this.weight = weight;
            }

        }

    }

    static class FastReader {
        private InputStream stream;
        private byte[] buf = new byte[8192];
        private int curChar;
        private int pnumChars;

        public FastReader(InputStream stream) {
            this.stream = stream;
        }

        private int pread() {
            if (pnumChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= pnumChars) {
                curChar = 0;
                try {
                    pnumChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (pnumChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }

        public int nextInt() {
            int c = pread();
            while (isSpaceChar(c))
                c = pread();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = pread();
            }
            int res = 0;
            do {
                if (c == ',') {
                    c = pread();
                }
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = pread();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        private boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

    }

    static class ArrayUtils {
        public static <T> void printArray(PrintWriter out, Collection<T> array) {
            if (array.size() == 0) return;
            int size = array.size();
            Iterator<T> iterator = array.iterator();
            int ct = 0;
            for (; ct < size && iterator.hasNext(); ct++) {
                if (ct != 0) out.print(" ");
                out.print(iterator.next());
            }
            out.println();
        }

    }
}

