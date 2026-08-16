import java.util.*;

class Main{
  public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
//    String s=sc.next();
    int a=sc.nextInt();
    int b=sc.nextInt();
    int x=sc.nextInt();
    System.out.println((a<=x&&x<=a+b)?"YES":"NO");
  }
}