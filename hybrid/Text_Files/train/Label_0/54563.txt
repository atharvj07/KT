import java.awt.Point;
import java.util.Scanner;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) throws java.io.IOException {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		while (true) {
			int m = sc.nextInt();
			int n = sc.nextInt();
			if ((n | m) == 0)
				break;
			Point pos = new Point(1, 1);
			int d = 0;
			boolean flag = true;
			while (flag) {
				String tmp = sc.next();
				char c = tmp.toCharArray()[0];
				switch (c) {
				case 'F':
					int f = sc.nextInt();
					switch (d) {
					case 0:
						for (int i = 0; i < f; i++) {
							int ny = pos.y + 1;
							if (ny <= n)
								pos.y++;
							else
								break;
						}
						break;
					case 1:
						for (int i = 0; i < f; i++) {
							int nx = pos.x + 1;
							if (nx <= m)
								pos.x++;
							else
								break;
						}
						break;
					case 2:
						for (int i = 0; i < f; i++) {
							int ny = pos.y - 1;
							if (ny > 0)
								pos.y--;
							else
								break;
						}
						break;
					case 3:
						for (int i = 0; i < f; i++) {
							int nx = pos.x - 1;
							if (nx > 0)
								pos.x--;
							else
								break;
						}
						break;
					}
					break;

				case 'B':
					int b = sc.nextInt();
					switch (d) {
					case 0:
						for (int i = 0; i < b; i++) {
							int ny = pos.y - 1;
							if (ny > 0)
								pos.y--;
							else
								break;
						}
						break;
					case 1:
						for (int i = 0; i < b; i++) {
							int nx = pos.x - 1;
							if (nx > 0)
								pos.x--;
							else
								break;
						}
						break;
					case 2:
						for (int i = 0; i < b; i++) {
							int ny = pos.y + 1;
							if (ny <= n)
								pos.y++;
							else
								break;
						}
						break;
					case 3:
						for (int i = 0; i < b; i++) {
							int nx = pos.x + 1;
							if (nx <= m)
								pos.x++;
							else
								break;
						}
						break;
					}
					break;
				case 'R':
					d = (d + 1) % 4;
					break;
				case 'L':
					d = (d + 3) % 4;
					break;
				case 'S':
					flag = false;
					break;
				}
			}
			System.out.println(pos.x + " " + pos.y);
		}
	}

}