import java.util.*;
import java.io.*;

public class c implements Runnable {
    static PrintWriter out;
    static int[] arr;
    static int n;
    static ArrayList<Integer>[] adjs;
    static int[] ans;
    static int count = 100;
    public void main() throws Throwable {
        FastScanner in = new FastScanner(System.in);
        out = new PrintWriter(System.out);
        
        n = in.nextInt();
        arr = in.nextIntArr(n);
        adjs = new ArrayList[n];
        ans = new int[n];
        for (int i = 0; i < n; i++) {
            adjs[i] = new ArrayList<>();
        }
        for (int i = 0; i < n - 1; i++) {
            int a = in.nextInt() - 1;
            int b = in.nextInt() - 1;
            adjs[a].add(b);
            adjs[b].add(a);
        }
        TreeSet<Integer> ts = new TreeSet<>();
        go(0, -1, 0, ts);
        
        out.print(arr[0]);
        for (int i = 1; i < n; i++)
            out.print(" " + ans[i]);
        out.println();
        out.close();
    }
    
    void go(int cur, int par, int g, TreeSet<Integer> ts) {
        TreeSet<Integer> ts2 = new TreeSet<>();
        for (int a : ts) {
            ts2.add(gcd(a, arr[cur]));
        }
        int gg = gcd(g, arr[cur]);
        ts2.add(g);
        ans[cur] = Math.max(gg, ts2.last());
        
        for (int next : adjs[cur]) {
            if (next == par) continue;
            go(next, cur, gg, ts2);
        }
    }
    
    public int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
    
    
    
    
    
    
    
    
    
    
    public static void main(String[] args) throws Exception {
        new Thread(null, new c(), "c", 1L << 29).start();
    }
    public void run() {
        try {
           main(); 
        } catch (Throwable t) {
            t.printStackTrace();
            System.exit(-1);
        }
    }
    static void sort(int[] arr) {
        Random rand = new Random();
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int j = rand.nextInt(n);
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
        Arrays.sort(arr);
    }
    static void sort(long[] arr) {
        Random rand = new Random();
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int j = rand.nextInt(n);
            long tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
        Arrays.sort(arr);
    }
    static void sort(double[] arr) {
        Random rand = new Random();
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int j = rand.nextInt(n);
            double tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
        Arrays.sort(arr);
    }
    static class FastScanner {
        BufferedReader br; StringTokenizer st;
        public FastScanner(InputStream i) {
            br = new BufferedReader(new InputStreamReader(i));
            st = new StringTokenizer("");
        }
        public String next() throws Exception {
            while (!st.hasMoreTokens()) {
                st = new StringTokenizer(br.readLine());
            }
            return st.nextToken();
        }
        public int nextInt() throws Exception {
            return Integer.parseInt(next());
        }
        public double nextDouble() throws Exception {
            return Double.parseDouble(next());
        }
        public long nextLong() throws Exception {
            return Long.parseLong(next());
        }
        public int[] nextIntArr(int n) throws Exception {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = nextInt();
            return arr;
        }
        public double[] nextDoubleArr(int n) throws Exception {
            double[] arr = new double[n];
            for (int i = 0; i < n; i++) arr[i] = nextDouble();
            return arr;
        }
        public long[] nextLongArr(int n) throws Exception {
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) arr[i] = nextLong();
            return arr;
        }
        public int[] nextOffsetIntArr(int n) throws Exception {
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = nextInt() - 1;
            return arr;
        }
        
        public int[][] nextIntArr(int n, int m) throws Exception {
            int[][] arr = new int[n][m];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    arr[i][j] = nextInt();
            return arr;
        }
        public double[][] nextDoubleArr(int n, int m) throws Exception {
            double[][] arr = new double[n][m];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    arr[i][j] = nextDouble();
            return arr;
        }
        public long[][] nextLongArr(int n, int m) throws Exception {
            long[][] arr = new long[n][m];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    arr[i][j] = nextLong();
            return arr;
        }
    }
}
