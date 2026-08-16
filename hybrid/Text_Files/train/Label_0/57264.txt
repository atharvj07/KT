import java.io.PrintWriter;
import java.util.*;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        new Thread(null, Main::solve, "solver", 64000000L).start();
    }
    public static void solve() {
        try (Scanner in = new Scanner(System.in); PrintWriter out = new PrintWriter(System.out)) {
            int n = in.nextInt(), m = in.nextInt();

            // Graph Construction
            Node[] nodes = new Node[n];
            for (int i = 0; i < n; i++) nodes[i] = new Node(i);
            for (int i = 0; i < m; i++) {
                int x = in.nextInt() - 1, y = in.nextInt() - 1;
                Edge nat = new Edge(nodes[x], nodes[y]);
                Edge rev = new Edge(nodes[y], nodes[x]);
                nat.rev = rev;
                rev.rev = nat;
                nodes[x].dest.add(nat);
                nodes[y].dest.add(rev);
            }

            // Bridge listing
            Bridges bridges = new Bridges(nodes);
            bridges.solve();

            int group = 0;
            for (int i = 0; i < n; i++) {
                if (nodes[i].visited) continue;
                nodes[i].dir(group);
                group++;
            }

            // Tree Construction
            Node[] tree = new Node[group];
            for (int i = 0; i < group; i++) tree[i] = new Node(i);
            for (int i = 0; i < n; i++) {
                for (Edge edge : nodes[i].dest) {
                    if (!edge.isBridge || edge.t.index < edge.s.index) continue;
                    int x = edge.s.group, y = edge.t.group;
                    Edge nat = new Edge(tree[x], tree[y]);
                    Edge rev = new Edge(tree[y], tree[x]);
                    nat.rev = rev;
                    nat.subEdge = edge;
                    rev.rev = nat;
                    rev.subEdge = edge.rev;
                    tree[x].dest.add(nat);
                    tree[y].dest.add(rev);
                }
            }
            tree[0].treenize(null);

            // Solve
            try {
                int k = in.nextInt();
                for (int i = 0; i < k; i++) {
                    int x = in.nextInt() - 1, y = in.nextInt() - 1;
                    int s = nodes[x].group, t = nodes[y].group;
                    if (s == t) continue;
                    Node lca = Node.lca(tree[s], tree[t]);
                    if (tree[s] != lca) {
                        Constraint c = new Constraint(Direction.UP, tree[s], lca);
                        tree[s].constraint = tree[s].constraint == null ? c : tree[s].constraint.merge(c);
                    }
                    if (tree[t] != lca) {
                        Constraint c = new Constraint(Direction.DOWN, tree[t], lca);
                        tree[t].constraint = tree[t].constraint == null ? c : tree[t].constraint.merge(c);
                    }
                }

                tree[0].solve();
            } catch (RuntimeException ex) {
                out.println("No");
                return;
            }

            out.println("Yes");
            for (int i = 0; i < n; i++) {
                for (Edge edge : nodes[i].dest) {
                    if (!edge.rev.valid) {
                        edge.valid = true;
                        out.println((edge.s.index + 1) + " " + (edge.t.index + 1));
                    }
                }
            }
        }
    }

    private static class Bridges {
        int n;
        Node[] p;
        int[] pre, low;
        int pr;

        Bridges(Node[] p) {
            this.n = p.length;
            this.pre = new int[n];
            this.low = new int[n];
            this.p = p;
        }

        int dfs(int i, int from) {
            if (pre[i] > 0) return low[i];
            pre[i] = pr;
            low[i] = pr;
            for (Edge edge : p[i].dest) {
                int j = edge.t.index;
                if (j == from) continue;
                pr++;
                int to = dfs(j, i);
                if (to < pre[i]) {
                    low[i] = Math.min(low[i], to);
                } else {
                    if (low[j] == pre[j]) {
                        edge.isBridge = edge.rev.isBridge = true;
                    }
                }
            }
            return low[i];
        }

        void solve() {
            pr = 1;
            dfs(0, -1);
        }

    }

    private static class Node {
        int index, group;
        List<Edge> dest = new ArrayList<>();
        boolean visited;
        Node[] parents;
        int depth;
        Constraint constraint;


        Node(int index) {
            this.index = index;
        }

        void dir(int group) {
            if (visited) return;
            visited = true;
            this.group = group;
            for (Edge edge : dest) {
                if (edge.isBridge) continue;
                if (!edge.rev.valid) edge.valid = true;
                if (edge.t.visited) continue;
                edge.t.dir(group);
            }
        }

        void treenize(Node from) {
            this.parents = new Node[20];
            this.depth = (from == null) ? 0 : from.depth + 1;
            this.parents[0] = (from == null) ? this : from;
            for (int i = 1; i < 20; i++) {
                parents[i] = parents[i - 1].parents[i - 1];
            }

            for (Edge edge : dest) {
                if (edge.t == from) continue;
                edge.t.treenize(this);
            }
        }

        static Node lca(Node x, Node y) {
            if (x.depth < y.depth) return lca(y, x);
            for (int i = 19; i >= 0; i--) {
                if (x.parents[i].depth > y.depth) x = x.parents[i];
            }
            if (x.depth > y.depth) x = x.parents[0];

            for (int i = 19; i >= 0; i--) {
                if (x.parents[i] != y.parents[i]) {
                    x = x.parents[i];
                    y = y.parents[i];
                }
            }
            if (x != y) return x.parents[0];
            return x;
        }

        void solve() {
            Constraint c = this.constraint;
            for (Edge e : dest) {
                if (parents[0] == e.t) continue;
                e.t.solve();
                if (e.t.constraint != null) {
                    if (e.t.constraint.direction == Direction.UP) e.subEdge.rev.valid = true;
                    else e.subEdge.valid = true;
                    if (e.t.constraint.until != this) {
                        if (c == null) c = e.t.constraint;
                        else c = c.merge(e.t.constraint);
                    }
                }
            }
            this.constraint = c;
        }
    }

    private static class Edge {
        Node s, t;
        Edge rev;
        Edge subEdge;
        boolean isBridge;
        boolean valid;

        Edge(Node s, Node t) {
            this.s = s;
            this.t = t;
        }
    }

    enum Direction {
        UP, DOWN;
    }

    private static class Constraint {
        Direction direction;
        Node from, until;

        Constraint(Direction direction, Node from, Node until) {
            this.direction = direction;
            this.from = from;
            this.until = until;
        }

        Constraint merge(Constraint other) {
            if (direction != other.direction) throw new RuntimeException("Constraint violation@"+from.index+"and"+other.from.index);
            return until.depth < other.until.depth ? this : other;
        }
    }

}

