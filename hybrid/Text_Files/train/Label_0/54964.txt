import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.io.UncheckedIOException;
import java.util.List;
import java.io.Closeable;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) throws Exception {
        Thread thread = new Thread(null, new TaskAdapter(), "", 1 << 27);
        thread.start();
        thread.join();
    }

    static class TaskAdapter implements Runnable {
        @Override
        public void run() {
            InputStream inputStream = System.in;
            OutputStream outputStream = System.out;
            FastInput in = new FastInput(inputStream);
            FastOutput out = new FastOutput(outputStream);
            TaskE solver = new TaskE();
            solver.solve(1, in, out);
            out.close();
        }
    }
    static class TaskE {
        private int inf = (int) 1e8;

        public void solve(int testNumber, FastInput in, FastOutput out) {
            int n = in.readInt();
            Node[] nodes = new Node[n + 1];
            for (int i = 1; i <= n; i++) {
                nodes[i] = new Node();
                nodes[i].id = i;
                nodes[i].val = in.readInt();
            }
            for (int i = 1; i < n; i++) {
                Node a = nodes[in.readInt()];
                Node b = nodes[in.readInt()];
                a.next.add(b);
                b.next.add(a);
            }

            dfs(nodes[1], null);
            dsuOnTree(nodes[1], null);
            int minCost = nodes[1].allPositive;
            for (int i = 0; i < nodes[1].size; i++) {
                if (nodes[1].dp[i] < 0) {
                    minCost = Math.min(minCost, i);
                    break;
                }
            }

            out.println(minCost);
        }

        public void dsuOnTree(Node root, long[] dp) {
            if (dp == null) {
                dp = new long[root.size];
            }
            root.dp = dp;
            if (root.size == 1) {
                root.allPositive = root.val > 0 ? 0 : inf;
                root.dp[0] = root.val;
                return;
            }

            dsuOnTree(root.heavy, dp);
            root.allPositive = root.heavy.allPositive;
            for (int i = 0; i < root.heavy.size; i++) {
                if (dp[i] < 0) {
                    root.allPositive = Math.min(root.allPositive, i + 1);
                    break;
                }
            }
            for (int i = root.heavy.size; i >= 0; i--) {
                dp[i] += root.val;
                if (i > 0 && dp[i - 1] < 0) {
                    dp[i] = Math.min(dp[i], root.val);
                }
                if (i > root.heavy.allPositive) {
                    dp[i] = Math.min(dp[i], root.val);
                }
            }
            for (int i = root.heavy.size + 1; i < root.size; i++) {
                dp[i] = (long) 1e18;
            }

            for (Node node : root.next) {
                if (node == root.heavy) {
                    continue;
                }
                dsuOnTree(node, null);
                // update all positive
                int localAllPos = node.allPositive;
                for (int i = 0; i < node.size; i++) {
                    if (node.dp[i] < 0) {
                        localAllPos = Math.min(localAllPos, i + 1);
                        break;
                    }
                }
                root.allPositive += localAllPos;

                int splitCost = node.allPositive + 1;
                for (int i = 0; i < node.size; i++) {
                    if (node.dp[i] < 0) {
                        splitCost = Math.min(splitCost, i + 1);
                        break;
                    }
                }
                // split or not
                for (int i = root.size - 1; i >= 0; i--) {
                    // split
                    dp[i] += node.dp[0];
                    if (i >= splitCost) {
                        dp[i] = Math.min(dp[i], dp[i - splitCost]);
                    }
                    for (int j = 1; j < node.size && j <= i; j++) {
                        int k = i - j;
                        dp[i] = Math.min(dp[i], dp[k] + node.dp[j]);
                    }
                }
            }

            if (root.val < 0) {
                root.allPositive = inf;
            }

        }

        public void dfs(Node root, Node p) {
            root.next.remove(p);
            root.size = 1;
            for (Node node : root.next) {
                dfs(node, root);
                root.size += node.size;
                if (root.heavy == null || root.heavy.size < node.size) {
                    root.heavy = node;
                }
            }
        }

    }
    static class FastInput {
        private final InputStream is;
        private byte[] buf = new byte[1 << 13];
        private int bufLen;
        private int bufOffset;
        private int next;

        public FastInput(InputStream is) {
            this.is = is;
        }

        private int read() {
            while (bufLen == bufOffset) {
                bufOffset = 0;
                try {
                    bufLen = is.read(buf);
                } catch (IOException e) {
                    bufLen = -1;
                }
                if (bufLen == -1) {
                    return -1;
                }
            }
            return buf[bufOffset++];
        }

        public void skipBlank() {
            while (next >= 0 && next <= 32) {
                next = read();
            }
        }

        public int readInt() {
            int sign = 1;

            skipBlank();
            if (next == '+' || next == '-') {
                sign = next == '+' ? 1 : -1;
                next = read();
            }

            int val = 0;
            if (sign == 1) {
                while (next >= '0' && next <= '9') {
                    val = val * 10 + next - '0';
                    next = read();
                }
            } else {
                while (next >= '0' && next <= '9') {
                    val = val * 10 - next + '0';
                    next = read();
                }
            }

            return val;
        }

    }
    static class FastOutput implements AutoCloseable, Closeable {
        private StringBuilder cache = new StringBuilder(10 << 20);
        private final Writer os;

        public FastOutput(Writer os) {
            this.os = os;
        }

        public FastOutput(OutputStream os) {
            this(new OutputStreamWriter(os));
        }

        public FastOutput println(int c) {
            cache.append(c).append('\n');
            return this;
        }

        public FastOutput flush() {
            try {
                os.append(cache);
                os.flush();
                cache.setLength(0);
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
            return this;
        }

        public void close() {
            flush();
            try {
                os.close();
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        }

        public String toString() {
            return cache.toString();
        }

    }
    static class Node {
        List<Node> next = new ArrayList<>();
        Node heavy;
        int size;
        long[] dp;
        int allPositive;
        int val;
        int id;

        public String toString() {
            return "" + id;
        }

    }
}

