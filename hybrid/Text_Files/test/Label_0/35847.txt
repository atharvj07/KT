import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        sc.close();

        if (k % n == 0 || k % m == 0) {
            System.out.println("Yes");
        } else {
            int judge = 0;
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) {
                    int temp = i * m - j * i + j * (n - i);
                    if (temp == k) {
                        judge = 1;
                    }
                }
            }
            if (judge == 1) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}
