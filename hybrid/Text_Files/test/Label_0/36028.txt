import java.util.*;

public class SummerEarnings{
    static class Center{
        int x,y;
        Center(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
    static int n;
    static Center[] centers;
    static int[] hull;
    static int[][] distance, cache;

    static int sign(int i, int j) {
        int x = centers[j].x - centers[i].x;
        int y = centers[j].y - centers[i].y;
        return y < 0 || y == 0 && x < 0 ? -1 : 1;
    }
    static boolean check(int d) {
        for (int i = 0; i < n; i++)
            if (check(i, d))
                return true;
        return false;
    }
    static boolean check(int i, int dist) {
        int count = 0;
        for (int h = 0; h < n - i - 1; h++) {
            int j = cache[i][h];
            if (distance[i][j] >= dist)
                hull[count++] = j;
        }
        for (int h = 0, h1 = 0; h < count; h++) {
            if (h1 < h)
                h1 = h;
            int j = hull[h], k;
            while (h1 + 1 < h + count && cross(i, j, k = hull[(h1 + 1) % count]) <= 0) {
                h1++;
                if (distance[j][k] >= dist)
                    return true;
            }
        }
        return false;
    }
    static int cross(int i, int j, int k) {
        int x1=centers[j].x - centers[i].x;
        int y1=centers[j].y - centers[i].y;
        int x2=centers[k].x - centers[i].x;
        int y2=centers[k].y - centers[i].y;
        return x1 * y2 - x2 * y1;
    }

    public static void main(String[] args) {
        Scanner cin= new Scanner(System.in);
        n = cin.nextInt();
        centers= new Center[n];
        for (int i = 0; i < n; i++) {
            centers[i]= new Center(cin.nextInt(),cin.nextInt());
        }
        distance = new int[n][n];
        hull = new int[n - 1];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int x = centers[i].x - centers[j].x, y = centers[i].y - centers[j].y;
                distance[i][j] = distance[j][i] = x * x + y * y;
            }
        }
        cache = new int[n][];
        Integer[] jj = new Integer[n - 1];
        for (int i = 0; i < n; i++) {
            int m = n - i - 1;
            cache[i] = new int[m];
            for (int h = 0; h < m; h++)
                jj[h] = i + 1 + h;
            int i1 = i;
            Arrays.sort(jj, 0, m, (j1, j2) -> {
                int sign1 = sign(i1, j1), sign2 = sign(i1, j2);
                return sign1 != sign2 ? sign1 - sign2 : cross(i1, j1, j2);
            });
            for (int h = 0; h < m; h++)
                cache[i][h] = jj[h];
        }
        int lower = 0, upper = Integer.MAX_VALUE;
        while (upper - lower > 1) {
            int dist = (lower + upper) / 2;
            if (check(dist))
                lower = dist;
            else
                upper = dist;
        }
        System.out.println(Math.sqrt(lower) / 2);
    }
}
