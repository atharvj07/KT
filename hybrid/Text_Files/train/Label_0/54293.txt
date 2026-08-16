import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int H = sc.nextInt();
		int W = sc.nextInt();
		int[] left = new int[H];
		int[] right = new int[H];
		Arrays.fill(left, -1);
		Arrays.fill(right, -1);
		for (int i = 0; i < H; i++) {
			char[] row = sc.next().toCharArray();
			for (int j = 0; j < W; j++) {
				if (row[j] == 'B') {
					if (left[i] == -1) left[i] = j;
					right[i] = j;
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < H; i++) {
			if (left[i] == -1) continue;
			for (int j = i; j < H; j++) {
				if (left[j] == -1) continue;
				ans = Math.max(ans, j - i + Math.abs(left[i] - right[j]));
				ans = Math.max(ans, j - i + Math.abs(right[i] - left[j]));
			}
		}
		System.out.println(ans);
	}

}

