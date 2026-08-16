import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n], w = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            w[i] = sc.nextInt();
        }
        int zeroMin = Integer.MAX_VALUE;
        int oneMin = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (a[i] == 0) {
            zeroMin = Math.min(zeroMin, w[i]);
        } else {
            oneMin = Math.min(oneMin, w[i]);
        }
    }
        if (Arrays.stream(a).allMatch(value -> value == 0)
                ||
                Arrays.stream(a).allMatch(value -> value == 1)
        ) {
            System.out.println(0);
        } else {
            System.out.println(oneMin + zeroMin);
        }
    }
}

