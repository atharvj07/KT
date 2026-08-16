import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long k = sc.nextInt();
        long[] arr = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            arr[i] = arr[i - 1] + sc.nextInt() - k;
        }
        ArrayList<Long> list = new ArrayList<>();
        list.add(Long.MIN_VALUE);
        list.add(0L);
        list.add(Long.MAX_VALUE);
        long count = 0;
        for (int i = 1; i <= n; i++) {
            int left = 0;
            int right = list.size() - 1;
            while (right - left > 1) {
                int m = (left + right) / 2;
                if (arr[i] < list.get(m)) {
                    right = m;
                } else {
                    left = m;
                }
            }
            count += left;
            list.add(right, arr[i]);

        }
        System.out.println(count);
    }
}
