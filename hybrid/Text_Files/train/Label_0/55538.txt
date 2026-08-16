import java.util.*;
import java.util.stream.Collectors;

public class Main implements Runnable {

    private static int MOD = 1_000_000_007;

    public static void main(String[] args) {
        // Run with 16MB stack
        Thread thread = new Thread(null, new Main(), "", 16 * 1024 * 1024);
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
        scanner.nextLine();

        BridgeAndActuationPointsDetection detection = new BridgeAndActuationPointsDetection(V);
        for (int i = 0; i < E; i++) {
            int[] e = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            detection.addEdge(e[0], e[1]);
            detection.addEdge(e[1], e[0]);
        }

        detection.run();
        for (Edge e: detection.bridges.stream()
                .map(b -> b.from > b.to ? new Edge(b.to, b.from, 1) : b)
                .sorted((b1, b2) -> b1.from == b2.from ? b1.to - b2.to : b1.from - b2.from)
                .collect(Collectors.toList())) {
            System.out.printf("%d %d\n", e.from, e.to);
        }
    }

}

class BridgeAndActuationPointsDetection {
    private int size;
    public Map<Integer, List<Edge>> edges;
    private TreeSet<Integer> unvisited;
    private int[] nodeId;
    private int[] lowLink;
    public List<Edge> bridges;
    public Set<Integer> actuationPoints;

    public BridgeAndActuationPointsDetection(int size) {
        this.size = size;
        edges = new HashMap<>();
        nodeId = new int[size];
        lowLink = new int[size];
        for (int i = 0; i < size; i++) {
            nodeId[i] = -1;
            lowLink[i] = -1;
        }
        unvisited = new TreeSet<>();
        for (int i = 0; i < size; i++) {
            unvisited.add(i);
        }

        bridges = new ArrayList<>();
        actuationPoints = new HashSet<>();
    }

    public void addEdge(int from, int to) {
        if (!edges.containsKey(from)) {
            edges.put(from, new ArrayList<>());
        }
        edges.get(from).add(new Edge(from, to, 1));
    }

    public void run() {
        while (!unvisited.isEmpty()) {
            dfs(unvisited.pollFirst(), -1, 0, new HashSet<>());
        }
    }

    private int dfs(int s, int from, int id, Set<Integer> visited) {
        nodeId[s] = id;
        lowLink[s] = id;
        if (visited.add(s)) {
            unvisited.remove(s);
            int cnt = 0;
            for (Edge e : edges.getOrDefault(s, Collections.emptyList())) {
                if (e.to == from) {
                    continue;
                }
                if (!visited.contains(e.to)) {
                    id = dfs(e.to, s, id + 1, visited);
                    if (nodeId[e.to] == lowLink[e.to]) {
                        bridges.add(e);
                    }
                    // Consider root node later
                    if (from != -1 && nodeId[s] <= lowLink[e.to]) {
                        actuationPoints.add(s);
                    }
                    cnt++;
                    lowLink[s] = Math.min(lowLink[s], lowLink[e.to]);
                } else {
                    lowLink[s] = Math.min(lowLink[s], nodeId[e.to]);
                }
            }

            // For root note
            if (from == -1 && cnt >= 2) {
                actuationPoints.add(s);
            }
        }
        return id;
    }

}

class Edge {
    public final int from;
    public final int to;
    public final int cost;

    public Edge(int from, int to, int cost) {
        this.from = from;
        this.to = to;
        this.cost = cost;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Edge edge = (Edge) o;
        return from == edge.from &&
                to == edge.to &&
                cost == edge.cost;
    }

    @Override
    public int hashCode() {
        return Objects.hash(from, to, cost);
    }
}

