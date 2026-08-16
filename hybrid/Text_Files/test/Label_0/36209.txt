import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class C {

    public static void main(String[] args) {

        Scanner I = new Scanner(new BufferedReader(new InputStreamReader(System.in)));

        int t = I.nextInt();
        while (t > 0) {
            t--;
            int n = I.nextInt();
            long sum = solve(n);
            System.out.println(sum);

        }

        //System.out.println(solve(5));

    }

    private static long solve(int n) {
        long sum = 0, d = 1;
        int i = n / 2 + 1, H = 3;
        for (; i <n; i++) {
            long x = 0;
            if (i > 1) {
                x = H * 2 + (H - 2) * 2;
                sum += (x * d);
                d++;
                H += 2;
            }

        }
        return sum;
    }

    private static void error(String msg) {

        throw new RuntimeException(msg);
    }
}
