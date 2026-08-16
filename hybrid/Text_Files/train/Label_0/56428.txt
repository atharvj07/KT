import java.io.*;
import java.util.*;
public class Main {
    public static void main(String args[])
    {
        FastReader input=new FastReader();
        PrintWriter out=new PrintWriter(System.out);
        int T=1;
        while(T-->0)
        {
            int n=input.nextInt();
            int c=input.nextInt();
            int a[]=new int[n-1];
            for(int i=0;i<n-1;i++)
            {
                a[i]=input.nextInt();
            }
            int b[]=new int[n-1];
            for(int i=0;i<n-1;i++)
            {
                b[i]=input.nextInt();
            }
            int pre=0;
            ArrayList<Integer> list=new ArrayList<>();
            list.add(0);
            int dp[][]=new int[n][2];
            dp[0][0]=0;
            dp[0][1]=c;
            for(int i=1;i<n;i++)
            {
                int x=a[i-1];
                int y=b[i-1];
                dp[i][0]=Math.min(dp[i-1][0]+x,dp[i-1][1]+x);
                dp[i][1]=Math.min(dp[i-1][0]+y+c,dp[i-1][1]+y);
                list.add(Math.min(dp[i][0],dp[i][1]));
            }
            for(int i=0;i<list.size();i++)
            {
                out.print(list.get(i)+" ");
            }
            out.println();
        }
        out.close();
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