import java.util.*;
import java.io.*;

// Solution

public class Main 
{    
  public static void main (String[] argv) 
  {
	  new Main();
  } 
     
  
  boolean test = false;

  public Main() {
	  FastReader in = new FastReader(new BufferedReader(new InputStreamReader(System.in)));
	  //FastReader in = new FastReader(new BufferedReader(new FileReader("Main.in")));
      int n = in.nextInt();
      int k = in.nextInt();
      int s = in.nextInt();
      
      
      int[] a = new int[n];
      for (int a0 = 0; a0 < n; a0++)
          a[a0] = in.nextInt();
      
      if (s >= n * (n - 1) / 2 || k >= n) {
          Arrays.sort(a);
          int sumk = 0;
          for (int i = 0; i < k; i++) sumk += a[i];
          
          System.out.println(sumk);
          return;
      }
      int INF = -1;
      int[][] dp = new int[k+1][s+1];
      int[][] dp2 = new int[k+1][s+1];
      for (int j = 1; j <= k; j++)
          for (int t = 0; t <= s; t++) 
              dp[j][t] = INF;
      
      for (int i = 1; i <= n; i++) {
          for (int j = 1; j <= k && j <= i; j++) {
              for (int t = 0; t <= s; t++) {                 
                 dp2[j][t] = INF;
                 if (i - 1 >= j) dp2[j][t] = dp[j][t];
                 
                 int si = i - j;
                 if (t >= si && (dp2[j][t] == INF || (dp[j-1][t-si] != INF && dp[j-1][t-si] + a[i-1] < dp2[j][t])))
                     dp2[j][t] = dp[j-1][t-si] + a[i-1];                     
              }              
          }
          
          int[][] tmp = dp;
          dp = dp2;
          dp2 = tmp;
      }
      
      System.out.println(dp[k][s]);
  }
  
  static class FastReader
    {
        BufferedReader br;
        StringTokenizer st;
 
        public FastReader(BufferedReader in)
        {            
            br = in;
        }
 
        String next()
        {
            while (st == null || !st.hasMoreElements())
            {
                try
                {
                    String line = br.readLine();
                    if (line == null || line.length() == 0) return "";
                    st = new StringTokenizer(line);
                }
                catch (IOException  e)
                {
                    return "";
                    //e.printStackTrace();
                }
            }
            return st.nextToken();
        }
 
        int nextInt()
        {
            return Integer.parseInt(next());
        }
 
        long nextLong()
        {
            return Long.parseLong(next());
        }
 
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
 
        String nextLine()
        {
            String str = "";
            try
            {
                str = br.readLine();
            }
            catch (IOException e)
            {
                return "";
                //e.printStackTrace();
            }
            return str;
        }
    }
}