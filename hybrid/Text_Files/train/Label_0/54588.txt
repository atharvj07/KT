import java.awt.Point;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Point[] ps = new Point[n + 1];
        for (int i = 1; i <= n; i++) {
            ps[i] = new Point(sc.nextInt(), sc.nextInt());
        }
        PriorityQueue<Fenth> q = new PriorityQueue<Fenth>();
        double ans = 0;

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            double dis = Math.hypot(ps[a].x - ps[b].x, ps[a].y - ps[b].y);
            q.add(new Fenth(a, b, dis));
            ans += dis;
        }
        UnionFind uf = new UnionFind(n + 1);
        while (!q.isEmpty()) {
            Fenth f = q.poll();
            int a = f.from;
            int b = f.to;
            if (uf.same(a, b))
                continue;
            uf.unite(a, b);
            ans -= f.length;
        }
        System.out.printf("%.4f\n", ans);
    }
}

class Fenth implements Comparable<Fenth> {
    int from;
    int to;
    double length;

    Fenth(int from, int to, double length) {
        this.from = from;
        this.to = to;
        this.length = length;
    }

    public int compareTo(Fenth f) {
        if (f.length > length)
            return 1;
        else if (f.length < length)
            return -1;
        else {
            return 0;
        }
    }

    public String toString() {
        return "from,to,length" + from + " " + to + " " + length;
    }
}

class UnionFind {
    int par[];
    int rank[];

    UnionFind(int n) {
        par = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            par[i] = i;
        }
    }

    public int find(int x) {
        if (x == par[x])
            return x;
        else
            return par[x] = find(par[x]);
    }

    public void unite(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y)
            return;
        if (rank[x] > rank[y])
            par[y] = x;
        else {
            par[x] = y;
            if (rank[x] == rank[y])
                rank[y]++;
        }
    }

    public boolean same(int x, int y) {
        return find(x) == find(y);
    }
}