import java.util.*;
import java.lang.*;

public class Main {
    static final int INF = (1 << 31) - 1;             
    static final int MAXN = 11111;     
    static double a, b, c;
    static double a1, b1, c1;
    static double resX, resY;
    
    public static void main(String[] args) throws Exception {                
        Scanner input = new Scanner(System.in);
        int x0, y0, x1, y1, x2, y2;
        int q;
        x0 = input.nextInt();
        y0 = input.nextInt();
        x1 = input.nextInt();
        y1 = input.nextInt();
        lineOf(x0, y0, y1 - y0, x0 - x1);
        q = input.nextInt();
        for (int i = 0; i < q; ++i) {
            x2 = input.nextInt();
            y2 = input.nextInt();
            line1Of(x2, y2, x0 - x1, y0 - y1);
            intersectionOf2Lines();
            resX = resX * 2 - x2;
            resY = resY * 2 - y2;
            System.out.printf("%.8f %.8f\n", resX, resY);
        }
    }
    
    static void lineOf(double x1, double y1, double vx, double vy) {
        a = vx;
        b = vy;
        c = - vx * x1 - vy * y1;
    }
    
    static void line1Of(double x1, double y1, double vx, double vy) {
        a1 = vx;
        b1 = vy;
        c1 = - vx * x1 - vy * y1;
    }
    
    static void intersectionOf2Lines() {
        double d = a * b1 - a1 * b;
        double dx = b * c1 - b1 * c;
        double dy = c * a1 - c1 * a;
        resX = dx / d;
        resY = dy / d;
    }
}