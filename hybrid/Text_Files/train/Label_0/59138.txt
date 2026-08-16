import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static boolean[][] pic;
	static int[] count = new int[80000];

	public static void main(String[] args) {
		for (int t = 0;; ++t) {
			int H = sc.nextInt();
			if (H == 0) break;
			pic = new boolean[H + 2][82];
			sc.nextLine();
			for (int i = 0; i < H; ++i) {
				char[] line = sc.nextLine().toCharArray();
				for (int j = 0; j < line.length; ++j) {
					pic[i + 1][j + 1] = line[j] == '*';
				}
			}
			Arrays.fill(count, 0);
			count();
			if (t > 0) System.out.println("----------");
			for (int i = 1; i < count.length; ++i) {
				if (count[i] > 0) {
					System.out.println(i + " " + count[i]);
				}
			}
		}
	}

	static void count() {
		boolean[][] visited = new boolean[pic.length][pic[0].length];
		for (int i = 0; i < pic.length; ++i) {
			for (int j = 0; j < pic[0].length; ++j) {
				if (pic[i][j] && pic[i][j + 1] && !visited[i][j]) {
					int r = j;
					while (true) {
						if (!pic[i][r]) break;
						visited[i][r] = true;
						++r;
					}
					int top = r - j;
					int cy = i;
					int cx = j;
					while (true) {
						if (pic[cy + 1][cx - 1]) {
							--cx;
						} else if (pic[cy + 1][cx]) {
							;
						} else if (pic[cy + 1][cx + 1]) {
							++cx;
						} else {
							break;
						}
						++cy;
						visited[cy][cx] = true;
					}
					int height = cy - i + 1;
					r = cx;
					while (true) {
						if (!pic[cy][r]) break;
						visited[cy][r] = true;
						++r;
					}
					int bottom = r - cx;
					++count[(top + bottom) * height / 2];
				}
			}
		}
	}

}