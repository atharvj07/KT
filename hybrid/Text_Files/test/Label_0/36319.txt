
import java.util.*;

public class Main {
    static Scanner in = new Scanner(System.in);

    static void run() {
        int n = in.nextInt(), m = in.nextInt();
        Map<Integer, List<Integer>> g = new HashMap<>();
        for (int i=0;i<m;i++) {
            int u = in.nextInt() - 1, v = in.nextInt() - 1;
            g.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
            g.computeIfAbsent(v, k -> new ArrayList<>()).add(u);
        }
        int[] p = new int[n];
        Arrays.fill(p, -1);
        p[0] = 0;
        Queue<Integer> q = new ArrayDeque<>();
        q.add(0);
        while (!q.isEmpty()) {
            int curr = q.poll();
            if (!g.containsKey(curr)) continue;
            for (int nxt : g.get(curr)) {
                if (p[nxt] == -1) {
                    p[nxt] = curr;
                    q.add(nxt);
                }
            }
        }
        for (int i=0;i<n;i++) {
            if (p[i] == -1) {
                System.out.println("No");
                return;
            }
        }
        System.out.println("Yes");
        for (int i=1;i<n;i++) System.out.println(p[i] + 1);
    }

    public static void main(String[] args) {
        run();
    }
}
