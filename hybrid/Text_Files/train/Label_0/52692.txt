
import java.util.*;
public class Main {
    double [] p;
    
    private void doit(){
        //SHA KYO
        Scanner sc = new Scanner(System.in);
        while(true){
            int n = sc.nextInt();
            int m = sc.nextInt();
            if((n|m) == 0) break;
            p= new double[n];
            for(int i = 0; i < n; i++){
                p[i] = sc.nextDouble();
            }
            double ans = Integer.MIN_VALUE;
            for(int node0 = 0; node0 < n; node0++){
                double [][] dp = new double[m+1][n];
                for(int i = node0 ; i < n; i++){
                    dp[m][i] = area(i, node0);
                }
                
                for(int mi = m-1 ; mi >= 1; mi--){
                    for(int ni = node0; ni < n; ni++){
                        double max = Integer.MIN_VALUE;
                        for(int nj = ni + 1; nj < n; nj++){
                            max = Math.max(max, area(ni, nj) + dp[mi+1][nj]);
                        }
                        dp[mi][ni] = max;
                    }
                }
                ans = Math.max(ans, dp[1][node0]);
            }
            System.out.printf("%.6f\n",ans);
        }
    }
    
    private double area(int i, int j){
        return Math.sin((p[j] - p[i]) * 2 * Math.PI) / 2;
    }

    public static void main(String[] args) {
        Main obj = new Main();
        obj.doit();
    }
}