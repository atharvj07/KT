import java.util.*;
import java.io.*;
public class JavaApplication14 {

    /**
     * @param args the command line arguments
     */
   static StreamTokenizer st;
    static int V;
    static final double g = 9.8;
    static class Angle implements Comparable<Angle> {
        double val;
        int id;
        public int compareTo(Angle arg0) {
            return Double.compare(this.val, arg0.val);
        }
    }
    static class Point implements Comparable<Point> {
        double x,y;
        public int compareTo(Point arg0) {
            return Double.compare(this.x, arg0.x);
        }
    }
    public static void main(String[] args) throws IOException{
        st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int n = nextInt();
        V = nextInt();
        Angle[]alpha = new Angle[n+1];
        for (int i = 1; i <= n; i++) {
            alpha[i] = new Angle();
            alpha[i].val = nextDouble();
            alpha[i].id = i;
        }
        Arrays.sort(alpha, 1, n+1);
        int m = nextInt();
        Point[]coord = new Point[m+1];
        for (int i = 1; i <= m; i++) {
            coord[i] = new Point();
            coord[i].x = nextDouble();
            coord[i].y = nextDouble();
        } 
        Arrays.sort(coord, 1, m+1);
        Point[]ans = new Point[n+1];
        for (int i = 1; i <= n; i++) {
            ans[i] = new Point();
        }
        int left = 1;
        for (int i = 1; i <= m; i++) {
            int right = n, first = left;
            while (left <= right) {
                int middle = (left+right) >> 1;
                if (get_y(alpha[middle].val, coord[i].x) > coord[i].y)
                    right = middle-1;
                else
                    left = middle+1;
            }
            left--;
            for (int j = first; j <= left; j++) {
                double y = get_y(alpha[j].val, coord[i].x);
                if (y >= 0) {
                    ans[alpha[j].id].x = coord[i].x;
                    ans[alpha[j].id].y = y;
                }
                else {
                    ans[alpha[j].id].x = get_x(alpha[j].val);
                    ans[alpha[j].id].y = 0;
                }
            }
            left++;
            if (left > n)
                break;
        }
        for (int i = left; i <= n; i++) {
            ans[alpha[i].id].x = get_x(alpha[i].val);
            ans[alpha[i].id].y = 0;
        }
        for (int i = 1; i <= n; i++) {
            pw.println(ans[i].x+" "+ans[i].y);
        }
        pw.close();
    }
    
    private static double get_x(double alpha) {
        return V*V*Math.sin(2*alpha)/g;
    }

    private static double get_y(double alpha, double x) {
        double t = x / (V*Math.cos(alpha));
        return V*Math.sin(alpha)*t-g*t*t / 2;
    }

    private static double nextDouble() throws IOException{
        st.nextToken();
        return st.nval;
    }

    private static int nextInt() throws IOException{
        st.nextToken();
        return (int) st.nval;
    }
}