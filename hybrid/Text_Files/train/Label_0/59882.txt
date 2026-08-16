import java.util.*;
import java.io.*;

public class Main{
  static int INF = 100000001;

  public static void main(String[] args)throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    int half = n / 2;
    int[] t = new int[n + 2];
    int[][][] dp = new int[2][n + 2][2];

    for(int i = 0; i < n - 1; i++){
      t[i] = Integer.parseInt(br.readLine());
      for(int j = 0; j < 2; j++){
        Arrays.fill(dp[j][i], INF);
      }
    }

    dp[0][0][0] = 0;

    for(int I = 0; I < n - 1; I++){
      int i = I % 2;
      int ni = (i + 1) % 2;

      for(int j = 0; j <= half; j++){
        dp[ni][j + 1][0] = Math.min(dp[i][j][0], dp[i][j][1] + t[I]);
        dp[ni][j    ][1] = Math.min(dp[i][j][1], dp[i][j][0] + t[I]);
        Arrays.fill(dp[i][j], INF);
      }
    }

    System.out.println(Math.min(dp[1][half - 1][0], dp[1][half - 1][1]));
  }
}