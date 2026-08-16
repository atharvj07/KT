import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(); // 冷蔵庫
		int b = sc.nextInt(); // 電子レンジ
		int c = sc.nextInt(); // 割引券
		Integer d[] = new Integer[a];
		Integer e[] = new Integer[b];
		int f = 0;

		for (int i = 0; i < a; i++) {
			d[i] = sc.nextInt();
		}
		for (int i = 0; i < b; i++) {
			e[i] = sc.nextInt();
		}
		for (int i = 0; i < c; i++) {
			int l = sc.nextInt() - 1;
			int m = sc.nextInt() - 1;
			int n = sc.nextInt();
			if (i > 0) {
				f = Integer.sum(d[l], e[m]) - n > f ? f
						: Integer.sum(d[l], e[m]) - n;
			} else {
				f = Integer.sum(d[l], e[m]) - n;
			}
		}

		Arrays.sort(d);
		Arrays.sort(e);
		int h = d[0] + e[0];

		System.out.println(f > h ? h : f);

	}
}