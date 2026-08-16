import java.util.*;
class Main
{
    public static void main (String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        long[] A = new long[N];

        for(int i = 0; i < N; i++){
             A[i] = sc.nextInt() - i - 1;
        }
        Arrays.sort(A);

        long ans = 0;
        if(N % 2 == 1){
            ans = A[(N-1)/2];
        }
        else{
            ans = ( A[(N - 1) / 2] + A[(N + 1) / 2] ) / 2;
        }
        long res = 0;
        for(int i = 0; i < N; i++){
            res += Math.abs(A[i] - ans);
        }
        System.out.println(res);
    }

    
}