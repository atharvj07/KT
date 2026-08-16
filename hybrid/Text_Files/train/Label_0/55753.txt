import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    int W, H;
    PriorityQueue<Edge> qs;

    public static void main(String[] args) {
        Main m = new Main();
        m.read();
        m.solve();
    }

    private void read() {
        Scanner sc = new Scanner(System.in);
        W = sc.nextInt();
        H = sc.nextInt();
        qs = new PriorityQueue<>((e1, e2) ->
           Long.compare(e1.cost, e2.cost));
        int i;
        long tmp;
        for (i = 0; i < W; i++) {
            tmp = sc.nextLong();
            qs.add(new Edge(i+1, i, tmp, true));
        }
        for (int j = 0; j < H; j++) {
            tmp = sc.nextLong();
            qs.add(new Edge(j+1, j, tmp, false));
        }
    }

    private void solve() {
        int a = H+1;
        int b = W+1;
        long ans = 0L;
        while (!qs.isEmpty()) {
            Edge e = qs.poll();
            if (e.isCol) {
                ans += e.cost * a;
                b--;
            } else {
                ans += e.cost * b;
                a--;
            }
        }
        System.out.println(ans);
    }

    private class Edge {
        boolean isCol;
        int to, from;
        long cost;
        Edge(int to, int from, long c, boolean isCol) {
            this.to = to;
            this.cost = c;
            this.from = from;
            this.isCol = isCol;
        }
    }

}
