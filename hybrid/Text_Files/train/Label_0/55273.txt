import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNextLine()) {
			String[] in = sc.nextLine().split(" ");
			ArrayList<Integer> list = new ArrayList<Integer>();
			int n = in.length-1;
			int s = Integer.parseInt(in[0]);
			for(int i = 0 ; i < n; i++) {
				list.add(Integer.parseInt(in[i+1]));
			}
			
			double[][] dp = new double[1 << n][n];
			for(int i = 1; i < 1 << n; i++) {
				Arrays.fill(dp[i], 2 << 27);
			}
			for(int i = 0; i < n; i++) {
				dp[1 << i][i] = list.get(i);
			}
			for(int i = 1; i < 1 << n; i++) {
				for(int j = 0; j < n; j++) {
					for(int k = 0; k < n; k++) {
						if((i & (1 << k)) == 0) {
							dp[i | (1 << k)][k] = Math.min(dp[i | (1 << k)][k], dp[i][j] + Math.sqrt(Math.pow(list.get(j) + list.get(k), 2) - Math.pow(list.get(j) - list.get(k), 2)));
						}
					}
				}
			}
			double min = Integer.MAX_VALUE;
			
			for(int i = 0; i < n; i++) {
				double tmp = dp[(1 << n) -1][i] + list.get(i);
				if(min > tmp) {
					min = tmp;
				}
			}
			if(min <= s) {
				System.out.println("OK");
			}
			else {
				System.out.println("NA");
			}
			
			
			
			
		}
	}
	

}