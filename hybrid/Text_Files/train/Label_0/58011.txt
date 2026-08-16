
import java.util.Scanner;

public class Main {
    public static void main(String [] args) {
        Scanner scanner = new Scanner(System.in);
        int h = scanner.nextInt();
        int w = scanner.nextInt();
        int [][] a = new int[h][w];
        int [][] b = new int[h][w];
        for(int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                a[i][j] = scanner.nextInt();
            }
        }
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                b[i][j] = scanner.nextInt();
            }
        }
        boolean[][][] dp = new boolean[2][w][13000];
        dp[0][0][Math.abs(a[0][0] - b[0][0])] = true;
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                if (i == 0 && j == 0) {
                    continue;
                }
                int diff = Math.abs(a[i][j] - b[i][j]);
                for (int k = 0; k <= 12800; ++k) {
                    dp[i%2][j][k] = false;
                }
                for (int k = 0; k <= 12800; ++k) {
                    if (i > 0 && dp[(i + 1) % 2][j][k]) {
                        dp[i % 2][j][Math.abs(k + diff)] = true;
                        dp[i % 2][j][Math.abs(k - diff)] = true;
                    }
                    if (j > 0 && dp[i % 2][j - 1][k]) {
                        dp[i % 2][j][Math.abs(k + diff)] = true;
                        dp[i % 2][j][Math.abs(k - diff)] = true;
                    }
                }
            }
        }
        for (int k = 0; k <= 12800; ++k) {
            if (dp[(h - 1) % 2][w - 1][k]) {
                System.out.println(k);
                return;
            }
        }
    }
}
