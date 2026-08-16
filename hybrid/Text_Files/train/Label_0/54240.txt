import java.util.*;
import java.io.*;

import static java.lang.System.in;

public class Main {
    public static void main(String[] args)throws IOException{
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long ans = solve(n);
        System.out.println(ans);
    }
    static long solve(long n){
        if(n==1) return 1;
        long hi = (n+1)/2, lo = 0;
        while(hi-lo>1){
            long mid = (hi+lo)/2;
            if(check(n,mid)) hi = mid;
            else lo = mid;
        }
        return hi;
    }
    static boolean check(long n, long k){
        long vas = 0,backup = n;
        while(n>0){
            vas +=  Math.min(k,n);
            n -= Math.min(k,n);
            n -= n/10;
        }
        return vas>=(backup+1)/2;
    }
}
