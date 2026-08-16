import java.util.Arrays;
import java.util.Scanner;


public class C {

	static class UnionFind {
		int[] prev;
		int n;
		
		UnionFind(int n) {
			this.n = n;
			prev = new int[n];
			Arrays.fill(prev, -1);
		}
		
		int getRootOf(int n) {
			int cur = n;
			while (prev[cur] != -1) {
				cur = prev[cur];
			}
			assert (prev[cur] == -1);
			return cur;
		}
	}
	
	static int encode(int x, int y) {
		if (y == 0) {
			return x;
		} else {
			return m + y - 1;
		}
	}
	
	static void join(int x1, int y1, int x2, int y2) {
		 int c1 = encode(x1, y1);
		 int c2 = encode(x2, y2);
		 if (c1 == c2) {
			 return;
		 }
		 int r1 = uf.getRootOf(c1);
		 int r2 = uf.getRootOf(c2);
		 if (r1 != r2) {
			 uf.prev[r1] = r2;
		 }
	}
	
	static UnionFind uf;
	static int n, m;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		if (n > m) {
			int tmp = n; n = m; m = tmp;
		}
		
		uf = new UnionFind(n+m-1);
		
		for (int i = 0; i < m - 1; ++i) {
//			System.out.print(i+": ");
			if (m-i <= n) {
//				System.out.println("right:"+(m-i-1));
				join(i, 0, m-1, m-i-1);
			} else if (m-i >= 2*n-1) {
//				System.out.println("down:"+(i+n+n-2));
				join(i, 0, i+n+n-2, 0);
			} else {
//				System.out.println("right (bond):"+(n-m+i+n-1));
				join(i, 0, m-1, n-m+i+n-1);
			}
		}
		
		for (int i = 1; i < n - 1; ++i) {
//			System.out.print(i+": ");
			if (m-(n-i-1) >= n) {
//				System.out.println("down:"+(n-i-1+n-1));
				join(i, 0, n-i-1+n-1, 0);
			} else {
//				System.out.println("right:"+(n-(m-(n-i-1))));
				join(i, 0, m-1, n-(m-(n-i-1)));
			}
		}
		
		int ans = 0;
		for (int i = 0; i < n+m-1; ++i) {
			if (uf.prev[i] == -1) {
				ans++;
			}
		}
		System.out.println(ans);
	}
}
