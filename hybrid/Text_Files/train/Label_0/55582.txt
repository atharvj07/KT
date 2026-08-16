import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    String S = sc.nextLine();
    if("Sunny".equals(S)){
      System.out.println("Cloudy");
    }else if("Cloudy".equals(S)){
      System.out.println("Rainy");
    }else if("Rainy".equals(S)){
      System.out.println("Sunny");
    }
  }
}
