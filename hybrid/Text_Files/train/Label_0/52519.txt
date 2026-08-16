import java.io.*;
import java.util.*;

public class A
{
    static int n, m, K;
    static int[][] arr;
    static char[] s;
    public static void main(String[] args) throws IOException
    {
        Flash f = new Flash();
        int T = 1;//f.ni();
        for(int tc = 1; tc <= T; tc++){
            n = f.ni(); m = f.ni(); K = f.ni();
            arr = new int[n+1][m+1];
            for(int i = 1; i <= n; i++){
                for(int j = 1; j <= m; j++) arr[i][j] = f.ni();
            }
            
            sop(fn());
        }
    }
    
    static long fn()
    {
        //dp to find the max value we can obtain for all mod values for all cnt values in a particular row
        //All the Integer.MIN_VALUE matters in both the dps
        long[][][][] dp = new long[n+1][m+1][m/2+1][K];
        for(long[][][] r : dp){
            for(long[][] c : r){
                for(long[] w : c){
                    Arrays.fill(w, Integer.MIN_VALUE);
                }
            }
        }
        
        for(int i = 1; i <= n; i++){
            dp[i][0][0][0] = 0;
            for(int j = 1; j <= m; j++){
                for(int k = m/2; k >= 0; k--){
                    for(int l = 0; l < K; l++){
                        dp[i][j][k][l] = Math.max(dp[i][j][k][l], dp[i][j-1][k][l]);
                        if(k == 0) continue;
                        dp[i][j][k][(l+arr[i][j])%K] = Math.max(dp[i][j][k][(l+arr[i][j])%K], dp[i][j-1][k-1][l] + arr[i][j]);
                    }
                }
            }
        }
        
        //dp to connect different rows
        long[][] dp2 = new long[n+1][K];
        for(int i = 0; i <= n; i++){
            for(int j = 0; j < K; j++){
                dp2[i][j] = Integer.MIN_VALUE;
            }
        }
        
        dp2[0][0] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 0; j < K; j++){
                for(int k = 0; k < K; k++){
                    long row = Integer.MIN_VALUE;//Think well why this matters..!!
                    for(int l = 0; l <= m/2; l++) row = Math.max(row, dp[i][m][l][k]);
                    //if(j == 0) sop("ROW :" + i + " MOD :" + k + " MAX :" + row);
                    dp2[i][(j+k)%K] = Math.max(dp2[i][(j+k)%K], row+dp2[i-1][j]);
                }
            }
        }
        
        long ans = 0;
        for(int i = 1; i <= n; i++) ans = Math.max(ans, dp2[i][0]);
        return ans;
    }
    
    static void sort(int[] a){
        List<Integer> A = new ArrayList<>();
        for(int i : a) A.add(i);
        Collections.sort(A);
        for(int i = 0; i < A.size(); i++) a[i] = A.get(i);
    }
    
    static int swap(int itself, int dummy){
        return itself;
    }
    
    static void sop(Object o){ System.out.println(o); }
    
    static void print(int[] a){
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < a.length; i++) sb.append(a[i] + " ");
        System.out.println(sb);
    }
    
    static class Flash
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        
        String next(){
            while(!st.hasMoreTokens()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch(IOException e){
                    e.printStackTrace();
                }
            }
            
            return st.nextToken();
        }
        
        String ns(){
            String s = new String();
            try{
                s = br.readLine().trim();
            }catch(IOException e){
                e.printStackTrace();
            }
            
            return s;
        }
        
        int ni(){
            return Integer.parseInt(next());
        }
        
        int[] arr(int n){
            int[] a = new int[n];
            for(int i = 0; i < n; i++) a[i] = ni();
            return a;
        }

        long nl(){
            return Long.parseLong(next());
        }
        
        double nd(){
            return Double.parseDouble(next());
        }
    }
}