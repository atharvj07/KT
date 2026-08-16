import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        int[] b = new int[n];
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            map.put(i, new ArrayList<>());
        }
        for (int i = 0; i < n - 1; i++) {
            a[i] = sc.nextInt();
            b[i] = sc.nextInt();
            List<Integer> alist = map.get(a[i]);
            alist.add(b[i]);
            map.put(a[i], alist);
            List<Integer> blist = map.get(b[i]);
            blist.add(a[i]);
            map.put(b[i], blist);
        }

        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] { 1, 0 });
        boolean[] visited = new boolean[n + 1];
        visited[1] = true;
        Map<Integer, Map<Integer, Integer>> ans = new HashMap<>();
        int max = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] q = queue.poll();
                int src = q[0];
                int prev = q[1];
                int color = 1;
                List<Integer> dests = map.get(src);
                for (int j = 0; j < dests.size(); j++) {
                    int dest = dests.get(j);
                    if (visited[dest]) {
                        continue;
                    }
                    visited[dest] = true;
                    if (color == prev) {
                        color++;
                    }
                    Map<Integer, Integer> destmap = ans.getOrDefault(src, new HashMap<>());
                    destmap.put(dest, color);
                    ans.put(src, destmap);
                    max = Math.max(max, color);
                    queue.add(new int[] { dest, color });
                    color++;
                }
            }
        }
        System.out.println(max);
        for (int i = 0; i < n - 1; i++) {
            System.out.println(ans.get(a[i]).get(b[i]));
        }
    }

}
