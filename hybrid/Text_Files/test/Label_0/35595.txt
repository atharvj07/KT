
import java.util.Scanner;

public class StringGeneration {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int tc = 0; tc < t; tc++) {
            int n = sc.nextInt();
            int l = sc.nextInt();
            int m = n / 3;
            int r = n % 3;
            String ans = "";
            for (int i = 0; i < m; i++) {
                ans += "abc";
            }
            if (r == 1)
                ans += "a";
            else if (r == 2)
                ans += "ab";
            System.out.println(ans);
        }
    }
}