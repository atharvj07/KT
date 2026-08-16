import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int p = 0;
    String ans = "Yes";
    for(int i = 0; i < n; i++) {
      int h = sc.nextInt();
      if(h > p) {
        h--;
        p = h;
      } else if(h == p) {
      
      } else {
        ans = "No";
        break;
      }
    }
    System.out.println(ans);
  }
}
