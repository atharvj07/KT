import java.util.*;

public class Main {
    static int[] arr;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();
        arr = new int[n + 2];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        arr[n] = Integer.MAX_VALUE;
        arr[n + 1] = Integer.MIN_VALUE;
        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            int left = sc.nextInt();
            int right = sc.nextInt();
            sb.append(getRightIdx(right) - getLeftIdx(left) + 1).append("\n");
        }
        System.out.print(sb);
    }
    
    static int getLeftIdx(int x) {
        int left = 0;
        int right = arr.length;
        while (right - left > 1) {
            int m = (left + right) / 2;
            if (arr[m] < x) {
                left = m;
            } else {
                right = m;
            }
        }
        return right;
    }
    
    static int getRightIdx(int x) {
        int left = 0;
        int right = arr.length;
        while (right - left > 1) {
            int m = (left + right) / 2;
            if (arr[m] <= x) {
                left = m;
            } else {
                right = m;
            }
        }
        return left;
    }
}
