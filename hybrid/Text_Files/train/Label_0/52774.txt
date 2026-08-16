import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int M = sc.nextInt();
    ArrayList<Integer> list = new ArrayList<>();
    for (int i = 1; i * i <= M; i++) {
      if (M % i == 0) {
        list.add(i);
        list.add(M / i);
      }
    }
    int ans = -1;
    for (int i = 0; i < list.size(); i++) {
      int value = list.get(i);
      if (ans < value && value <= M / N) {
        ans = value;
      }
    }
    System.out.println(ans);
  }
}