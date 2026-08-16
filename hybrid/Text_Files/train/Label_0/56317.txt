import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		new Main().mainrun();
	}

	Scanner scan;
	int A,B;

	private void mainrun() {
		scan = new Scanner(System.in);
		int N = scan.nextInt();

		for(;N != 0;N = scan.nextInt()) {
			looprun(N);
		}

		scan.close();
	}

	private void looprun(int N) {
		int[][] F = new int[N][N];
		int Ans = 0;
		Integer[] cmin = new Integer[N];
		Integer[] rmax = new Integer[N];

		Arrays.fill(cmin, Integer.MAX_VALUE);
		Arrays.fill(rmax, Integer.MIN_VALUE);

		//初期化&標準入力からの読み込み
		for(int i = 0;i < N;i++) {
			for(int j = 0;j < N;j++) {
				F[i][j] = scan.nextInt();
				cmin[i] = Math.min(cmin[i], F[i][j]);
			}
		}

		for(int i = 0;i < N;i++) {
			for(int j = 0;j < N;j++) {
				rmax[i] = Math.max(rmax[i], F[j][i]);
			}
		}

		for(Integer c : cmin) {
			for(Integer r: rmax) {
				if(c == r) {
					Ans = r;
				}
			}
		}

		System.out.println(Ans);
	}
}
