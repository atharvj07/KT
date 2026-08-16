import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();

		// A:値を保存する主配列
		// B:累積和を表現する副配列
		int[] A = new int[N + 1];
		int[] B = new int[N + 1];

		// Aの要素に入力を代入
		for (int i = 0; i < N; i++) {
			int a = sc.nextInt();
			A[i] = a;
		}
		
		// K回の試行を行う主反復
		for (int i = 0; i < Math.min(K, 42); i++) {
			/* 解法
			 * 長さNの配列について累積和を計算。それぞれの加算範囲はAのn番目の要素ajについてn-aj~n+ajの範囲
			 * 配列外参照に注意
			 */
			// Bを初期化
			Arrays.fill(B, 0);
			for (int j = 0; j < N; j++) {
				// j番目の要素について、それぞれの始点、終点を記録。配列範囲より大きければ0もしくはNを指定
				// j - ajを始点とすると
				int start = Math.max(0, j - A[j]);
				// j + aj - 1が終点となる(終わりをふくむため)
				int end = Math.min(N, j + A[j] + 1);
				//始点を+1、終点を-1
				B[start]++;
				B[end]--;
			}
			for (int j = 1; j < N; j++) {
				// Bを順に加算していく
				B[j] += B[j - 1];
			}
			// Bの値をAとする
			A = B.clone();
		}

		// 出力
		for (int i = 0; i < N; i++) {
			System.out.print(A[i] + (i < N - 1 ? " " : "\n"));
		}
	}
}