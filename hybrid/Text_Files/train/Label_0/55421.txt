import java.util.*;
public class Main{
  public static void main(String[]args){
    Scanner sc = new Scanner(System.in);
    int A = sc.nextInt();
    int B = sc.nextInt();
    int n = A - B*2;
    if(n > 0){
      System.out.println(n);
    }else{
      System.out.println(0);
    }


  }
}