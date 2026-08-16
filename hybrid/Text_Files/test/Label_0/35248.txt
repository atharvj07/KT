import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // Your code here! 
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int d = sc.nextInt();
        
        List<Integer>[] list = new List[d+1];
        for (int i = 0; i < d+1; i++) {
            list[i] = new ArrayList<Integer>();
        }
        
        for (int i = 0; i < n; i++) {
            int day = sc.nextInt();
            int value = sc.nextInt();
            if (day > d) continue;
            
            list[day].add(value);
        }
        
        PriorityQueue<Integer> que = new PriorityQueue<>(Collections.reverseOrder()); // 降順で
        
        long ans = 0;
        for (int i = 1; i <= d; i++) {
            if (list[i].size() != 0) {
                for (Integer num : list[i]) {
                    que.add(num);
                }
            }
            if (que.isEmpty()) continue;
            ans += (long)que.poll();
        }
        System.out.println(ans);
    }
}