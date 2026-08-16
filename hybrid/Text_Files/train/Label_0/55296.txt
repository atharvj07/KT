import java.util.*;

class Main{

    void solve(){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] P = new int[N];
        for ( int i = 0; i < N; i++ ) P[i] = sc.nextInt();

        int ans = 0;
        for ( int A = 0; A <= 100; A++ ){
            int cnt = 0;
            for ( int i = 0; i < N; i++ ){
                if ( A <= P[i] ) cnt++;
            }
            if ( A <= cnt ) ans = A;
        }

        System.out.println(ans);
    }

    public static void main(String[] a){
        new Main().solve();
    }
}

