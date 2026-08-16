import java.util.Scanner;

public class E {
    static int n;
    static double[] a;

    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);

        n = cin.nextInt();
        a = new double[n];
        for (int i=0;i<n;i++) {
            a[i]=cin.nextDouble();
        }

        double left, right;
        left = -1e5;
        right = 1e5;
        for (int i = 0; i < 100; i++) {
            double x = (left + right) / 2;
            if (f(x) > f((x + right) / 2)) {
                left = x;
            } else {
                right = (x + right) / 2;
            }
        }

        System.out.println(f(right));

        cin.close();
    }

    private static double f(double x) {
        double ans = 0;
        double sum = 0;
        for (int i = 0; i < n; i++) {
            sum += a[i] - x;
            if (sum > ans) ans = sum;
            if (sum < 0) sum = 0;
        }

        sum = 0;
        for (int i = 0; i < n; i++) {
            sum -= a[i] - x;
            if (sum > ans) ans = sum;
            if (sum < 0) sum = 0;
        }
        return ans;
    }
}
