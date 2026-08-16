import java.util.*;

public class Main {
    public static void main(final String[] args) {
        final Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long[] A = new long[N];
        for (int i = 0; i < N; ++i) {
            A[i] = sc.nextLong();
        }
        sc.close();

        int odd = 0;
        for (int i = 0; i < N; ++i) {
            if (A[i] % 2 != 0) {
                ++odd;
            }
        }

        if (odd % 2 == 0) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}