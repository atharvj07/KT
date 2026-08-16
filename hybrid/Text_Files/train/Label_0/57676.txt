import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO ?????????????????????????????????????????????
		BufferedReader br =
				new BufferedReader(new InputStreamReader(System.in));
		/*
		 * 1 <= i, j < = 5
		 * horiEdge[i][0] = horiEdge[i][5] = '\u0000'
		 * vertEdge[0][j] = vertEdge[5][j] = '\u0000'
		 */
		char[][] horiEdge = new char[6][6];
		char[][] vertEdge = new char[6][6];
		for (int i=1; /* i <= 5 */; i++) {
			char[] data;

			data = br.readLine().toCharArray();
			for (int j=1; j <= 4; j++) {
				horiEdge[i][j] = data[j-1];
			}

			if (i==5) break;

			data = br.readLine().toCharArray();
			for (int j=1; j <= 5; j++) {
				vertEdge[i][j] = data[j-1];
			}
		}

		Wanderer man = new Wanderer();
		StringBuilder ans = new StringBuilder();
		do {
			String temp = man.go(horiEdge, vertEdge);
			ans.append(temp);
		} while ( ! (man.x == 1 && man.y == 1) );

		System.out.println(ans);
	}

	public static final int right = 0;
	public static final int down = 1;
	public static final int left= 2;
	public static final int up = 3;

	public static class Wanderer {
		int x; // coordinate
		int y; // coordinate
		int dir; // direction

		public Wanderer() {
			this.x = 1;
			this.y = 1;
			this.dir = right;
		}

		public String go(char[][] horiEdge, char[][] vertEdge) {
			if (dir == right) {
				x = x+1;
				if (vertEdge[y-1][x] == '1') {
					dir = up;
				} else if (horiEdge[y][x] == '1') {
					dir = right;
				} else if (vertEdge[y][x] == '1') {
					dir = down;
				} else {
					dir = left;
				}
				return "R";
			}

			if (dir == down) {
				y = y+1;
				if (horiEdge[y][x] == '1') {
					dir = right;
				} else if (vertEdge[y][x] == '1') {
					dir = down;
				} else if (horiEdge[y][x-1] == '1') {
					dir = left;
				} else {
					dir = up;
				}
				return "D";
			}

			if (dir == left) {
				x = x-1;
				if (vertEdge[y][x] == '1') {
					dir = down;
				} else if (horiEdge[y][x-1] == '1') {
					dir = left;
				} else if (vertEdge[y-1][x] == '1') {
					dir = up;
				} else {
					dir = right;
				}
				return "L";
			}

			if (dir == up) {
				y = y-1;
				if (horiEdge[y][x-1] == '1') {
					dir = left;
				} else if (vertEdge[y-1][x] == '1') {
					dir = up;
				} else if (horiEdge[y][x] == '1') {
					dir = right;
				} else {
					dir = down;
				}
				return "U";
			}

			return "hoge";
		}
	}
}