

import java.util.Scanner;

public class Main {
    static Scanner sc = new Scanner(System.in);


    public static void main(String[] args) {
        int n = sc.nextInt();
        int m = sc.nextInt();
        int c = sc.nextInt();
        int[] b = new int[m];
        for (int i = 0; i < m; i++) {
            b[i] = sc.nextInt();
        }
        int count = 0;
        for (int i = 0; i < n; i++) {
            int amount = 0;
            for (int j = 0; j < m; j++) {
                amount += sc.nextInt() * b[j];
            }
            amount += c;
            if (amount > 0) {
                count++;
            }
        }
        System.out.println(count);
    }
}
