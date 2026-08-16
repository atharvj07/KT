import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        long MOD = 1_000_000_007;
        long ans = 1;
        int[] c = new int[3];
        for (int i = 0; i < n; i++) {
            long cnt = 0;
            int id = -1;
            if (a[i] == c[0]) {
                cnt++;
                id = 0;
            }
            if (a[i] == c[1]) {
                cnt++;
                id = 1;
            }
            if (a[i] == c[2]) {
                cnt++;
                id = 2;
            }
            if (id == -1) {
                System.out.println(0);
                return;
            }
            ans *= cnt;
            c[id]++;
            ans %= MOD;
        }
        System.out.println(ans);
    }

}
