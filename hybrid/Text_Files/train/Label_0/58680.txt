import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int n = in.nextInt();
    int m = in.nextInt();
    int[][] a = new int[n][m];
    int[] b = new int[m];
    int[] c = new int[n];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        a[i][j] = in.nextInt();
      }
    }
    for (int i = 0; i < m; i++) {
      b[i] = in.nextInt();
    }
    for (int i = 0; i < n; i++) {
      c[i] = 0;
      for (int j = 0; j < m; j++) {
        c[i] += a[i][j] * b[j];
      }
    }
    for (int i = 0; i < n; i++) {
      System.out.println(c[i]);
    }
  }
}