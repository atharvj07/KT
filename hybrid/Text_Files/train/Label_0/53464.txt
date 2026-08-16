import java.io.*;
import java.util.*;

public class Main {
    Scanner sc;

    void run() {
        sc = new Scanner(System.in);
        int t = sc.nextInt();
        double[] exp_value = new double[t];

        for (int i = 0; i < t; i++) {
            // 使えるダイス
            int n = sc.nextInt();
            int m = sc.nextInt();
            double zero_pos = 1.0;
            for (int j = 0; j < m; j++) {
                int v = sc.nextInt();
                double r = sc.nextDouble();
                exp_value[i] += v * r;
                zero_pos -= r;
            }
            exp_value[i] *= 1.0 / (1.0 - zero_pos);
        }

        // 班長のダイス
        int p = sc.nextInt();
        int q = sc.nextInt();
        double leader_exp_value = 0.0;
        double leader_zero_pos = 1.0;
        for (int j = 0; j < q; j++) {
            int v = sc.nextInt();
            double r = sc.nextDouble();
            leader_exp_value += v * r;
            leader_zero_pos -= r;
        }
        leader_exp_value *= 1.0 / (1.0 - leader_zero_pos);

        boolean exist = false;
        for (int i = 0; i < t; i++) {
            if (exp_value[i] > leader_exp_value + 0.0000001) {
                exist = true;
                break;
            }
        }
        if (exist) System.out.println("YES");
        else System.out.println("NO");
    }

    public static void main(String[] args) {
        new Main().run();
    }
}