import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    int[] maxTree;
    int[] lazyMax;
    int[] minTree;
    int[] lazyMin;

    private void push(int node) {
        maxTree[node  *2] += lazyMax[node];
        maxTree[node * 2 + 1] += lazyMax[node];
        lazyMax[node * 2] += lazyMax[node];
        lazyMax[node  * 2 + 1] += lazyMax[node];
        minTree[node * 2] += lazyMin[node];
        minTree[node * 2 + 1] += lazyMin[node];
        lazyMin[node * 2] += lazyMin[node];
        lazyMin[node * 2 + 1] += lazyMin[node];
        lazyMax[node] = 0;
        lazyMin[node] = 0;
    }

    private void addMax(int add, int from, int to, int a, int b, int node) {
        if (from <= a && b <= to) {
            maxTree[node] += add;
            lazyMax[node] += add;
            return;
        }

        push(node);

        int mid = (a + b) / 2;
        if (from <= mid) addMax(add, from, to, a, mid, node  * 2);
        if (to > mid) addMax(add, from, to, mid + 1, b, node * 2 + 1);

        maxTree[node] = Math.max(maxTree[node * 2], maxTree[node  *2 + 1]);
    }

    private void addMin(int add, int from, int to, int a, int b, int node) {
        if (from <= a && b <= to) {
            minTree[node] += add;
            lazyMin[node] += add;
            return;
        }

        push(node);

        int mid = (a + b) / 2;
        if (from <= mid) addMin(add, from, to, a, mid, node  *2);
        if (to > mid) addMin(add, from, to, mid + 1, b, node * 2  +1);

        minTree[node] = Math.min(minTree[node  *2 ], minTree[node  *2 + 1]);
    }

    private int getMax(int from, int to, int a, int b, int node) {
        if (from <= a && b <= to) return maxTree[node];

        push(node);

        int mid = (a + b) / 2;
        int max = Integer.MIN_VALUE;
        if (from <= mid) max = Math.max(max, getMax(from, to, a, mid, node * 2));
        if (to > mid) max = Math.max(max, getMax(from, to, mid + 1 , b, node *  2 + 1));

        return max;
    }

    private int getMin(int from, int to, int a, int b, int node) {
        if (from <= a && b <= to) return minTree[node];

        push(node);

        int mid = (a + b) / 2;
        int min = Integer.MAX_VALUE;
        if (from <= mid) min = Math.min(min, getMin(from, to, a, mid, node * 2));
        if (to > mid) min = Math.min(min, getMin(from, to, mid + 1 , b, node *  2 + 1));

        return min;
    }

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    private void solve() throws IOException {
        BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int n = Integer.parseInt(f.readLine());
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            StringTokenizer tokenizer = new StringTokenizer(f.readLine());
            points[i] = new Point(Integer.parseInt(tokenizer.nextToken()), Integer.parseInt(tokenizer.nextToken()));
        }

        Arrays.sort(points);
        maxTree = new int[4 * n];
        minTree = new int[4 * n];
        lazyMin = new int[4* n];
        lazyMax = new int[4 * n];
        for (int i = 0; i < n; i++) {
            addMin(points[i].y, i, i, 0, n - 1, 1);
            addMax(points[i].y, i, i, 0, n - 1, 1);
        }


        int res = 0;
        for (int i = 1;  i< n; i++) {
            addMax(points[i].x - points[i - 1].x, 0, i - 1, 0, n - 1, 1);
            addMin(points[i - 1].x - points[i].x, 0, i - 1, 0, n - 1, 1);

            int res1 = getMax(0, i - 1, 0, n - 1, 1) - points[i].y;
            int res2 = points[i].y - getMin(0, i - 1, 0, n - 1, 1);
            res = Math.max(res, res1);
            res = Math.max(res, res2);
        }

        out.println(res);
        out.close();
    }

    private static class Point implements Comparable<Point> {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Point o) {
            return Integer.compare(this.x, o.x);
        }
    }
}