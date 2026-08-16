
import java.io.*;
import java.util.*;

class Graph
{
    //開始,ゴール,頂点,辺
    int s, g, n, e;
    //無向の場合もコンストラクタでうまくやってくれるはず
    int[] f, t;
    long[] c;
    long d[];/*sからの最短距離*/
    long d2[][];/*2点間の最短距離*/

    public Graph(int s, int N, int[] f, int[] t, long[] c)
    {
        this.s = s;
        this.n = N;
        this.f = f;
        this.t = t;
        this.c = c;
        this.e = f.length;
    }

    //O( EV )type 0 : sから到達できなくても、負経路があればtrueを返す
    //       type 1 : sから到達できる　　　　負経路があればtrueを返す
    public boolean bellmanFord(int s, int type)
    {
        this.s = s;
        d = new long[n];
        if (type == 0)
        {
            Arrays.fill(d, 0);
        }
        else
        {
            Arrays.fill(d, Main.LINF);
            d[s] = 0;
        }
        //負経路がなければn-1回で最短が求まるため、N回目に更新されたら不経路がある
        for (int i = 0; i < n; i++)
        {
            for (int ei = 0; ei < e; ei++)
            {
                int f_ = f[ei];
                int t_ = t[ei];
                long c_ = c[ei];
                if (d[f_] != Main.LINF && d[t_] > d[f_] + c_)
                {
                    d[t_] = d[f_] + c_;
                    if (i == n - 1) return true;
                }
            }
        }
        return false;
    }

    //O( EV ) sからgの中に不経路があればtrueを返す
    public boolean bellmanFordSubset(int s, int g)
    {
        this.s = s;
        this.g = g;
        d = new long[n];
        Arrays.fill(d, Main.MINF);
        d[s] = 0;
        //負経路がなければn-1回で最短が求まるため、n～2N回目にgが更新されたら、s-gに不経路がある
        for (int i = 0; i < 2 * n; i++)
        {
            for (int ei = 0; ei < e; ei++)
            {
                int f_ = f[ei];
                int t_ = t[ei];
                long c_ = c[ei];
                if (d[f_] != Main.MINF && d[t_] < d[f_] + c_)
                {
                    d[t_] = d[f_] + c_;
                    if (i >= n - 1 && t_ == g) return true;
                }
            }
        }
        return false;
    }

    //O( E log V)
    public void dijkstra(int s)
    {
        class Edge implements Comparable<Edge>
        {
            int to;
            long cos;

            Edge(int to, long cost)
            {
                this.to = to;
                this.cos = cost;
            }

            public int compareTo(Edge ed)
            {
                if (cos != ed.cos)
                {
                    if (cos > ed.cos) return 1;
                    else if (cos == ed.cos) return 0;
                    else return -1;
                }
                else return to - ed.to;
            }
        }
        this.s = s;
        d = new long[n];
        List<ArrayList<Edge>> elist = new ArrayList<>();
        for (int i = 0; i < n; i++)
            elist.add(new ArrayList<>());

        Arrays.fill(d, Main.LINF);
        d[0] = 0;
        for (int ei = 0; ei < e; ei++)
        {
            int f_ = f[ei];
            int t_ = t[ei];
            long c_ = c[ei];
            elist.get(f_).add(new Edge(t_, c_));
        }
        PriorityQueue<Edge> q = new PriorityQueue<>();
        q.add(new Edge(s, 0));
        while (!q.isEmpty())
        {
            Edge p = q.poll();
            int nowt = p.to;
            long nowc = p.cos;
            if (d[nowt] < nowc) continue;
            for (int ti = 0; ti < elist.get(nowt).size(); ti++)
            {
                Edge ne = elist.get(nowt).get(ti);
                int newt = ne.to;
                long newc = nowc + ne.cos;
                if (newc < d[newt])
                {
                    d[newt] = newc;
                    q.add(new Edge(newt, newc));
                }
            }
        }

    }

    //O( E ^ 2) 辺が密の時用
    public void dijkstra2(int s)
    {
        this.s = s;
        boolean[] used = new boolean[e];
        long[][] cost = new long[n][n];
        d = new long[n];
        Main.fill(cost, Main.LINF);
        Arrays.fill(d, Main.LINF);
        d[s] = 0;

        for (int i = 0; i < e; i++)
            cost[f[i]][t[i]] = c[i];

        while (true)
        {
            int v = -1;
            //まだ使われていない頂点のうち、距離が最小のものを探す。
            for (int u = 0; u < n; u++)
                if (!used[u] && (v == -1 || d[u] < d[v])) v = u;
            if (v == -1) break;
            used[v] = true;
            for (int u = 0; u < n; u++)
                d[u] = Math.min(d[u], d[v] + cost[v][u]);
        }

    }

    public void warshall()
    {
        d2 = new long[n][n];
        Main.fill(d2, Main.LINF);
        for (int i = 0; i < n; i++)
            d2[i][i] = 0;
        for (int ei = 0; ei < e; ei++)
            d2[f[ei]][t[ei]] = Math.min(d2[f[ei]][t[ei]], c[ei]);
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    d2[i][j] = Math.min(d2[i][j], d2[i][k] + d2[k][j]);
    }

    public long dis(int to)
    {
        return d[to];
    }

    public long dis2(int from, int to)
    {
        return d2[from][to];
    }
}

/**
 * @author baito
 */
public class Main
{
    static StringBuilder sb = new StringBuilder();
    static FastScanner sc = new FastScanner(System.in);
    static int INF = 12345678;
    static long LINF = 123456789123456789L;
    static long MINF = -123456789123456789L;
    static long MOD = 1000000007;
    static int[] y4 = {0, 1, 0, -1};
    static int[] x4 = {1, 0, -1, 0};
    static int[] y8 = {0, 1, 0, -1, -1, 1, 1, -1};
    static int[] x8 = {1, 0, -1, 0, 1, -1, 1, -1};
    static long[] F;//factorial
    static boolean[] isPrime;
    static int[] primes;

    static int N, M;


    public static void main(String[] args)
    {
        N = sc.nextInt();
        M = sc.nextInt();
        int[] a = new int[M];
        int[] b = new int[M];
        long[] c = new long[M];
        for (int i = 0; i < M; i++)
        {
            a[i] = sc.nextInt()-1;
            b[i] = sc.nextInt()-1;
            c[i] = sc.nextLong();
        }

        Graph g = new Graph(0, N, a, b, c);
        if (g.bellmanFordSubset(0, N - 1)) System.out.println("inf");
        else System.out.println(g.dis(N - 1));


    }

    public static void revSort(int[] a)
    {
        Arrays.sort(a);
        reverse(a);
    }

    public static void revSort(long[] a)
    {
        Arrays.sort(a);
        reverse(a);
    }

    public static int[][] copy(int[][] ar)
    {
        int[][] nr = new int[ar.length][ar[0].length];
        for (int i = 0; i < ar.length; i++)
            for (int j = 0; j < ar[0].length; j++)
                nr[i][j] = ar[i][j];
        return nr;
    }

    public static long sumMod(long... lar)
    {
        long sum = 0;
        for (long l : lar)
            sum = (sum + l % MOD) % MOD;
        return sum;
    }

    /**
     * <h1>指定した値以上の先頭のインデクスを返す</h1>
     * <p>配列要素が０のときは、０が返る。</p>
     *
     * @return<b>int</b> ： 探索した値以上で、先頭になるインデクス
     */
    public static int lowerBound(final int[] arr, final int value)
    {
        int low = 0;
        int high = arr.length;
        int mid;
        while (low < high)
        {
            mid = ((high - low) >>> 1) + low;    //(low + high) / 2 (オーバーフロー対策)
            if (arr[mid] < value)
            {
                low = mid + 1;
            }
            else
            {
                high = mid;
            }
        }
        return low;
    }

    /**
     * <h1>指定した値より大きい先頭のインデクスを返す</h1>
     * <p>配列要素が０のときは、０が返る。</p>
     *
     * @return<b>int</b> ： 探索した値より上で、先頭になるインデクス
     */
    public static int upperBound(final int[] arr, final int value)
    {
        int low = 0;
        int high = arr.length;
        int mid;
        while (low < high)
        {
            mid = ((high - low) >>> 1) + low;    //(low + high) / 2 (オーバーフロー対策)
            if (arr[mid] <= value)
            {
                low = mid + 1;
            }
            else
            {
                high = mid;
            }
        }
        return low;
    }

    //次の順列に書き換える、最大値ならfalseを返す
    public static boolean nextPermutation(int A[])
    {
        int len = A.length;
        int pos = len - 2;
        for (; pos >= 0; pos--)
        {
            if (A[pos] < A[pos + 1]) break;
        }
        if (pos == -1) return false;

        //posより大きい最小の数を二分探索
        int ok = pos + 1;
        int ng = len;
        while (Math.abs(ng - ok) > 1)
        {
            int mid = (ok + ng) / 2;
            if (A[mid] > A[pos]) ok = mid;
            else ng = mid;

        }

        swap(A, pos, ok);
        reverse(A, pos + 1, len - 1);


        return true;
    }

    //次の順列に書き換える、最小値ならfalseを返す
    public static boolean prevPermutation(int A[])
    {
        int len = A.length;
        int pos = len - 2;
        for (; pos >= 0; pos--)
        {
            if (A[pos] > A[pos + 1]) break;
        }
        if (pos == -1) return false;

        //posより小さい最大の数を二分探索
        int ok = pos + 1;
        int ng = len;
        while (Math.abs(ng - ok) > 1)
        {
            int mid = (ok + ng) / 2;
            if (A[mid] < A[pos]) ok = mid;
            else ng = mid;

        }

        swap(A, pos, ok);
        reverse(A, pos + 1, len - 1);


        return true;
    }

    //↓nCrをmod計算するために必要。　***factorial(N)を呼ぶ必要がある***
    static long ncr(int n, int r)
    {
        if (n < r) return 0;
        else if (r == 0) return 1;

        factorial(n);
        return F[n] / (F[n - r] * F[r]);
    }

    static long ncr2(int a, int b)
    {
        if (b == 0) return 1;
        else if (a < b) return 0;
        long res = 1;
        for (int i = 0; i < b; i++)
        {
            res *= a - i;
            res /= i + 1;
        }
        return res;
    }

    static long ncrdp(int n, int r)
    {
        if (n < r) return 0;
        long[][] dp = new long[n + 1][r + 1];
        for (int ni = 0; ni < n + 1; ni++)
        {
            dp[ni][0] = dp[ni][ni] = 1;
            for (int ri = 1; ri < ni; ri++)
            {
                dp[ni][ri] = dp[ni - 1][ri - 1] + dp[ni - 1][ri];
            }
        }
        return dp[n][r];
    }

    static long modNcr(int n, int r)
    {
        long result = F[n];
        result = result * modInv(F[n - r]) % MOD;
        result = result * modInv(F[r]) % MOD;
        return result;
    }

    static long modInv(long n)
    {
        return modPow(n, MOD - 2);
    }

    static void factorial(int n)
    {
        F = new long[n + 1];
        F[0] = F[1] = 1;
        for (int i = 2; i <= n; i++)
        {
            F[i] = (F[i - 1] * i) % MOD;
        }
    }

    static long modPow(long x, long n)
    {
        long res = 1L;
        while (n > 0)
        {
            if ((n & 1) == 1)
            {
                res = res * x % MOD;
            }
            x = x * x % MOD;
            n >>= 1;
        }
        return res;
    }

    //↑nCrをmod計算するために必要

    static int gcd(int n, int r)
    {
        return r == 0 ? n : gcd(r, n % r);
    }

    static long gcd(long n, long r)
    {
        return r == 0 ? n : gcd(r, n % r);
    }

    static <T> void swap(T[] x, int i, int j)
    {
        T t = x[i];
        x[i] = x[j];
        x[j] = t;
    }

    static void swap(int[] x, int i, int j)
    {
        int t = x[i];
        x[i] = x[j];
        x[j] = t;
    }

    public static void reverse(int[] x)
    {
        int l = 0;
        int r = x.length - 1;
        while (l < r)
        {
            int temp = x[l];
            x[l] = x[r];
            x[r] = temp;
            l++;
            r--;
        }
    }

    public static void reverse(long[] x)
    {
        int l = 0;
        int r = x.length - 1;
        while (l < r)
        {
            long temp = x[l];
            x[l] = x[r];
            x[r] = temp;
            l++;
            r--;
        }
    }

    public static void reverse(int[] x, int s, int e)
    {
        int l = s;
        int r = e;
        while (l < r)
        {
            int temp = x[l];
            x[l] = x[r];
            x[r] = temp;
            l++;
            r--;
        }
    }

    static int length(int a)
    {
        int cou = 0;
        while (a != 0)
        {
            a /= 10;
            cou++;
        }
        return cou;
    }

    static int length(long a)
    {
        int cou = 0;
        while (a != 0)
        {
            a /= 10;
            cou++;
        }
        return cou;
    }

    static int countC2(char[][] a, char c)
    {
        int co = 0;
        for (int i = 0; i < a.length; i++)
            for (int j = 0; j < a[0].length; j++)
                if (a[i][j] == c) co++;
        return co;
    }

    static int countI(int[] a, int key)
    {
        int co = 0;
        for (int i = 0; i < a.length; i++)
            if (a[i] == key) co++;
        return co;
    }

    static int countI(int[][] a, int key)
    {
        int co = 0;
        for (int i = 0; i < a.length; i++)
            for (int j = 0; j < a[0].length; j++)
                if (a[i][j] == key) co++;
        return co;
    }

    static void fill(int[][] a, int v)
    {
        for (int i = 0; i < a.length; i++)
            for (int j = 0; j < a[0].length; j++)
                a[i][j] = v;
    }

    static void fill(long[][] a, long v)
    {
        for (int i = 0; i < a.length; i++)
            for (int j = 0; j < a[0].length; j++)
                a[i][j] = v;
    }

    static void fill(int[][][] a, int v)
    {
        for (int i = 0; i < a.length; i++)
            for (int j = 0; j < a[0].length; j++)
                for (int k = 0; k < a[0][0].length; k++)
                    a[i][j][k] = v;
    }

    static int max(int a, int b, int c)
    {
        return Math.max(a, Math.max(b, c));
    }

    static int max(int[] ar)
    {
        int res = Integer.MIN_VALUE;
        for (int i : ar)
            res = Math.max(res, i);
        return res;
    }

    static int max(int[][] ar)
    {
        int res = Integer.MIN_VALUE;
        for (int i[] : ar)
            res = max(i);
        return res;
    }

    static int min(int a, int b, int c)
    {
        return Math.min(a, Math.min(b, c));
    }

    static int min(int[] ar)
    {
        int res = Integer.MAX_VALUE;
        for (int i : ar)
            res = Math.min(res, i);
        return res;
    }

    static int min(int[][] ar)
    {
        int res = Integer.MAX_VALUE;
        for (int i[] : ar)
            res = min(i);
        return res;
    }

    static int abs(int a)
    {
        return Math.abs(a);
    }

    static class FastScanner
    {

        private BufferedReader reader = null;
        private StringTokenizer tokenizer = null;

        public FastScanner(InputStream in)
        {
            reader = new BufferedReader(new InputStreamReader(in));
            tokenizer = null;
        }

        public String next()
        {
            if (tokenizer == null || !tokenizer.hasMoreTokens())
            {
                try
                {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e)
                {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        /*public String nextChar(){
            return (char)next()[0];
        }*/
        public String nextLine()
        {
            if (tokenizer == null || !tokenizer.hasMoreTokens())
            {
                try
                {
                    return reader.readLine();
                } catch (IOException e)
                {
                    throw new RuntimeException(e);
                }
            }

            return tokenizer.nextToken("\n");
        }

        public long nextLong()
        {
            return Long.parseLong(next());
        }

        public int nextInt()
        {
            return Integer.parseInt(next());
        }

        public double nextDouble()
        {
            return Double.parseDouble(next());
        }

        public int[] nextIntArray(int n)
        {
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
            {
                a[i] = nextInt();
            }
            return a;
        }

        public int[][] nextIntArray2(int h, int w)
        {
            int[][] a = new int[h][w];
            for (int hi = 0; hi < h; hi++)
            {
                for (int wi = 0; wi < w; wi++)
                {
                    a[hi][wi] = nextInt();
                }
            }
            return a;
        }

        //縦２つの列を一つにまとめる
        public int[] nextIntArray21(int n, int scalar)
        {
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt() * scalar + nextInt();
            return a;
        }

        //複数の配列を受け取る
        public void nextIntArrays2ar(int n, int[] a, int[] b)
        {
            for (int i = 0; i < n; i++)
            {
                a[i] = sc.nextInt();
                b[i] = sc.nextInt();
            }
        }

        //複数の配列を受け取る
        public void nextIntArrays3ar(int n, int[] a, int[] b, int[] c)
        {
            for (int i = 0; i < n; i++)
            {
                a[i] = sc.nextInt();
                b[i] = sc.nextInt();
                c[i] = sc.nextInt();
            }
        }

        public Integer[] nextIntegerArray(int n)
        {
            Integer[] a = new Integer[n];
            for (int i = 0; i < n; i++)
            {
                a[i] = nextInt();
            }
            return a;
        }

        public char[] nextCharArray(int n)
        {
            char[] a = next().toCharArray();

            return a;
        }

        public char[][] nextCharArray2(int h, int w)
        {
            char[][] a = new char[h][w];
            for (int i = 0; i < h; i++)
            {
                a[i] = next().toCharArray();
            }
            return a;
        }

        //スペースが入っている場合
        public char[][] nextCharArray2s(int h, int w)
        {
            char[][] a = new char[h][w];
            for (int i = 0; i < h; i++)
            {
                a[i] = nextLine().replace(" ", "").toCharArray();
            }
            return a;
        }

        public char[][] nextWrapCharArray2(int h, int w, char c)
        {
            char[][] a = new char[h + 2][w + 2];
            //char c = '*';
            int i;
            for (i = 0; i < w + 2; i++)
                a[0][i] = c;
            for (i = 1; i < h + 1; i++)
            {
                a[i] = (c + next() + c).toCharArray();
            }
            for (i = 0; i < w + 2; i++)
                a[h + 1][i] = c;
            return a;
        }

        //スペースが入ってる時用
        public char[][] nextWrapCharArray2s(int h, int w, char c)
        {
            char[][] a = new char[h + 2][w + 2];
            //char c = '*';
            int i;
            for (i = 0; i < w + 2; i++)
                a[0][i] = c;
            for (i = 1; i < h + 1; i++)
            {
                a[i] = (c + nextLine().replace(" ", "") + c).toCharArray();
            }
            for (i = 0; i < w + 2; i++)
                a[h + 1][i] = c;
            return a;
        }

        public long[] nextLongArray(int n)
        {
            long[] a = new long[n];
            for (int i = 0; i < n; i++)
            {
                a[i] = nextLong();
            }
            return a;
        }

        public long[][] nextLongArray2(int h, int w)
        {
            long[][] a = new long[h][w];
            for (int hi = 0; hi < h; hi++)
            {
                for (int wi = 0; wi < h; wi++)
                {
                    a[h][w] = nextLong();
                }
            }
            return a;
        }
    }
}
