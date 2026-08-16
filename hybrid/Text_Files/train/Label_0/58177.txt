import java.io.*;
import java.util.*;

public class P604E {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] line = br.readLine().split(" ");
        int[] p = new int[n];
        for(int i=0; i<n; i++) {
            p[i] = Integer.parseInt(line[i]);
        }

        long pMult = 1;
        long sum = 0;
        long mod = 998244353;

        for(int i=0; i<n; i++) {
            sum = ((sum + pMult) * 100) % mod;
            pMult = (pMult * p[i]) % mod;
        }

        long inv = modInv(pMult, mod);
        long ans = (sum * inv) % mod;

        System.out.println(ans);
    }

    public static long modInv(long a, long mod) {
        long ret = 1;
        long mult = a;
        long k = mod - 2;

        while(k > 0) {
            if((k & 1) > 0)
                ret = (ret * mult) % mod;
            mult = (mult * mult) % mod;
            k >>= 1;
        }

        return ret;
    }
}
