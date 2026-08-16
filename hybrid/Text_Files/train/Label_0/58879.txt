import java.util.*;

class Main{

    void solve(){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(), m = sc.nextInt();
        int[] dist = new int[n+1];
        for(int i=2; i<=n; i++) dist[i] += dist[i-1] + sc.nextInt();
        int ans = 0;
        int pos = 1;
        for(int i=0; i<m; i++){
            int a = sc.nextInt();
            int np = pos + a;
            ans += dist[Math.max(pos, np)] - dist[Math.min(pos, np)];
            ans %= 100000;
            pos = np;
        }
        System.out.println(ans);
    }

    public static void main(String[] args){
        new Main().solve();
    }
}



        