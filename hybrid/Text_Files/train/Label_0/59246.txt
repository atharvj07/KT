import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (sc.hasNext()) {
			String line = sc.nextLine();
			Scanner scan = new Scanner(line);
			int n = scan.nextInt();
			int s = scan.nextInt();
			if (n == 0)
				break;
			int[] a = new int[n];
			System.out.println(comb(a, 0, 0, s));
		}
	}

	static int comb(int[] a, int b, int ix, int s) {
		if (ix == a.length) {
			// 合計がsになるか？
			int sum = 0;
			for (int i = 0; i < a.length; i++)
				sum += a[i];
			if (sum == s) {
				return 1;
			}
			// なれば 1、そうでなければ 0 と数える
			return 0;
		}
		int sum = 0;
		for (int i = b; i <= 9; i++) {
			a[ix] = i;
			sum += comb(a, a[ix] + 1, ix + 1, s);
		}
		return sum;
	}
}