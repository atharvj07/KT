import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        final int N = sc.nextInt();
        final int Y = sc.nextInt();

        for (int a = 0; a <= N; a++) {
            for (int b = 0; a+b <= N; b++) {
                int c = N - a - b;
                if (Y == 10000 * a + 5000 * b + 1000 * c) {
                    System.out.println(a + " " + b + " " + c);
                    return;
                }
            }
        }
        System.out.println("-1 -1 -1");
    }
}
