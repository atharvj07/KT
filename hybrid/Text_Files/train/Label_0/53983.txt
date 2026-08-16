import java.util.*;
import java.awt.geom.*;
public class Main {

	private void doit(){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n == 0) break;
			int s = sc.nextInt();
			int numbers = n * 2;
			int [] takestone = new int[numbers];
			for(int i = 0; i < numbers; i++){
				takestone[i] = sc.nextInt();
			}
			boolean [][] dp = new boolean[numbers][s + 1];
			for(int i = 0; i < numbers; i++){
				if(i % 2 == 0){
					dp[i][1] = false;
				}
				else{
					dp[i][1] = true;
				}
			}
			for(int i = 2; i <= s; i++){
				for(int j = 0; j < numbers; j++){
					boolean iswin = dp[(j+1) % numbers][i-1];
					for(int k = 2; k <= takestone[j]; k++){
						if(i- k <= 0) break;
						if(j % 2 == 0){
							iswin = iswin || dp[(j+1) % numbers][i - k];
						}
						else{
							iswin = iswin && dp[(j+1) % numbers][i - k];
						}
					}
					dp[j][i] = iswin;
				}
			}

			System.out.println(dp[0][s] ? 1 : 0);
		}
	}

	public static void main(String[] args) {
		Main obj = new Main();
		obj.doit();
	}
}