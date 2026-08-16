

import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static class Dish {
        long a;
        long b;
        public Dish(long a, long b) {
            this.a = a;
            this.b = b;
        }
    }
    public static void main(String [] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        PriorityQueue<Dish> food = new PriorityQueue<>(
                (d1, d2) ->
                {
                    long diff = d2.a + d2.b - (d1.a + d1.b);
                    if (diff > 0) {
                        return 1;
                    } else if (diff == 0) {
                        return 0;
                    } else {
                        return -1;
                    }
                }
        );
        for (int i = 0; i < n; ++i) {
            long a = scanner.nextLong();
            long b = scanner.nextLong();
            food.add(new Dish(a, b));
        }
        long result = 0;
        for (int i = 0; i < n; ++i) {
            final Dish dish = food.poll();
            if (i % 2 == 0) {
                result += dish.a;
            } else {
                result -= dish.b;
            }
        }
        System.out.println(result);
    }
}
