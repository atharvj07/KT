import java.util.Scanner;

public class Main {
    private static double[] p;
    private static double[] q;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        p = new double[n+1];
        q = new double[n+1];
        for (int i = 1; i <= n; i++) {
            p[i] = in.nextDouble();
        }
        for (int i = 0; i <= n; i++) {
            q[i] = in.nextDouble();
        }
        System.out.println(minimumCost());
    }

    private static double minimumCost() {
        int n = p.length - 1;
        double[][] weight = new double[n+2][n+1];
        double[][] cost = new double[n+2][n+1];

        for (int i = 1; i <= n + 1; i++) {
            weight[i][i-1] = q[i-1];
            cost[i][i-1] = q[i-1];
        }

        for (int size = 1; size <= n; size++) {
            for (int i = 1; i <= n - size + 1; i++) {
                int j = i + size - 1;
                cost[i][j] = Double.MAX_VALUE;
                weight[i][j] = weight[i][j-1] + p[j] + q[j];
                for (int r = i; r <= j; r++) {
                    double testCost = cost[i][r-1] + cost[r + 1][j] + weight[i][j];
                    if (testCost < cost[i][j]) {
                        cost[i][j] = testCost;
                    }
                }
            }
        }
        return cost[1][n];
    }
}


