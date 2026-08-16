import java.util.ArrayList;
import java.util.Arrays;
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
		long[] value = new long[N];
		for (int i = 0; i < N; i++) {
			value[i] = Integer.parseInt(sc.next());
		}
		for (int i = 0; i < N; i++) {
			value[i] -= Integer.parseInt(sc.next());
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
		long[] sum = new long[N];
		for (int i = N - 1; i >= 0; i--) {
			int cur = q.get(i);
			sum[cur] = value[cur];
			for (int adj : g.get(cur)) {
				if (adj == parent[cur]) continue;
				sum[cur] += sum[adj];
			}
		}
		boolean[] visited = new boolean[N];
		int[] bfs = new int[N];
		bfs[0] = q.get(N - 1);
		visited[bfs[0]] = true;
		long[] count = new long[N];
		for (int i = 0, qi = 1; i < N; i++) {
			int cur = bfs[i];
			for (int adj : g.get(cur)) {
				if (visited[adj]) continue;
				if (adj == parent[cur]) {
					count[adj] = count[cur] - sum[cur];
				} else {
					count[adj] = count[cur] + sum[adj];
				}
				bfs[qi++] = adj;
				visited[adj] = true;
			}
		}
		long ans = 0;
		long min = 0;
		for (int i = 0; i < N; i++) {
			ans += count[i];
			min = Math.min(min, count[i]);
		}
		ans += -min * N;
		System.out.println(ans);
	}

}

