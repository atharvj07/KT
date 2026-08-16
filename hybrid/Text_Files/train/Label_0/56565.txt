import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		Pair[] pairs = new Pair[m];
		for (int i = 0; i < m; i++) {
		    pairs[i] = new Pair(sc.nextInt(), sc.nextInt());
		}
		Arrays.sort(pairs);
		UnionFindTree uft = new UnionFindTree(n);
		for (int i = m - 1; i >= 0; i--) {
		    uft.unite(pairs[i]);
		}
		int q = sc.nextInt();
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < q; i++) {
		    if (uft.same(sc.nextInt(), sc.nextInt())) {
		        sb.append("yes");
		    } else {
		        sb.append("no");
		    }
		    sb.append("\n");
		}
		System.out.print(sb);
	}
	
	static class UnionFindTree {
	    int[] parents;
	    
	    public UnionFindTree(int size) {
	        parents = new int[size];
	        for (int i = 0; i < size; i++) {
	            parents[i] = i;
	        }
	    }
	    
	    public int find(int x) {
	        if (parents[x] == x) {
	            return x;
	        } else {
	            return parents[x] = find(parents[x]);
	        }
	    }
	    
	    public boolean same(int x, int y) {
	        return find(x) == find(y);
	    }
	    
	    public void unite(int x, int y) {
	        if (same(x, y)) {
	            return;
	        }
	        parents[find(x)] = find(y);
	        find(x);
	    }
	    
	    public void unite(Pair p) {
	        unite(p.left, p.right);
	    }
	}
	
	static class Pair implements Comparable<Pair> {
	    int left;
	    int right;
	    
	    public Pair(int x, int y) {
	        left = Math.min(x, y);
	        right = Math.max(x, y);
	    }
	    
	    public int compareTo(Pair another) {
	        if (left == another.left) {
	            return right - another.right;
	        } else {
	            return left - another.left;
	        }
	    }
	}
}

