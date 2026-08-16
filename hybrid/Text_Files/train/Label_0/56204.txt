import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.List;
import java.io.IOException;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in Actual solution is at the top
 * 
 * @author daltao
 */
public class Main {
    public static void main(String[] args) throws Exception {
        Thread thread = new Thread(null, new TaskAdapter(), "daltao", 1 << 27);
        thread.start();
        thread.join();
    }

    static class TaskAdapter implements Runnable {
        @Override
        public void run() {
            InputStream inputStream = System.in;
            OutputStream outputStream = System.out;
            FastInput in = new FastInput(inputStream);
            PrintWriter out = new PrintWriter(outputStream);
            TaskE solver = new TaskE();
            solver.solve(1, in, out);
            out.close();
        }
    }
    static class TaskE {
        int inf = (int) 1e8;

        public void solve(int testNumber, FastInput in, PrintWriter out) {
            int n = in.readInt();

            Node[] nodes = new Node[n + 1];
            for (int i = 1; i <= n; i++) {
                nodes[i] = new Node();
                nodes[i].id = i;
            }

            Node x = nodes[in.readInt()];
            Node y = nodes[in.readInt()];

            List<Query> querys = new ArrayList<>(n);
            for (int i = 1; i < n; i++) {
                Node a = nodes[in.readInt()];
                Node b = nodes[in.readInt()];
                a.red.add(b);
                b.red.add(a);
                Query q = new Query();
                q.a = a;
                q.b = b;
                querys.add(q);
                a.lcaQueries.add(q);
                b.lcaQueries.add(q);
            }

            for (int i = 1; i < n; i++) {
                Node a = nodes[in.readInt()];
                Node b = nodes[in.readInt()];
                a.blue.add(b);
                b.blue.add(a);
            }

            dfsForDepth(y, null, 0);
            dfsForLca(y, null);

            for (Query q : querys) {
                if (q.a.depth + q.b.depth - 2 * q.lca.depth >= 3) {
                    q.a.escape = q.b.escape = true;
                }
            }

            int escape = escape(x, null, 0);
            if (escape == inf) {
                out.println(-1);
            } else {
                out.println(escape * 2);
            }
        }

        public void dfsForLca(Node root, Node fa) {
            root.blue.remove(fa);
            root.lca = root;
            root.visited = true;
            for (Node node : root.blue) {
                if (node == fa) {
                    continue;
                }
                dfsForLca(node, root);
                Node.merge(node, root);
                root.find().lca = root;
            }

            for (Query q : root.lcaQueries) {
                Node other = q.a == root ? q.b : q.a;
                if (!other.visited) {
                    continue;
                }
                q.lca = other.find().lca;
            }
        }

        public int escape(Node root, Node fa, int depth) {
            root.red.remove(fa);
            if (root.depth <= depth) {
                return root.depth;
            }
            if (root.escape) {
                return inf;
            }
            int max = root.depth;
            for (Node node : root.red) {
                max = Math.max(max, escape(node, root, depth + 1));
            }
            return max;
        }

        public void dfsForDepth(Node root, Node fa, int depth) {
            root.blue.remove(fa);
            root.depth = depth;
            for (Node node : root.blue) {
                dfsForDepth(node, root, depth + 1);
            }
        }

    }
    static class Query {
        Node a;
        Node b;
        Node lca;

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
                    throw new RuntimeException(e);
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
    static class Node {
        List<Node> red = new ArrayList<>();
        List<Node> blue = new ArrayList<>();
        List<Query> lcaQueries = new ArrayList<>();
        boolean escape;
        int depth;
        int id;
        boolean visited = false;
        Node p = this;
        int rank;
        Node lca;

        Node find() {
            return p == p.p ? p : (p = p.find());
        }

        static void merge(Node a, Node b) {
            a = a.find();
            b = b.find();
            if (a == b) {
                return;
            }
            if (a.rank == b.rank) {
                a.rank++;
            }
            if (a.rank > b.rank) {
                b.p = a;
            } else {
                a.p = b;
            }
        }

    }
}

