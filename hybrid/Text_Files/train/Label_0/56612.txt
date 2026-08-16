import java.io.*;
import java.util.*;

public class Main {
	
	int[] p, who, where;
	ArrayList<Integer> ans = new ArrayList<>();
	
	void makeSwap(int v, int u) {
		int whoV = who[v];
		int whoU = who[u];
		who[v] = whoU;
		who[u] = whoV;
		where[whoV] = u;
		where[whoU] = v;
	}
	
	void makeQuery(int v) {
		ans.add(v);
		if (v == 0) {
			return;
		}
		
		ArrayList<Integer> path = new ArrayList<>();
		for (int i = v; i > 0; i = p[i]) {
			path.add(i);
		}
		path.add(0);
		Collections.reverse(path);
		for (int i = 0; i < path.size() - 1; i++) {
			makeSwap(path.get(i), path.get(i + 1));
		}
		
//		System.err.println(v);
//		System.err.println(Arrays.toString(who));
	}

	void submit() {
		int n = nextInt();
		p = new int[n];
		who = new int[n];
		where = new int[n];
		int[] depth = new int[n];
		for (int i = 1; i < n; i++) {
			p[i] = nextInt();
			depth[i] = depth[p[i]] + 1;
		}
		
		for (int i = 0; i < n; i++) {
			who[i] = nextInt();
			where[who[i]] = i;
		}
		
		boolean[] dead = new boolean[n];
		while (true) {
			int[] deg = new int[n];
			for (int i = 1; i < n; i++) {
				if (!dead[i]) {
					deg[p[i]]++;
				}
			}
			boolean[] mark = new boolean[n];
			int[] end = new int[n];
			int reds = 0;
			for (int i = 1; i < n; i++) {
				if (!dead[i] && deg[i] == 0) {
					reds++;
					mark[i] = true;
					end[i] = i;
					for (int v = p[i]; v > 0; v = p[v]) {
						if (deg[v] > 1) {
							break;
						}
						reds++;
						mark[v] = true;
						end[v] = i;
					}
				}
			}
//			System.err.println(reds);
			if (reds == 0) {
				break;
			}
			
			boolean[] touch = new boolean[n];
			while (reds > 0) {
				int ball = who[0];
				if (mark[ball]) {
					if (touch[ball]) {
						throw new AssertionError();
					}
					reds--;
					int ins = end[ball];
					while (true) {
						int here = who[ins];
						if (mark[here]) {
							if (!touch[here] || depth[here] < depth[ball]) {
								break;
							}
						} else {
							break;
						}
						ins = p[ins];
					}
					makeQuery(ins);
				} else {
					int target = 0;
					for (int i = 1; i < n; i++) {
						if (!dead[i] && !touch[i] && depth[where[i]] > depth[target]) {
							target = where[i];
						}
					}
					makeQuery(target);
				}
				touch[ball] = true;
			}
			
			for (int i = 0; i < n; i++) {
				dead[i] |= mark[i];
			}
		}
		out.println(ans.size());
		ans.forEach(out::println);
	}

	void preCalc() {

	}

	void stress() {

	}

	void test() {

	}

	Main() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		preCalc();
		submit();
		//stress();
		//test();
		out.close();
	}

	static final Random rng = new Random();

	static int rand(int l, int r) {
		return l + rng.nextInt(r - l + 1);
	}

	public static void main(String[] args) throws IOException {
		new Main();
	}

	BufferedReader br;
	PrintWriter out;
	StringTokenizer st;

	String nextToken() {
		while (st == null || !st.hasMoreTokens()) {
			try {
				st = new StringTokenizer(br.readLine());
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}
		return st.nextToken();
	}

	String nextString() {
		try {
			return br.readLine();
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}

	int nextInt() {
		return Integer.parseInt(nextToken());
	}

	long nextLong() {
		return Long.parseLong(nextToken());
	}

	double nextDouble() {
		return Double.parseDouble(nextToken());
	}
}
