import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		while(true){
			final int n = sc.nextInt();
			
			if(n == 0){
				break;
			}
			
			int[][] items = new int[n][4];
			
			for(int i = 0; i < n; i++){
				for(int j = 0; j < 4; j++){
					items[i][j] = sc.nextInt();
				}
			}
			
			int[] limits = new int[4]; 
			for(int i = 0; i < 4; i++){
				limits[i] = sc.nextInt();
			}
			
			boolean found = false;
			START:for(int i = 0; i < n; i++){
				for(int j = 1; j < 4; j++){
					if(items[i][j] > limits[j-1]){
						continue START;
					}
				}
				
				if(items[i][1]*4 + items[i][2]*9 + items[i][3]*4 > limits[3]){
					continue START;
				}
				
				found = true;
				System.out.println(items[i][0]);
			}
			
			if(!found){
				System.out.println("NA");
			}
		}
	}
}