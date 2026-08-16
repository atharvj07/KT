
import java.io.*;
import java.util.*;

/**
 * AIZU ONLINE JUDGE
 * 2852 Tiny Room
 *    2018/02/19
 */
public class Main {

    int N;
    int W;
    int H;
    int R;
    int[] x;
    int[] y;
    
    double func(double th) {
        double xmax = -Double.MAX_VALUE;
        double ymax = -Double.MAX_VALUE;
        double xmin = Double.MAX_VALUE;
        double ymin = Double.MAX_VALUE;
        double cos = Math.cos(th);
        double sin = Math.sin(th);
        for(int n = 0; n < N; n++) {
            double x0 = cos * x[n] - sin * y[n];
            double y0 = sin * x[n] + cos * y[n];
            if (x0 > xmax)
                xmax = x0;
            if (x0 < xmin)
                xmin = x0;
            if (y0 > ymax)
                ymax = y0;
            if (y0 < ymin)
                ymin = y0;
        }
        double max = Math.max(xmax - xmin - W, ymax - ymin - H);
        return max;
    }
    
    boolean smin(double x0, double x1) {
        for(int i = 0; i < 20; i++) {
        double m = (x0 + x1) / 2;
        double delta = 0.0000000001;
        double k = func(m);
        double kd = func(m + delta);
            log.printf("x0 x1, m (%f %f %f) k = %f\n", x0, x1, m, k);
        if (k <= 0)
                return true;
        if (k < kd) {
                x1 = m;
        }
        else {
                x0 = m;
            }
        }
        return false;
    }

    boolean main() throws IOException {

        Scanner sc = new Scanner(systemin);

        N = sc.nextInt();
        H = sc.nextInt();
        W = sc.nextInt();
        R = sc.nextInt();
        H -= R * 2;
        W -= R * 2;
        //log.printf("%d %d\n",  N, M);
        x = new int[N];
        y = new int[N];
        for(int i = 0; i < N; i++) {
            x[i] = sc.nextInt();
            y[i] = sc.nextInt();
            //log.printf("%d %d\n", x[i], y[i]);
        }

        
        int ret = 0;
        int B = 1000;
        double k2 = 0;
        double d2 = 0;
        double d;
        for(int i = 0; i < B + 3; i++) {
            double s = i * Math.PI / B;
            double k = func(s);
            if (k < 0) {
                ret = 1;
                break;
            }
            //log.printf("i%d x%f(%f %f) y%f(%f %f) %f %s\n", i,xmax-xmin, xmin,xmax, ymax-ymin,ymin, ymax, min, f != 0?"OK":"");
            log.printf("%d\t%f\t%s\n", i, k, k <= 0?"OK":"");
            
            d = k - k2;
            if (i >= 2 && d2 <= 0 && d >= 0) {
                boolean sm = smin((i - 2) * Math.PI / B, s);
                if (sm) {
                    ret = 1;
                    break;
                }
            }
            
            k2 = k;
            d2 = d;
            
        }

        result.printf("%s\n", ret != 0? "Yes":"No");

        sc.close();
        return false;
    }

    PrintStream log;
    PrintStream result = System.out;
    BufferedReader systemin;

    static Main instance = new Main();

    Main() {
        systemin = new BufferedReader(new InputStreamReader(System.in));
        log = new PrintStream(new OutputStream() { public void write(int b) {} } );
    }

    public static void main(String[] args) throws IOException {

        instance.main();

        instance.systemin.close();
    }


}


