import java.util.*;

public class Main{
	public static void main(String args[]){
     	Scanner sc = new Scanner(System.in);
      	int n = sc.nextInt();
      	long d = sc.nextLong();
        int count = 0;
        while(n-->0){
        	long a = sc.nextLong();
            long b = sc.nextLong();
            double ans = Math.sqrt(a*a + b*b);
            if(ans<=d)
                count++;
        }
        System.out.println(count);
    }
}
