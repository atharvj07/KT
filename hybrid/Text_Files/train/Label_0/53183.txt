import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	
	public static final int MAX = 50000;
	
	public static long gcd(long x, long y){
		if(x == 0){
			return y;
		}else{
			return gcd(y % x, x);
		}
	}
	
	public static long lcm(long x, long y){
		return x / gcd(x, y) * y;
	}
	
	public static void main(String[] args) {
		final Scanner sc = new Scanner(System.in);
		
		while(true){
			final int a = sc.nextInt();
			final int b = sc.nextInt();
			final int d = sc.nextInt();
			
			if(a == 0 && b == 0 && d == 0){
				break;
			}
			
			final long lcm = lcm(a, b);
			
			//System.out.println(lcm);
			
			long min_count = Integer.MAX_VALUE;
			long min_x = 0;
			long min_y = 0;
			
			//same
			for(long x = 0; ; x++){
				long rest = d - a * x;
				
				if(rest < 0){
					break;
				}else if(rest % b != 0){
					continue;
				}
				
				long y = rest / b;
				
				//System.out.println("=>1 " +  x + " " + y + " " + (a * x + b * y) + " " + d);
				
				if(min_count > x + y){
					min_count = x + y;
					min_x = x;
					min_y = y;
				}
			}
			
			//other(a = b + d)
			for(long x = 0; a * x < lcm; x++){
				long rest = a * x - d;
				
				if(rest < 0){
					continue;
				}else if(rest % b != 0){
					continue;
				}
				
				long y = rest / b;
				
				//System.out.println("=>2 " +  x + " " + y + " " + (a * x) + " " + (b * y + d));
				
				if(min_count > x + y){
					min_count = x + y;
					min_x = x;
					min_y = y;
				}
			}
			
			//other(a * x + d = b * y)
			for(long x = 0; a * x < lcm; x++){
				long rest = a * x + d;
				
				if(rest % b != 0){
					continue;
				}
				
				long y = rest / b;
				
				//System.out.println("=>3 " +  x + " " + y + " " + (a * x + d) + " " + (b * y));
				
				if(min_count > x + y){
					min_count = x + y;
					min_x = x;
					min_y = y;
				}
			}
			
			System.out.println(min_x + " " + min_y);
		}
		
	}

}