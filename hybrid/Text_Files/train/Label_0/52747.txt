import java.util.*;

public class CF209A {
    static long M = 1000L*1000*1000+7;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        g = new long[n+1];
        Arrays.fill(g, -1);
        System.out.println(f(n));
    }

    public static long f(int n) {
        if(n==1) return 1;
        return (f(n-1) + g(n-1))%M;
    }

    static long[] g;
    public static long g(int n) {
        if(n == 0) return 1;
        if(n == 1) return 2;
        if(g[n] > -1) return g[n];
        return g[n] = (g(n-1) + g(n-2))%M;
    }
}
