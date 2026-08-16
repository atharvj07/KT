import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int N = scanner.nextInt();
    int[] a = new int[N];
    int max = -1_000_001;
    int min = 1_000_001;
    int maxi = -1;
    int mini = -1;
    for (int i = 0; i < N; i++) {
      a[i] = scanner.nextInt();
      if (a[i] > max) {
        max = a[i];
        maxi = i;
      }
      if (a[i] < min) {
        min = a[i];
        mini = i;
      }
    }

    List<int[]> operations = new ArrayList<>();
    boolean ltr;
    if (max >= 0 && min >= 0) ltr = true;
    else if (max < 0 && min < 0) ltr = false;
    else {
      if (max + min >= 0) {
        ltr = true;
        for (int i = 0; i < N; i++) {
          operations.add(new int[]{maxi, i});
          a[i] += max;
        }
      } else {
        ltr = false;
        for (int i = 0; i < N; i++) {
          operations.add(new int[]{mini, i});
          a[i] += min;
        }
      }
    }

    if (ltr) {
      for (int i = 0; i < N - 1; i++) {
        operations.add(new int[]{i, i + 1});
        a[i + 1] += a[i];
      }
    } else {
      for (int i = N - 1; i > 0; i--) {
        operations.add(new int[]{i, i - 1});
        a[i - 1] += a[i];
      }
    }

    System.out.println(operations.size());
    for (int[] p : operations) System.out.printf("%d %d\n", p[0] + 1, p[1] + 1);
  }
}
