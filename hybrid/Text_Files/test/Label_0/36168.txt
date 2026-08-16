import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String S = sc.next();
    boolean n = false;
    boolean w = false;
    boolean s = false;
    boolean e = false;
    for (int i = 0; i < S.length(); i++) {
      char c = S.charAt(i);
      if (c == 'N') {
        n = true;
      } else if (c == 'W') {
        w = true;
      } else if (c == 'S') {
        s = true;
      } else if (c == 'E') {
        e = true;
      }
    }
    System.out.println((n^s)||(w^e) ? "No" : "Yes");
  }
}