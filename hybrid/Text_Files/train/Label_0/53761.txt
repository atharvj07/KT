import java.util.*;
import java.lang.*;
import java.math.*;

public class Main {
	Scanner sc = new Scanner(System.in);

	void run() {
		for (;;) {
			String f = sc.next();
			if (f.equals("#")) {
				break;
			}

			char[][][] dice = new char[6][3][];
			dice[0][0] = f.toCharArray();
			dice[0][1] = sc.next().toCharArray();
			dice[0][2] = sc.next().toCharArray();

			int[] z = { 0, 1, 3, 4, 2, 5 };

			for (int i = 0; i < 6; i++) {
				// z[zinv[i]]= i;
			}
			for (int i = 1; i < 6; i++) {
				for (int j = 0; j < 3; j++) {
					if (i == 5) {
						dice[z[i]][2 - j] = sc.next().toCharArray();
					} else if (i == 2 || i == 3) {
						char temp;
						dice[z[i]][j] = sc.next().toCharArray();
						temp = dice[z[i]][j][0];
						dice[z[i]][j][0] = dice[z[i]][j][2];
						dice[z[i]][j][2] = temp;
					} else {
						dice[z[i]][j] = sc.next().toCharArray();
					}
				}
			}

			boolean ok[][] = new boolean[3][4];

			for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 3; j++) {
					if (dice[i][0][j] == '*') {
						ok[i][0] = true;
					}
				}
				if (ok[i][0]) {
					ok[i][0] = false;
					for (int j = 0; j < 3; j++) {
						if (dice[i + 3][0][j] == '*') {
							ok[i][0] = true;
						}
					}
				} else {
					ok[i][0] = false;
				}
				//
				for (int j = 0; j < 3; j++) {
					if (dice[i][2][j] == '*') {
						ok[i][3] = true;
					}
				}
				if (ok[i][3]) {
					ok[i][3] = false;
					for (int j = 0; j < 3; j++) {
						if (dice[i + 3][2][j] == '*') {
							// System.out.println((i+3)+" "+j);
							ok[i][3] = true;
						}
					}
				} else {
					ok[i][3] = false;
				}
				//
				for (int j = 0; j < 3; j++) {
					if (dice[i][j][0] == '*') {
						ok[i][1] = true;
					}
				}
				if (ok[i][1]) {
					ok[i][1] = false;
					for (int j = 0; j < 3; j++) {
						if (dice[i + 3][j][0] == '*') {
							ok[i][1] = true;
						}
					}
				} else {
					ok[i][1] = false;
				}

				//
				for (int j = 0; j < 3; j++) {
					if (dice[i][j][2] == '*') {
						ok[i][2] = true;
					}
				}
				if (ok[i][2]) {
					ok[i][2] = false;
					for (int j = 0; j < 3; j++) {
						if (dice[i + 3][j][2] == '*') {
							ok[i][2] = true;
						}
					}
				} else {
					ok[i][2] = false;
				}
			}

			int ans[][] = { { 2, 1, 1, 0 }, { 3, 2, 2, 3 }, { 1, 2, 2, 1 } };
			int min = Integer.MAX_VALUE;
			for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 4; j++) {
					if (ok[i][j]) {
						// System.out.println(i+" "+j);
						min = Math.min(ans[i][j], min);
					}
				}
			}
			System.out.println(min);
		}

	}

	public static void main(String[] args) {
		Main m = new Main();
		m.run();
	}
}