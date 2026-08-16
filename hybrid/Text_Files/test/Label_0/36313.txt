import java.util.Scanner;

public class Omkar {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        while (t-- > 0) {
            int n = in.nextInt();
            int[] qus = new int[n];
            for (int i = 0; i < qus.length; i++) {
                qus[i] = in.nextInt();
            }
            long ans = 0;
            for (int i = 1; i < n; i++) {
                ans += Math.max(qus[i-1] - qus[i], 0);
            }
            System.out.println(ans);

        }
    }


}
