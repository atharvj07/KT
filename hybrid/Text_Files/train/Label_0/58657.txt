/*-
 * Codeforces problem :
 * http://codeforces.com/problemset/problem/645/G
 *
 * Find the number of distinct possible suffixes of length 2 or 3 for a
 * given string with minimum length 4 or more.
 * Two identical suffixes should not be appended. 
 * 
 */

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * @author Karthik Venkataraman
 * @email kafy83@gmail.com
 */
public class MaxDiffEuclideanDistance {

    static class InputReader {

        private static final int inputKb = 5 * 1024;
        private final BufferedReader bufferedReader;
        private StringTokenizer stringTokenizer;

        InputReader(InputStream stream) {
            bufferedReader = new BufferedReader(new InputStreamReader(stream), inputKb);
        }

        private String readNext() {
            while (stringTokenizer == null || !stringTokenizer.hasMoreTokens()) {
                try {
                    stringTokenizer = new StringTokenizer(bufferedReader.readLine());
                } catch (IOException ex) {
                    throw new IllegalArgumentException(ex);
                }
            }
            return stringTokenizer.nextToken();
        }

        private int nextInt() {
            return Integer.parseInt(readNext());
        }
    }

    static class Point {

        private double x;
        private double y;

        //w.r.t (a,0)
        private double xa;
        private double ya;
        private double da;
        private double ra;
        private double theta;

        Point(double x, double y, double a) {
            this.x = x;
            this.y = y;
            this.xa = (x - a) / 2;
            this.ya = y / 2;
            this.da = Math.sqrt(xa * xa + ya * ya);
            this.ra = Math.sqrt((xa + a) * (xa + a) + ya * ya);
            this.theta = Math.atan2(ya, xa);
        }
    }

    static class Angle implements Comparable<Angle> {

        private double angleInRad;
        private int pointIdx;

        public Angle(double angleInRad, int pointIdx) {
            this.angleInRad = angleInRad;
            this.pointIdx = pointIdx;
        }

        @Override
        public int hashCode() {
            int hash = 5;
            hash = 79 * hash + (int) (Double.doubleToLongBits(this.angleInRad) ^ (Double.doubleToLongBits(this.angleInRad) >>> 32));
            hash = 79 * hash + this.pointIdx;
            return hash;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj == null) {
                return false;
            }
            if (getClass() != obj.getClass()) {
                return false;
            }
            final Angle other = (Angle) obj;
            if (Double.doubleToLongBits(this.angleInRad) != Double.doubleToLongBits(other.angleInRad)) {
                return false;
            }
            if (this.pointIdx != other.pointIdx) {
                return false;
            }
            return true;
        }

        public int getPointIdx() {
            return pointIdx;
        }

        @Override
        public int compareTo(Angle that) {
            Angle angle1 = this;
            Angle angle2 = that;
            double d1 = angle1.angleInRad;
            double d2 = angle2.angleInRad;
            if (d1 > d2) {
                return 1;
            }
            if (d2 > d1) {
                return -1;
            }
            long d1bits = Double.doubleToLongBits(d1);
            long d2bits = Double.doubleToLongBits(d2);
            return (d1bits == d2bits) ? 0 : (d1bits > d2bits) ? 1 : -1;
        }
    }

    static class AngleStack {

        private Angle[] stack;
        private int sz;

        AngleStack(int capacity) {
            stack = new Angle[capacity];
        }

        public void pushIfDifferentPoint(Angle x) {
            if (sz > 0 && stack[sz - 1].getPointIdx() == x.getPointIdx()) {
                stack[sz - 1] = null;
                sz--;
            } else {
                stack[sz++] = x;
            }
        }

        public void resetStack() {
            sz = 0;
        }

        public boolean isEmpty() {
            return sz == 0;
        }
    }

    private int a;
    private int n;
    private Angle[] angle;
    private AngleStack angleStack;
    private Point[] points;

    private double make2Quad(double d) {
        while (d >= Math.PI) {
            d -= 2 * Math.PI;
        }
        while (d < -Math.PI) {
            d += 2 * Math.PI;
        }
        return d;
    }

    private void input() {
        InputReader sc = new InputReader(System.in);
        n = sc.nextInt();
        points = new Point[n];
        angle = new Angle[2 * n];
        angleStack = new AngleStack(2 * n);
        a = sc.nextInt();
        for (int i = 0; i < n; i++) {
            points[i] = new Point(sc.nextInt(), sc.nextInt(), a);
        }
    }

    private void compute() {
        double lo = 0.0;
        double hi = 2 * a;
        while (hi - lo > Math.max(1, hi) * 1e-9) {
            double mid = (lo + hi) / 2;
            double rvar = mid / 2;
            int idx = 0;
            boolean isVeryLargeGuess = false;
            for (int i = 0; i < n; i++) {
                if (points[i].da + points[i].ra <= rvar) {
                    hi = mid;
                    isVeryLargeGuess = true;
                    break;
                }
                /*-
                 * distance between two polar coordinates (r1, theta1)
                 * and (r2, theta2)
                 * 
                 *  d = sqrt(r1^2+r2^2-2*r^1*r^2*cos(theta1-theta2))
                 *
                 *  ra^2 = da^2+rvar^2-2*da*rvar*cos(theta1-theta2))
                 *  
                 * cos (difference of polar angle between da and rvar) =
                 * (da^2+rvar^2-ra^2)/2*da*rvar
                 * 
                 * 
                 * polar angle of point + (difference of polar angle between da and rvar)
                 * polar angle of point - (difference of polar angle between da and rvar)
                 * 
                 */
                double cosaInRad = (points[i].da * points[i].da + rvar * rvar - points[i].ra * points[i].ra) / (2 * points[i].da * rvar);
                if (cosaInRad < 1 && cosaInRad > -1) {
                    double alphaDiffInRad = Math.acos(cosaInRad);
                    double thetaPlusAlpha = make2Quad(points[i].theta + alphaDiffInRad);
                    double thetaMinusAlpha = make2Quad(points[i].theta - alphaDiffInRad);
                    angle[idx++] = new Angle(thetaPlusAlpha, i);
                    angle[idx++] = new Angle(thetaMinusAlpha, i);
                }
            }
            if (isVeryLargeGuess) {
                continue;
            }
            angleStack.resetStack();
            Arrays.sort(angle, 0, idx);
            /*
             * Increase the guess if sorting angle puts  
             * same point's distance to a and -a next to each other.
             * else decrease the guess;
             */
            for (int i = 0; i < idx; i++) {
                angleStack.pushIfDifferentPoint(angle[i]);
            }
            if (angleStack.isEmpty()) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        System.out.println(String.format("%.15f", hi));
    }

    public static void main(String[] args) {
        MaxDiffEuclideanDistance maxDiffEuclideanDistance = new MaxDiffEuclideanDistance();
        maxDiffEuclideanDistance.input();
        maxDiffEuclideanDistance.compute();
    }
}
