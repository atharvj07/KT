import java.util.*;
public class Main {
    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        double P [] = new double[N+1];
        double DP[][] = new double[N+1][N+1];
        for(int i=1;i<=N;i++){
            P[i]= sc.nextDouble();
            Arrays.fill(DP[i],0);
        }
        DP[0][0]=1;
        for(int i=1;i<=N;i++){
            for(int j=0;j<=i;j++){
                if(j>0)DP[i][j] = DP[i-1][j-1] * P[i]+DP[i-1][j]*(1-P[i]);
                else DP[i][j]=DP[i-1][j]*(1-P[i]);
            }
        }
        double opt = 0;
        for(int i=(N+1)/2;i<=N;i++) opt += DP[N][i];
        System.out.println(opt);
    }
}