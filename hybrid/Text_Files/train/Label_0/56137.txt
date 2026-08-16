import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

/**
 * 解説通りに作成したソースコード
 */
public class Main {

	public static void main(String[] args) {
		try (Scanner scanner = new Scanner(System.in)) {
			int n = scanner.nextInt(), m = scanner.nextInt(), q = scanner.nextInt();
			int[][] x = new int[n + 1][n + 1], c = new int[n + 1][n + 1];
			IntStream.range(0, n + 1).forEach(i -> Arrays.fill(x[i], 0));
			IntStream.range(0, m).forEach(i -> x[scanner.nextInt()][scanner.nextInt()]++);
			Arrays.fill(c[0], 0);
			IntStream.rangeClosed(1, n).forEach(i -> c[i][0] = 0);
			IntStream.rangeClosed(1, n)
					.forEach(i -> IntStream.rangeClosed(1, n).forEach(j -> c[i][j] = c[i][j - 1] + x[i][j]));
			IntStream.range(0, q).forEach(i -> {
				int l = scanner.nextInt(), r = scanner.nextInt();
				System.out.println(IntStream.rangeClosed(l, r).map(j -> c[j][r] - c[j][l - 1]).sum());
			});
		}
	}
}
