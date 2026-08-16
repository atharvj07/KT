import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int N = sc.nextInt();
		int[][] W = new int[N][N];
		int[][] E = new int[N][N];
		boolean[][] F = new boolean[N][N];
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				W[i][j] = sc.nextInt();
			}
		}
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				E[i][j] = sc.nextInt();
			}
		}
		for (int i = 0; i < N; ++i) {
			char[] line = sc.next().toCharArray();
			for (int j = 0; j < N; ++j) {
				F[i][j] = line[j] == 'o';
			}
		}
		MinCostFlow mcf = new MinCostFlow(2 * N + 2);
		for (int i = 0; i < N; ++i) {
			mcf.addEdge(0, i + 1, 0, 1);
			mcf.addEdge(N + 1 + i, 2 * N + 1, 0, 1);
			for (int j = 0; j < N; ++j) {
				int cost = F[i][j] ? 0 : 2 * W[i][j];
				for (int k = 0; k < N; ++k) {
					if (k != j && F[i][k]) cost += E[i][k];
					if (k != i && F[k][j]) cost += E[k][j];
				}
				mcf.addEdge(i + 1, N + 1 + j, cost, 1);
			}
		}
		int flow = mcf.calc(N);
		System.out.println(flow / 2);
		ArrayList<Integer> op = new ArrayList<Integer>();
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if (mcf.cap[i + 1][N + 1 + j] == 0) {
					if (!F[i][j]) op.add((i << 8) + j);
				} else {
					if (F[i][j]) op.add((i << 8) + j);
				}
			}
		}
		System.out.println(op.size());
		for (int p : op) {
			int r = p >> 8;
			int c = p & 0xFF;
			System.out.println((r+1) + " " + (c+1) + " " + (F[r][c] ? "erase" : "write"));
		}
	}

	static class MinCostFlow {
		int size;
		int[][] cost;
		int[][] cap;

		MinCostFlow(int size) {
			this.size = size;
			cost = new int[size][size];
			cap = new int[size][size];
		}

		void addEdge(int from, int to, int c, int capacity) {
			cost[from][to] = c;
			cap[from][to] = capacity;
			cost[to][from] = -c;
		}

		int calc(int flow) {
			final int INF = 1 << 25;
			int total = 0;
			int[] h = new int[size];
			Arrays.fill(h, 0);
			int[] prev = new int[size];
			while (flow > 0) {
				int[] dist = new int[size];
				Arrays.fill(dist, INF);
				dist[0] = 0;
				PriorityQueue<State> q = new PriorityQueue<State>();
				q.add(new State(0, dist[0]));
				while (!q.isEmpty()) {
					State st = q.poll();
					if (st.cost > dist[st.v]) continue;
					for (int i = 0; i < size; ++i) {
						if (cap[st.v][i] == 0) continue;
						int nCost = dist[st.v] + cost[st.v][i] + h[st.v] - h[i];
						if (dist[i] > nCost) {
							dist[i] = nCost;
							q.add(new State(i, nCost));
							prev[i] = st.v;
						}
					}
				}
				if (dist[size - 1] == INF) break;
				for (int i = 0; i < size; ++i) {
					h[i] += dist[i];
				}
				int f = Integer.MAX_VALUE;
				for (int pos = size - 1; pos != 0; pos = prev[pos]) {
					f = Math.min(f, cap[prev[pos]][pos]);
				}
				for (int pos = size - 1; pos != 0; pos = prev[pos]) {
					cap[prev[pos]][pos] -= f;
					cap[pos][prev[pos]] += f;
				}
				total += h[size - 1] * f;
				flow -= f;
			}
			return total;
		}

		static class State implements Comparable<State> {
			int v;
			int cost;

			public State(int v, int cost) {
				this.v = v;
				this.cost = cost;
			}

			public int compareTo(State o) {
				return this.cost - o.cost;
			}
		}
	}

}