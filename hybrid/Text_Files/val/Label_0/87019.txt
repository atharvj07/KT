import java.io.*;
import java.util.*;

class Main{

    static final int M = 1000000007;
    static final int N_MAX = 200000;
    long[]  fact;
    Scanner sc;

    void compute(int N, int H){
        int[] word = new int[N];
        boolean[] invalid = new boolean[N];

        for ( int i = 0; i < N; i++ ) word[i] = i;
        int s, t;
        for ( int i = 0; i < H; i++ ){
            s = sc.nextInt();
            t = sc.nextInt();
            s--; t--; // to 0 origin
            int tmp = word[s];
            word[s] = word[t];
            word[t] = tmp;
        }

        for ( int i = 0; i < N; i++ ) if ( word[i] != i ) invalid[i] = true;

        long ans = 0;
        ArrayList<Integer> deleted = new ArrayList<Integer>();
        ArrayList<Integer> inserted = new ArrayList<Integer>();

        for ( int i = 0; i < N; i++ ){
            long unable = Math.min(word[i], i);
            for ( int j = 0; j < deleted.size(); j++ )
                if ( deleted.get(j) < word[i] ) unable--;
            for ( int j = 0; j < inserted.size(); j++ )
                if ( inserted.get(j) < word[i] ) unable++;

            ans += ((word[i] - unable) * fact[N-i-1])%M;
            ans %= M;

            if ( invalid[i] ){
                deleted.add(i);
                inserted.add(word[i]);
            }
        }

        System.out.println(ans);
    }
 void solve(){
        fact = new long[N_MAX+1];
        fact[0] = 1;
        for ( int i = 1; i <= N_MAX; i++ ) fact[i] = (fact[i-1]*i)%M;
        sc = new Scanner(System.in);

        int N, H;
        while(true){
            N = sc.nextInt();
            if ( N == 0 ) break;
            H = sc.nextInt();
            compute(N, H);
        }
    }

    public static void main(String[] arfv){
        new Main().solve();
    }
}


