import java.util.Scanner;

//http://codeforces.com/contest/920/problem/B
public class Tea_Queue {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();
		String result[] = new String[t];
		for (int j = 0; j < t; j++) {
		
			int n = scan.nextInt();
			int l[] = new int[n];
			int r[] = new int[n];
			for (int i = 0; i < n; i++) {
				l[i] = scan.nextInt();
				r[i] = scan.nextInt();
			}

			result[j] = "";

			int time = 1;
			for (int i = 0; i < n; i++) {
				if (time <= r[i] && time >= l[i]) {
					result[j] += (time + " ");
					time++;
				} else if (time > r[i]) {
					result[j] += (0 + " ");
				} else if (time < l[i]) {
					time++;
					i--;
				}
			}
		}

		scan.close();
		for (int i = 0; i < t - 1; i++) {
			System.out.println(result[i]);
		}
		System.out.print(result[t - 1]);
	}
}