import java.util.*;

public class Main {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();

        if (b - a <= 2) {
            System.out.println(k + 1);
            return;
        } else {
            // A回目からスタート
            long ans = a;
            for (int i = a - 1; i < k; i += 2) {
                if (i + 2 > k) {
                    ans += 1;
                    i--;
                } else {
                    ans -= a;
                    ans += b;
                }
            }
            System.out.println(ans);
        }

    }

}
