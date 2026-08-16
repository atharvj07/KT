
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Main main = new Main();
		main.run();
	}

	long MOD = 1000000007;

	public void run() {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		int x[] = new int[n];
		for(int i=0; i<n; i++) {
			x[i]=sc.nextInt();
		}

		int y[] = new int[m];
		for(int i=0; i<m; i++) {
			y[i]=sc.nextInt();
		}

		long xx = 0;
		for(int k=0; k<n; k++) {

			xx += ((2*k-n+1) * (long)x[k]) % MOD;
			xx %= MOD;
			//xx = xx + (((2 * k  + n  + 1) * x[k]) % MOD) % MOD;
		}

		long yy = 0;
		for(int k=0; k<m; k++) {

			yy += ((2*k-m+1) * (long)y[k]) % MOD;
			yy %= MOD;
			//yy = yy + (((2*k-m-1) * y[k]) % MOD) % MOD;
		}

		System.out.println((xx * yy) % MOD);
		sc.close();
	}

}


