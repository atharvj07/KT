import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int K = sc.nextInt();
		int a[] = new int[n];
		for (int i = 0; i < n; i++) a[i] = sc.nextInt();
		int DP[] = new int[n];
		for (int i = 0; i < n; i++) DP[i] = (int)1e9;
		DP[0] = 0;
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n && j <= i + K; j++) {
				DP[j] = Math.min(DP[j], DP[i] + Math.abs(a[i] - a[j]));
			}
		}
		System.out.print(DP[n - 1]);
	}

}
