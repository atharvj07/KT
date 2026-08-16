import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class C687 {
    static boolean dp[][][] = new boolean[555][555][555];

    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String in[] = br.readLine().trim().split(" ");
        int n = Integer.parseInt(in[0]);
        int k = Integer.parseInt(in[1]);
        //int a[] = new int [n];
        in = br.readLine().trim().split(" ");
//        for (int i=0;i<n;++i) {
//            a[i] = Integer.parseInt(in[i]);
//        }
        //Arrays.sort(a);

        dp[0][0][0] = true;

        for (int i=1;i<=n;++i){
            int x = Integer.parseInt(in[i-1]);
            for (int j = 0;  j<=k ; ++j){
                for (int l = 0; l<=j; ++l){
                    dp[i][j][l] = dp[i-1][j][l];
                    if (j>=x){
                        dp[i][j][l] |= dp[i-1][j-x][l];
                        if (l>=x){
                            dp[i][j][l] |= dp[i-1][j-x][l-x];
                        }
                    }
                    //System.out.println(dp[i][j][l]);
                }
            }
        }
        List<Integer>L=new ArrayList<>();
        for (int i=0;i<=k;++i){
            if (dp[n][k][i]) {
                L.add(i);
            }
        }
        System.out.println(L.size());
        for (int e:L){
            System.out.print(e+" ");
        }


//        solve(a, 0, k, 0);
//        for (int i=0;i<=500;++i){
//            if (store.containsKey(i)){
//                System.out.print(i + " ");
//            }
//        }
    }
}
