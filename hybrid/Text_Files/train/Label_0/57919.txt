import java.util.*;

public class ArtUnion {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int p[][] = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++)
                p[i][j] = sc.nextInt();
        }
        int tt[] = new int[m];
        for (int i = 0; i < n; i++) {
            int done = 0;
            for (int j = 0; j < m; j++) {
                int t = (int) (Math.max(done, tt[j]));
                tt[j] = t + p[j][i];
                done = tt[j];
            }
        }
        for (int i = 0; i < m; i++)
            System.out.print(tt[i] + " ");
    }
}