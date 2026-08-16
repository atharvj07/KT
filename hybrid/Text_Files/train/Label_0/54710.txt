import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.next();
    int[] a = new int[3];
    for(int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      if(c == 'a') a[0] += 1;
      if(c == 'b') a[1] += 1;
      if(c == 'c') a[2] += 1;
    }
    int m = Math.min(a[0], Math.min(a[1], a[2]));
    String ans = "YES";
    for(int i = 0; i < 3; i++) {
      if((a[i] != m) && (a[i] != (m + 1))) ans = "NO";
    }
    System.out.println(ans);
  }
}
