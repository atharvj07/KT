import java.io.*;
import java.util.*;
import java.math.*;

public class Task {

    static Point[] a;
    static int sum;
    static int[] took;
    static int[] ans;
    static int size;

    static void go(int need, int last) {
        if (need == 0) {
            int ret = 0;
            for (int i = 0; i < size; ++i) {
                for (int j = i + 1; j < size; ++j) {
                    ret += a[took[i]].sub(a[took[j]]).len2();
                }
            }
            if (ret > sum) {
                sum = ret;
                ans = Arrays.copyOf(took, size);
            }
        } else {
            ++size;
            for (int i = last; i < a.length; ++i) {
                took[size - 1] = i;
                go(need - 1, i);
            }
            --size;
        }
    }

    public void solve() throws IOException {
        int n = in.nextInt();
        int r = in.nextInt();
        a = new Point[3000];
        int s = 0;
        for (int i = 0; i <= r; ++i) {
            for (int j = 0; i * i + j * j <= r * r; ++j) {
                a[s++] = new Point(i, j);
                if (i > 0) a[s++] = new Point(-i, j);
                if (i > 0 & j > 0) a[s++] = new Point(-i, -j);
                if (j > 0) a[s++] = new Point(i, -j);
            }
        }
        a = Point.convexHull(Arrays.copyOf(a, s));
        took = new int[n];
        for (int i = 0; i < n / 2 - 1; ++i) {
            took[size++] = 0;
        }
        go(n - n / 2 + 1, 0);
        out.println(sum);
        for (int i : ans) {
            out.println(a[i].x + " " + a[i].y);
        }
    }

    static FastReader in;
    static PrintWriter out;
    static PrintStream err;

    public static void main(String[] args) throws IOException {
        try {
            in = new FastReader();
            out = new PrintWriter(System.out);
            err = System.err;
            new Task().solve();
            out.close();
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}

class FastReader {
    BufferedReader br;
    StringTokenizer in;

    FastReader() {
        this.br = new BufferedReader(new InputStreamReader(System.in));
    }

    FastReader(String filename) {
        try {
            this.br = new BufferedReader(new FileReader(filename));
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    public String nextToken() throws IOException {
        while (in == null || !in.hasMoreTokens()) {
            in = new StringTokenizer(br.readLine());
        }

        return in.nextToken();
    }

    public int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    public double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }

    public long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }
}

class Point implements Comparable<Point> {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int mulv(Point a) {
        return this.x * a.y - this.y * a.x;
    }

    public int len2() {
        return x * x + y * y;
    }

    public int compareTo(Point o) {
        if (o == null) {
            return -1;
        }
        int m = this.mulv(o);
        if (m != 0) {
            return m > 0 ? -1 : 1;
        }
        int d = this.len2() - o.len2();
        return d > 0 ? 1 : d < 0 ? -1 : 0;
    }

    public Point sub(Point a) {
        return new Point(this.x - a.x, this.y - a.y);
    }

    public Point add(Point a) {
        return new Point(this.x + a.x, this.y + a.y);
    }

    public static Point[] convexHull(Point[] a) {
        int n = a.length;
        int mn = 0;
        for (int i = 1; i < n; ++i) {
            if (a[i].x < a[mn].x || (a[i].x == a[mn].x && a[i].y < a[mn].y)) {
                mn = i;
            }
        }
        Point start = a[mn];
        a[mn] = a[0];
        a[0] = start;
        Point[] b = new Point[n - 1];
        for (int i = 0; i < n - 1; ++i) {
            b[i] = a[i + 1].sub(start);
        }
        Arrays.sort(b);
        for (int i = 0; i < n - 1; ++i) {
            a[i + 1] = b[i].add(start);
        }
        Point[] h = new Point[n];
        int size = 0;
        for (int i = 0; i < n; ++i) {
            while (size > 1 && h[size - 1].sub(h[size - 2]).compareTo(a[i].sub(h[size - 2])) == 1) {
                --size;
            }
            h[size++] = a[i];
        }
        return Arrays.copyOf(h, size);
    }
}
