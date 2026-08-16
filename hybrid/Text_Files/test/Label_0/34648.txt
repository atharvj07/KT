import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int N = scanner.nextInt();
    int[] a = new int[N];
    for (int i = 0; i < N; i++) a[i] = scanner.nextInt();

    int[] dp = new int[N + 1];
    for (int i = 1; i <= N; i++) {
      dp[i] = dp[i - 1];
      if (a[i - 1] == dp[i - 1] + 1) dp[i]++;
    }
    if (dp[N] == 0) System.out.println(-1);
    else System.out.println(N - dp[N]);
  }
}
