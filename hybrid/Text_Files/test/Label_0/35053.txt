import java.awt.*;
import java.io.*;
import java.util.*;

public class Abc {
    public static void main(String[] args) {
        FastReader sc = new FastReader();
        int n=sc.nextInt();
        int t[]=new int[n+1];
        int w[]=new int[n+1];
        for (int i=1;i<=n;i++){
            t[i]=sc.nextInt();
            w[i]=sc.nextInt();
        }
        int dp[][]=new int[n+1][206];
        for (int arr[]:dp){
            Arrays.fill(arr,50000);
        }
        dp[0][0]=0;
        for (int i=1;i<=n;i++){
            for (int j=0;j<=205;j++){
                if (j-t[i]>=0) {
                    dp[i][j] = Math.min(dp[i - 1][j] + w[i], dp[i - 1][j - t[i]]);
                }else dp[i][j]=dp[i-1][j]+w[i];
            }
        }
        for (int i=1;i<205;i++){
            if (dp[n][i]<=i){
                System.out.println(i);
                return;
            }
        }
    }


    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
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

        String nextLine() {
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