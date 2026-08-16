import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        SqueezeTheCylinders solver = new SqueezeTheCylinders();
        solver.solve(1, in, out);
        out.close();
    }

    static class SqueezeTheCylinders {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            double[] r = new double[n];
            for (int i = 0; i < n; i++) {
                r[i] = in.nextDouble();
            }
            double[] center = new double[n];
            Arrays.fill(center, -1e9);
            center[0] = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < i; j++) {
                    center[i] = Math.max(center[i], center[j] + Math.sqrt((r[i] + r[j]) * (r[i] + r[j]) - (r[i] - r[j]) * (r[i] - r[j])));
                }
            }
            double L = 1e9, R = -1e9;
            for (int i = 0; i < n; i++) {
                //System.err.println(center[i]);
                L = Math.min(L, center[i] - r[i]);
                R = Math.max(R, center[i] + r[i]);
            }
            out.printf("%.8f\n", R - L);
        }

    }
}