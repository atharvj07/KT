import java.util.*;

public class WorkoutPlan {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        long k = s.nextLong();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = s.nextInt();

        long boost = s.nextLong();

        int[] c = new int[n];
        for (int i = 0; i < n; i++)
            c[i] = s.nextInt();

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        long ret = 0;
        for (int i = 0; i < n; i++) {
            pq.offer(c[i]);
            while (k < arr[i] && pq.size() > 0) {
                long buy = pq.poll();
                ret += buy;
                k += boost;
            }
            if (k < arr[i]) {
                System.out.println(-1);
                return;
            }
        }
        System.out.println(ret);
        s.close();
    }
}