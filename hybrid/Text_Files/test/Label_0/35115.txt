import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.TreeSet;

import javax.management.Query;

public class Main {

	public static void main(String[] args) throws IOException {
		Main mainObj = new Main();
		mainObj.solve();
	}

	public void solve() throws IOException {
		FastScanner fs = new FastScanner();
		int n = fs.nextInt();
		int k = fs.nextInt();
		
		int[] aArr = fs.nextIntArr(n);
		
		SegmentTree segTree = new SegmentTree(300_001, (a,b) -> Math.max(a,b), 0);
		
		for(int i = 0; i < n; i++) {
			
			int a = aArr[i];
			int left = Math.max(0, a-k);
			int right = Math.min(300_000, a+k);
			
			int maxLength = segTree.query(left, right+1, 0, 0, segTree.reafSize);
			segTree.update(a, maxLength+1);
		}
		
		
		System.out.println(segTree.query(0, 300_001, 0, 0, segTree.reafSize));
	}
	
	public class SegmentTree {
		int reafSize;
		int[] tree;
		TreeFunc treeFunc;
		int notInSectionValue;

		public SegmentTree(int size, TreeFunc treeFunc, int notInSectionValue) {
			reafSize = 1;
			while (reafSize < size) {
				reafSize *= 2;
			}
			tree = new int[reafSize * 2 - 1];
			this.treeFunc = treeFunc;
			this.notInSectionValue = notInSectionValue;
		}

		public void update(int pos, int val) {
			int pointer = reafSize + pos - 1;
			tree[pointer] = val;
			while (pointer > 0) {
				pointer = (pointer - 1) / 2;
				tree[pointer] = treeFunc.calc(tree[pointer * 2 + 1], tree[pointer * 2 + 2]);
			}
		}

		public int query(int a, int b, int k, int l, int r) {

			if (r < 0) {
				r = reafSize;
			}

			if (r <= a || b <= l) {
				return notInSectionValue;
			}
			if (a <= l && r <= b) {
				return tree[k];
			}

			return treeFunc.calc(query(a, b, k * 2 + 1, l, (l + r) / 2), query(a, b, k * 2 + 2, (l + r) / 2, r));
		}
	}

	@FunctionalInterface
	interface TreeFunc {
		public int calc(int left, int right);
	}


	public class FastScanner {

		BufferedReader reader;
		private StringTokenizer st;

		public FastScanner() {
			st = null;
			reader = new BufferedReader(new InputStreamReader(System.in));
		}

		public String next() throws IOException {
			if (st == null || !st.hasMoreElements()) {
				st = new StringTokenizer(reader.readLine());
			}
			return st.nextToken();
		}

		public String nextLine() throws IOException {
			st = null;
			String readLine = null;
			readLine = reader.readLine();
			return readLine;
		}

		public int nextInt() throws NumberFormatException, IOException {
			return Integer.parseInt(next());
		}

		public long nextLong() throws NumberFormatException, IOException {
			return Long.parseLong(next());
		}

		public int[] nextIntArr(int n) throws NumberFormatException, IOException {
			int[] retArr = new int[n];
			for (int i = 0; i < n; i++) {
				retArr[i] = nextInt();
			}
			return retArr;
		}

		public long[] nextLongArr(int n) throws NumberFormatException, IOException {
			long[] retArr = new long[n];
			for (int i = 0; i < n; i++) {
				retArr[i] = nextLong();
			}
			return retArr;
		}

		public void close() throws IOException {
			reader.close();
		}
	}

}
