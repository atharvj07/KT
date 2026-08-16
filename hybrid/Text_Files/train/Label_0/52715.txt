import java.io.PrintWriter;
import java.util.*;

public class Main {

    private static long gcd(long a, long b) {
        if ( a== 0)return b;
        return gcd(b % a, a);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        long p = in.nextLong(),q = in.nextLong();
        //while (p > 0) {
            q /= gcd(p, q);
            long ans = 1;
            for (long i = 2; i * i <= q; i++) {
                if (q % i != 0) continue;
                ans *= i;
                while (q % i == 0) {
                    q /= i;
                }
            }
            ans *= q;
            out.println(ans);

            //p = in.nextLong();
            //q = in.nextLong();
        //}
        out.flush();
    }

}

