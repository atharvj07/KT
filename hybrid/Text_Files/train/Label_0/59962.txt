import java.util.*;

public class Main {

    static final int MOD = 1000000007;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long t[]= new long[n];
        for(int i=0;i<n;i++)t[i]=sc.nextLong();
        for(int i=1;i<n;i++){
            t[i]=lcm(t[i],t[i-1]);
        }
        System.out.println(t[n-1]);

    }

    private static long gcd(long a,long b){
        if(b==0)return a;
        return gcd(b,a%b);
    }
    private static long lcm(long a,long b){
        return (a/gcd(a,b))*b;
    }
}
