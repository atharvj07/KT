import java.util.Arrays;
import java.util.Scanner;

public class Main {
  static Scanner sc = new Scanner(System.in);

  public static void main(String[] args) {
    int H = sc.nextInt();
    int W = sc.nextInt();
    int[][] A = new int[400][400];
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        A[i][j] = sc.nextInt();
      }
    }
    if (H <= 2 || W <= 2) {
      int ans = 0;
      for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
          ans += A[i][j];
        }
      }
      System.out.println(ans);
      return;
    }
    int[][][] dp = new int[2][H + W][H + W];
    dp[0][0][1] = A[0][0] + A[1][0] + A[0][1];
    int t = 1;
    for (int i = 1; i < H + W - 3; i++) {
      int len = i + 1;
      for (int j = 0; j < dp[0].length; j++) {
        Arrays.fill(dp[t][j], 0);
      }
      for (int j = 0; j < len; j++) {
        for (int k = j + 1; k < len; k++) {
          dp[t][j][k] = Math.max(dp[t][j][k], dp[1 - t][j][k] + A[i + 1 - j][j] + A[i + 1 - k][k]);
          dp[t][j][k + 1] = Math.max(dp[t][j][k + 1], dp[1 - t][j][k] + A[i + 1 - j][j] + A[i - k][k + 1]);
          if (k > j + 1) {
            dp[t][j + 1][k] = Math.max(dp[t][j + 1][k], dp[1 - t][j][k] + A[i - j][j + 1] + A[i + 1 - k][k]);
          }
          dp[t][j + 1][k + 1] = Math.max(dp[t][j + 1][k + 1], dp[1 - t][j][k] + A[i - j][j + 1] + A[i - k][k + 1]);
        }
      }
      t = 1 - t;
    }
    System.out.println(dp[1 - t][W - 2][W - 1] + A[H - 1][W - 1]);
  }
}
