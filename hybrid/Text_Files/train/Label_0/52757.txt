import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {

	Scanner sc;

	Main() {
		sc = new Scanner(System.in);
	}

	void run() {
		boolean p[] = new boolean[30001];

		Arrays.fill(p, true);

		p[0] = false;
		p[1] = false;
		LinkedList<Integer> pr = new LinkedList<Integer>();

		int dp[] = new int[30001];

		for (int i = 2; i * i < 30001; i++) {
			if (p[i]) {
				for (int j = i + i; j < 30001; j = j + i) {
					p[j] = false;
				}
			}
		}
		int pm[] = new int[3333];
		int ind = 0;
		for (int i = 0; i < 30001; i++) {
			if (p[i]) {
				pm[ind++] = i;
			}
		}
//		System.out.println(Arrays.toString(pm));
		for (int i = 0; pm[i]!=0; i++) {
			int pi = pm[i];
			for (int j = i; pm[j]!=0; j++) {
				int pj = pm[j];
				if (pi + pj > 30000) {
					break;
				}
				for (int k = j; pm[k]!=0; k++) {
					int pk = pm[k];
					if (pi + pj <= pk) {
						break;
					}
					if(pi+pj+pk>30000){
						break;
					}
//					System.out.println(pi+" "+pj+" "+ pk +" " + (pi + pj + pk));
					dp[pi + pj + pk]++;
				}
			}
		}

		for (;;) {
			int t = sc.nextInt();

			if (t == 0) {
				break;
			}
			System.out.println(dp[t]);
		}
	}

	public static void main(String[] args) {
		Main m = new Main();
		m.run();
	}

}