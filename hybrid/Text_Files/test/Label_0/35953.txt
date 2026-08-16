import java.io.*;
import java.util.*;

public class ETry implements Runnable {

    private PrintWriter out = new PrintWriter(System.out, true);
    private Scanner scanner;

    int n;
    int[] size;
    int[] parent;
    PointWI[] points;
    int[] ans;
    
    Graph graph;

    @Override
    public void run() {
        n = scanner.nextInt();
        // читаем граф
        graph = new Graph(n);
        
        for (int i = 0; i < n - 1; i++) {
            int x = scanner.nextInt() - 1;
            int y = scanner.nextInt() - 1;
            graph.addEdge(x, y);
        }
        
        // читаем точки
        points = new PointWI[n];
        for (int i = 0; i < n; i++) {
            points[i] = new PointWI(scanner.nextLong(), scanner.nextLong(), i);
        }

        // подвешиваем дерево и 
        size = new int[n];
        parent = new int[n];
        dfs(0, -1);
        
        // считаем ответ
        ans = new int[n];
        Arrays.fill(ans, -1);
        
        // ищем самый левый
        List<PointWI> pointsList = Arrays.asList(points);
        
        PointWI min = Collections.min(pointsList, new MostLeftPointComparator());
        Collections.swap(pointsList, 0, min.i);
        
        // считаем
        rec(0, 0, n - 1);
        
        // ответ
        for (int i = 0; i < n; i++) {
            out.print(ans[i] + 1);
            out.print(' ');
        }
        
        out.flush();
    }

    private void rec(int x, int left, int right) {
        ans[points[left].i] = x;
        Arrays.sort(points, left + 1, right + 1, new AnglePointComparator(points[left]));
        int i = left + 1;
        for (int y : graph.adjacent(x)) {
            if (y != parent[x]) {
                rec(y, i, i + size[y] - 1);
                i += size[y];
            }
        }
    }

    private void dfs(int x, int p) {
        parent[x] = p;
        size[x] = 1;
        for (int y : graph.adjacent(x)) {
            if (y != p) {
                dfs(y, x);
                size[x] += size[y];
            }
        }
    }
    
    public ETry setInput(InputStream inputStream) {
        this.scanner = new Scanner(inputStream);
        return this;
    }

    public static void main(String[] args) {
        new ETry().setInput(System.in).run();
    }
}

class Graph {
    private final int n;
    private final List<List<Integer>> adj;
    
    public Graph(int n) {
        this.n = n;
        this.adj = new ArrayList<List<Integer>>(n);
        createAdjList(n);
    }

    private void createAdjList(int n) {
        while (n > 0) {
            this.adj.add(new ArrayList<Integer>());
            n--;
        }
    }
    
    public void addEdge(int v, int u) {
        adj.get(v).add(u);
        adj.get(u).add(v);
    }
     
    public Iterable<Integer> adjacent(int v) {
        return adj.get(v);
    }

    public int getN() {
        return n;
    }
}

//solution

class PointWI {
    long x, y;
    int i;

    public PointWI(long x, long y, int i) {
        this.x = x;
        this.y = y;
        this.i = i;
    }

    @Override
    public String toString() {
        return String.format("[(%d %d) %d]", x, y, i);
    }

}

class MostLeftPointComparator implements Comparator<PointWI> {
    @Override
    public int compare(PointWI p1, PointWI p2) {
        int byx = compare(p1.x, p2.x);
        if (byx == 0) {
            return compare(p1.y, p2.y);
        }
        return byx;
    }
    
    public static int compare(long a, long b) {
        return a < b ? -1 : (a == b ? 0 : 1);
    }
}

class AnglePointComparator implements Comparator<PointWI> {
    PointWI root;

    public AnglePointComparator(PointWI root) {
        this.root = root;
    }

    @Override
    public int compare(PointWI a, PointWI b) {
        long wp = (a.x - root.x) * (b.y - root.y) - (a.y - root.y) * (b.x - root.x);
        
        if (wp < 0) {
            return -1;
        }
        
        if (wp > 0) {
            return 1;
        }

        return 0;
    }
}