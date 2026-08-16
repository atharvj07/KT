import java.util.Scanner;

public class Main {

	/**
	 * @param args
	 */
	
	public static final int C = 0;
	public static final int V = 1;
	public static final int D = 2;
	public static final int L = 3;
	public static void main(String[] args) {
		doIt();

	}
	
	public static void doIt(){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			int n = sc.nextInt();
			int m = sc.nextInt();
			int[][] bydol = new int[n][4];
			for(int i = 0; i < n; i++){
				sc.nextLine();
				sc.nextLine();
				bydol[i][C] = sc.nextInt();
				bydol[i][V] = sc.nextInt();
				bydol[i][D] = sc.nextInt();
				bydol[i][L] = sc.nextInt();
			}
			int max = 0;
			//各能力値に付いて
			for(int i = 1; i <= 3; i++){
				int dp[][] = new int[n + 1][m + 1];
				//各BYDOLについて
				for(int j = 1; j < n + 1; j++){
					//各費用に付いて
					for(int k = 1; k < m + 1; k++){
						//各個数について
						dp[j][k] = dp[j - 1][k];
						for(int l = 1; l*bydol[j - 1][C] <= k; l++){
							dp[j][k] = Math.max(dp[j][k], dp[j - 1][k - l*bydol[j - 1][C]] + l*bydol[j - 1][i]);
						}
					}
				}
				if(max < dp[n][m]){
					max = dp[n][m];
				}
			}
			System.out.println(max);
		}
	}

}