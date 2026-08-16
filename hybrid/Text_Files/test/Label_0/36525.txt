
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            int n = scanner.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextInt();
            }
            int q = scanner.nextInt();
            for (int i = 0; i < q; i++) {
                int k = scanner.nextInt();
                int findPosition = binarySearch(a, k, n);
                System.out.println(findPosition);
            }

        } catch (Exception e) {

        } finally {

        }

    }

    public static int binarySearch(int[] a, int q, int n) {
        int start = 0;
        int end = a.length-1;
       
        while (start <= end) {
            int midpoint = (start + end) / 2;
            if (a[midpoint] >= q) {
                end = midpoint - 1;
            } else {
                start = midpoint + 1;
            }

        }
      
        return start;
    }
}


