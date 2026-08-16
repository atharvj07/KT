import java.util.*;
public class Main {

  public static void main(String[] args) { 
      Scanner sc = new Scanner(System.in);
      long h = sc.nextInt();
      long w = sc.nextInt();
      
      if(h == 1 || w == 1) {
        System.out.println(1);
        return;
      }
      long res = w * (h / 2);
      if(h % 2 == 1) {
        res += (w + 1) / 2;
      }
      System.out.println(res);
  }
}