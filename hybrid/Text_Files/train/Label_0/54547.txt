import java.util.*;
import java.lang.*;

class Main {
	static int[] segTree;
	static int n;

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		n = scanner.nextInt();
		int q = scanner.nextInt();

		initSegTree();

		for(int i = 0; i < q; i++) {
			int type = scanner.nextInt();

			if(type == 0) {
				int s = scanner.nextInt();
				int t = scanner.nextInt();
				int x = scanner.nextInt();

				// Change a[s] ... a[t] to x
				update(s,t,x);

			} else if(type == 1) {
				// Find value of a[i]
				int result = find(scanner.nextInt());
				System.out.println(result);
			}
		}
	}

	static void initSegTree() {
		int _n = 1;
		while(_n < n)
			_n *= 2;

		segTree = new int[2*_n];
		Arrays.fill(segTree, Integer.MAX_VALUE);
	}

	static void update(int s, int t, int x) {
		updateRange(1, 0, n, s, t+1, x);
	}

	/*	k: index of current node in segTree
		l & r: range covered by node k
		s & t: range of query
		x: new value to update
	*/
	static void updateRange(int k, int l, int r, int s, int t, int x) {

		if(s >= t) // out of range
			return;

		if(s == l && t == r) { // (s,t) fully inside (l,r)
			segTree[k] = x;
			return;
		}

		if(segTree[k] >= 0) {
			segTree[k*2] = segTree[k];
			segTree[k*2+1] = segTree[k];
			segTree[k] = -1;
		}

		// (s,t) and (l,r) intersect
		int mid = (l+r)/2;
		updateRange(k*2, l, mid, Math.max(s,l), Math.min(mid,t), x);
		updateRange(k*2+1, mid, r, Math.max(s,mid), Math.min(r,t), x);
	}

	static int find(int i) {
		return find(i, 0, n, 1);
	}

	static int find(int i, int l, int r, int k) {
		if(segTree[k] >= 0)
			return segTree[k];
		else {
			int mid = (l+r)/2;
			if(i < mid)
				return find(i,l,mid,k*2);
			else
				return find(i,mid,r,k*2+1);
		}
	}
}
