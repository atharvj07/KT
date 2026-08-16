import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        NumberFormat formatter = new DecimalFormat("#0.000000");

        int n = scanner.nextInt();
        int T = scanner.nextInt();
        double c = scanner.nextDouble();

        long summs[] = new long[n];

        double means[] = new double[n];

        int i1 = scanner.nextInt();

        summs[0] = i1;
        means[0] = i1 / (double) T / c;

        for (int i = 1; i < n; i++) {
            i1 = scanner.nextInt();
            means[i] = (means[i - 1] + i1 / (double) T) / c;
            summs[i] = summs[i - 1] + i1;

        }

        int m = scanner.nextInt();

        double reals[] = new double[m];
        double rmeans[] = new double[m];

        int j = scanner.nextInt();
        rmeans[0] = means[j - 1];

        if (j - T - 1 < 0) {
            reals[0] = (double) summs[j - 1] / T;
        } else {
            reals[0] = (double) (summs[j - 1] - Math.max(0, summs[j - T - 1])) / T;
        }
        System.out.println(formatter.format(reals[0]) + ' ' + formatter.format(rmeans[0]) + ' ' + formatter.format(Math.abs(rmeans[0] - reals[0]) / reals[0]));
        for (int i = 1; i < m; i++) {
            j = scanner.nextInt();
            reals[i] = (double) (summs[j - 1] - Math.max(0, summs[j - T - 1])) / T;
            rmeans[i] = means[j - 1];
            System.out.println(formatter.format(reals[i]) + ' ' + formatter.format(rmeans[i]) + ' ' + formatter.format(Math.abs(rmeans[i] - reals[i]) / reals[i]));
        }

        
    }
}