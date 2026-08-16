import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n;
		int b[] = new int[10005];
		int length;
		int t[] = new int[10005];

		for (int i = 0; i < 10005; i++) {
			t[i] = i * (i + 1) / 2;
		}

		while (true) {
			n = sc.nextInt();
			if (n == 0) {
				break;
			}

			int sum = 0;
			length = n;
			for (int i = 0; i < n; i++) {
				sum += b[i] = sc.nextInt();
			}
			int f = Arrays.binarySearch(t, sum);

			if (f < 0) {
				System.out.println("-1");
			} else {
				int cnt = 0;
				int id;
				int bottom;
				boolean flag;

				while (true) {
					flag = true;
					for (int i = 0; i < length; i++) {
						if (b[i] != i + 1) {
							flag = false;
						}
					}
					if (flag) {
						break;
					}

					cnt++;
					bottom = length;
					for (int i = 0; i < length; i++) {
						b[i]--;
					}
					int nlen = 0;
					id = 0;
					for (int i = 0; i < length; i++) {
						if (b[i] != 0) {
							b[id] = b[i];
							id++;
							nlen++;
						}
					}
					b[id] = bottom;
					nlen++;
					length = nlen;
					for (int i = 0; i < length; i++) {
						if (b[i] != i + 1) {
							flag = true;
						}
					}
					if (10005 <= cnt) {
						break;
					}
				}
				if (cnt <= 10000) {
					System.out.println(cnt);
				} else {
					System.out.println("-1");
				}
			}
		}
	}
}