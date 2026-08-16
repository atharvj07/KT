import java.util.*;

class Main {
  public static void main (String[] args) {
    Scanner scanner = new Scanner(System.in);
    while (scanner.hasNext()) {
      int n = scanner.nextInt();
      if (n == 0) {
        break;
      }
      int[] ages = new int[7];
      int c = 0;
      for (int ii = 0; ii < n; ii++) {
        int a = scanner.nextInt();
        if (a < 10) {
          c = 0;
        } else if (a < 20) {
          c = 1;
        } else if (a < 30) {
          c = 2;
        } else if (a < 40) {
          c = 3;
        } else if (a < 50) {
          c = 4;
        } else if (a < 60) {
          c = 5;
        } else {
          c = 6;
        }
        ages[c]++;
      }
      for (int ii = 0; ii < 7; ii++) {
        System.out.println(ages[ii]);
      }
    }
  }
}