
import java.io.*;
import java.util.*;

public class Main {

    static FastReader in = new FastReader("in.txt");
    static PrintWriter out = new PrintWriter(System.out);

    static long x, y;

    public static void main(String[] args) throws IOException {
        long a = in.nextInt(), 
             b = in.nextInt(), 
             c = -in.nextInt();
             
        long d = extendedEuclid(a, b);

        if(c%d != 0)
            out.println(-1);
        else
            out.println(x * c/d + " " + y * c/d);

        out.flush();
    }

    static long extendedEuclid(long a, long b){
        if (b == 0) { x = 1; y = 0; return a; }
        long d = extendedEuclid(b, a % b);

        long x1 = y;
        long y1 = x - (a / b) * y;
        x = x1; y = y1;

        return d;
    }

    static class FastReader {

        BufferedReader br;
        StringTokenizer st;

        public FastReader(String file) {
            try {
                br = new BufferedReader(new FileReader(file));
            } catch (FileNotFoundException e) {
                br = new BufferedReader(new InputStreamReader(System.in));
            }
        }

        String next() {

            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) { e.printStackTrace(); }
            }

            return st.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }

        long nextLong() { return Long.parseLong(next()); }

        double nextDouble() { return Double.parseDouble(next()); }

        String nextLine() {

            String str = "";

            try {
                str = br.readLine();
            } catch (IOException e) { e.printStackTrace(); }

            return str;
        }
    }
}