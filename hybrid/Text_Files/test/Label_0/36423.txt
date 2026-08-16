import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        int[] a = new int[m];
        for (int i = 0; i < m; i++)
            a[i] = 10000000;
        for (int i = 0; i < n; i++) {
            int t = sc.nextInt() - 1;
            int p = sc.nextInt();
            a[t] = Math.min(a[t], p);
        }
        long sum = 0;
        for (int i = 0; i < m; i++)
            sum += a[i];
        System.out.println(Math.min(sum, k));
    }
}
