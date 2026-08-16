import java.util.*;

public class Main {
  private final Scanner sc = new Scanner(System.in);

  public void run() {
    int n = sc.nextInt();

    int[][] list = new int[n][];

    for (int i = 0; i < n; i++) {
      int u = sc.nextInt() - 1;
      int k = sc.nextInt();

      list[u] = new int[k];

      for (int j = 0; j < k; j++) {
        list[u][j] = sc.nextInt() - 1;
      }

      Arrays.sort(list[u]);
    }

    int time = 1;

    int[] ds = new int[n];
    int[] fs = new int[n];

    for (int i = 0; i < n; i++) {
      ds[i] = 0;
      fs[i] = 0;
    }

    Deque<Integer> stack = new ArrayDeque<Integer>();
    stack.push(0);
    while(true) {
      if (stack.size() == 0) {
        boolean flag = true;
        for (int i = 0; i < n; i++) {
          if (ds[i] == 0) {
            stack.push(i);
            flag = false;
            break;
          }
        }
        if(flag) break;
      }

      int p = stack.peek();

      if (fs[p] != 0) {
        stack.pop();
      }
      else if (ds[p] != 0) {
        fs[p] = time;
        time++;
        stack.pop();
      }
      else {
        ds[p] = time;
        time++;
        for(int i = list[p].length - 1; i >= 0; i--) {
          if (ds[list[p][i]] == 0) stack.push(list[p][i]);
        }
      }
    }

    for (int i = 0; i < n; i++) {
      System.out.println((i + 1) + " " + ds[i] + " " + fs[i]);
    }
  }

  public static void main(String[] args) {
    new Main().run();
  }
}