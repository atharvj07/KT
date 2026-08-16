
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class D {
	static int[] vals;

	static class Pair implements Comparable<Pair> {
		int node, idx;

		public Pair(int n, int i) {
			node = n;
			idx = i;
		}

		public int compareTo(Pair p) {
			return new Integer(vals[idx]).compareTo(vals[p.idx]);
		}
	}

	public static void main(String[] args) throws Exception {
		int nodeCnt = nextInt();
		int d = nextInt();
		int[] gain = new int[nodeCnt];
		for (int i = 1; i < nodeCnt - 1; i++) {
			gain[i] = nextInt();
		}
		int[][] pos = new int[nodeCnt][2];
		for (int i = 0; i < nodeCnt; i++) {
			pos[i][0] = nextInt();
			pos[i][1] = nextInt();
		}
		int[][] dist = new int[nodeCnt][nodeCnt];
		int max = -1;
		for (int i = 0; i < nodeCnt; i++) {
			for (int j = i + 1; j < nodeCnt; j++) {
				dist[i][j] = (Math.abs(pos[j][0] - pos[i][0]) + Math
						.abs(pos[j][1] - pos[i][1])) * d;
				dist[j][i] = dist[i][j];
				max = Math.max(max, dist[i][j]);
			}
		}
		int l = 0, h = max * (nodeCnt - 1) + 1, mid;
		while (l < h) {
			mid = l + (h - l) / 2;
			boolean valid = false;
			int[] lastVis=new int[nodeCnt];
			Arrays.fill(lastVis, -1);
//			boolean[][] vis = new boolean[nodeCnt][200000];
			HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
			vals = new int[200000];
			int idx = 0;
			PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
			map.put(mid, 0);
			vals[idx++] = mid;
			pq.add(new Pair(0, 0));
			while (!pq.isEmpty()) {
				Pair tmp = pq.remove();
				if (lastVis[tmp.node]>=vals[tmp.idx])
					continue;
				if (tmp.node == nodeCnt - 1) {
					valid = true;
					break;
				}
				lastVis[tmp.node]=vals[tmp.idx];
				int curVal = vals[tmp.idx];
				for (int i = 0; i < nodeCnt; i++) {
					if (i != tmp.node) {
						int req = dist[tmp.node][i];
						if (req <= curVal) {
							int newVal = curVal - req + gain[i];
							int nIdx = -1;
							if (map.containsKey(newVal)) {
								nIdx = map.get(newVal);
							} else {
								map.put(newVal, idx);
								nIdx = idx;
								vals[idx++] = newVal;
							}
							if (lastVis[i]<newVal) {
								pq.add(new Pair(i, nIdx));
							}
						}
					}
				}
			}
			if (!valid) {
				l = mid + 1;
			} else {
				h = mid;
			}
		}
		System.out.println(l);
	}

	static BufferedReader br = new BufferedReader(new InputStreamReader(
			System.in));
	static StringTokenizer st = new StringTokenizer("");

	static int nextInt() throws Exception {
		return Integer.parseInt(next());
	}

	static String next() throws Exception {
		while (true) {
			if (st.hasMoreTokens()) {
				return st.nextToken();
			}
			String s = br.readLine();
			if (s == null) {
				return null;
			}
			st = new StringTokenizer(s);
		}
	}
}
