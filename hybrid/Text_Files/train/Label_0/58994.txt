import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Num[] nums = new Num[n];
		for (int i = 0; i < n; i++) {
		    nums[i] = new Num(i, sc.nextInt());
		}
		Arrays.sort(nums);
		UnionFindTree uft = new UnionFindTree(n);
		HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
		for (int i = 0; i < n; i++) {
		    for (int j = 2; j <= Math.sqrt(nums[i].value); j++) {
		        if (nums[i].value % j == 0) {
		            if (!map.containsKey(j)) {
		                map.put(j, new ArrayList<>());
		            }
		            map.get(j).add(i);
		        }
		        while (nums[i].value % j == 0) {
		            nums[i].value /= j;
		        }
		    }
		    if (nums[i].value != 1) {
	            if (!map.containsKey(nums[i].value)) {
	                map.put(nums[i].value, new ArrayList<>());
	            }
	            map.get(nums[i].value).add(i);
		    }
		}
		for (ArrayList<Integer> list : map.values()) {
		    for (int i = 1; i < list.size(); i++) {
		        uft.unite(list.get(i), list.get(0));
		    }
		}
		for (int i = 0; i < n; i++) {
		    if (!uft.same(i, nums[i].idx)) {
		        System.out.println(0);
		        return;
		    }
		}
		System.out.println(1);
	}
	
	static class Num implements Comparable<Num> {
	    int idx;
	    int value;
	    
	    public Num(int idx, int value) {
	        this.idx = idx;
	        this.value = value;
	    }
	    
	    public int compareTo(Num another) {
	        return value - another.value;
	    }
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

