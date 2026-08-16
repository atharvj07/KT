import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        ArrayList<ArrayDeque<Integer>> lanes = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            lanes.add(new ArrayDeque<>());
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            if (x == 0) {
                int idx = sc.nextInt();
                sb.append(lanes.get(idx).poll()).append("\n");
            } else {
                int car = sc.nextInt();
                int min = Integer.MAX_VALUE;
                int minIdx = 0;
                for (int j = 1; j <= n; j++) {
                    if (min > lanes.get(j).size()) {
                        min = lanes.get(j).size();
                        minIdx = j;
                        if (min == 0) {
                            break;
                        }
                    }
                }
                lanes.get(minIdx).add(car);
            }
        }
        System.out.print(sb);
    }
}
