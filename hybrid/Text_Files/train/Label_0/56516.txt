import java.util.ArrayList;
import java.util.Scanner;

public class _277_A {
	static int[][] ar;
	static boolean[] check;

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int m = in.nextInt();
		ar = new int[n][n];
		check = new boolean[n];
		int[] lang = new int[m];
		ArrayList[] al = new ArrayList[n];
		for (int i = 0; i < al.length; i++) {
			al[i] = new ArrayList<Integer>();
			int k = in.nextInt();
			for (int j = 0; j < k; j++) {
				int l = in.nextInt() - 1;
				al[i].add(l);
				lang[l] = 1;
			}
		}
		for (int i = 0; i < al.length; i++) {
			for (int j = 0; j < al[i].size(); j++) {
				for (int j2 = i + 1; j2 < al.length; j2++) {
					for (int k = 0; k < al[j2].size(); k++) {
						if (al[i].get(j) == al[j2].get(k)) {
							ar[i][j2] = 1;
							ar[j2][i] = 1;
						}
					}
				}
			}
		}
		int ans = 0;
		boolean b = false;
		for (int i = 0; i < al.length; i++) {
			if (al[i].size() != 0)
				b = true;
			if (!check[i]) {
				dfs(i);
				ans++;
			}
		}

		System.out.println(b ? ans - 1 : ans);

	}

	public static void dfs(int node) {
		check[node] = true;
		for (int i = 0; i < ar.length; i++) {
			if (ar[node][i] == 1 && !check[i])
				dfs(i);
		}
	}
}
