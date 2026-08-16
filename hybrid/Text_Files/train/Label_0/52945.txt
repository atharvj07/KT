import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int H = sc.nextInt();
		int W = sc.nextInt();
		char[][] charArr = new char[H][W];
		String str;

		for (int i = 0; i < H; i++) {
			str = sc.next();
			for (int j = 0; j < W; j++) {
				charArr[i][j] = str.charAt(j);
			}
		}

		List<Integer> mRowPos = new ArrayList<>();
		List<Integer> mColPos = new ArrayList<>();
		boolean match;

		for (int i = 0; i < H; i++) {
			match = false;
			for (int j = 0; j < W; j++) {
				if (charArr[i][j] == '.') {
					match = true;
				} else {
					match = false;
					break;
				}
			}
			if (match == true) {
				mRowPos.add(i);
			}
		}

		for (int j = 0; j < W; j++) {
			match = false;
			for (int i = 0; i < H; i++) {
				if (charArr[i][j] == '.') {
					match = true;
				} else {
					match = false;
					break;
				}
			}
			if (match == true) {
				mColPos.add(j);
			}
		}
		
		for (int i = 0; i < H; i++) {
			if (mRowPos.contains(i)) {
				continue;
			}
			for (int j = 0; j < W; j++) {
				if (!mColPos.contains(j)) {
					System.out.print(charArr[i][j]);
				}
			}
			System.out.println();
		}
	}
}