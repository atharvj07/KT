import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();

		int[] seq = new int[N];
		int[] run = new int[M];

		for (int i = 0; i < seq.length; i++) {
			seq[i] = sc.nextInt();
		}

		for (int i = 0; i < run.length; i++) {
			run[i] = sc.nextInt();
		}
		sc.close();

		int zero = swap(seq.clone(), run, 0);
		int one = swap(seq.clone(), run, 1);
		System.out.println(Math.min(zero, one));

	}

	static int swap(int[] clone, int[] run, int now) {
		int swapNum = 0;
		int k = 0;
		for (int i = 0; i < run.length; i++) {
			for (int j = 0; j < run[i]; j++) {
				if (clone[k] != now) {
					if (k == clone.length - 1) {
						return Integer.MAX_VALUE;
					}
					for (int l = k + 1; l < clone.length; l++) {
						if (clone[l] == now) {
							int tmp = clone[l];
							clone[l] = clone[k];
							clone[k] = tmp;

							swapNum += l - k;
							break;
						}
						if (l == clone.length - 1) {
							return Integer.MAX_VALUE;
						}
					}
				}

				k++;
			}
			now = (now + 1) % 2;
		}
		return swapNum;
	}
}