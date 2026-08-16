import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		int n = stdIn.nextInt();
		int d = stdIn.nextInt();
		int cnt = 0;
		
		int[][] point = new int[n][d];
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < d; j++) {
				point[i][j] = stdIn.nextInt();
			}
		}
		
		
		for(int i = 0; i < n-1; i++) {
			
			for(int j = i+1; j < n; j++) {
				int distance = 0;
				for(int k = 0; k < d; k++) {
				distance += (point[j][k] - point[i][k])*(point[j][k] - point[i][k]);
				}
				if(Math.sqrt(distance)==(int)Math.sqrt(distance)){
					//System.out.println(distance);
					cnt++;
				}
			}
		}
		
		System.out.println(cnt);
		
		
		
		
		
		
		
	}

}
