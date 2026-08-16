import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int a[][];

		while (true) {
			String s = sc.next();
			if (s.equals("0")) {
				break;
			}
			a = new int[3][3];
			for (int i = 0; i < 3; i++) {
				a[0][i] = s.charAt(i);
			}
			for (int i = 1; i < 3; i++) {
				s = sc.next();
				for (int j = 0; j < 3; j++) {
					a[i][j] = s.charAt(j);
				}
			}
			if (
					(a[0][0] == 'b' && a[0][1] == 'b' && a[0][2] == 'b') ||
					(a[1][0] == 'b' && a[1][1] == 'b' && a[1][2] == 'b') ||
					(a[2][0] == 'b' && a[2][1] == 'b' && a[2][2] == 'b') ||
					(a[0][0] == 'b' && a[1][0] == 'b' && a[2][0] == 'b') ||
					(a[0][1] == 'b' && a[1][1] == 'b' && a[2][1] == 'b') ||
					(a[0][2] == 'b' && a[1][2] == 'b' && a[2][2] == 'b') ||
					(a[0][0] == 'b' && a[1][1] == 'b' && a[2][2] == 'b') ||
					(a[0][2] == 'b' && a[1][1] == 'b' && a[2][0] == 'b')) {
				System.out.println("b");
			} else if (
					(a[0][0] == 'w' && a[0][1] == 'w' && a[0][2] == 'w') ||
					(a[1][0] == 'w' && a[1][1] == 'w' && a[1][2] == 'w') ||
					(a[2][0] == 'w' && a[2][1] == 'w' && a[2][2] == 'w') ||
					(a[0][0] == 'w' && a[1][0] == 'w' && a[2][0] == 'w') ||
					(a[0][1] == 'w' && a[1][1] == 'w' && a[2][1] == 'w') ||
					(a[0][2] == 'w' && a[1][2] == 'w' && a[2][2] == 'w') ||
					(a[0][0] == 'w' && a[1][1] == 'w' && a[2][2] == 'w') ||
					(a[0][2] == 'w' && a[1][1] == 'w' && a[2][0] == 'w')) {
				System.out.println("w");
			} else {
				System.out.println("NA");
			}
		}
	}
}