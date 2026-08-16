import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int min = Integer.MAX_VALUE;
        int minIdx = 0;
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            if (min > x) {
                min = x;
                minIdx = i + 1;
            }
        }
        System.out.println(minIdx);
    }
}
