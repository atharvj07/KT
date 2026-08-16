import java.text.CollationElementIterator;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {

	static int[][] map;
	static int[][] directions8 = { { -1, -1 }, { -1, 0 }, { -1, 1 }, { 0, -1 }, { 0, 1 }, { 1, -1 }, { 1, 0 },
			{ 1, 1 } };
	static int[][] directions4 = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
	static int ans;
	static int[][] puyo;
	static int H;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		while (true) {

			H = sc.nextInt();

			if (H == 0) {
				break;
			}

			puyo = new int[H][5];

			for (int i = 0; i < H; i++) {
				for (int j = 0; j < 5; j++) {
					puyo[i][j] = sc.nextInt();
				}
			}
			ans = 0;
			int tmpAns = -1;
			while (ans != tmpAns) {
				tmpAns = ans;
				// 各行を見る
				for (int i = 0; i < H; i++) {

					// それぞれの開始列
					for (int j = 0; j <= 2; j++) {
						if (puyo[i][j] == 0) {
							continue;
						}
						int samePuyos = 1;
						// 後の数字と比べる
						for (int k = j + 1; k < 5; k++) {
							if (puyo[i][j] == puyo[i][k]) {
								samePuyos++;
							}
							if (puyo[i][j] != puyo[i][k] || k == 4) {
								if (samePuyos > 2) {
									ans += puyo[i][j] * samePuyos;
									for (int l = j; l < j + samePuyos; l++) {
										// 消えたぷよを0にする
										puyo[i][l] = 0;
									}
								}
								break;
							}
						}
					}
				}
				puyoFall();
			}

			System.out.println(ans);
		}

	}

	static void puyoFall() {
		for (int k = 0; k < H; k++) {
			for (int i = H - 1; i > 0; i--) {
				for (int j = 0; j < 5; j++) {
					if (puyo[i][j] == 0) {
						puyo[i][j] = puyo[i - 1][j];
						puyo[i - 1][j] = 0;
					}
				}
			}
		}
	}

	static int getNum(List<Integer> column, int idx, int count) {
		if (column.get(count) != 0) {
			idx--;
		}

		if (idx == -1 || column.get(count) == -1) {
			return column.get(count);
		}
		count++;
		return getNum(column, idx, count);
	}

	// BFS用に二つの配列を足し算する
	static int[] addArrayElms(int[] a, int[] b) {
		int[] c = new int[a.length];
		for (int i = 0; i < a.length; i++) {
			c[i] = a[i] + b[i];
		}
		return c;
	}

	// //二分探索
	// k <= num となる最小の配列要素kのインデックスを返す
	static private int binarySearch(long num, long[] orderedArray) {
		int lowerBorder = -1;
		int upperBorder = orderedArray.length;
		int mid;

		while (upperBorder - lowerBorder > 1) {
			mid = (upperBorder + lowerBorder) / 2;
			if (orderedArray[mid] <= num) {
				lowerBorder = mid;
			} else {
				upperBorder = mid;
			}
		}
		return lowerBorder;
	}

	// 二分探索
	// k <= num となる最小のList要素kのインデックスを返す
	static private int binarySearch(long num, ArrayList<Long> orderedList) {
		int lowerBorder = -1;
		int upperBorder = orderedList.size();
		int mid;

		while (upperBorder - lowerBorder > 1) {
			mid = (upperBorder + lowerBorder) / 2;
			if (orderedList.get(mid) <= num) {
				lowerBorder = mid;
			} else {
				upperBorder = mid;
			}
		}
		return lowerBorder;
	}

	// aとbの最小公倍数を求める
	public static int gcd(int a, int b) {
		return b == 0 ? a : gcd(b, a % b);
	}

	public static long gcd(long a, long b) {
		return b == 0 ? a : gcd(b, a % b);
	}
}

