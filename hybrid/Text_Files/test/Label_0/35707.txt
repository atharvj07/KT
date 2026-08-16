import java.io.*;
import java.util.*;


public class Main{
    static long MOD = 1000000007;
    static long dp[] = new long[1 << 21];
    public static void main(String[] args) {
        MyScanner sc = new MyScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));

        // Start writing your solution here. -------------------------------------
        long MOD = 1000000007;
        //int t = sc.nextInt();
        int t = 1;
        while(t -- > 0)
        {
            int n = sc.nextInt(), sqrt = (int)(Math.sqrt(n));
            int res[] = new int[n + 1];
            boolean[] used = new boolean[n + 1];
            int pos = n;
            for(int i = n / 2; i >= 1; i--)
            {
                int cnt = 0;
                for(int j = 2 * i; j <= n; j += i)
                {
                    if(!used[j])
                    {
                        cnt++;
                        used[j] = true;
                    }
                }
                for(int j = pos; j > pos - cnt; j--)
                    res[j] = i;
                pos -= cnt;
            }
            for(int i = 2; i <= n; i++)
                out.print(res[i] + " ");
            out.println("");
            //for(int ii = 0; ii <= n; ii++) System.out.println(Arrays.toString(dp[ii]));
        }
        out.close();
    }
    private static int dfs(int[][] dp, int x, int st, boolean op, int[] num) {
        if (x == 0) return st == 11 ? 0 : 1;
        if (!op && dp[x][st] != -1) return dp[x][st];
        int maxx = op ? num[x] : 9, res = 0;
        for(int i = 0; i <= maxx; i++)
        {
            if(st != 11 && Math.abs(st - i) >= 2) continue;
            if(st == 11 && i == 0)
                res += dfs(dp, x - 1, 11, op && (i == maxx), num);
            else
                res += dfs(dp, x - 1, i, op && (i == maxx), num);
        }
        if(!op) dp[x][st] = res;
        return res;
    }

    private static int solve(long n) {
        long tmp = n;
        int[][] dp = new int[20][20];
        for (int i = 0; i < 20; i++)
            Arrays.fill(dp[i], -1);
        int[] num = new int[20];
        int count = 0;
        while (n != 0) {
            num[++count] = (int)(n % 10);
            n /= 10;
        }
        int res =  dfs(dp, count, 11, true, num);
        return res;
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