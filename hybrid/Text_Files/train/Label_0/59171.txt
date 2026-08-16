import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    long a = sc.nextLong();
    long b = sc.nextLong();
    long c = sc.nextLong();
    long d = sc.nextLong();
    long e = lcm(c,d);
    long count = b-a+1;
    count -= b/c - (a-1)/c;
    count -= b/d - (a-1)/d;
    count += b/e - (a-1)/e;
    System.out.println(count);

  }

  private static long lcm(long a, long b){
    long temp;
    long c = a;
    c *= b;
    while((temp = a%b)!=0){
      a=b;
      b=temp;
    }
    return c/b;
  }
}
