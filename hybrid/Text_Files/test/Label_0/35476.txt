import java.util.Scanner;
import java.util.SplittableRandom;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int[][] idx = new int[30][500];
	static SplittableRandom rnd = new SplittableRandom(42);

	public static void main(String[] args) {
		String person = sc.next();
		int[] pos = new int[1000];
		for (int i = 0; i < 1000; i++) {
			pos[i] = i;
		}
		for (int i = 0; i < idx.length; i++) {
			for (int j = 0; j < idx[0].length; j++) {
				int p = rnd.nextInt(1000 - j) + j;
				int tmp = pos[j];
				pos[j] = pos[p];
				pos[p] = tmp;
				idx[i][j] = pos[j];
			}
		}
		if (person.equals("Charlie")) {
			char[] X = sc.next().toCharArray();
			char[] Y = sc.next().toCharArray();
			int[][] parityX = new int[100][30];
			int[][] parityY = new int[100][30];
			for (int i = 0; i < 100; i++) {
				for (int j = 0; j < 30; j++) {
					parityX[i][j] = X[i * 30 + j] - '0';
					parityY[i][j] = Y[i * 30 + j] - '0';
				}
			}
			for (int i = 0; i < 100; i++) {
				char[] s = sc.next().toCharArray();
				int[] d = new int[1000];
				for (int j = 0; j < 1000; j++) {
					d[j] = s[j] - '0';
				}
				int[] parity = new int[30];
				for (int j = 0; j < 30; j++) {
					int sum = 0;
					for (int k = 0; k < 500; k++) {
						sum += d[idx[j][k]];
					}
					parity[j] = sum % 2;
				}
				OUT:
				for (int j = 0; j < 100; j++) {
					for (int k = 0; k < 100; k++) {
						boolean ok = true;
						for (int l = 0; l < 30; l++) {
							if ((parityX[j][l] ^ parityY[k][l]) != parity[l]) {
								ok = false;
								break;
							}
						}
						if (ok) {
							System.out.println((j + 1) + " " + (k + 1));
							break OUT;
						}
					}
				}
			}
		} else {
			char[] ret = new char[3000];
			for (int i = 0; i < 100; i++) {
				char[] s = sc.next().toCharArray();
				int[] d = new int[1000];
				for (int j = 0; j < 1000; j++) {
					d[j] = s[j] - '0';
				}
				for (int j = 0; j < 30; j++) {
					int sum = 0;
					for (int k = 0; k < 500; k++) {
						sum += d[idx[j][k]];
					}
					ret[i * 30 + j] = (char) (sum % 2 + '0');
				}
			}
			System.out.println(String.valueOf(ret));
		}
	}

}
