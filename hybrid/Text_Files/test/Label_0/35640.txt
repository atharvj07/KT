import java.io.*;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        new Solution().run();
    }
}



final class Solution implements Runnable {

    ArrayList<Integer>[] g;

    class Pair implements Comparable<Pair> {
        public int val;
        public int idx;

        public Pair(int val, int idx) {
            this.val = val;
            this.idx = idx;
        }

        @Override
        public int compareTo(Pair o) {
            return val - o.val;
        }
    }

    ArrayList<Integer> order = new ArrayList<>();
    int[] color;
    int[] inCnt;
    boolean cycle = false;

    int m;


    void dfs(int v) {
        if (color[v] == 1)
            cycle = true;
        if (color[v] != 0)
            return;
        color[v] = 1;
        for (int i = 0; i < g[v].size(); i++)
            dfs(g[v].get(i));
        color[v] = 2;
        if (v < m)
            order.add(v);
    }


    int solve() throws Throwable {

        int n = in.nextInt();
        m = in.nextInt();
        Pair[][] a = new Pair[n][m];
        int VERTEX_COUNT = 10 * n * m;
        g = new ArrayList[VERTEX_COUNT];
        inCnt = new int[VERTEX_COUNT];
        color = new int[VERTEX_COUNT];
        for (int i = 0; i < g.length; i++)
            g[i] = new ArrayList<>();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                a[i][j] = new Pair(in.nextInt(), j);
            }

        ArrayList<Integer> l = new ArrayList<>();
        ArrayList<Integer> r = new ArrayList<>();

        int tempVertex = m;

        for (int i = 0; i < n; i++) {
            l.clear();
            r.clear();
            Pair[] cur = a[i];
            Arrays.sort(cur);
            int j = 0;
            for (; j < m && cur[j].val == -1; j++);
            int prev = j;
            for (; j < m;) {
                while (j + 1 < m && cur[j].val == cur[j + 1].val)
                    j++;
                l.add(prev);
                r.add(j);
                j++;
                prev = j;
            }
            for (j = 0; j < l.size() - 1; j++) {
                for (int pos = l.get(j); pos <= r.get(j); pos++) {
                    g[cur[pos].idx].add(tempVertex);
                    inCnt[tempVertex]++;
                }
                for (int pos = l.get(j + 1); pos <= r.get(j + 1); pos++) {
                    g[tempVertex].add(cur[pos].idx);
                    inCnt[cur[pos].idx]++;
                }
                tempVertex++;
            }
        }

        for (int i = 0; i < tempVertex; i++) {
            dfs(i);
        }
        if (cycle) {
            out.print(-1);
            return 0;
        }
        for (int i = order.size() - 1; i >= 0; i--)
            out.print((order.get(i) + 1) + " ");
        return 0;
    }


    FastScanner in;
    PrintWriter out;

    @Override
    public void run() {
        try {
            boolean ONLINE_JUDGE = false;
            try {
                Locale.setDefault(Locale.US);
                ONLINE_JUDGE = System.getProperty("ONLINE_JUDGE") != null;
            } catch (SecurityException e) {
                System.err.println("Operation forbidden");
            }


            long time = System.currentTimeMillis();
            if (ONLINE_JUDGE) {
                in = new FastScanner(new InputStreamReader(System.in));
                out = new PrintWriter(System.out);
            } else {
                in = new FastScanner(new FileReader("input.txt"));
                out = new PrintWriter("output.txt");
            }

            int ret = solve();
            out.close();
            in.close();

            long delta = System.currentTimeMillis() - time;

            long freeMem = Runtime.getRuntime().freeMemory();
            long totalMem = Runtime.getRuntime().totalMemory();

            System.err.printf("Time: %.3f s\n", delta / 1000.0f);
            System.err.printf("Memory: %.3f MB\n", (float)(totalMem - freeMem) / (1 << 20));

            if (ret != 0)
                System.exit(ret);

        } catch (Throwable t) {
            t.printStackTrace(System.err);
            System.exit(-1);
        }
    }
}

@SuppressWarnings("unused")
final class FastScanner {
    BufferedReader bufferedReader;
    StringTokenizer stringTokenizer;

    public FastScanner(Reader r) {
        bufferedReader = new BufferedReader(r);
    }

    public String nextToken() throws IOException, NullPointerException {
        while (stringTokenizer == null || !stringTokenizer.hasMoreTokens())
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        return stringTokenizer.nextToken();
    }

    public String nextLine() throws IOException {
        return bufferedReader.readLine();
    }

    public int nextInt() throws IOException, NullPointerException {
        return Integer.parseInt(nextToken());
    }

    public long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }

    public BigInteger nextBigInteger() throws IOException {
        return new BigInteger(nextToken());
    }

    public float nextFloat() throws IOException {
        return Float.parseFloat(nextToken());
    }

    public double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }

    public int read() throws IOException {
        return bufferedReader.read();
    }

    public void close() throws IOException {
        bufferedReader.close();
    }

    public int[] readIntArray(int n) throws Throwable {
        int[] array = new int[n];
        for (int i = 0; i < n; i++)
            array[i] = nextInt();
        return array;
    }

    @Override
    protected void finalize() throws Throwable {
        super.finalize();
        close();
    }
}

final class DisjointSetUnion {
    int[] parent;
    int[] rank;

    public DisjointSetUnion(int size) {
        parent = new int[size];
        rank = new int[size];
        for (int i = 0; i < size; i++)
            parent[i] = i;
    }

    public int getLeader(int element) {
        if (parent[element] == element)
            return element;
        else
            return parent[element] = getLeader(parent[element]);
    }

    public boolean union(int x, int y) {
        x = getLeader(x);
        y = getLeader(y);
        if (x == y)
            return true;
        if (rank[x] < rank[y]) {
            int temp = x;
            x = y;
            y = temp;
        }
        parent[y] = x;
        if (rank[x] == rank[y])
            ++rank[x];
        return false;
    }
}

@SuppressWarnings("unused")
final class Utils {
    private Utils() {}

    public static long sqr(long x) {
        return x * x;
    }

    public static int gcd(int x, int y) {
        while (y > 0) {
            x %= y;
            int temp = x;
            x = y;
            y = temp;
        }
        return x;
    }

    public static int lcm(int x, int y) {
        return x / gcd(x, y) * y;
    }

    public static long gcd(long x, long y) {
        while (y > 0) {
            x %= y;
            long temp = x;
            x = y;
            y = temp;
        }
        return x;
    }

    public static long lcm(long x, long y) {
        return x / gcd(x, y) * y;
    }

    public static long modInverse(long x, long mod) {
        return BigInteger.valueOf(x).modInverse(BigInteger.valueOf(mod)).longValue();
    }

    static Random r = new Random(System.nanoTime());

    public static<T> void shuffle(T[] array) {
        int n = array.length;
        for (int i = 0; i < n; i++) {
            int j = r.nextInt(n);
            T t = array[i];
            array[i] = array[j];
            array[j] = t;
        }
    }

    public static void shuffle(int[] array) {
        int n = array.length;
        for (int i = 0; i < n; i++) {
            int j = r.nextInt(n);
            int t = array[i];
            array[i] = array[j];
            array[j] = t;
        }
    }
}