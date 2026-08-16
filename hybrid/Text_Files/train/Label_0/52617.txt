import java.util.LinkedList;
import java.util.Scanner;

public class Main {
	Scanner sc = new Scanner(System.in);
	int kaeruDx[] = { 2, 2, 2, -2, -2, -2, 0, 1, -1, 0, 1, -1 };
	int kaeruDy[] = { 0, 1, -1, 0, 1, -1, 2, 2, 2, -2, -2, -2 };

	void run() {
		for (;;) {
			int w = sc.nextInt();
			int h = sc.nextInt();
			if ((w | h) == 0) {
				return;
			}
			int n = sc.nextInt();
			Pos[] sprin = new Pos[n];
			for (int i = 0; i < n; i++) {
				sprin[i] = new Pos(sc.nextInt(), sc.nextInt());
			}
			LinkedList<Pos> que = new LinkedList<Pos>();
			que.add(new Pos(w, h));
			int sIndex = 0;
			boolean goal = false;
			while (!que.isEmpty()) {
				int size = que.size();
				for (int i = 0; i < size; i++) {
					Pos now = que.poll();
					for (int j = 0; j < 12; j++) {
						int nextW = now.x + kaeruDx[j];
						int nextH = now.y + kaeruDy[j];
						if (inner(nextW, nextH)) {
							Pos sp = sprin[sIndex % n];
							for (int dx = -1; dx <= 1; dx++) {
								for (int dy = -1; dy <= 1; dy++) {
									if (nextW == sp.x + dx && nextH == sp.y + dy) {
										que.add(new Pos(nextW, nextH));
									}
								}
							}
						}
					}
				}
				if (sIndex == n) {
					goal = true;
					break;
				}
				sIndex++;
			}
			System.out.println(goal ? "OK" : "NA");
		}
	}

	class Pos {
		int x;
		int y;

		public Pos(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
	}

	boolean inner(int x, int y) {
		return 0 <= x && x < 10 && 0 <= y && y < 10;
	}

	public static void main(String[] args) {
		new Main().run();
	}
}