import java.util.*;
import java.io.*;

public class ForProblems {

    Random rnd = new Random();

    void solve() throws IOException {

        int n = readInt();
        int[] p = new int[n];
        for (int i = 0; i < n; ++i)
            p[i] = readInt();
        String str = readString();
        long sumB = 0;
        for (int i = 0; i < str.length(); ++i)
            if (str.charAt(i) == 'B')
                sumB += p[i];

        long ans = 0;

        long sumB1 = sumB;
        long sum1 = 0;
        for (int i = 0; i < n; ++i) {
            if (str.charAt(i) == 'A')
                sum1 += p[i];
            else
                sumB1 -= p[i];

            ans = Math.max(ans, sum1 + sumB1);
        }

        long sumB2 = sumB;
        long sum2 = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (str.charAt(i) == 'A')
                sum2 += p[i];
            else
                sumB2 -= p[i];

            ans = Math.max(ans, sum2 + sumB2);
        }

        out.print(Math.max(ans, sumB));
    }


    BufferedReader in;
    PrintWriter out;
    StringTokenizer tok = new StringTokenizer("");

    final boolean ONLINE_JUDGE = System.getProperty("ONLINE_JUDGE") != null;

    public static void main(String[] args){

        new ForProblems().run();
    }

    public void run() {

        try {
            long timeBegin = System.currentTimeMillis();
            Locale.setDefault(Locale.US);

            init();
            solve();

            out.close();

            long timeEnd = System.currentTimeMillis();
            System.err.println("Time = " + (timeEnd - timeBegin));
        } catch (Exception e) {
            e.printStackTrace(System.err);
            System.exit(-1);
        }
    }

    void init() throws FileNotFoundException {

        Locale.setDefault(Locale.US);

        if (ONLINE_JUDGE) {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(System.out);
        } else {
            in = new BufferedReader(new FileReader("input.txt"));
            out = new PrintWriter("output.txt");
        }
    }

    String readString() throws IOException {
        while(!tok.hasMoreTokens()){
            try{
                tok = new StringTokenizer(in.readLine());
            } catch (Exception e) {
                return null;
            }
        }
        return tok.nextToken();
    }

    int readInt() throws IOException {
        return Integer.parseInt(readString());
    }

    long readLong() throws IOException {
        return Long.parseLong(readString());
    }

}