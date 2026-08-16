import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        TreeSet<Integer> plusSet = new TreeSet<>();
        TreeSet<Integer> minusOneSet = new TreeSet<>();
        TreeMap<Integer, Integer> minusMap = new TreeMap<>();
        for (int i = 1; i <= n; i++) {
            int x = sc.nextInt();
            if (x > 1) {
                plusSet.add(i);
            } else if (x == -1) {
                minusOneSet.add(i);
            } else if (x < -1) {
                minusMap.put(i, x);
            }
        }
        if (minusMap.size() % 2 == 1) {
            if (minusOneSet.size() > 0) {
                plusSet.addAll(minusMap.keySet());
                plusSet.add(minusOneSet.first());
            } else {
                int min = Integer.MAX_VALUE;
                int minIdx = 0;
                for (Map.Entry<Integer, Integer> entry : minusMap.entrySet()) {
                    if (min >= entry.getValue()) {
                        min = entry.getValue();
                        minIdx = entry.getKey();
                    }
               }
                minusMap.remove(minIdx);
                plusSet.addAll(minusMap.keySet());
            }
        } else {
            plusSet.addAll(minusMap.keySet());
        }
        StringBuilder sb = new StringBuilder();
        sb.append(plusSet.size()).append("\n");
        for (int x : plusSet) {
            sb.append(x).append("\n");
        }
        System.out.print(sb);
    }
}

