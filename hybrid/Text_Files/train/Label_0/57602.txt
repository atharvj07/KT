import java.util.*;
import java.io.*;

public class TaskC {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int[] w = new int[n];
        int[] b = new int[m];
        for (int i = 0; i < n; i++) {
            w[i] = in.nextInt();
        }
        for (int i = 0; i < m; i++) {
            b[i] = in.nextInt() - 1;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            boolean[] existed = new boolean[n];
            int cur = 0;
            for (int j = 0; j < m; j++) {
                if (b[j] != i) {
                    if (!existed[b[j]]) {
                        cur += w[b[j]];
                        existed[b[j]] = true;
                    }
                } else {
                    ans += cur;
                    existed = new boolean[n];
                    cur = 0;
                }
            }
        }
        System.out.println(ans);
    }
}
