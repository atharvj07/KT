import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		while (true) {
			int P = sc.nextInt();
			if (P == 0) break;
			int Q = sc.nextInt();
			sc.nextLine();
			int[] depth = new int[3];
			int[][] indent = new int[P][4];
			for (int i = 0; i < P; ++i) {
				char[] line = sc.nextLine().toCharArray();
				indent[i][0] = depth[0];
				indent[i][1] = depth[1];
				indent[i][2] = depth[2];
				for (int j = 0;; ++j) {
					if (line[j] != '.') {
						indent[i][3] = j;
						break;
					}
				}
				update(line, depth);
			}
			ArrayList<Amount> list = new ArrayList<Amount>();
			for (int R = 1; R <= 20; ++R) {
				for (int C = 1; C <= 20; ++C) {
					for (int S = 1; S <= 20; ++S) {
						boolean match = true;
						for (int i = 0; i < P; ++i) {
							if (indent[i][0] * R + indent[i][1] * C + indent[i][2] * S != indent[i][3]) {
								match = false;
								break;
							}
						}
						if (match) {
							list.add(new Amount(R, C, S));
						}
					}
				}
			}
			for (int i = 0; i < Q; ++i) {
				char[] line = sc.nextLine().toCharArray();
				int ans = -999;
				for (Amount a : list) {
					int c = a.a[0] * depth[0] + a.a[1] * depth[1] + a.a[2] * depth[2];
					if (ans > 0 && ans != c) {
						ans = -999;
						break;
					}
					ans = c;
				}
				System.out.print((i != 0 ? " " : "") + (ans < 0 ? -1 : ans));
				update(line, depth);
			}
			System.out.println();
		}
	}

	static void update(char[] line, int[] depth) {
		for (int i = 0; i < line.length; ++i) {
			switch (line[i]) {
			case '(':
				depth[0]++;
				break;
			case '{':
				depth[1]++;
				break;
			case '[':
				depth[2]++;
				break;
			case ')':
				depth[0]--;
				break;
			case '}':
				depth[1]--;
				break;
			case ']':
				depth[2]--;
				break;
			}
		}
	}

	static class Amount {
		int[] a = new int[3];

		Amount(int R, int C, int S) {
			a[0] = R;
			a[1] = C;
			a[2] = S;
		}
	}

}