import java.util.*;
import java.io.*;

public class program {
    public static void main (String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(in.readLine());
        long n = Long.parseLong(stk.nextToken());
        long p = Long.parseLong(stk.nextToken());
        long m = Long.parseLong(stk.nextToken());
        long d, t, ans = 0, pst = 1, blc = 0, dn;
        for (long i = 1; i <= n; i++) {
            stk = new StringTokenizer(in.readLine());
            d = Long.parseLong(stk.nextToken());
            t = Long.parseLong(stk.nextToken());
            if (blc >= 0) dn = blc / p;
            else dn = 0;
            if (pst + dn < d) ans += d - (pst + dn);
            blc -= p * (d - pst);
            blc += t;
            pst = d;
        }
        if (blc >= 0) dn = blc / p;
        else dn = 0;
        if (pst + dn <= m) ans += m - (pst + dn) + 1;
        System.out.println(ans);
    }
}
