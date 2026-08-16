import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static ArrayList<ArrayList<Integer>> g = new ArrayList<>();

	public static void main(String[] args) {
		int N = sc.nextInt();
		for (int i = 0; i < N; i++) {
			g.add(new ArrayList<>());
		}
		for (int i = 0; i < N - 1; i++) {
			int u = Integer.parseInt(sc.next()) - 1;
			int v = Integer.parseInt(sc.next()) - 1;
			g.get(u).add(v);
			g.get(v).add(u);
		}
		int[] parent = new int[N];
		Arrays.fill(parent, -1);
		ArrayList<Integer> q = new ArrayList<>();
		q.add(0);
		for (int i = 0; i < N; i++) {
			int cur = q.get(i);
			for (int adj : g.get(cur)) {
				if (adj == parent[cur]) continue;
				parent[adj] = cur;
				q.add(adj);
			}
		}
		int maxInvalid = 0;
		int[] len = new int[N];
		int[] lenDown = new int[N];
		for (int i = N - 1; i >= 0; i--) {
			int cur = q.get(i);
			for (int adj : g.get(cur)) {
				if (adj == parent[cur]) continue;
				len[cur] = Math.max(len[cur], len[adj]);
			}
			len[cur] += 1;
		}
		for (int i = 0; i < N; i++) {
			int cur = q.get(i);
			int[] maxLeft = new int[g.get(cur).size() + 1];
			maxLeft[0] = lenDown[cur];
			for (int j = 0; j < g.get(cur).size(); j++) {
				int adj = g.get(cur).get(j);
				maxLeft[j + 1] = Math.max(maxLeft[j], adj == parent[cur] ? 0 : len[adj]);
			}
			int maxRight = 0;
			for (int j = g.get(cur).size() - 1; j >= 0; j--) {
				int adj = g.get(cur).get(j);
				if (adj == parent[cur]) continue;
				lenDown[adj] = Math.max(maxLeft[j], maxRight) + 1;
				maxRight = Math.max(maxRight, len[adj]);
			}
			if (g.get(cur).size() >= 3) {
				ArrayList<Integer> lens = new ArrayList<>();
				lens.add(lenDown[cur]);
				for (int adj : g.get(cur)) {
					if (adj == parent[cur]) continue;
					lens.add(len[adj]);
				}
				Collections.sort(lens);
				int len0 = lens.get(lens.size() - 1);
				int len1 = lens.get(lens.size() - 2);
				int len2 = lens.get(lens.size() - 3);
				maxInvalid = Math.max(maxInvalid, len0);
				if (len0 == len2) {
					maxInvalid = Math.max(maxInvalid, len0 + len2 - 1);
				} else {
					maxInvalid = Math.max(maxInvalid, len0 + len2);
				}
			}
		}
		char[] ans = new char[N];
		Arrays.fill(ans, '1');
		for (int i = 3; i <= maxInvalid; i++) {
			ans[i - 1] = '0';
		}
		System.out.println(String.valueOf(ans));
	}

}

