import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String... args) {
		Scanner scan = new Scanner(System.in);
		int[] a = new int[9];
		for (int i = 0; i < 9; i++) {
			a[i] = scan.nextInt();
		}
		int n = scan.nextInt();
		List<Integer> b = new ArrayList<Integer>();
		for (int i = 0; i < n; i++) {
			b.add(scan.nextInt());
		}

		System.out.println(bingo(a, b) ? "Yes" : "No");
		scan.close();
	}

	private static boolean bingo(int[] a, List<Integer> b) {
		for (int i = 0; i < 3; i++) {
			if (b.contains(a[i * 3]) && b.contains(a[i * 3 + 1]) && b.contains(a[i * 3 + 2])) {
				return true;
			}
		}

		for (int i = 0; i < 3; i++) {
			if (b.contains(a[i]) && b.contains(a[3 + i]) && b.contains(a[6 + i])) {
				return true;
			}
		}

		if (b.contains(a[0]) && b.contains(a[4]) && b.contains(a[8])) {
			return true;
		}

		if (b.contains(a[2]) && b.contains(a[4]) && b.contains(a[6])) {
			return true;
		}

		return false;
	}
}