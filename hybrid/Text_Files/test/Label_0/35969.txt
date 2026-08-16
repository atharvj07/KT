import java.util.*;
public class Main {
	public static void main(String[] args){
	Scanner sc = new Scanner(System.in);
    int K = sc.nextInt();
    int X = sc.nextInt();
    int total = 500 * K;
    if(total >= X)
      System.out.println("Yes");
    else
   	  System.out.println("No");
    }
}
