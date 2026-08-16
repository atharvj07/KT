import java.io.PrintWriter;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        int n = in.nextInt();
        int m = in.nextInt();
        char[][] a = new char[n][m];
        boolean[] has_w = new boolean[n];
        in.nextLine();

        for (int i = 0; i < n; i++) {
            String s = in.nextLine();

            for (int j = 0; j < s.length(); j++) {
                a[i][j] = s.charAt(j);
                if (a[i][j] == 'W')
                    has_w[i] = true;
            }
        }

        int ans = 0;
        int state = 1; // 1 - right, 2 - left
        int prev_state = 1;
        int cur_j = 0;
        int cur_i = 0;

        if (has_w[0]) {
            int right = 0;
            for (int j = 0; j < m; j++) {
                if (a[0][j] == 'W')
                    right = j;
            }
            ans += right;
            cur_j = right;
        }

        while (true) {
            int non_empty = cur_i;

            do {
                non_empty++;
                state = state == 1 ? 2 : 1;
            } while (non_empty < n && !has_w[non_empty]);

            if (non_empty == n)
                break;

            int left = m;
            int right = 0;
            for (int j = 0; j < m; j++)
                if (a[non_empty][j] == 'W') {
                    left = Math.min(j, left);
                    right = Math.max(j, right);
                }

            if (prev_state == 1 && state == 1) {
                if (cur_j > left) {
                    ans += cur_j - left;
                    cur_j = left;
                    ans += right - left;
                    cur_j = right;
                } else {
                    ans += right - cur_j;
                    cur_j = right;
                }
            } else if (prev_state == 2 && state == 2) {
                if (cur_j < right) {
                    ans += right - cur_j;
                    cur_j = right;
                    ans += right - left;
                    cur_j = left;
                } else {
                    ans += cur_j - left;
                    cur_j = left;
                }
            } else if (prev_state == 1 && state == 2) {
                if (cur_j < right) {
                    ans += right - cur_j;
                    cur_j = right;
                    ans += right - left;
                    cur_j = left;
                } else {
                    ans += cur_j - left;
                    cur_j = left;
                }
            } else {
                if (cur_j > left) {
                    ans += cur_j - left;
                    cur_j = left;
                    ans += right - left;
                    cur_j = right;
                } else {
                    ans += right - cur_j;
                    cur_j = right;
                }
            }
            ans += non_empty - cur_i;
            cur_i = non_empty;

            prev_state = state;
        }

        out.print(ans);
        out.close();
    }
}
