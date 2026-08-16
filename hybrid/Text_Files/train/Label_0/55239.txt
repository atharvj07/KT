import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskD {
        final long infinity = (long) 1e17;
        int[] firstEdge;
        int[] edgeDst;
        int[] edgeNxt;
        int[] edgeLen;
        int numEdges;
        int[] heap;
        int[] heapWhere;
        int heapSize;
        long[] d;
        long[] phi;
        boolean[] was;
        final int QUEUE_SIZE = (int) 1e6;
        int[] queueFirst = new int[QUEUE_SIZE];
        int[] queueNext = new int[QUEUE_SIZE];
        int[] queueItemValue = new int[QUEUE_SIZE];
        int queueLastItem;

        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            int n = in.nextInt();
            int m = in.nextInt();
            init(n, m);
            int numQueries = in.nextInt();
            for (int i = 0; i < m; i++) {
                int a = in.nextInt() - 1;
                int b = in.nextInt() - 1;
                int c = in.nextInt();
                addEdge(a, b, c);
            }
            d = new long[n];
            phi = new long[n];
            shortestPaths(0);
            System.arraycopy(d, 0, phi, 0, n);
            was = new boolean[d.length];
            int kSum = 0;
            for (int queryId = 0; queryId < numQueries; queryId++) {
                int type = in.nextInt();
                if (type == 1) {
                    if (kSum > 0) {
                        bfs(0, kSum + 1);
                        kSum = 0;
                        for (int i = 0; i < n; i++) {
                            if (d[i] < infinity / 2) {
                                phi[i] += d[i];
                            }
                        }
                    }

                    int t = in.nextInt() - 1;
                    long ans = phi[t];
                    if (ans >= infinity / 2) {
                        out.println(-1);
                        continue;
                    }
                    out.println(ans);
                } else {
                    int k = in.nextInt();
                    for (int i = 0; i < k; i++) {
                        int e = in.nextInt() - 1;
                        ++edgeLen[e];
                    }
                    kSum += k;
                }
            }
        }

        private void init(int n, int m) {
            firstEdge = new int[n];
            Arrays.fill(firstEdge, -1);
            edgeNxt = new int[m];
            edgeDst = new int[m];
            edgeLen = new int[m];
            numEdges = 0;

            heap = new int[n];
            heapWhere = new int[n];
            heapSize = 0;
        }

        private void addEdge(int a, int b, int c) {
            int e = numEdges++;
            edgeNxt[e] = firstEdge[a];
            edgeDst[e] = b;
            edgeLen[e] = c;
            firstEdge[a] = e;
        }

        private void shortestPaths(int s) {
            Arrays.fill(d, infinity);
            Arrays.fill(heapWhere, -1);
            d[s] = 0;
            heapSize = 1;
            heapWhere[s] = 0;
            heap[0] = s;
            while (heapSize > 0) {
                int v = heap[0];
                if (heapSize > 1) {
                    heapSwap(0, heapSize - 1);
                    --heapSize;
                    heapWhere[v] = -1;
                    heapDown(0);
                } else {
                    --heapSize;
                    heapWhere[v] = -1;
                }
                for (int e = firstEdge[v]; e >= 0; e = edgeNxt[e]) {
                    int u = edgeDst[e];
                    long w = edgeLen[e] + phi[v] - phi[u];
                    if (d[u] > d[v] + w) {
                        d[u] = d[v] + w;
                        if (heapWhere[u] < 0) {
                            heapWhere[u] = heapSize++;
                            heap[heapSize - 1] = u;
                        }
                        heapUp(heapWhere[u]);
                        heapDown(heapWhere[u]);
                    }
                }
            }
        }

        private void addToQueue(int v) {
            if (d[v] >= queueFirst.length) {
                return;
            }
            int qId = (int) d[v];
            int item = queueLastItem++;
            queueItemValue[item] = v;
            queueNext[item] = queueFirst[qId];
            queueFirst[qId] = item;
        }

        private void bfs(int s, int numQueues) {
            queueLastItem = 0;
            Arrays.fill(d, infinity);
            d[s] = 0;
            Arrays.fill(queueFirst, 0, numQueues, -1);
            addToQueue(s);
            Arrays.fill(was, false);
            for (int qId = 0; qId < numQueues; qId++) {
                while (queueFirst[qId] >= 0) {
                    int item = queueFirst[qId];
                    queueFirst[qId] = queueNext[item];
                    int v = queueItemValue[item];
                    if (was[v]) {
                        continue;
                    }
                    was[v] = true;
                    for (int e = firstEdge[v]; e >= 0; e = edgeNxt[e]) {
                        int u = edgeDst[e];
                        if (was[u]) {
                            continue;
                        }
                        long w = edgeLen[e] + phi[v] - phi[u];
                        long nd = d[v] + w;
                        if (d[u] > nd) {
                            d[u] = nd;
                            addToQueue(u);
                        }
                    }
                }
            }
        }

        private void heapUp(int i) {
            while (i > 0) {
                int p = (i - 1) / 2;
                if (d[heap[i]] < d[heap[p]]) {
                    heapSwap(i, p);
                    i = p;
                } else {
                    break;
                }
            }
        }

        private void heapDown(int i) {
            while (true) {
                int j = i;
                if (2 * i + 1 < heapSize && d[heap[2 * i + 1]] < d[heap[j]]) {
                    j = 2 * i + 1;
                }
                if (2 * i + 2 < heapSize && d[heap[2 * i + 2]] < d[heap[j]]) {
                    j = 2 * i + 2;
                }
                if (i == j) {
                    break;
                } else {
                    heapSwap(i, j);
                    i = j;
                }
            }
        }

        private void heapSwap(int i, int j) {
            int ai = heap[i];
            int aj = heap[j];
            heapWhere[ai] = j;
            heapWhere[aj] = i;
            heap[i] = aj;
            heap[j] = ai;
        }

    }

    static class FastScanner {
        private BufferedReader in;
        private StringTokenizer st;

        public FastScanner(InputStream stream) {
            in = new BufferedReader(new InputStreamReader(stream));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(in.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

