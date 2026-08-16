import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int m = 1;
        while (true) {
            int n = sc.nextInt();
            if (n == 0)
                break;
            int[][] map = new int[n][n];
            int dx[] = { 1, -1, 0, 1 };
            int dy[] = { 0, 1, 1, -1 };
            int x = 0;
            int y = 0;
            int c = 1;
            int d = 0;
            while (true) {
                map[y][x] = c;
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (x == n - 1 && y == n - 1)
                    break;
                if (nx >= n) {
                    d = 2;
                    nx = x + dx[d];
                    ny = y + dy[d];
                    d = 1;
                } else if (ny < 0) {
                    d = 0;
                    nx = x + dx[d];
                    ny = y + dy[d];
                    d = 1;
                } else if (ny >= n) {
                    d = 0;
                    nx = x + dx[d];
                    ny = y + dy[d];
                    d = 3;
                } else if (nx < 0) {
                    d = 2;
                    nx = x + dx[d];
                    ny = y + dy[d];
                    d = 3;
                }
                if (c == 1)
                    d = 1;

                x = nx;
                y = ny;
                c++;
            }
            System.out.println("Case " + m + ":");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.printf("%3d",map[i][j]);
                }
                System.out.println();
            }
            m++;
        }
    }
}