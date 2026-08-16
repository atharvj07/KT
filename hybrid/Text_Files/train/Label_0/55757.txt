//--- pF ---//
import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
	public static void main (String[] args) throws java.lang.Exception {
		new Solution();
	}
}
class Solution {
	Scanner scanner;
	public Solution() {
		scanner = new Scanner(System.in);

		// scanner.nextLine();
		while (scanner.hasNext()) {
			run_case();
		}
	}
	private void run_case() {
		// scanner.nextLine();
		String line = scanner.nextLine();

		int N = Integer.parseInt(line.split("\\s+")[0]);
		int D = Integer.parseInt(line.split("\\s+")[1]);
		int A = Integer.parseInt(line.split("\\s+")[2]);

		TreeMap<Integer, Integer> map = new TreeMap<>();
		int max_idx = 0;
		for (int i=0; i<N; i++) {
			line = scanner.nextLine();
			int X = Integer.parseInt(line.split("\\s+")[0]);
			int H = Integer.parseInt(line.split("\\s+")[1]);
			map.put(X, H);

			max_idx = Math.max(max_idx, X);
		}

		// int[] stArr = new int[max_idx + 1];
		// Arrays.fill(stArr, 0);
		SegmentTreeRSQ st = new SegmentTreeRSQ(1, max_idx);

		long res = 0;
		for (;map.keySet().size() != 0;) {
			int cur = map.firstKey();

			long H = map.get(cur) - st.query(Math.max(1, cur-2*D), cur);
			H = Math.max(H, 0);

			int times = (int)Math.ceil(1.0 * H / A);
			int damage = A * times;

			st.update(cur, st.query(cur, cur) + damage);
			map.remove(cur);

			res += times;
		}

		System.out.println(res);

		return;
	}

	private int[] strToIntArray(String str) {
	    String[] vals = str.split("\\s+");
	    int sz = vals.length;
	    int[] res = new int[sz];
	    for (int i=0; i<sz; i++) {
	        res[i] = Integer.parseInt(vals[i]);
	    }
	    return res;
	}
}

class SegmentTreeRSQ {
	SegmentTreeRSQNode root = null;
    int[] nums;
	int inf = Integer.MAX_VALUE;

	public SegmentTreeRSQ(int start, int end) {
		root = new SegmentTreeRSQNode(start, end);
	}

	public void update(int i, long val) {
		if (root == null) return;
        update(root, i, val);
    }
    public void update(SegmentTreeRSQNode root, int i, long val) {
		if (root == null) return;
        if (root.start == i && root.end == i) root.sum = val;
        else {
            int mid = root.mid();
			// split
			if (root.left == null) root.left = new SegmentTreeRSQNode(root.start, mid);
            if (root.right == null) root.right = new SegmentTreeRSQNode(mid+1, root.end);
			// visit
            if (i <= mid) update(root.left, i, val);
            else update(root.right, i, val);
			// merge
			root.sum = root.left.sum + root.right.sum;
        }
    }

	public long query(int start, int end) {
        if (root == null) return 0;
        else return query(root, start, end);
    }
	public long query(SegmentTreeRSQNode root, int start, int end) {
		if (root == null) return 0;
        if (start > end) {
			return 0;
        } else if (root.start == start && root.end == end){
			return root.sum;
        } else {
            int mid = root.mid();
            if (end <= mid) { // in left
                return query(root.left, start, end);
            } else if (start >= mid+1) { // in right
                return query(root.right, start, end);
            } else {
				return query(root.left, start, mid) + query(root.right, mid+1, end);
            }
        }
    }
}

class SegmentTreeRSQNode {
	int inf = Integer.MAX_VALUE;
    public int start, end, min, max;
	public long sum;
    public SegmentTreeRSQNode left, right;
    public SegmentTreeRSQNode(int start, int end) {
        this.left = null;
        this.right = null;
        this.start = start;
        this.end = end;

        this.min = inf;
		this.max = -inf;
		this.sum = 0;
    }
	public int mid() {return this.start + (this.end - this.start) / 2;}
}
