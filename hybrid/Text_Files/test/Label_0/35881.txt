

import java.util.Arrays;
import java.util.Scanner;

public class Main {

	private static Scanner in;

    private static int n;
    private static int[] a;
    private static double[][][] dp;

    public static void main(String[] args) {
        in = new Scanner(System.in);
        n = in.nextInt();
        a = new int[n];

        for(int i=0; i<n; i++) a[i] = in.nextInt();

        dp = new double[n+1][n+1][n+1];

        for(int i=0; i<n+1; i++) {
        	for(int j=0; j<n+1; j++) {
        		Arrays.fill(dp[i][j], -1);
        	}
        }
        
        int one=0;
        int two=0;
        int three=0;

        for(int i=0; i<n; i++) {
            switch(a[i]) {
	            case 1: one++; break;
	            case 2: two++; break;
	            case 3: three++; break;
                default:
                    break;
            }
        }

        System.out.println(solve(one, two, three));

    }

    private static double solve(int one, int two, int three) {
        if (one<0 || two<0 || three<0) return 0;

        if (one+two+three==0) return 0;

        if (dp[one][two][three]!=-1) return dp[one][two][three];

        double A = one*1.0/n*solve(one-1, two, three);
        double B = two*1.0/n*solve(one+1, two-1, three);
        double C = three*1.0/n*solve(one, two+1, three-1);

        return dp[one][two][three] = n*(1+A+B+C)/(one+two+three);

    }

}
