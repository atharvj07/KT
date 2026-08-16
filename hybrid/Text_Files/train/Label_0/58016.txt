import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int N = scanner.nextInt();
    Block[] blocks = new Block[N];
    for (int i = 0; i < N; i++) {
      blocks[i] = new Block(scanner.nextInt(), scanner.nextInt(), scanner.nextInt());
    }

    Arrays.sort(blocks, (b1, b2) -> b2.s + b2.w - b1.s - b1.w);

    final int MAX_S = 20_000;
    long[][] dp = new long[N + 1][MAX_S + 1];
    for (int i = 1; i <= N; i++) {
      Block b = blocks[i - 1];
      for (int j = 0; j <= MAX_S; j++) {
        if (j + b.w <= MAX_S && j <= b.s) {
          dp[i][j] = Math.max(dp[i - 1][j + b.w] + b.v, dp[i - 1][j]);
        } else {
          dp[i][j] = dp[i - 1][j];
        }
      }
    }

    long max = 0;
    for (int i = 0; i <= MAX_S; i++) {
      max = Math.max(max, dp[N][i]);
    }
    System.out.println(max);
  }

  private static class Block {
    public final int w;
    public final int s;
    public final int v;

    private Block(int w, int s, int v) {
      this.w = w;
      this.s = s;
      this.v = v;
    }
  }
}
