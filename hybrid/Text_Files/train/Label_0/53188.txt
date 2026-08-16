import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int mm = sc.nextInt();
        TreeMap<Integer, Integer> counts = new TreeMap<>();
        int start = sc.nextInt();
        int prev = start;
        for (int i = 1; i < mm; i++) {
            int x = sc.nextInt();
            if (counts.containsKey(x - prev)) {
                counts.put(x - prev, counts.get(x - prev) + 1);
            } else {
                counts.put(x - prev, 1);
            }
            prev = x;
        }
        if (counts.containsKey(n + 1 - prev)) {
            counts.put(n + 1 - prev, counts.get(n + 1 - prev) + 1);
        } else {
            counts.put(n + 1 - prev, 1);
        }
        int[] sums = new int[n + 1];
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            for (int i = 0; i < entry.getKey(); i++) {
                sums[i] += (entry.getKey() - i) * entry.getValue();
            }
        }
        int q = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            int x = sc.nextInt();
            if (x < start - 1) {
                sb.append(-1).append("\n");
                continue;
            }
            x -= start - 1;
            int left = 0;
            int right = n;
            while (right - left > 1) {
                int m = (left + right) / 2;
                if (sums[m] > x) {
                    left = m;
                } else {
                    right = m;
                }
            }
            sb.append(right).append("\n");
        }
        System.out.print(sb);
    }
}
