import java.util.Scanner;

public class Main{
	public static void main(String[] args){
      Scanner sc = new Scanner(System.in);
      long a = sc.nextLong();
      long b = sc.nextLong();
      long c = sc.nextLong();
      boolean ans = true;
      if((c - a - b <= 0) || 4*a*b >= (c - a - b)*(c - a - b)){
        ans = false;
      }
      
	  System.out.println(ans?"Yes":"No");
    }
}
