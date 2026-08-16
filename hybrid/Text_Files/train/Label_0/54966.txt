import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
		    arr[i] = sc.nextInt();
		}
		PriorityQueue<Query> begins = new PriorityQueue<Query>(new Comparator<Query>() {
		    public int compare(Query q1, Query q2) {
		        return q1.begin - q2.begin;
		    }
		});
		PriorityQueue<Query> ends = new PriorityQueue<Query>(new Comparator<Query>() {
		    public int compare(Query q1, Query q2) {
		        return q1.end - q2.end;
		    }
		});
		int m = sc.nextInt();
		Query[] queries = new Query[m];
		for (int i = 0; i < m; i++) {
		    queries[i] = new Query(sc.nextInt(), sc.nextInt(), sc.nextInt());
		    begins.add(queries[i]);
		    ends.add(queries[i]);
		}
		HashMap<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i <= n; i++) {
		    while (begins.size() > 0 && begins.peek().begin == i) {
		        Query q = begins.poll();
		        if (map.containsKey(q.value)) {
		            q.left = map.get(q.value);
		        }
		    }
		    while (ends.size() > 0 && ends.peek().end == i) {
		        Query q = ends.poll();
		        if (map.containsKey(q.value)) {
		            q.right = map.get(q.value);
		        }
		    }
		    if (i == n) {
		        break;
		    }
		    if (map.containsKey(arr[i])) {
		        map.put(arr[i], map.get(arr[i]) + 1);
		    } else {
		        map.put(arr[i], 1);
		    }
		}
		StringBuilder sb = new StringBuilder();
		for (Query q : queries) {
		    sb.append(q).append("\n");
		}
		System.out.print(sb);
	}
	
	static class Query {
	    int begin;
	    int end;
	    int value;
	    int left;
	    int right;
	    
	    public Query(int begin, int end, int value) {
	        this.begin = begin;
	        this.end = end;
	        this.value = value;
	    }
	    
	    public String toString() {
	        return String.valueOf(right - left);
	    }
	}
}

