import java.util.*;

public class Main {
     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Node[] arrA = new Node[n];
        for (int i = 0; i < n; i++) {
            arrA[i] = new Node(i, sc.nextInt());
        }
        Arrays.sort(arrA);
        int[] idxesA = new int[n];
        for (int i = 0; i < n; i++) {
            idxesA[arrA[i].idx] = i;
        }
        Node[] arrB = new Node[n];
        for (int i = 0; i < n; i++) {
            arrB[i] = new Node(i, sc.nextInt());
        }
        Arrays.sort(arrB);
        int[] idxesB = new int[n];
        for (int i = 0; i < n; i++) {
            idxesB[arrB[i].idx] = i;
        }
        long[] costs = new long[n];
        Arrays.fill(costs, Long.MAX_VALUE);
        PriorityQueue<Path> queue = new PriorityQueue<>();
        queue.add(new Path(0, 0));
        while (queue.size() > 0) {
            Path p = queue.poll();
            if (costs[p.idx] <= p.value) {
                continue;
            }
            costs[p.idx] = p.value;
            if (idxesA[p.idx] != 0) {
                int next = idxesA[p.idx] - 1;
                queue.add(new Path(arrA[next].idx, p.value + Math.abs(arrA[idxesA[p.idx]].value - arrA[next].value)));
            }
            if (idxesA[p.idx] != n - 1) {
                int next = idxesA[p.idx] + 1;
                queue.add(new Path(arrA[next].idx, p.value + Math.abs(arrA[idxesA[p.idx]].value - arrA[next].value)));
            }
            if (idxesB[p.idx] != 0) {
                int next = idxesB[p.idx] - 1;
                queue.add(new Path(arrB[next].idx, p.value + Math.abs(arrB[idxesB[p.idx]].value - arrB[next].value)));
            }
            if (idxesB[p.idx] != n - 1) {
                int next = idxesB[p.idx] + 1;
                queue.add(new Path(arrB[next].idx, p.value + Math.abs(arrB[idxesB[p.idx]].value - arrB[next].value)));
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(costs[i]).append("\n");
        }
        System.out.print(sb);
    }
    
    static class Node implements Comparable<Node>{
        int idx;
        int value;
        
        public Node(int idx, int value) {
            this.idx = idx;
            this.value = value;
        }
        
        public int compareTo(Node another) {
            return value - another.value;
        }
    }
    
    static class Path implements Comparable<Path> {
        int idx;
        long value;
        public Path(int idx, long value) {
            this.idx = idx;
            this.value = value;
        }
        
        public int compareTo(Path another) {
            if (value == another.value) {
                return 0;
            } else if (value < another.value) {
                return -1;
            } else {
                return 1;
            }
        }
        
        public String toString() {
            return idx + ":" + value;
        }
    }
}
