import java.util.*;

public class Main {
    public static void main(String[] args) {
        int mod = 1000000007;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int[] s = new int[n];
        for(int i=0;i<n;i++) s[i] = sc.nextInt();
        Arrays.sort(s);
        int index = 0;
        long[] dp = new long[x+1];
        for(int v=0;v<x+1;v++) dp[v] = 0;
        for(int v=1;v<x+1;v++) {
            while(index < n && s[index] <= v) {
                index++;
            }
            // System.out.println(index);
            if(index == 0) {
                dp[v] = v%mod;
                // System.out.println(dp[v]);
            } else {
                for(int i=0;i<index;i++) {
                    int res = v%s[i];
                    dp[v] += dp[res];
                    dp[v] %= mod;
                }
            }
            if(index > 0) {
                int divideBy = modPow(index,mod-2,mod);
                dp[v] *= divideBy;
                dp[v] %= mod;
            }
        }
        int coeff = 1;
        for(int v=1;v<n+1;v++) {
            coeff = modProd(coeff,v,mod);
        }
        // long ans = dp[x] * coeff;
        int ans = modProd((int) dp[x],coeff,mod);
        // ans %= mod;
        System.out.println(ans);
        // System.out.println("dp table");
        // for(int v=0;v<x+1;v++) {
            // System.out.println(dp[v]);
        // }
        // int value = modPow(2, mod-2, mod);
        // int w = modProd(3,value,mod);

        // int y = modProd(w,(int) coeff,mod);
        // System.out.println(coeff);
        // System.out.println(w);
        // System.out.println(y);
    }
    public static int modProd(int x,int y,int mod){
        long xx = (long) x;
        long yy = (long) y;
        long v = xx * yy;
        v %= mod;
        return((int) v);
    }
    public static int modPow(int value,int exponent,int mod) {
        if (exponent == 0) return(1);
        if (exponent == 1) return(value%mod);
        long longValue = (long) value;
        int res = exponent%2;
        int q = exponent/2;
        long answer = 1;
        if(res == 1) answer *= longValue;
        longValue *= longValue;
        longValue %= mod;
        answer = (answer * ((long) modPow((int) longValue, q, mod)))%mod;
        return((int) answer);
    }
}   