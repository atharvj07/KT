import java.util.Scanner;

/**
 * https://abc050.contest.atcoder.jp/tasks/abc050_b
 */
public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = Integer.parseInt(sc.next());
		int[] t = new int[N];
		long sum = 0;
		for(int i=0; i<N; i++){
			t[i] = Integer.parseInt(sc.next());
			sum = sum + t[i];
		}
		int M = Integer.parseInt(sc.next());
		long[] ans = new long[M];
		for(int i=0; i<M; i++){
			int p = Integer.parseInt(sc.next())-1;
			int x = Integer.parseInt(sc.next());
			ans[i] = sum - t[p] + x;
		}
		sc.close();

		for(long a: ans) System.out.println(a);
		
	}

}
