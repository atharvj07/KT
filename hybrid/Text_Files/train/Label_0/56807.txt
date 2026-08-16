import java.util.*;
import java.lang.*;


public class Main {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] B = new int[N+1];
        for(int n=1; n<N; n++) B[n]=sc.nextInt();
        B[0] = B[1];
        B[N] = B[N-1];

        long ans = 0;

        for(int n=0; n<N; n++) ans += Math.min(B[n], B[n+1]);

        System.out.println(ans);

    }
}
