import java.util.*;

public class Main {
  public static void main (String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int[] p = new int[n];
    int[] q = new int[n];

    for (int i = 0; i < n; i++) {
      p[i] = sc.nextInt();
      q[i] = p[i];
    }

    Arrays.sort(q);

    int cnt = 0;
    for (int i = 0; i < n; i++) {
      if (p[i] != q[i]) cnt++;
      if (cnt > 2) break;
    }
    
    System.out.println(cnt > 2 ? "NO" : "YES");
  }
}
