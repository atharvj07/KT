/**
 * Created by IntelliJ IDEA.
 * User: Taras_Brzezinsky
 * Date: 8/13/11
 * Time: 6:10 PM
 * To change this template use File | Settings | File Templates.
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;
import java.io.IOException;

public class DarkAssembly extends Thread {

    public DarkAssembly() {
        this.input = new BufferedReader(new InputStreamReader(System.in));
        this.output = new PrintWriter(System.out);
        this.setPriority(Thread.MAX_PRIORITY);
    }

    static class Senator {
        int loyalty;
        int level;

        public Senator(int level, int loyalty) {
            this.level = level;
            this.loyalty = loyalty;
        }
    }

    private static double doIt(Senator[] senators, int A) {
        double probability = .0;
        for (int mask = 0; mask < (1 << senators.length); ++mask) {
            int sum = A;
            double current = 1.0;
            for (int i = 0; i < senators.length; ++i) {
                if ((mask & (1 << i)) != 0) {
                    current *= .01 * senators[i].loyalty;
                } else {
                    current *= .01 * (100 - senators[i].loyalty);
                    sum += senators[i].level;
                }
            }
            if (getOnes(mask) > senators.length / 2) {
                probability += current;
            } else {
                probability += current * (double)A / sum;
            }
        }
        return probability;
    }

    private static double go(Senator []senators, int candies, int A, int current) {
        if (current == senators.length) {
            return doIt(senators, A);
        } else {
            double result = go(senators, candies, A, current + 1);
            if (candies > 0 && senators[current].loyalty < 100) {
                senators[current].loyalty += 10;
                result = Math.max(result, go(senators, candies - 1, A, current));
                senators[current].loyalty -= 10;
            }
            return result;
        }        
    }



    static int getOnes(int mask) {
        int result = 0;
        while (mask != 0) {
            mask &= mask - 1;
            ++result;
        }
        return result;
    }

    public void run() {
        try {
            int n = nextInt();
            int k = nextInt();
            int A = nextInt();
            Senator[] senators = new Senator[n];
            for (int i = 0; i < n; ++i) {
                senators[i] = new Senator(nextInt(), nextInt());
            }
            output.printf("%.10f", go(senators, k, A, 0));

            output.flush();
            output.close();

        } catch (Throwable e) {
            System.err.println(e.getMessage());
            System.err.println(Arrays.deepToString(e.getStackTrace()));
        }
    }


    public static void main(String[] args) {
        new DarkAssembly().start();
    }

    private String nextToken() throws IOException {
        while (tokens == null || !tokens.hasMoreTokens()) {
            tokens = new StringTokenizer(input.readLine());
        }
        return tokens.nextToken();
    }

    private int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    private double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }

    private long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }


    private BufferedReader input;
    private PrintWriter output;
    private StringTokenizer tokens = null;
}
