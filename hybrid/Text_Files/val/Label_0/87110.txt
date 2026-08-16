import java.util.Arrays;
import java.util.BitSet;
import java.util.Scanner;

public class Main {
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int x = in.nextInt();
		int y = in.nextInt();
		final int os = 301;
		final int U = 603+os;
		final int F= 603+os;
		int[][] dp = new int[U][F];
		final int inf = -Integer.MAX_VALUE;
		int[][] newdp = new int[U][F];
		for(int j=0; j<U; j++)
			Arrays.fill(dp[j], inf);
		dp[x+os][y+os] = 0;
		for(int i=0; i<n; i++){
//			for(int j=0; j<U; j++)
//				Arrays.fill(newdp[j], inf);
			int a = in.nextInt();
			int b = in.nextInt();
			int c = in.nextInt();
			int d = in.nextInt();
			for(int j=0; j<U; j++){
				for(int k=0; k<F; k++){
					newdp[j][k] = dp[j][k];
				}
			}
			for(int j=-os; j<U-os; j++){
				for(int k=-os; k<F-os; k++){
					if(j+os>=U || k+os>=F || dp[j+os][k+os]==inf) continue;
					newdp[j-a+os][k+b+os] = Math.max(newdp[j-a+os][k+b+os], dp[j+os][k+os]);
					newdp[j+os][k-c+os] = Math.max(newdp[j+os][k-c+os], dp[j+os][k+os]+d);
				}
			}
			for(int j=0; j<U; j++){
				for(int k=0; k<F; k++){
					dp[j][k] = newdp[j][k];
				}
			}
//			for(int j=-10; j<=20; j++){
//				for(int k=-10; k<=20; k++){
//					System.out.printf("%18s",j+":"+k+":"+dp[j+os][k+os]+"\t");
//				}
//				System.out.println();
//			}
//			System.out.println();
		}
		int max = 0;
		for(int i=os; i<U; i++){
			for(int j=os; j<F; j++){
				max = Math.max(dp[i][j], max);
			}
		}
		System.out.println(max);
	}
}