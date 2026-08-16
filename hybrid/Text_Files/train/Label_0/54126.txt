import java.util.Scanner;

public class H549 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long a = in.nextInt();
        long b = in.nextLong();
        long c = in.nextLong();
        long d = in.nextLong();
        if (a * d == c * b) {
            System.out.println(0);
            return;
        }

        long r = Math.abs(a + b + c + d);
        r = Math.max(Math.abs(a - b - c + d), r);
        r = Math.max(Math.abs(-a - b - c - d), r);
        r = Math.max(Math.abs(-a + b + c - d), r);
        r = Math.max(Math.abs(a - d + b - c), r);
        r = Math.max(Math.abs(-a + d - b + c), r);
        r = Math.max(Math.abs(a - d - b + c), r);
        r = Math.max(Math.abs(-a + d + b - c), r);

        double t = Math.abs(b * c - a * d - 0.0) / r;

        double left = b * c - a * d;
        double APlusD = a + d;
        double ASD = a - d;
        double BpusC = b + c;
        double BSC = b - c;

        double mid = APlusD + BSC;
        double delta = mid * mid + 8 * left;
        if (delta >= 0) {
            double x1 = Math.abs((-mid + Math.sqrt(delta)) / 4);
            x1 = Math.min(x1, Math.abs((-mid - Math.sqrt(delta)) / 4));
            t = Math.min(t, x1);
        }

        mid = APlusD - BSC;
        delta = mid * mid + 8 * left;
        if (delta >= 0) {
            double x1 = Math.abs((-mid + Math.sqrt(delta)) / 4);
            x1 = Math.min(x1, Math.abs((-mid - Math.sqrt(delta)) / 4));
            t = Math.min(t, x1);
        }

        mid = -APlusD + BSC;
        delta = mid * mid + 8 * left;
        if (delta >= 0) {
            double x1 = Math.abs((-mid + Math.sqrt(delta)) / 4);
            x1 = Math.min(x1, Math.abs((-mid - Math.sqrt(delta)) / 4));
            t = Math.min(t, x1);
        }

        mid = -APlusD - BSC;
        delta = mid * mid + 8 * left;
        if (delta >= 0) {
            double x1 = Math.abs((-mid + Math.sqrt(delta)) / 4);
            x1 = Math.min(x1, Math.abs((-mid - Math.sqrt(delta)) / 4));
            t = Math.min(t, x1);
        }

        mid = ASD - BpusC;
        delta = mid * mid - 8 * left;
        if (delta >= 0) {
            double x1 = Math.abs((-mid + Math.sqrt(delta)) / 4);
            x1 = Math.min(x1, Math.abs((-mid - Math.sqrt(delta)) / 4));
            t = Math.min(t, x1);
        }

        mid = ASD + BpusC;
        delta = mid * mid - 8 * left;
        if (delta >= 0) {
            double x1 = Math.abs((-mid + Math.sqrt(delta)) / 4);
            x1 = Math.min(x1, Math.abs((-mid - Math.sqrt(delta)) / 4));
            t = Math.min(t, x1);
        }

        mid = -ASD - BpusC;
        delta = mid * mid - 8 * left;
        if (delta >= 0) {
            double x1 = Math.abs((-mid + Math.sqrt(delta)) / 4);
            x1 = Math.min(x1, Math.abs((-mid - Math.sqrt(delta)) / 4));
            t = Math.min(t, x1);
        }

        mid = -ASD + BpusC;
        delta = mid * mid - 8 * left;
        if (delta >= 0) {
            double x1 = Math.abs((-mid + Math.sqrt(delta)) / 4);
            x1 = Math.min(x1, Math.abs((-mid - Math.sqrt(delta)) / 4));
            t = Math.min(t, x1);
        }
        System.out.println(t);

    }
}
