import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    boolean found = false;
    for (int j = 1; j < 5; ++j) {
      int a = s.nextInt();
      int b = s.nextInt();
      int c = s.nextInt();
      int d = s.nextInt();
      for (int g1 = Math.min(a, b); g1 <= n; g1++) {
        int g2 = n - g1;
        if (g2 >= Math.min(c, d)) { System.out.println(j + " " + g1 + " " + g2); found = true; break; }
      }
      if (found) break;
    }
    if (!found) System.out.println(-1);
  }
}
