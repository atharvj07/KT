import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author gaidash
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        DCandidatesOfNoShortestPaths solver = new DCandidatesOfNoShortestPaths();
        solver.solve(1, in, out);
        out.close();
    }

    static class DCandidatesOfNoShortestPaths {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            final int INF = Integer.MAX_VALUE / 2;

            int nVertices = in.nextInt();
            int nEdges = in.nextInt();
            DCandidatesOfNoShortestPaths.Edge[] edges = new DCandidatesOfNoShortestPaths.Edge[nEdges];
            for (int i = 0; i < nEdges; i++) {
                int u = in.nextInt() - 1;
                int v = in.nextInt() - 1;
                int c = in.nextInt();
                edges[i] = new DCandidatesOfNoShortestPaths.Edge(u, v, c);
            }

            int[][] dist = new int[nVertices][nVertices];
            for (int[] a : dist) {
                Arrays.fill(a, INF);
            }
            for (int i = 0; i < nVertices; i++) {
                dist[i][i] = 0;
            }
            for (DCandidatesOfNoShortestPaths.Edge edge : edges) {
                dist[edge.from][edge.to] = dist[edge.to][edge.from] = edge.cost;
            }
            for (int k = 0; k < nVertices; k++) {
                for (int i = 0; i < nVertices; i++) {
                    for (int j = 0; j < nVertices; j++) {
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }

            int ret = 0;
            for (DCandidatesOfNoShortestPaths.Edge edge : edges) {
                if (edge.cost > dist[edge.from][edge.to]) {
                    ret++;
                }
            }

            out.println(ret);
        }

        private static class Edge {
            private int from;
            private int to;
            private int cost;

            private Edge(int from, int to, int cost) {
                this.from = from;
                this.to = to;
                this.cost = cost;
            }

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

        public void close() {
            writer.close();
        }

        public void println(int i) {
            writer.println(i);
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
            if (numChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }

        public int nextInt() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public boolean isSpaceChar(int c) {
            if (filter != null) {
                return filter.isSpaceChar(c);
            }
            return isWhitespace(c);
        }

        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);

        }

    }
}

