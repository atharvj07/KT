import java.util.*;
public class Main {
    public static void main(String args[]) {
      Scanner sc=new Scanner(System.in);
      //int n=sc.nextInt();
      long n=sc.nextLong();
      long a=0,b=0;
      for(int i=(int)Math.ceil(Math.sqrt((double)n));i>=1;i--)
      {
          if(n%i==0)
          {
              a=i;
              b=n/i;
              break;
          }
      }
      System.out.println(((a-1)+(b-1)));
    }
}
