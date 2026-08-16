import java.util.*;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int b0 = 0, b1 = 0, b2 = 1;
        int max = 1;
        int prev = sc.nextInt();
        for (int i = 1; i < N; i++) {
            int x = sc.nextInt();
            if (x != prev) {
                b2++;
            } else {
                int len = b0 + b1 + b2;
                if (max < len) max = len;
                b0 = b1;
                b1 = b2;
                b2 = 1;
            }
            prev = x;
        }
        int len = b0 + b1 + b2;
        if (max < len) max = len;
        System.out.printf("%d\n", max);
    }
}