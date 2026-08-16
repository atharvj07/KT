import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    String S = sc.next();
    String ans = "";
    int d = 0;
    for (int i = 0; i < N; i++) {
      if (S.charAt(i) == '(') {
        ans = ans + "(";
        d++;
      } else {
        if (d > 0) {
          d--;
          ans = ans + ")";
        } else {
          ans = "(" + ans + ")";
        }
      }
    }
    while (d-- > 0) {
      ans = ans + ")";
    }

    System.out.println(ans);
  }
}