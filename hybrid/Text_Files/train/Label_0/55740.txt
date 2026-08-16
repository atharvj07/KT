import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        new Solver().solve(new Scanner(System.in));
//        new Solver().solve(new Scanner(ex));
    }

    private static final String ex = "7 0 0 0\n" +
            "200\n" +
            "23 39\n" +
            "-2 22\n" +
            "-36 33\n" +
            "-28 -11\n" +
            "-37 17\n" +
            "-3 -19\n" +
            "-49 -5\n" +
            "18 -29\n" +
            "0 -20\n" +
            "40 -24\n" +
            "8 3\n" +
            "-33 16\n" +
            "-44 6\n" +
            "49 45\n" +
            "-49 -23\n" +
            "14 39\n" +
            "-23 -43\n" +
            "47 19\n" +
            "33 -4\n" +
            "15 -10\n" +
            "-16 22\n" +
            "-30 -45\n" +
            "49 -19\n" +
            "-28 36\n" +
            "48 -38\n" +
            "-42 41\n" +
            "-16 -48\n" +
            "17 41\n" +
            "-36 -22\n" +
            "-44 -24\n" +
            "18 47\n" +
            "-14 -45\n" +
            "-17 32\n" +
            "25 -35\n" +
            "6 3\n" +
            "-44 -9\n" +
            "27 30\n" +
            "8 -20\n" +
            "43 -16\n" +
            "31 -2\n" +
            "-12 -48\n" +
            "48 -11\n" +
            "-8 16\n" +
            "-24 -37\n" +
            "-21 -17\n" +
            "5 42\n" +
            "41 14\n" +
            "-5 -17\n" +
            "-1 -26\n" +
            "49 -24\n" +
            "-10 3\n" +
            "-3 -2\n" +
            "-6 -37\n" +
            "-32 34\n" +
            "-42 20\n" +
            "-1 -48\n" +
            "41 18\n" +
            "15 33\n" +
            "5 20\n" +
            "-3 1\n" +
            "40 -20\n" +
            "2 -40\n" +
            "9 42\n" +
            "11 12\n" +
            "25 24\n" +
            "-29 23\n" +
            "-16 -42\n" +
            "24 -34\n" +
            "42 -48\n" +
            "3 20\n" +
            "11 -5\n" +
            "-28 -3\n" +
            "-5 -10\n" +
            "-4 -11\n" +
            "31 4\n" +
            "-35 -16\n" +
            "27 26\n" +
            "-29 -2\n" +
            "-20 -45\n" +
            "-1 -18\n" +
            "11 -30\n" +
            "-29 -41\n" +
            "-43 47\n" +
            "46 -16\n" +
            "-47 -1\n" +
            "-32 28\n" +
            "-35 14\n" +
            "-9 45\n" +
            "21 -13\n" +
            "36 -23\n" +
            "-1 -40\n" +
            "-36 -17\n" +
            "-18 -38\n" +
            "-49 21\n" +
            "30 -1\n" +
            "39 19\n" +
            "-42 12\n" +
            "-34 -17\n" +
            "-16 -36\n" +
            "-8 -17\n" +
            "40 20\n" +
            "-34 -35\n" +
            "-30 -31\n" +
            "-42 12\n" +
            "-38 18\n" +
            "16 -28\n" +
            "35 37\n" +
            "-13 42\n" +
            "-12 -49\n" +
            "8 -17\n" +
            "-44 46\n" +
            "30 28\n" +
            "-10 -35\n" +
            "45 -37\n" +
            "31 16\n" +
            "-31 -48\n" +
            "-40 -42\n" +
            "27 -39\n" +
            "-42 47\n" +
            "41 21\n" +
            "-40 17\n" +
            "19 10\n" +
            "-8 37\n" +
            "37 32\n" +
            "28 23\n" +
            "-15 38\n" +
            "-43 -8\n" +
            "1 16\n" +
            "-2 -30\n" +
            "36 34\n" +
            "10 20\n" +
            "-26 -3\n" +
            "-19 -14\n" +
            "44 38\n" +
            "-1 -39\n" +
            "-13 -7\n" +
            "40 17\n" +
            "-44 25\n" +
            "-10 -31\n" +
            "0 -10\n" +
            "-10 -47\n" +
            "11 42\n" +
            "16 -20\n" +
            "31 5\n" +
            "-1 -37\n" +
            "-44 -14\n" +
            "25 27\n" +
            "14 31\n" +
            "19 47\n" +
            "45 -22\n" +
            "31 0\n" +
            "28 17\n" +
            "23 -26\n" +
            "0 -37\n" +
            "43 -4\n" +
            "48 25\n" +
            "10 -6\n" +
            "-47 43\n" +
            "-32 46\n" +
            "8 28\n" +
            "48 11\n" +
            "-12 -1\n" +
            "-25 48\n" +
            "-44 11\n" +
            "33 0\n" +
            "-40 7\n" +
            "-3 30\n" +
            "-21 34\n" +
            "-32 -22\n" +
            "17 34\n" +
            "-22 -40\n" +
            "36 -41\n" +
            "8 47\n" +
            "-3 -39\n" +
            "-28 46\n" +
            "-9 -13\n" +
            "37 -46\n" +
            "13 -33\n" +
            "30 22\n" +
            "28 -10\n" +
            "-3 28\n" +
            "26 21\n" +
            "-28 4\n" +
            "26 -11\n" +
            "-41 40\n" +
            "-43 47\n" +
            "37 4\n" +
            "41 -30\n" +
            "-27 -3\n" +
            "14 31\n" +
            "-13 -20\n" +
            "47 -49\n" +
            "29 -27\n" +
            "33 25\n" +
            "-10 45\n" +
            "-7 1\n" +
            "15 29\n" +
            "32 -15\n" +
            "17 46\n" +
            "-36 -38\n";
}

class Solver {
    private static final double EPS = 1e-10;

    void solve(Scanner scanner) {
        Line line = new Line(
                new Vector(scanner.nextInt(), scanner.nextInt()),
                new Vector(scanner.nextInt(), scanner.nextInt())
        );

        int q = scanner.nextInt();

        for (int i = 0; i < q; i ++) {
            Vector vector = new Vector(scanner.nextInt(), scanner.nextInt());
            Vector reflection = vector.reflectTo(line);
            System.out.println(reflection.x + " " + reflection.y);
        }
    }

    private int[] splitInt(String s) {
        String[] split = s.split(" ");
        int[] splitInt = new int[split.length];
        for (int i = 0; i < split.length; i ++) {
            splitInt[i] = Integer.parseInt(split[i]);
        }
        return splitInt;
    }

    private long[] splitLong(String s) {
        String[] split = s.split(" ");
        long[] splitLong = new long[split.length];
        for (int i = 0; i < split.length; i ++) {
            splitLong[i] = Long.parseLong(split[i]);
        }
        return splitLong;
    }
}


class Vector {
    double x;
    double y;

    Vector(double x, double y) {
        this.x = x;
        this.y = y;
    }

    Vector (Vector from, Vector to) {
        this(to.x - from.x, to.y - from.y);
    }

    double innerProduct(Vector v) {
        return this.x * v.x + this.y * v.y;
    }

    double outerProduct(Vector v) {
        return this.x * v.y - this.y * v.x;
    }

    double abs() {
        return Math.sqrt(this.norm());
    }

    double norm() {
        return x * x + y * y;
    }

    Vector minus(Vector v) {
        return new Vector(this.x - v.x, this.y - v.y);
    }

    Vector plus(Vector v) {
        return new Vector(this.x + v.x, this.y + v.y);
    }

    Vector reflectTo(Line reflectedLine) {
        Vector base = new Vector(reflectedLine.point1, reflectedLine.point2);
        Vector hypo = this.minus(reflectedLine.point1);
        double r = hypo.innerProduct(base) / base.norm();

        base.x *= r;
        base.y *= r;

        Vector result = reflectedLine.point1.plus(base);
        return result;
    }
}

class Line {
    Vector point1;
    Vector point2;

    Line(Vector point1, Vector point2) {
        this.point1 = point1;
        this.point2 = point2;
    }
}