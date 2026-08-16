import java.util.Scanner;

public class Main {
	char[][] map;
	int h, w;
	char c;
	
	void run() {
		Scanner scan = new Scanner(System.in);
		while (true) {
			h = scan.nextInt();
			w = scan.nextInt();
			if (w == 0 && h == 0) break;
			map = new char[h][];
			int section = 0;
			scan.nextLine();
			for (int i = 0; i < h; i++)
				map[i] = new char[w];
			for (int y = 0; y < h; y++) {
				String str = scan.nextLine();
				for (int x = 0; x < w; x++) {
					map[y][x] = str.charAt(x);
				}
			}
			for (int y = 0; y < h; y++) {
				for (int x = 0; x < w; x++) {
					if (map[y][x] != 'x') {
						c = map[y][x];
						solve(y, x);
						section++;
					}
				}
			}
			System.out.println(section);
		}
	}
	
	void solve(int y, int x) {
		if (y < 0 || x < 0 || y >= h || x >= w || map[y][x] != c) return;
		map[y][x] = 'x';
		solve(y + 1, x);
		solve(y - 1, x);
		solve(y, x + 1);
		solve(y, x - 1);
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}