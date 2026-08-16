//Abra at 22.06.11 21:36

import java.io.*;
import java.math.*;
import java.util.*;

public class Abra {
    void solve() throws IOException {
        int x = nextInt(), y = nextInt();
        boolean f = true;
        while (true) {
            if ((x >= 2 && y < 2) || (x == 1 && y < 12) || (x == 0 && y < 22)) break;
            if (f) {
                if (x == 0) {
                    y -= 22;
                } else
                if (x == 1) {
                    x--;
                    y -= 12;
                } else
                if (x >= 2) {
                    x -= 2;
                    y -= 2;
                }
            } else {
                if (y >= 22) {
                    y -= 22;
                } else
                if (y >= 12) {
                    x--;
                    y -= 12;
                } else
                if (y >= 2) {
                    x -= 2;
                    y -= 2;
                }
            }
            f = !f;
        }
        out.println(f ? "Hanako" : "Ciel");
    }

    public static void main(String[] args) throws IOException {
        new Abra().run();
    }

    StreamTokenizer in;
    PrintWriter out;
    boolean oj;
    BufferedReader br;

    void init() throws IOException {
        oj = System.getProperty("ONLINE_JUDGE") != null;
        Reader reader = oj ? new InputStreamReader(System.in) : new FileReader("input.txt");
        Writer writer = oj ? new OutputStreamWriter(System.out) : new FileWriter("output.txt");
        br = new BufferedReader(reader);
        in = new StreamTokenizer(br);
        out = new PrintWriter(writer);
    }

    long beginTime;

    void run() throws IOException {
        beginTime = System.currentTimeMillis();
        long beginMem = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        init();
        solve();
        long endMem = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        long endTime = System.currentTimeMillis();
        if (!oj) {
            System.out.println("Memory used = " + (endMem - beginMem));
            System.out.println("Total memory = " + (Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory()));
            System.out.println("Running time = " + (endTime - beginTime));
        }
        out.flush();
    }

    int nextInt() throws IOException {
        in.nextToken();
        return (int) in.nval;
    }

    long nextLong() throws IOException {
        in.nextToken();
        return (long) in.nval;
    }

    String nextString() throws IOException {
        in.nextToken();
        return in.sval;
    }

    double nextDouble() throws IOException {
        in.nextToken();
        return in.nval;
    }
}
