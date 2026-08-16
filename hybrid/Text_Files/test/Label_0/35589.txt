import java.util.*;

public class Main {
     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            graph.add(new ArrayList<>());
        }
        int[] types = new int[n];
        for (int i = 0; i < n; i++) {
            int x = sc.next().charAt(0) - 'a';
            graph.get(x).add(i);
            types[i] = x;
        }
        int[] costs = new int[n];
        Arrays.fill(costs, Integer.MAX_VALUE);
        PriorityQueue<Path> queue = new PriorityQueue<>();
        queue.add(new Path(0, 0));
        while (queue.size() > 0) {
            Path p = queue.poll();
            if (p.idx >= n) {
                continue;
            }
            if (costs[p.idx] <= p.value) {
                continue;
            }
            costs[p.idx] = p.value;
            queue.add(new Path(p.idx + 1, p.value + 1));
            for (int x : graph.get(types[p.idx])) {
                if (x <= p.idx) {
                    continue;
                }
                queue.add(new Path(x, p.value));
            }
            graph.get(types[p.idx]).clear();
        }
        System.out.println(costs[n - 1] + 1);
    }
    
    static class Path implements Comparable<Path> {
        int idx;
        int value;
        
        public Path(int idx, int value) {
            this.idx = idx;
            this.value = value;
        }
        
        public int compareTo(Path another) {
            return value - another.value;
        }
    }
}
