import java.io.IOException;
import java.util.Scanner;

public class Main{
	public static void main(String args[]) throws IOException {
		Scanner scan = new Scanner(System.in);
		int Ans = 0;
		int N = scan.nextInt();
		int[] P = new int[N];
		
		//標準入力からの格納
		for(int i = 0; i < N;i++) {
			P[i] = scan.nextInt();
		}
		
		for(int i = 0;i <= P[0];i++){
			//左端の処理
			int ans = i;
			
			int nextS = P[0] - i;
			
			//全体の処理
			for(int cursor = 0;cursor < N - 1;cursor++) {
				ans += nextS * 2;
				nextS = P[cursor + 1] - nextS;
				if(nextS < 0) {
					nextS = 0;
				}
			}
			
			//右端の処理
			if(nextS > 0) {
				ans += nextS;
			}
			
			if(i == 0 || Ans > ans) {
				Ans = ans;
			}
		}
		

		System.out.println(Ans);
		
		scan.close();
	}
}
