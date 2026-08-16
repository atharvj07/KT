import java.util.ArrayDeque;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);
	static int N, E;
	static boolean[][] g;

	public static void main(String[] args) {
		N = sc.nextInt();
		g = new boolean[N][N];
		E = 0;
		for (int i = 0; i < N; ++i) {
			char[] row = sc.next().toCharArray();
			for (int j = 0; j < N; ++j) {
				g[i][j] = row[j] == 'Y';
				if (g[i][j]) ++E;
			}
		}
		E /= 2;
		System.out.println(solve() ? "Taro" : "Hanako");
	}

	static boolean solve() {
		if (N % 2 == 1) {
			return ((N * (N - 1)) / 2 - E) % 2 != 0;
		}
		if (E == 0) return false;
		boolean[] visited = new boolean[N];
		int ec = 0;
		int oc = 0;
		for (int i = 0; i < N; ++i) {
			if (visited[i]) continue;
			int count = 1;
			visited[i] = true;
			ArrayDeque<Integer> q = new ArrayDeque<Integer>();
			q.add(i);
			while (!q.isEmpty()) {
				int pos = q.poll();
				for (int j = 0; j < N; ++j) {
					if (!visited[j] && g[pos][j]) {
						++count;
						q.add(j);
						visited[j] = true;
					}
				}
			}
			if (count % 2 == 0) {
				++ec;
			} else {
				++oc;
			}
		}
		boolean taroEven = ((N * (N - 1)) / 2 - E) % 2 != 0;
		if (taroEven) {
			int turnTaro = ((ec + oc) - 1) / 2;
			return oc <= turnTaro * 2;
		} else {
			int turnHanako = ((ec + oc) - 2) / 2;
			return !(oc <= turnHanako * 2);
		}
	}

}