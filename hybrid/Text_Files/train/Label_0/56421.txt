import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    long M = 1_000_000_007;
    int N = scanner.nextInt();
    int K = scanner.nextInt();
    long[] fact = new long[N + 1];
    fact[0] = 1;
    for (int i = 1; i <= N; i++) fact[i] = fact[i - 1] * i % M;
    long[] factinv = new long[N + 1];
    factinv[0] = 1;
    for (int i = 1; i <= N; i++) factinv[i] = factinv[i - 1] * inverse(i, M) % M;

    for (int i = 1; i <= K; i++) {
      if (i > N - K + 1) {
        System.out.println(0);
        continue;
      }
      long d = choose(fact, factinv, N - K + 1, i, M);
      d *= choose(fact, factinv, K - 1, i - 1, M);
      d %= M;
      System.out.println(d);
    }
  }

  private static long inverse(long a, long mod) {
    return modpow(a, mod - 2, mod);
  }

  private static long modpow(long a, long n, long mod) {
    long res = 1;
    while (n > 0) {
      if (n % 2 == 1) res = (res * a) % mod;
      a = (a * a) % mod;
      n >>= 1;
    }
    return res % mod;
  }

  private static long choose(long[] fact, long[] factinv, int n, int k, long M) {
    if (n < k) return 0;
    return fact[n] * factinv[n - k] % M * factinv[k] % M;
  }
}
