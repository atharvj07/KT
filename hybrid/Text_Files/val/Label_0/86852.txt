import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int C = sc.nextInt();

        double h = b * Math.sin(C * Math.PI / 180);
        double S = h * a / 2;
        double c = Math.sqrt(a * a + b * b - 2 * a * b * Math.cos(C * Math.PI / 180));
        double l = a + b + c;
        System.out.printf("%f\n%f\n%f\n", S, l, h);
    }
}