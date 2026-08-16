import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
		    arr[i] = sc.nextInt();
		}
		UnionFindTree uft = new UnionFindTree(n);
		for (int i = 0; i < m; i++) {
		    uft.unite(sc.nextInt() - 1, sc.nextInt() - 1);
		}
		int count = 0;
		for (int i = 0; i < n; i++) {
		    if (uft.same(arr[i] - 1, i)) {
		        count++;
		    }
		}
		System.out.println(count);
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
        }
    }
}

