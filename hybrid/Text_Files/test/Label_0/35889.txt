import java.util.Scanner;
import java.util.ArrayList;

public class Main {
	Scanner sc;
	public void run(){
		sc = new Scanner(System.in);
		while(sc.hasNextInt()){
			int n = sc.nextInt();
			if(n != 0){
				calc(n);
			}
			else{
				break;
			}
		}
	}
	public void calc(int n){
		int ps[] = new int[n+1];
		int ts[] = new int[n+1];
		for(int i = 1; i < n+1; i++){
			ps[i] = sc.nextInt();
			ts[i] = sc.nextInt();
		}
		
		int[][] memo = new int[n+1][4];
		for(int i = 0; i < n+1; i++){
			for(int j = 0; j < 4; j++){
				memo[i][j] = Integer.MAX_VALUE; 
			}
		}
		memo[0][1] = 0; 
		memo[0][2] = -1; 
		memo[0][3] = 1;
		
		boolean result = true;
		
		for(int i = 0; i < n; i++){
			int nextT = ts[i+1];
			int nextP = ps[i+1];
			int nowT = ts[i];
			int nowP = ps[i];
			for(int k = 1; k < 4; k++){
				if(memo[i][k] != -1) {
					//置いてから来る
					int needT = (k + 1) * nowP + nextP + nowT;
					int needP = nowP + nextP + memo[i][k];
					if(needT <= nextT && needP < memo[i+1][1]) {
						memo[i+1][1] = needP;
					}
					//置かない
					if(k != 3){
						needT = (k + 1) * Math.abs(nowP - nextP) + nowT;
						needP = Math.abs(nowP - nextP) + memo[i][k];
						if(needT <= nextT && needP < memo[i+1][k+1]){
							memo[i+1][k+1] = needP;
						}
					}
				}
						
			}
			for(int k = 1; k < 4; k++){
				if(memo[i+1][k] == Integer.MAX_VALUE){
					memo[i+1][k] = -1;
				}
			}
			
			if(memo[i+1][1] == -1 && memo[i+1][2] == -1 && memo[i+1][3] == -1){
				System.out.println("NG " + (i+1));
				result = false;
				break;
			}
		}
		
		if(result){
			int min = Integer.MAX_VALUE;
			for(int k = 1; k < 4; k++){
				if(memo[n][k] != -1){
					int dis = memo[n][k] + ps[n];
					if(dis < min) min = dis;
				}
			}
			System.out.println("OK " + min);
		}
	}
	public static void main(String[] args){
		new Main().run();
	}
}