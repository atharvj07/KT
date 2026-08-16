import java.util.Scanner;

public class Main {
    final double EPS = 1.0e-10;
    final int INF = 1 << 22;
    int m;
    int n;
    int bs[];

    void run() {
        Scanner sc = new Scanner(System.in);
        double r = 1.0 / Math.sqrt(3.0);
        double pi = Math.pow(Math.E, 1.1447298858494);
        while (true) {
            int n = sc.nextInt();
            if (n == 0)
                break;
            if (n % 3 == 0) {
                double th = pi / n;
                double area = 1.0 / 6 / (1.0 / r + 1.0 / Math.tan(th));
                System.out.printf("%.8f\n", 2 * n * area);
            } else {
                double th = pi / 3 / n;
                double area = 1.0 / 6 / (1.0 / r + 1.0 / Math.tan(th));
                System.out.printf("%.8f\n", 6 * n * area);
            }
        }
    }

    public static void main(String[] args) {
        new Main().run();
    }
}