import java.util.*;
import java.io.*;

public class Main{
  public static void main(String[] args)throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    final int MOD = 1000000007;

    while(br.ready()){
      String[] s = br.readLine().split(" ");
      int N = Integer.parseInt(s[0]);
      int W = Integer.parseInt(s[1]);
      ArrayList<Integer> wal = new ArrayList<Integer>();
      int[] pre = new int[W + 2];

      for(int i = 0; i < N; i++){
        int x = Integer.parseInt(br.readLine());

        if(x <= W){
          pre[x] += x;
          wal.add(x);
        }
      }

      for(int i = 0; i < W; i++){
        pre[i + 1] += pre[i];
      }

      Collections.sort(wal);
      Integer[] w = (Integer[])wal.toArray(new Integer[0]);
      N = w.length;

      int[] idx = new int[W + 2];
      Arrays.fill(idx, -1);

      int[][] dp = new int[N + 2][W + 2];
      dp[N][0] = 1;

      for(int i = N; i > 0; i--){
        for(int j = 0; j <= W; j++){
          dp[i - 1][j] += dp[i][j];
          dp[i - 1][j] %= MOD;

          if(j + w[i - 1] <= W){
            dp[i - 1][j + w[i - 1]] += dp[i][j];
            dp[i - 1][j + w[i - 1]] %= MOD;
          }
        }

        if(w[i - 1] <= W){
          idx[w[i - 1]] = i - 1;
        }
      }

      idx[W + 1] = N;
      for(int i = W + 1; i > 0; i--){
        if(idx[i - 1] == -1){
          idx[i - 1] = idx[i];
        }
      }

      int ans = 0;

      for(int x = 0; x <= W; x++){
        if(x < pre[W - x]) continue;
        ans += dp[ idx[W - x + 1] ][ x - pre[W - x] ];
        ans %= MOD;
      }

      System.out.println(ans);
    }
  }
}