import java.io.*;
import java.math.*;
import java.util.*;


public class Main{
    static long MOD = 998244353 ;
    static long [] fac;
    static int [] num;
    static int max = 0;
    static int n;
    static int m;
    static int q;
    static int [] a, b, c, d;
    public static void main(String[] args) {
        MyScanner sc = new MyScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        // Start writing your solution here. -------------------------------------
        //int t = sc.nextInt();
        int t = 1;
        while(t-- > 0)
        {
            n = sc.nextInt();
            m = sc.nextInt();
            q = sc.nextInt();
            a = new int[q]; b = new int[q]; c = new int[q]; d = new int[q];
            num = new int[n + 1];
            for(int i = 0; i < q; i++)
            {
                a[i] = sc.nextInt();
                b[i] = sc.nextInt();
                c[i] = sc.nextInt();
                d[i] = sc.nextInt();
            }
            num[1] = 1;
            dfs(2, 1);
            out.println(max);
        }
        out.close();
    }
    public static void dfs(int ind, int now)
    {
        if(ind > n)
        {
            int sum = 0;
            for(int i = 0; i < q; i++)
            {
                if(num[b[i]] - num[a[i]] == c[i])
                sum += d[i];
            }
            if(sum > max)
                max = sum;
            return;
        }
        for(int j = now; j <= m; j++)
        {
            num[ind] = j;
            dfs(ind + 1, j);
        }
    }
    public static long C(int n, int m)
    {
        if(m == 0 || m == n) return 1l;
        if(m > n || m < 0) return 0l;
        long res = fac[n] * quickPOW((fac[m] * fac[n - m]) % MOD, MOD - 2) % MOD;

        return res;
    }
    public static long quickPOW(long n, long m)
    {
        long ans = 1l;
        while(m > 0)
        {
            if(m % 2 == 1)
                ans = (ans * n) % MOD;
            n = (n * n) % MOD;
            m >>= 1;
        }
        return ans;
    }
    public static int gcd(int a, int b)
    {
        if(a % b == 0) return b;
        return gcd(b, a % b);
    }
    public static long solve(long x, long[] res){
        int n = res.length;
        long a = x / n;
        int b = (int)(x % n);
        return res[n - 1] * a + res[b];
    }
    //-----------PrintWriter for faster output---------------------------------
    public static PrintWriter out;
    //-----------MyScanner class for faster input----------
    public static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        public MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        String nextLine(){
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
    //--------------------------------------------------------
}