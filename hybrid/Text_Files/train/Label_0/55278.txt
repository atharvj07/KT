import java.util.Scanner;
public class Main{
	public static void main(String[] args){
		new Main().run();
	}
	int w;
	int h;
	int count;
	short[][] map;
	int[][] dp;
	public void run(){
		Scanner scan = new Scanner(System.in);
		while(scan.hasNext()){
			w = scan.nextInt();
			h = scan.nextInt();
			if(w == 0 && h == 0){
				break;
			}
			map = new short[h][w];
			for(int i = 0;i < h;i++){
				for(int j = 0;j < w;j++){
					map[i][j] = scan.nextShort();
				}
			}
			dp = new int[h+1][w];
			for(int i = 0;i < w;i++){
				if(map[0][i] == 0){
					dp[0][i] = 1;
				}else{
					dp[0][i] = 0;
				}
			}
			for(int i = 1;i < h;i++){
				for(int j = 0;j < w;j++){
					if(map[i][j] == 1){
						dp[i][j] = 0;
					}else if(map[i][j] == 2){
						if(i < h-1){
							dp[i+2][j] += dp[i-1][j] + dp[i][j];
							dp[i][j] = 0;
						}else{
							dp[i][j] += dp[i-1][j];
						}
					}else{
						if(j != 0){
							dp[i][j] += dp[i-1][j-1];
						}
						if(j != w-1){
							dp[i][j] += dp[i-1][j+1];
						}
						dp[i][j] += dp[i-1][j];
					}
				}
			}
			count = 0;
			for(int i = 0;i < w;i++){
				count += dp[h-1][i] + dp[h][i];
			}
			System.out.println(count);
		}
	}
}