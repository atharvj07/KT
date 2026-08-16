import java.util.*;

public class Main {
    static HashMap<Integer, HashMap<Integer, Long>> dp = new HashMap<>();
     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Snack[] snacks = new Snack[n];
        for (int i = 0; i < n; i++) {
            snacks[i] = new Snack(sc.nextInt(), sc.nextInt());
        }
        Arrays.sort(snacks, new Comparator<Snack>() {
            public int compare(Snack s1, Snack s2) {
                return s2.price - s1.price;
            }
        });
        Friend[] friends = new Friend[m];
        for (int i = 0; i < m; i++) {
            friends[i] = new Friend(sc.nextInt(), sc.nextInt());
        }
        Arrays.sort(friends);
        PriorityQueue<Snack> queue = new PriorityQueue<Snack>(new Comparator<Snack>() {
            public int compare(Snack s1, Snack s2) {
                return s1.value - s2.value;
            }
        });
        int idx = 0;
        for (int i = 0; i < m; i++) {
            while (idx < n && friends[i].price <= snacks[idx].price) {
                queue.add(snacks[idx]);
                idx++;
            }
            while (friends[i].count <= queue.size()) {
                queue.poll();
            }
        }
        while (idx < n) {
            queue.add(snacks[idx]);
            idx++;
        }
        long total = 0;
        while (queue.size() > 0) {
            total += queue.poll().value;
        }
        System.out.println(total);
    }
    
    static class Snack {
        int price;
        int value;
        
        public Snack(int price, int value) {
            this.price = price;
            this.value = value;
        }
        
        public String toString() {
            return "price:" + price + " value:" + value;
        }
    }
    
    static class Friend implements Comparable<Friend> {
        int price;
        int count;
        
        public Friend(int price, int count) {
            this.price = price;
            this.count = count;
        }
        
        public int compareTo(Friend another) {
            return another.price - price;
        }
    }
}
