import java.util.*;
public class Main{
  public static void main(String[]args){
      Scanner sc = new Scanner(System.in);

      String a = sc.next();

      char b = a.charAt(0);
      char c = a.charAt(1);

      if(b=='9'||c=='9'){
        System.out.println("Yes");
      }else{
          System.out.println("No");
      }
  }
}