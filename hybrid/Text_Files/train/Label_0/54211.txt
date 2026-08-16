import java.util.*;

class Main{

    void solve(){
        Scanner sc = new Scanner(System.in);

        int INF = 1<<27;

        while(true){
            int n = sc.nextInt(), m = sc.nextInt();
            if(n==0 && m==0) break;

            int[][] riku = new int[n][n];
            int[][] umi = new int[n][n];
            for(int i=0; i<n; i++){
                Arrays.fill(riku[i], INF);
                Arrays.fill(umi[i], INF);
            }


            for(int i=0; i<m; i++){
                int x = sc.nextInt()-1, y = sc.nextInt()-1;
                int t = sc.nextInt(); String s = sc.next();
                if(s.equals("L")){
                    riku[x][y] = Math.min(riku[x][y], t);
                    riku[y][x] = Math.min(riku[y][x], t);
                }else{
                    umi[x][y] = Math.min(umi[x][y], t);
                    umi[y][x] = Math.min(umi[y][x], t);
                }
            }

            for(int i=0; i<n; i++){
                riku[i][i] = 0;
                umi[i][i] = 0;
            }

            int r = sc.nextInt();
            int[] z = new int[r];
            for(int i=0; i<r; i++) z[i] = sc.nextInt()-1;

            for(int k=0; k<n; k++){
                for(int i=0; i<n; i++){
                    for(int j=0; j<n; j++){
                        riku[i][j] = Math.min(riku[i][j], riku[i][k] + riku[k][j]);
                        umi[i][j] = Math.min(umi[i][j], umi[i][k] + umi[k][j]);
                    }
                }
            }

            int[][] dp = new int[r][n];
            for(int i=0; i<r; i++) Arrays.fill(dp[i], INF);
            dp[0][z[0]] = 0;

            for(int k=0; k<r-1; k++){
                for(int i=0; i<n; i++){
                    if(dp[k][i]==INF) continue;
                    for(int j=0; j<n; j++){
                        dp[k+1][j] = Math.min(dp[k+1][j], 
                                              dp[k][i] + riku[z[k]][i] + umi[i][j] + riku[j][z[k+1]]);
                    }
                    dp[k+1][i] = Math.min(dp[k+1][i], dp[k][i] + riku[z[k]][z[k+1]]);
                }
            }

            int min = INF;
            for(int i=0; i<n; i++) min = Math.min(min, dp[r-1][i]);
            System.out.println(min);
        }
    }

    public static void main(String[] args){
        new Main().solve();
    }
}