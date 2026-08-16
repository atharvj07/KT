import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Locale;
import java.util.Scanner;

import static java.lang.Math.max;
import static java.lang.Math.min;

public class E {
    static int n, from, to;
    static int[] left, right;
    static double[][][] res;
    static double[][][][] allD;

    static void addSinglePlayer(double[][] d, int who, int done) {
        double len = right[who] - left[who];
        double downD = min(1, max(0, right[who] - to) / len);
        double upD = min(1, max(0, from - left[who]) / len);
        double hereD = (1 - upD - downD);
        for (int up = 0; up <= done + 1; up++) {
            d[up][done + 1 - up] = 0;
        }
        for (int up = done; up >= 0; up--) {
            for (int here = done - up; here >= 0; here--) {
                double p = d[up][here];
                d[up + 1][here] += p * upD;
                d[up][here + 1] += p * hereD;
                d[up][here] = p * downD;
            }
        }
    }

    static double[][] addTo(double[][] d, int from, int to, int done) {
        if (allD[from][to] == null) {
            int sz = done + to - from + 2;
            allD[from][to] = new double[sz][sz];
            for (int i = 0; i < sz; i++) {
                allD[from][to][i] = new double[sz - i];
            }
        }
        double[][] nd = allD[from][to];
        for (int i = 0; i < d.length; i++)
            System.arraycopy(d[i], 0, nd[i], 0, d[i].length);
        for (int who = from; who <= to; who++) {
            addSinglePlayer(nd, who, done++);
        }
        return nd;
    }

    static void calcAll(double[][] d, int from, int to, int done) {
        if (from == to) {
            calcFor(from, d);
            return;
        }
        int mid = (from + to) >> 1;
        double[][] dForRight = addTo(d, from, mid, done);
        calcAll(dForRight, mid + 1, to, done + (mid - from + 1));
        double[][] dForLeft = addTo(d, mid + 1, to, done);
        calcAll(dForLeft, from, mid, done + (to - mid));
    }

    static void calcFor(int player, double[][] d) {
        if (from >= right[player] || to <= left[player])
            return;
        double c = (to - from) * 1D / (right[player] - left[player]);
        for (int up = 0; up < n; up++) {
            for (int here = 0; here < n - up; here++) {
                res[player][up][here] += d[up][here] * c / (here + 1);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        Locale.setDefault(Locale.US);
        Scanner in = new Scanner(System.in);
        PrintWriter writer = new PrintWriter(System.out);
        n = in.nextInt();
        left = new int[n];
        right = new int[n];
        ArrayList<Integer> all = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            left[i] = in.nextInt();
            right[i] = in.nextInt();
            all.add(left[i]);
            all.add(right[i]);
        }
        Collections.sort(all);
        res = new double[n][n][n];
        allD = new double[n][n][][];
        for (int i = 0; i < all.size() - 1; i++) {
            from = all.get(i);
            to = all.get(i + 1);
            double[][] init = new double[][] { new double[] { 1, 0 }, new double[] { 0 } };
            calcAll(init, 0, n - 1, 0);
        }
        double[][] ans = new double[n][n];
        for (int player = 0; player < n; player++) {
            for (int up = 0; up < n; up++) {
                for (int here = 0; here < n - up; here++) {
                    for (int choose = 0; choose <= here; choose++) {
                        ans[player][up + choose] += res[player][up][here];
                    }
                }
            }
        }
        for (double[] vA : ans) {
            for (double v : vA) {
                writer.print(v + " ");
            }
            writer.println();
        }
        in.close();
        writer.close();
    }
}