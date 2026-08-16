import java.util.*;
import java.math.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String S = sc.next();
    sc.close();

    String ans = ("AAA".equals(S) || "BBB".equals(S)) ? "No" : "Yes";
    System.out.println(ans);
  }
}