import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class E {

    static int root = 0;
    static ArrayList<Edge>[] adj;
    static int[][] p;
    static long[] prefSum;
    static int[] id;
    static int[] minId;
    static int[] maxId;
    static long total = 0;
    static int last = -1;

    static class Edge {
        int to, cst;

        public Edge(int to, int cst) {
            this.to = to;
            this.cst = cst;
        }
    }

    static class Node {
        int node, parent;

        public Node(int node, int parent) {
            this.node = node;
            this.parent = parent;
        }
    }

    public static void prec() {
        Stack<Node> s = new Stack<Node>();
        s.add(new Node(root, -1));
        while (!s.isEmpty()) {
            Node cur = s.pop();
            int size = adj[cur.node].size();
            for (int i = 0; i < size; i++) {
                int nxt = adj[cur.node].get(i).to;
                if (nxt != cur.parent) {
                    s.push(new Node(nxt, cur.node));
                    p[nxt][0] = cur.node;
                    for (int j = 0; j < 20; j++) {
                        if (p[nxt][j] != -1) {
                            p[nxt][j + 1] = p[p[nxt][j]][j];
                        }
                    }
                }
            }
        }
    }

    static int counter = 0;

    public static int pre(int cur, long sum, int p) {
        prefSum[cur] = sum;
        id[cur] = counter++;
        int size = adj[cur].size();
        int max = id[cur];
        for (int i = 0; i < size; i++)
            if (adj[cur].get(i).to != p)
                max = Math.max(max, pre(adj[cur].get(i).to, sum
                        + adj[cur].get(i).cst, cur));
        minId[cur] = id[cur];
        return maxId[cur] = max;
    }

    static int[] tree;
    static int n;

    public static void set(int idx, int v) {
        idx++;
        while (idx < n + 10) {
            tree[idx] += v;
            idx += (idx & -idx);
        }
    }

    public static int get(int idx) {
        idx++;
        int s = 0;
        while (idx > 0) {
            s += tree[idx];
            idx -= (idx & -idx);
        }
        return s;
    }

    public static boolean isfilled(int node) {
        if (minId[node] == -1) {
            // shouldn't happen
            return false;
        }
        if (v[node])
            return true;
        return get(maxId[node]) - get(minId[node]) != 0;
    }

    static TreeSet<Integer> tr = new TreeSet<Integer>();
    static boolean[] v;

    public static void main(String[] args) throws IOException {
        InputReader in = new InputReader();
        StringBuilder sb = new StringBuilder();
        n = in.nextInt();
        adj = new ArrayList[n];
        p = new int[n][20];
        v = new boolean[n];
        id = new int[n];
        tree = new int[n + 10];
        prefSum = new long[n];
        minId = new int[n];
        Arrays.fill(minId, -1);
        maxId = new int[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<Edge>();
            Arrays.fill(p[i], -1);
        }
        for (int i = 0; i < n - 1; i++) {
            int a = in.nextInt() - 1;
            int b = in.nextInt() - 1;
            int c = in.nextInt();
            Edge e1 = new Edge(a, c);
            Edge e2 = new Edge(b, c);
            adj[a].add(e2);
            adj[b].add(e1);
        }

        prec();
        pre(root, 0, -1);
        int q = in.nextInt();
        while (q-- > 0) {
            char x = in.next().charAt(0);
            if (x == '?') {
                if (tr.size() == 1)
                    sb.append(0 + "\n");
                else {
                    int node = last;

                    if (node == -1)
                        sb.append(total + "\n");
                    else {
                        for (int pow = 19; pow >= 0; pow--) {
                            if (p[node][pow] != -1) {
                                // System.out.println(get(minId[p[node][pow]]));
                                // System.out.println(get(maxId[p[node][pow]]));
                                int size = get(maxId[p[node][pow]])
                                        - get(minId[p[node][pow]]);
                                if ((size + (v[p[node][pow]] ? 1 : 0) < tr
                                        .size())
                                        || (size + (v[p[node][pow]] ? 1 : 0) == tr
                                                .size() && size < tr.size())) {
                                    node = p[node][pow];
                                }
                            }
                        }
                        int size = get(maxId[node]) - get(minId[node]);
                        if (size + (v[node] ? 1 : 0) < tr.size())
                            node = p[node][0];
                        sb.append((total - prefSum[node]) + "\n");
                    }
                }
            } else {
                int node = in.nextInt() - 1;
                if (x == '+') {
                    int Z = node;
                    for (int pow = 19; pow >= 0; pow--) {
                        if (p[Z][pow] != -1) {
                            if (!isfilled(p[Z][pow])) {
                                Z = p[Z][pow];
                            }
                        }
                    }
                    if (!isfilled(Z)) {
                        total += prefSum[node]
                                - (p[Z][0] == -1 ? 0 : prefSum[p[Z][0]]);
                        if (last == -1 || id[node] < id[last])
                            last = node;
                    }
                    set(id[node], 1);
                    tr.add(node);
                    v[node] = true;
                } else {
                    v[node] = false;
                    tr.remove(new Integer(node));
                    set(id[node], -1);
                    int Z = node;
                    for (int pow = 19; pow >= 0; pow--) {
                        if (p[Z][pow] != -1) {
                            if (!isfilled(p[Z][pow])) {
                                Z = p[Z][pow];
                            }
                        }
                    }
                    if (!isfilled(Z)) {
                        total -= (prefSum[node] - (p[Z][0] == -1 ? 0
                                : prefSum[p[Z][0]]));
                    }
                    if (last == node && !tr.isEmpty()) {
                        last = tr.first();
                    } else if (last == node) {
                        last = -1;
                    }
                }
            }
        }
        System.out.print(sb);
    }

    static class InputReader {
        BufferedReader in;
        StringTokenizer st;
        String cur;

        public InputReader() throws IOException {
            in = new BufferedReader(new InputStreamReader(System.in));
            st = new StringTokenizer(cur = in.readLine());
        }

        public boolean hasNext() throws IOException {
            if (!st.hasMoreElements()) {
                cur = in.readLine();
                if (cur == null)
                    return false;
                st = new StringTokenizer(cur);
            }
            return true;
        }

        public String next() throws IOException {
            while (!st.hasMoreElements())
                st = new StringTokenizer(cur = in.readLine());
            return st.nextToken();
        }

        public int nextInt() throws NumberFormatException, IOException {
            return Integer.parseInt(next());
        }

        public long nextLong() throws NumberFormatException, IOException {
            return Long.parseLong(next());
        }
    }
}
