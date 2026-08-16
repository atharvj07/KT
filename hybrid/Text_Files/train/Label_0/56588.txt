import java.util.*;

class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Map<Long, Integer> map = new HashMap<>();

        for (int i = 0; i < N; i++) {
            long value = sc.nextLong();
            if (map.containsKey(value)) {
                map.put(value, map.get(value) + 1);
            } else {
                map.put(value, 1);
            }
        }

        List<Long> candidates = new ArrayList<>();
        for (Map.Entry<Long, Integer> entry : map.entrySet()) {
            if (entry.getValue() >= 4) {
                candidates.add(entry.getKey());
                candidates.add(entry.getKey());
            } else if (entry.getValue() >= 2) {
                candidates.add(entry.getKey());
            }
        }
        Collections.sort(candidates);

        if (candidates.size() >= 2) {
            long a = candidates.get(candidates.size() - 1);
            long b = candidates.get(candidates.size() - 2);
            System.out.println(a * b);
        } else {
            System.out.println(0);
        }
    }
}