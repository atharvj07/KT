import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int ans = 0;
	static ArrayList<ArrayList<Integer>> g;
	static int x;

	public static void main(String[] args) throws Exception {
		while (true) {
			x = sc.nextInt();
			int y = sc.nextInt();
			if (x == 0 && y == 0) break;
			g = new ArrayList<ArrayList<Integer>>();
			for (int i = 0; i < x; ++i) {
				g.add(new ArrayList<Integer>());
			}
			for (int i = 0; i < y; ++i) {
				int f = sc.nextInt();
				int t = sc.nextInt();
				g.get(f).add(t);
				g.get(t).add(f);
			}
			ans = x;
			int[] cover = new int[x];
			dfs(0, cover, 0);
			System.out.println(ans);
		}
	}

	static void dfs(int cur, int[] cover, int use) {
		if (use >= ans) return;
		if (cur == x) {
			for (int i = 0; i < x; ++i) {
				if (cover[i] == 0) return;
			}
			ans = use;
			return;
		}
		dfs(cur + 1, cover, use);
		for (int i = 0; i < g.get(cur).size(); ++i) {
			++cover[g.get(cur).get(i)];
		}
		++cover[cur];
		dfs(cur + 1, cover, use + 1);
		--cover[cur];
		for (int i = 0; i < g.get(cur).size(); ++i) {
			--cover[g.get(cur).get(i)];
		}
	}

}