import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while (scan.hasNext()) {
            int n = scan.nextInt();
            int m = scan.nextInt();
            char[][] res = new char[101][101];
            for (int i = 0; i < n; ++i) {
                if (i % 2 == 0) {
                    for (int j = 0; j < m; ++j) {
                        res[i][j] = '#';
                    }
                } else if (i % 4 == 1) {
                    for (int j = 0; j < m; ++j) {
                        res[i][j] = '.';
                    }
                    res[i][m - 1] = '#';
                } else {
                    for (int j = 0; j < m; ++j) {
                        res[i][j] = '.';
                    }
                    res[i][0] = '#';
                }
            }
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    System.out.print(res[i][j]);
                }
                System.out.println("");
            }
        }
    }
}
