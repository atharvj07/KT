import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int w = sc.nextInt();
        int start = sc.next().charAt(0) - 'A';
        int end = sc.next().charAt(0) - 'A';
        char[][] field = new char[h][];
        for (int i = 0; i < h; i++) {
            field[i] = sc.next().toCharArray();
        }
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (field[i][j] >= 'A' && field[i][j] <= 'Z') {
                    char a = field[i][j];
                    if (j + 2 < w && field[i][j + 2] == '-') {
                        int right = j + 2;
                        while (field[i][right] < 'A' || field[i][right] > 'Z') {
                            right++;
                        }
                        char b = field[i][right];
                        graph.get(a - 'A').add(b - 'A');
                        graph.get(b - 'A').add(a - 'A');
                    }
                    if (i + 2 < h && field[i + 2][j] == '|') {
                        int down = i + 2;
                        while (field[down][j] < 'A' || field[down][j] > 'Z') {
                            down++;
                        }
                        char b = field[down][j];
                        graph.get(a - 'A').add(b - 'A');
                        graph.get(b - 'A').add(a - 'A');
                    }
                }
            }
        }
        int[] costs = new int[26];
        Arrays.fill(costs, Integer.MAX_VALUE);
        PriorityQueue<Path> queue = new PriorityQueue<>();
        queue.add(new Path(start, 0));
        while (queue.size() > 0) {
            Path p = queue.poll();
            if (p.value >= costs[p.idx]) {
                continue;
            }
            costs[p.idx] = p.value;
            for (int x : graph.get(p.idx)) {
                queue.add(new Path(x, p.value + 1));
            }
        }
        System.out.println(costs[end]);
    }
    
    static class Path implements Comparable<Path> {
        int idx;
        int value;
        
        public Path (int idx, int value) {
            this.idx = idx;
            this.value = value;
        }
        
        public int compareTo(Path another) {
            return value - another.value;
        }
    }
}

