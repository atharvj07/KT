import java.util.Scanner;
import java.lang.Math;
import java.util.ArrayList;
import java.util.List;
//List<Integer> list = new ArrayList<>();

class Main {
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		//int n = stdIn.nextInt();
		//int k = stdIn.nextInt();
		int[] a = new int[3];
		int[] b = new int[3];
		int[] c = new int[4];
		for (int i = 0; i < 3; i++) {
			a[i] = stdIn.nextInt();
			b[i] = stdIn.nextInt();
		}
		for (int i = 1; i < 5; i++) {
			for (int j = 0; j < 3; j++) {
				if (a[j] == i)
					c[i-1] = c[i-1] + 1;
				if (b[j] == i)
					c[i-1] = c[i-1] + 1;
			}
		}
		String s = "YES";
		for (int i = 0; i < 4; i++) {
			if (c[i] % 2 == 1) {
				s = "NO";
				break;
			}
		}
		int d = 0;
		for (int i = 0; i < 4; i++) {
			if (c[i] % 2 == 1)
				d = d + 1;
		}
		if (d == 2)
			s = "YES";

		System.out.println(s);
	}
}