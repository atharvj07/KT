import java.io.*;
import java.nio.CharBuffer;
import java.util.*;

public class Main {

    private static final int MOD = 998244353;

    public static void main(String[] args) {
        SimpleScanner scanner = new SimpleScanner(System.in);
        PrintWriter writer = new PrintWriter(System.out);

        int n = scanner.nextInt();
        ArrayList<Point> points = new ArrayList<>(n);
        for (int i = 0; i < n; ++i) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            points.add(new Point(x, y));
        }
        int[] leftTop = new int[n];
        int[] leftBottom = new int[n];
        int[] rightTop = new int[n];
        int[] rightBottom = new int[n];
        points.sort(Comparator.comparingInt(o -> -o.x));
        TreapWithOutRotation treap = new TreapWithOutRotation();
        for (int i = 0; i < n; ++i) {
            rightBottom[n - i - 1] = treap.getRank(points.get(i).y);
            rightTop[n - i - 1] = i - rightBottom[n - i - 1];
            treap.insert(points.get(i).y);
        }
        Collections.reverse(points);
        treap = new TreapWithOutRotation();
        for (int i = 0; i < n; ++i) {
            leftBottom[i] = treap.getRank(points.get(i).y);
            leftTop[i] = i - leftBottom[i];
//            writer.println(leftTop[i] + " " + leftBottom[i] + " " + rightTop[i] + " " + rightBottom[i]);
//            writer.flush();
            treap.insert(points.get(i).y);
        }
        long[] power2 = new long[n + 1];
        power2[0] = 1;
        for (int i = 1; i <= n; ++i)
            power2[i] = power2[i - 1] * 2 % MOD;
        long ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = (ans + power2[n - 1]) % MOD;
            long t = (power2[leftTop[i]] - 1) * (power2[rightBottom[i]] - 1) % MOD * power2[leftBottom[i] + rightTop[i]] % MOD
                    + (power2[rightTop[i]] - 1) * (power2[leftBottom[i]] - 1) % MOD * power2[rightBottom[i] + leftTop[i]] % MOD
                    - (power2[leftTop[i]] - 1) * (power2[rightBottom[i]] - 1) % MOD * (power2[rightTop[i]] - 1) % MOD * (power2[leftBottom[i]] - 1) % MOD;
            t = (t + MOD) % MOD;
            ans = (ans + t) % MOD;
        }
        writer.println(ans);

        writer.close();
    }

    private static class Point {
        final int x, y;

        private Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private static class TreapWithOutRotation {

        private Node root;
        private final int maxPriority;
        private Random random;

        private TreapWithOutRotation() {
            this(Integer.MAX_VALUE);
        }

        private TreapWithOutRotation(int maxPriority) {
            this.maxPriority = maxPriority;
            this.random = new Random();
        }

        private Node[] split(int key, Node node) {
            if (node == null)
                return new Node[]{null, null};
            if (key < node.key) {
                Node[] t = split(key, node.lChild);
                node.lChild = t[1];
                node.updateSize();
                return new Node[]{t[0], node};
            } else {
                Node[] t = split(key, node.rChild);
                node.rChild = t[0];
                node.updateSize();
                return new Node[]{node, t[1]};
            }
        }

        private Node merge(Node l, Node r) {
            if (l == null)
                return r;
            if (r == null)
                return l;
            if (l.priority > r.priority) {
                l.rChild = merge(l.rChild, r);
                l.updateSize();
                return l;
            } else {
                r.lChild = merge(l, r.lChild);
                r.updateSize();
                return r;
            }
        }

        private void insert(int key) {
            root = insert(key, random.nextInt(maxPriority), root);
        }

        private Node insert(int key, int priority, Node node) {
            if (node == null) {
                return new Node(key, priority, null, null);
            }
            if (priority > node.priority) {
                Node[] t = split(key, node);
                return new Node(key, priority, t[0], t[1]);
            }
            if (key < node.key) {
                node.lChild = insert(key, priority, node.lChild);
            } else if (key > node.key) {
                node.rChild = insert(key, priority, node.rChild);
            }
            node.updateSize();
            return node;
        }

        private int getRank(int key) {
            return getRank(key, root);
        }

        private int getRank(int key, Node node) {
            if (node == null)
                return 0;
            if (key < node.key)
                return getRank(key, node.lChild);
            if (key == node.key)
                return Node.getSize(node.lChild);
            return Node.getSize(node.lChild) + 1 + getRank(key, node.rChild);
        }

        private static class Node {
            private int key, priority, size;
            private Node lChild, rChild;

            private Node(int key, int priority, Node lChild, Node rChild) {
                this.key = key;
                this.priority = priority;
                this.lChild = lChild;
                this.rChild = rChild;
                this.size = getSize(lChild) + getSize(rChild) + 1;
            }

            private void updateSize() {
                size = getSize(lChild) + getSize(rChild) + 1;
            }

            private static int getSize(Node node) {
                return node == null ? 0 : node.size;
            }
        }
    }

    private static class SimpleScanner {

        private static final int BUFFER_SIZE = 10240;

        private Readable in;
        private CharBuffer buffer;
        private boolean eof;

        private SimpleScanner(InputStream in) {
            this.in = new BufferedReader(new InputStreamReader(in));
            buffer = CharBuffer.allocate(BUFFER_SIZE);
            buffer.limit(0);
            eof = false;
        }


        private char read() {
            if (!buffer.hasRemaining()) {
                buffer.clear();
                int n;
                try {
                    n = in.read(buffer);
                } catch (IOException e) {
                    n = -1;
                }
                if (n <= 0) {
                    eof = true;
                    return '\0';
                }
                buffer.flip();
            }
            return buffer.get();
        }

        void checkEof() {
            if (eof)
                throw new NoSuchElementException();
        }

        char nextChar() {
            checkEof();
            char b = read();
            checkEof();
            return b;
        }

        String next() {
            char b;
            do {
                b = read();
                checkEof();
            } while (Character.isWhitespace(b));
            StringBuilder sb = new StringBuilder();
            do {
                sb.append(b);
                b = read();
            } while (!eof && !Character.isWhitespace(b));
            return sb.toString();
        }

        int nextInt() {
            return Integer.valueOf(next());
        }

        long nextLong() {
            return Long.valueOf(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }
    }
}