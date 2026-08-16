import java.util.Arrays;
import java.util.Scanner;

public class Main {
  static Scanner sc = new Scanner(System.in);

  public static void main(String[] args) {
    int N = sc.nextInt();
    int[] A = new int[N];
    int sum = 0;
    for (int i = 0; i < N; i++) {
      A[i] = sc.nextInt();
      sum += A[i];
    }
    if (N == 1) {
      System.out.println(sum);
      return;
    }
    long[] exist = new long[(sum + 63) / 64];
    exist[0] = 1L;
    long[] tmp = new long[exist.length];
    for (int i = 0; i < N; i++) {
      Arrays.fill(tmp, 0L);
      for (int j = 0; j < exist.length; j++) {
        if (A[i] % 64 == 0) {
          if (j + A[i] / 64 < tmp.length) tmp[j + A[i] / 64] |= exist[j];
        } else {
          if (j + A[i] / 64 < tmp.length) tmp[j + A[i] / 64] |= exist[j] << (A[i] % 64);
          if (j + A[i] / 64 + 1 < tmp.length) tmp[j + A[i] / 64 + 1] |= exist[j] >>> (64 - A[i] % 64);
        }
        exist[j] |= tmp[j];
      }
      exist[A[i] / 64] |= 1L << (A[i] % 64);
    }

    for (int i = (sum + 1) / 2; ; i++) {
      if ((exist[i / 64] & (1L << i % 64)) != 0) {
        System.out.println(i);
        return;
      }
    }
  }

}
