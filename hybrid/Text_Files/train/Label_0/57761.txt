import java.io.*;
import java.util.*;
 
public class Main {
    static final boolean ONLINE_JUDGE = System.getProperty("ONLINE_JUDGE") != null;
 
    final int N = 200200;
    final int LOG = 18;
 
    List<Integer>[] g = new ArrayList[N];
    int[] depth = new int[N];
    int[][] par = new int[N][LOG];
 
    void Dfs(int from, int p, int d) {
        par[from][0] = p;
        depth[from] = d;
        for (int i = 1; i < LOG; i++) {
            par[from][i] = par[par[from][i - 1]][i - 1];
        }
        for (int v : g[from]) {
            if (v == p) continue;
            Dfs(v, from, d + 1);
        }
    }
 
    int Lca(int a, int b) {
        if (depth[a] < depth[b]) {
            int c = a;
            a = b;
            b = c;
        }
        for (int i = LOG - 1; i >= 0; i--) {
            if (depth[par[a][i]] >= depth[b]) {
                a = par[a][i];
            }
        }
        if (a == b) return a;
        for (int i = LOG - 1; i >= 0; i--) {
            if (par[a][i] != par[b][i]) {
                a = par[a][i];
                b = par[b][i];
            }
        }
        return par[a][0];
    }
 
    int Dist(int a, int b) {
        return depth[a] + depth[b] - 2 * depth[Lca(a, b)];
    }
 
    void solve() throws IOException {
        int n = readInt(), m = readInt();
        for (int i = 1; i <= n; i++) {
            g[i] = new ArrayList<>();
        }
        for (int i = 0; i < n - 1; i++) {
            int f = readInt(), t = readInt();
            g[f].add(t);
            g[t].add(f);
        }
        Dfs(1, 1, 1);
        while (m-- > 0) {
            int k = readInt();
            int [] arr = readIntArray(k);
            int min = arr[0];
            for (int i = 1; i < k; i++) {
                if (depth[arr[i]] > depth[min]) {
                    min = arr[i];
                }
            }
            int from = 1;
            min = par[min][0];
            boolean good = true;
            for (int i = 0; i < k; i++) {
                if (depth[arr[i]] + Dist(arr[i], min) - 2 > depth[min]) {
                    good = false;
                }
            }
            out.print(good ? "YES\n" : "NO\n");
        }
    }
 
    void init() throws FileNotFoundException {
        if (ONLINE_JUDGE) {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(System.out);
        } else {
            in = new BufferedReader(new FileReader("input.txt"));
            out = new PrintWriter("output.txt");
        }
        tok = new StringTokenizer("");
    }
 
    public static void main(String[] args) {
        new Main().run();
    }
 
    BufferedReader in;
    PrintWriter out;
    StringTokenizer tok;
 
    void run() {
        try {
            long timeStart = System.currentTimeMillis();
            init();
            solve();
            out.close();
            long timeEnd = System.currentTimeMillis();
            System.err.println("time = " + (timeEnd - timeStart) + " compiled");
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
        }
    }
 
    String readLine() throws IOException {
        return in.readLine();
    }
 
    String delimiter = " ";
 
    String readString() throws IOException {
        while (!tok.hasMoreTokens()) {
            String nextLine = readLine();
            if (null == nextLine)
                return null;
            tok = new StringTokenizer(nextLine);
        }
        return tok.nextToken(delimiter);
    }
 
    int[] readIntArray(int b) {
        int[] a = new int[b];
        for (int i = 0; i < b; i++) {
            try {
                a[i] = readInt();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return a;
    }
 
    int[] readIntArrayWithDecrease(int b) {
        int[] a = new int[b];
        for (int i = 0; i < b; i++) {
            try {
                a[i] = readInt() - 1;
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return a;
    }
 
    long[] readLongArray(int b) {
        long[] a = new long[b];
        for (int i = 0; i < b; i++) {
            try {
                a[i] = readLong();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return a;
    }
 
    int readInt() throws IOException {
        return Integer.parseInt(readString());
    }
 
    long readLong() throws IOException {
        return Long.parseLong(readString());
    }
 
    void sortArrayInt(int[] a) {
        Integer[] arr = new Integer[a.length];
        for (int i = 0; i < a.length; i++) {
            arr[i] = a[i];
        }
        Arrays.sort(arr);
        for (int i = 0; i < a.length; i++) {
            a[i] = arr[i];
        }
    }
 
    void sortArrayLong(long[] a) {
        Long[] arr = new Long[a.length];
        for (int i = 0; i < a.length; i++) {
            arr[i] = a[i];
        }
        Arrays.sort(arr);
        for (int i = 0; i < a.length; i++) {
            a[i] = arr[i];
        }
    }
}