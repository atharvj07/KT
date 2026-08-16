import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int p = sc.nextInt();
        int[] a = new int[n];
        int odd = 0;
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
            if (a[i] % 2 != 0) {
                odd++;
            }
        }
        if (odd == 0) {
            if (p == 0) {
                System.out.println((long) Math.pow(2, n));
            } else {
                System.out.println(0);
            }
            return;
        }
        System.out.println((long) Math.pow(2, n - 1));
    }

}
