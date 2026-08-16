import java.io.*;
import java.util.List;
import java.util.Objects;
import java.util.StringTokenizer;
import java.util.Vector;

public class Main {

    public static void main(String[] args) throws IOException {
        Reader in = new Reader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));

        int n = in.nextInt();
        int m = in.nextInt();
        Node[] nodes = new Node[n];
        for (int i = 0; i < 2 * m; i++) {
            int x = in.nextInt() - 1;
            nodes[x] = new Node(x, true);
        }
        for (int i = 0; i < n; i++) {
            if (nodes[i] == null) nodes[i] = new Node(i, false);
        }

        for (int i = 0; i < n - 1; i++) {
            int x = in.nextInt() - 1;
            int y = in.nextInt() - 1;

            nodes[x].kids.add(nodes[y]);
            nodes[y].kids.add(nodes[x]);
        }

        countChild(nodes[0]);
        long ans = dfs(nodes[0], 0);

        out.println(ans);

        out.flush();
        in.close();
        out.close();
    }

    private static void countChild(Node now) {
        now.sum = now.mark ? 1 : 0;
        for (Node kid : now.kids) {
            kid.kids.remove(now);
            countChild(kid);
            now.sum += kid.sum;
        }
    }

    private static long dfs(Node now, int father) {
        long ans = 0;
        for (Node kid : now.kids) {
            ans += Math.min(kid.sum, now.sum - kid.sum + father);
            ans += dfs(kid, now.sum - kid.sum + father);
        }
        return ans;
    }

    static class Node {
        private final int index;
        private final boolean mark;
        private final List<Node> kids;
        private int sum;

        public Node(int index, boolean mark) {
            this.index = index;
            this.mark = mark;
            this.kids = new Vector<>();
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Node node = (Node) o;
            return index == node.index;
        }

        @Override
        public int hashCode() {
            return Objects.hash(index);
        }
    }

    static class Reader {
        BufferedReader reader;
        StringTokenizer st;

        Reader(InputStreamReader stream) {
            reader = new BufferedReader(stream);
            st = null;
        }

        void close() throws IOException {
            reader.close();
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        String nextLine() throws IOException {
            return reader.readLine();
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

    }
}