import java.util.*;

public class Main{
  public static void main(String[]args){
    Scanner sc=new Scanner(System.in);
    
    int a=sc.nextInt();
    int b=sc.nextInt();
    int c=a+b;
    if(a%3==0 || b%3==0 ||c%3==0){
      System.out.println("Possible");
    }else{
      System.out.println("Impossible");
    }
    sc.close();
  }
}