import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int A = scan.nextInt();
    int B = scan.nextInt();
    if(A != 1 && B != 1){
      System.out.print(1);
    }
    else if(A != 2 && B != 2){
      System.out.print(2);
    }
    else if(A != 3 && B != 3){
      System.out.print(3);
    }
  }
}