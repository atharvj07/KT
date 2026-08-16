import java.util.*;

public class Main implements Runnable {

    private static int MOD = 1_000_000_007;

    public static void main(String[] args) {
        // Run with 32MB stack
        Thread thread = new Thread(null, new Main(), "", 32 * 1024 * 1024);
        thread.start();
    }

    @Override
    public void run() {
        final Scanner scanner = new Scanner(System.in);
        solve(scanner);
    }

    static void solve(Scanner scanner) {
        int V = scanner.nextInt();
        int E = scanner.nextInt();
        int F = scanner.nextInt();
        scanner.nextLine();

        MinCost minCost = new MinCost(V);
        for (int i = 0; i < E; i++) {
            int[] e = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            minCost.addEdge(e[0], e[1], e[3], e[2]);
        }

        minCost.run(0, V - 1, F);
        if (minCost.totalFlow == F) {
            System.out.println(minCost.totalCost);
        } else {
            System.out.println(-1);
        }
    }

}

class MinCost {
    private int size;
    private Map<Integer, Map<Integer, Edge>> edges;
    public long totalFlow;
    public long totalCost;

    public MinCost(int size) {
        this.size = size;
        edges = new HashMap<>();
        totalFlow = 0;
        totalCost = 0;
    }

    public void addEdge(int from, int to, int cost, int cap) {
        if (!edges.containsKey(from)) {
            edges.put(from, new HashMap<>());
        }
        edges.get(from).put(to, new Edge(from, to, cost, cap));

        if (!edges.containsKey(to)) {
            edges.put(to, new HashMap<>());
        }
        edges.get(to).put(from, new Edge(to, from, -cost, 0));
    }

    public void run(int s, int e, long flow) {
        List<Integer> path = findPath(s, e);
        while (!path.isEmpty()) {
            long maxFlow = Integer.MAX_VALUE;
            for (int i = 0; i < path.size() - 1; i++) {
                maxFlow = Math.min(maxFlow, edges.get(path.get(i)).get(path.get(i + 1)).cap);
            }
            if (totalFlow + maxFlow >= flow) {
                maxFlow = flow - totalFlow;
            }
            totalFlow += maxFlow;

            long costSum = 0;
            for (int i = 0; i < path.size() - 1; i++) {
                costSum += maxFlow * edges.get(path.get(i)).get(path.get(i + 1)).cost;
            }
            for (int i = 0; i < path.size() - 1; i++) {
                edges.get(path.get(i)).get(path.get(i + 1)).cap -= maxFlow;
                edges.get(path.get(i + 1)).get(path.get(i)).cap += maxFlow;
            }
            totalCost = totalCost + costSum;
            if (totalFlow == flow) {
                break;
            }
            path = findPath(s, e);
        }
    }

    private List<Integer> findPath(int s, int e) {
        BellmanFord bellmanFord = new BellmanFord(size);
        edges.forEach((from, toMap) ->
                toMap.forEach((to, edge) -> {
                    if (edge.cap > 0)
                        bellmanFord.addEdge(edge.from, edge.to, edge.cost);
                }));
        bellmanFord.run(s);
        if (bellmanFord.dist[e] == Long.MAX_VALUE / 2) {
            return Collections.emptyList();
        }
        List<Integer> nodes = new ArrayList<>();
        int curr = e;
        while (curr != s) {
            nodes.add(curr);
            curr = bellmanFord.from[curr];
        }
        nodes.add(curr);
        Collections.reverse(nodes);
        return nodes;
    }

}

class BellmanFord {

    private int size;
    public long[] dist;
    public int[] from;
    public List<Edge> edges;

    public BellmanFord(int size) {
        this.size = size;
        dist = new long[size];
        Arrays.fill(dist, Long.MAX_VALUE / 2);
        from = new int[size];
        Arrays.fill(from, -1);
        edges = new ArrayList<>();
    }

    public void addEdge(int from, int to, int cost) {
        edges.add(new Edge(from, to, cost));
    }

    public void run(int start) {
        dist[start] = 0;
        for (int i = 0; i < size; i++) {
            boolean updated = false;
            for (Edge e : edges) {
                if (dist[e.from] != Long.MAX_VALUE / 2
                        && dist[e.to] > dist[e.from] + e.cost) {
                    dist[e.to] = dist[e.from] + e.cost;
                    from[e.to] = e.from;
                    updated = true;
                }
            }
            // found loops. update all nodes in loops with Long.MIN_VALUE
            if (i == size - 1 && updated) {
                for (int j = 0; j < size; j++) {
                    for (Edge e : edges) {
                        if (dist[e.from] == Long.MIN_VALUE || dist[e.to] > dist[e.from] + e.cost) {
                            dist[e.to] = Long.MIN_VALUE;
                        }
                    }
                }
            }
        }
    }
}

class Edge {
    public int from;
    public int to;
    public int cost;
    public int cap;

    public Edge(int from, int to) {
        this.from = from;
        this.to = to;
        this.cost = 1;
        this.cap = 1;
    }

    public Edge(int from, int to, int cost) {
        this.from = from;
        this.to = to;
        this.cost = cost;
        this.cap = 1;
    }

    public Edge(int from, int to, int cost, int cap) {
        this.from = from;
        this.to = to;
        this.cost = cost;
        this.cap = cap;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Edge edge = (Edge) o;
        return from == edge.from &&
                to == edge.to &&
                cost == edge.cost &&
                cap == edge.cap;
    }

    @Override
    public int hashCode() {
        return Objects.hash(from, to, cost, cap);
    }
}

