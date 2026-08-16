import java.io.*;
import java.util.*;


class Main {
    static void solve(int n,int m,int k,long[]a){
        long[][]dp=new long[2][n];
        for(int i=0;i<n;++i){
            dp[0][i]=a[i];
        }
        int[]deq=new int[n];
        for(int i=1;i<k;++i){
            int s=0,t=0;
            int u=(i-1)%2;
            int nxt=1-u;
            for(int j=i-1;j<n;++j){
                if(j>=i){
                    assert s < t;
                    long val=dp[u][deq[s]]+(i+1)*a[j];
                    dp[nxt][j]=val;
                    if(deq[s]==j-m)s++;
                }
                while(s<t&&dp[u][deq[t-1]]<=dp[u][j])t--;
                deq[t++]=j;
            }
        }
        long ans=0;
        for(int i=k-1;i<n;++i)ans=Math.max(ans,dp[(k-1)%2][i]);
        out.println(ans);
    }
    public static void main(String[] args) {
        MyScanner sc = new MyScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        int n=sc.nextInt();
        int m=sc.nextInt();
        int k=sc.nextInt();
        long[]a=new long[n];
        for(int i=0;i<n;++i){
            a[i]=sc.nextLong();
        }
        solve(n,m,k,a);
        out.close();
    }
    // http://codeforces.com/blog/entry/7018
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
}
