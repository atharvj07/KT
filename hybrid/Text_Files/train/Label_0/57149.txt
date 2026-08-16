import java.awt.geom.Rectangle2D;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	
	public static final int MAX = 100000;
	public static final int MAX_D = 15;
	
	public static void main(String[] args) {
		final Scanner sc = new Scanner(System.in);
		
		double[][] DP = new double[MAX + 1][MAX_D + 1];
		double[] ans = new double[MAX];
		
		DP[0][0] = 1;
		
		double sum = 0;
		for(int day = 0; day < MAX; day++){
			for(int suc = 0; suc < MAX_D; suc++){
				if(DP[day][suc] <= 0){
					continue;
				}
				
				sum += DP[day][suc] * Math.pow(0.5, suc);
				
				if(suc == 0){
					DP[day + 1][suc + 1] += DP[day][suc];
				}else{
					DP[day + 1][0]       += DP[day][suc] * (1 - Math.pow(0.5, suc));
					DP[day + 1][suc + 1] += DP[day][suc] * Math.pow(0.5, suc);
				}
			}
			
			ans[day] = sum;
		}
		
		while(true){
			final int n = sc.nextInt();
			
			if(n == 0){
				break;
			}
			
			System.out.println(ans[n - 1]);
		}
	}

}