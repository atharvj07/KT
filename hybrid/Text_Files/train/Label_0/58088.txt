import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int N = scanner.nextInt();
    Number[] numbers = new Number[N];
    for (int i = 0; i < N; i++) numbers[i] = new Number(i, scanner.nextInt());
    Arrays.sort(numbers, (n1, n2) -> n2.value - n1.value);

    long[][] dp = new long[N + 1][N + 1];
    for (int i = 0; i <= N; i++) {
      for (int j = 0; j <= N - i; j++) {
        if (i == 0 && j == 0) continue;
        Number a = numbers[i + j - 1];
        long left = 0;
        if (i > 0) left = dp[i - 1][j] + (long) a.value * (a.pos - i + 1);
        long right = 0;
        if (j > 0) right = dp[i][j - 1] + (long) a.value * (N - j - a.pos);
        dp[i][j] = Math.max(left, right);
      }
    }
    long max = 0;
    for (int i = 0; i <= N; i++) max = Math.max(max, dp[i][N - i]);
    System.out.println(max);
  }

  private static class Number {
    private final int pos;
    private final int value;

    private Number(int pos, int value) {
      this.pos = pos;
      this.value = value;
    }
  }
}
