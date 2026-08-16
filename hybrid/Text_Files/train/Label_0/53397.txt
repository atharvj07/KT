import java.util.Arrays;
import java.util.Scanner;

public class Main {

  Scanner sc;

  Main() {
    sc = new Scanner(System.in);
  }

  int ni() {
    return sc.nextInt();
  }

  public static void main(String[] args) {
    new Main().run();
  }

  void run() {
    for (; ; ) {
      int n = ni();
      if (n == 0) {
        break;
      }
      int w = ni();
      int h = ni();
      boolean[][] f = new boolean[h][w];
      for (int i = 0; i < n; ++i) {
        int x = ni() - 1;
        int y = ni() - 1;
        f[y][x] |= true;
      }
      int s = ni();
      int t = ni();
      int ans = 0;
      for (int i = 0; i <= h - t; ++i) {
        for (int j = 0; j <= w - s; ++j) {
          int cnt = 0;
          for (int k = 0; k < t; ++k) {
            for (int l = 0; l < s; ++l) {
              if (f[k + i][l + j]) {
                ++cnt;
              }
            }
          }
          ans = Math.max(ans, cnt);
        }
      }
      System.out.println(ans);
    }
  }

  void debug(Object... os) {
    System.err.println(Arrays.deepToString(os));
  }
}