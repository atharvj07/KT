import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int H = sc.nextInt();
		int W = sc.nextInt();
		int[][] field = new int[H][W];
		for (int i = 0; i < H; i++) {
			char[] row = sc.next().toCharArray();
			for (int j = 0; j < W; j++) {
				if (row[j] == '#') {
					field[i][j] = -1;
				} else {
					field[i][j] = row[j] - '1';
				}
			}
		}
		boolean[][][][] visited = new boolean[H][W][6][6];
		visited[0][0][1][2] = true;
		ArrayList<Integer> que = new ArrayList<>();
		que.add(encode(0, 0, 1, 2));
		for (int i = 0; i < que.size(); i++) {
			int cur = que.get(i);
			int r = cur >> 24;
			int c = (cur >> 16) & 0xFF;
			int f = (cur >> 8) & 0xFF;
			int s = (cur >> 0) & 0xFF;
			if (r == H - 1 && c == W - 1) {
				System.out.println("YES");
				return;
			}
			// up
			if (r > 0 && field[r - 1][c] == 5 - f && !visited[r - 1][c][field[r][c]][s]) {
				visited[r - 1][c][field[r][c]][s] = true;
				que.add(encode(r - 1, c, field[r][c], s));
			}
			// down
			if (r < H - 1 && field[r + 1][c] == f && !visited[r + 1][c][5 - field[r][c]][s]) {
				visited[r + 1][c][5 - field[r][c]][s] = true;
				que.add(encode(r + 1, c, 5 - field[r][c], s));
			}
			// left
			if (c > 0 && field[r][c - 1] == 5 - s && !visited[r][c - 1][f][field[r][c]]) {
				visited[r][c - 1][f][field[r][c]] = true;
				que.add(encode(r, c - 1, f, field[r][c]));
			}
			// right
			if (c < W - 1 && field[r][c + 1] == s && !visited[r][c + 1][f][5 - field[r][c]]) {
				visited[r][c + 1][f][5 - field[r][c]] = true;
				que.add(encode(r, c + 1, f, 5 - field[r][c]));
			}
		}
		System.out.println("NO");
	}

	static int encode(int r, int c, int f, int s) {
		return (r << 24) | (c << 16) | (f << 8) | s;
	}

}

