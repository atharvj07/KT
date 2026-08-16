/*
 * 配るDP
 */
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();
        // A[i]：i円引き出す時の最小回数。
        int[] A = new int[N+1];
        Arrays.fill(A, N);
        A[0] = 0;
        for(int n = 0; n <= N; n++){
            for(int i = 1; n+i <= N; i*=6){
                A[n+i] = Math.min(A[n+i], A[n]+1);
            }
            for(int i = 1; n+i <= N; i*=9){
                A[n+i] = Math.min(A[n+i], A[n]+1);
            }
        }
        System.out.println(A[N]);
    }

}
