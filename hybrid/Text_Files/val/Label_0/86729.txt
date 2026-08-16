

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		String[] s = new String[n];
		for (int i = 0; i < n; i++) {
			s[i] = sc.next();
		}
		int[] ans = new int[4];
		for (int i = 0; i < n; i++) {
			if (s[i].equals("AC"))
				ans[0]++;
			if (s[i].equals("WA"))
				ans[1]++;
			if (s[i].equals("TLE"))
				ans[2]++;
			if (s[i].equals("RE"))
				ans[3]++;
		}

		System.out.println("AC x " + ans[0]);
		System.out.println("WA x " + ans[1]);
		System.out.println("TLE x " + ans[2]);
		System.out.println("RE x " + ans[3]);

	}

}
