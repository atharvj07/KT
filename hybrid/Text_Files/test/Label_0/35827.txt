import java.util.*;

class Main {
  public static void main (String[] args) {
    int[] ps = {6, 8, 10, 12, 14, 16, 0};
    Scanner scanner = new Scanner(System.in);
    while (scanner.hasNext()) {
      int n = scanner.nextInt();
      if (n == 0) {
        break;
      }
      int p = 0;
      for (int ii = 0; ii < n; ii++) {
        int xyh = scanner.nextInt() + scanner.nextInt() + scanner.nextInt();
        int w = scanner.nextInt();
        int xyhp = 0;
        int wp = 0;
        if (xyh <= 60) {
          xyhp = ps[0];
        } else if (xyh <= 80) {
          xyhp = ps[1];
        } else if (xyh <= 100) {
          xyhp = ps[2];
        } else if (xyh <= 120) {
          xyhp = ps[3];
        } else if (xyh <= 140) {
          xyhp = ps[4];
        } else if (xyh <= 160) {
          xyhp = ps[5];
        } else {
          xyhp = 0;
        }
        if (w <= 2) {
          wp = ps[0];
        } else if (w <= 5) {
          wp = ps[1];
        } else if (w <= 10) {
          wp = ps[2];
        } else if (w <= 15) {
          wp = ps[3];
        } else if (w <= 20) {
          wp = ps[4];
        } else if (w <= 25) {
          wp = ps[5];
        } else {
          wp = 0;
        }
        if (xyhp == 0 || wp == 0) {
          continue;
        }
        if (xyhp > wp) {
          p += xyhp;
        } else {
          p += wp;
        }
      }
      System.out.println(p * 100);
    }
  }
}