import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		int m = scan.nextInt();
		int x = scan.nextInt();
		int skill[][] = new int[n][m+1];
		for(int i=0;i<n;i++) {
			for(int j=0;j<m+1;j++) {
				skill[i][j] = scan.nextInt();
			}
		}
		
		boolean check = false;
		int min_cost = 1500000;
		
		for(int i=0;i<(1<<n);i++) {
			boolean judge = true;
			int cost = 0;
			int now_skill[] = new int[m];
			
			for(int j=0;j<n;j++) {
				if((1 & i>>j)==1) {
					cost += skill[j][0];
					for(int k=0;k<m;k++) {
						now_skill[k] += skill[j][k+1];
					}
				}
			}
			
			for(int j=0;j<m;j++) {
				if(now_skill[j] < x) {
					judge = false;
					break;
				}
			}
			
			if(judge) {
				if(min_cost > cost) {
					check = true;
					min_cost = cost;
				}
			}
			
		}
		
		if(check) {
			System.out.println(min_cost);
		}else {
			System.out.println(-1);
		}
		
		
		
	}	
}
 