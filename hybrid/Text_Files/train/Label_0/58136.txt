import java.util.Arrays;
import java.util.Scanner;

public class Main {
	Scanner sc = new Scanner(System.in);

	int n;
	int s;
	int[] ans;

	int memo[][];

	int rep(int masked, int answer) {
		if (memo[masked][answer] != -1) {
			return memo[masked][answer];
		}

		int count = 0;
		for (int i = 0; i < n; i++) {
			if ((ans[i] & masked) == answer) {
				count++;
			}
		}
		if (count < 2) {
			memo[masked][answer] = 0;
			return 0;
		}

		int min = 100;

		for (int i = 0; i < s; i++) {
			int shi =  1<<i;
			
			if((masked &shi) != 0){
				continue;
			}
			int z = shi;
			min = Math.min(
					min,
					Math.max(rep(masked | z, answer),
							rep(masked | z, answer | z)));
		}
		memo[masked][answer] = min+1;
		return min+1;
	}

	void run() {
		memo = new int[1 << 11][1 << 11];
		for (;;) {
			s = sc.nextInt();
			n = sc.nextInt();
			if (s + n == 0) {
				break;
			}
			ans = new int[n];

			for (int i = 0; i < n; i++) {
				ans[i] = sc.nextInt(2);
			}

			for (int i = 0; i < 1 << 11; i++) {
				Arrays.fill(memo[i], -1);
			}
			int m = rep(0, 0);

			System.out.println(m);
		}
	}

	public static void main(String[] a) {
		Main aa = new Main();
		aa.run();
	}

}