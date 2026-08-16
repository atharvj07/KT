import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, t;
        double a = 0.0, x, h;

        n = sc.nextInt();
        t = sc.nextInt();
        for(int i = 0; i < n; i++) {
            x = sc.nextInt();
            h = sc.nextInt();
            a = Math.max(a, h / x);
        }

        System.out.printf("%.6f", a * t);
    }
}