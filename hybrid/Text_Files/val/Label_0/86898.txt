
import java.util.Scanner;

public class KspecialTables {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[][] a = new int[n][n];

        for (int i = 0; i < (k - 1) * n; i++) {
            int c = i / n;
            int r = i % n;
            a[r][c] = i + 1;
        }

        for (int i = (k - 1) * n; i < n * n; i++) {
            int num = (i - (k - 1) * n);
            int r = num / (n - k + 1);
            int c = num % (n - k + 1) + k - 1;
            a[r][c] = i + 1;
        }
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += a[i][k - 1];
        }
        System.out.println(sum);
        print(n, a);
    }

    private static void print(int n, int[][] a) {
        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                sb.append(a[i][j] + " ");
            }
            System.out.println(sb.toString().trim());
        }
    }
}
