import java.util.*;

public class B {

    static int solve(char c[], int n, int x, int y) {
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int cur = c[i] - '0';
            if (cur == x) {
                ans++;
                int temp = x;
                x = y;
                y = temp;
            }
        }
        if (x != y && ans % 2 != 0) {
            --ans;
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int testCases = sc.nextInt();
        sc.nextLine();
        for (int t = 0; t < testCases; t++) {
            String str = sc.nextLine();
            char c[] = str.toCharArray();
            int n = c.length;
            if (n == 1) {
                sb.append("0").append("\n");
                continue;
            }
            HashSet<Integer> set = new HashSet<>();
            for (int i = 0; i < n; i++) {
                int cur = c[i] - '0';
                if (!set.contains(cur)) {
                    set.add(cur);
                }
            }
            if (set.size() == 1) {
                sb.append("0").append("\n");
                continue;
            }
            int max = Integer.MIN_VALUE;
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    max = Math.max(max, solve(c, n, i, j));
                }
            }
            sb.append(n - max).append("\n");
        }
        System.out.print(sb);
    }
}