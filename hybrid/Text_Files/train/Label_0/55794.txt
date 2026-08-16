import java.io.*;
import java.util.*;

public class GameOnPaper {
    public static void main(String[] args) throws IOException {
        BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(f.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        boolean[][] a = new boolean[n+4][n+4];
        for (int t = 1; t <= m; t++) {
            st = new StringTokenizer(f.readLine());
            int x = Integer.parseInt(st.nextToken())+1;
            int y = Integer.parseInt(st.nextToken())+1;
            a[x][y] = true;
            for (int i = -1; i <= 1; i++)
                for (int j = -1; j <= 1; j++) {
                    boolean b = true;
                    for (int dx = -1; dx <= 1; dx++)
                        for (int dy = -1; dy <= 1; dy++)
                            if (!a[x+i+dx][y+j+dy])
                                b = false;
                    if (b) {
                        System.out.println(t);
                        return;
                    }
                }
        }
        System.out.println(-1);
    }
}