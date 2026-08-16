import java.util.*;

public class Main {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    String str1 = sc.next();
    String str2 = sc.next();
    int a1 = sc.nextInt();
    int a2 = sc.nextInt();
    String str = sc.next();

    if (str.equals(str1)) {
      a1--;
    }
    if (str.equals(str2)) {
      a2--;
    }
    System.out.print(a1 + " " + a2);
    
  }
}
