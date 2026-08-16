
import java.util.HashMap;
import java.util.Scanner;

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author duc
 */
public class CF70_C {
    static int reverseNumber(int n) {
        int m = 0;
        while (n > 0) {
            m = m * 10 + n%10;
            n/=10;
        }
        return m;
    }

    public static void main(String [] args) {
        Scanner in = new Scanner(System.in);

        int maxX, maxY, w;
        maxX = in.nextInt();
        maxY = in.nextInt();
        w = in.nextInt();

        int max = Math.max(maxX, maxY);
        int [] reverse = new int[max+1];
        for (int i = 1; i <= max; ++i) {
            reverse[i] = reverseNumber(i);
        }

        HashMap<Double, Integer> left = new HashMap<Double, Integer>();
        HashMap<Double, Integer> right = new HashMap<Double, Integer>();
        left.put(1.0, 1);

        long nLucky = 0;

        int bestArea = Integer.MAX_VALUE, bestX = -1, bestY = -1;

        int y;

        for (y = 1; y <= maxY; ++y) {
            double ratio = (double) reverse[y] / y;
            right.put(ratio, right.containsKey(ratio) ? (right.get(ratio) + 1) : 1);
            nLucky += left.containsKey(ratio) ? left.get(ratio) : 0;
            if (nLucky >= w) {
                if (y < bestArea) {
                    bestArea = y;
                    bestX = 1;
                    bestY = y;
                }
                break;
            }
        }
        if (y > maxY) {
            y = maxY;
        }

        for (int x = 2; x <= maxX; ++x) {
            double ratioLeft = (double) x / reverse[x];
            left.put(ratioLeft, left.containsKey(ratioLeft) ? (left.get(ratioLeft) + 1) : 1);
            nLucky += right.containsKey(ratioLeft) ? right.get(ratioLeft) : 0;
            while (true) {
                double ratioRight = (double) reverse[y] / y;
                int loss = left.containsKey(ratioRight) ? left.get(ratioRight) : 0;
                if (nLucky - loss >= w) {
                    right.put(ratioRight, right.get(ratioRight) - 1);
                    nLucky -= loss;
                    --y;
                } else {
                    break;
                }
            }
            if (nLucky >= w && x * y < bestArea) {
                bestArea = x * y;
                bestX = x;
                bestY = y;
            }
        }

        if (bestArea == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(bestX + " " + bestY);
        }
    }
}
