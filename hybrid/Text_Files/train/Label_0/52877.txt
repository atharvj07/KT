
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int r = scan.nextInt();
		int c = scan.nextInt();

		int Arrays[][] = new int[r + 1][c + 1];

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				Arrays[i][j] = scan.nextInt();
			}
		}

		for (int i = 0; i < c; i++) {
			for (int j = 0; j < r; j++) {
				Arrays[j][c] += Arrays[j][i];

			}
		}

		for (int i = 0; i < r; i++) {
			for (int j = 0; j <= c; j++) {
				Arrays[r][j] += Arrays[i][j];
			}
		}



		for (int i = 0; i <= r; i++) {
			for (int j = 0; j <= c; j++) {
				System.out.print(Arrays[i][j]);
				if(j != c) {
					System.out.print(" ");
				}else {

				}
			}
			System.out.println();
		}

		scan.close();
	}

}

