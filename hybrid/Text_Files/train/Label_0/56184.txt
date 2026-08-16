import java.io.*;
import java.util.*;

/**
 * Codeforces #68C "Synchrophasotron"
 * @link http://codeforces.ru/problemset/problem/68/C
 * @author Caesar
 */
public class Solution68C implements Runnable {

    private static final int EXIT_CODE = -1;
    private static final boolean ONLINE_JUDGE = System.getProperty("ONLINE_JUDGE") != null;
    private static final String INPUT = "input.txt";
    private static final String OUTPUT = "output.txt";

    private StringTokenizer tok;
    private BufferedReader in;
    private PrintWriter out;

    public static void main(String[] args) {
        new Thread(new Solution68C()).start();
    }

    public void run() {
        try {
            in = ONLINE_JUDGE ?
                new BufferedReader(new InputStreamReader(System.in)) :
                new BufferedReader(new FileReader(INPUT));
            out = ONLINE_JUDGE ? new PrintWriter(System.out) : new PrintWriter(OUTPUT);
            long start = System.currentTimeMillis();
            try {
                solve();
            } finally {
                if (ONLINE_JUDGE) {
                    out.flush();
                } else {
                    out.close();
                }
            }
            System.err.println("Time used: " + (System.currentTimeMillis() - start));
        } catch (Throwable ex) {
            ex.printStackTrace();
            System.exit(EXIT_CODE);
        }
    }

    private String readString() throws IOException {
        while (tok == null || !tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine());
        }
        return tok.nextToken();
    }

    private int readInt() throws IOException {
        return Integer.parseInt(readString());
    }
    
    int n;
    private int[] fin;
    private int[][] l;
    private int[][] h;
    private int[][] a;
    private int minFlow = Integer.MAX_VALUE;
    private int maxCost = Integer.MIN_VALUE;
    private int cost;

    private void brute(int start, int finish) {
        if (start == n - 1) {
            if (fin[start] < minFlow) {
                minFlow = fin[start];
                maxCost = cost;
            } else if (fin[start] == minFlow && cost > maxCost) {
                maxCost = cost;
            }
            return;
        }
        if (finish == n) {
            brute(start + 1, start + 2);
            return;
        }
        if (finish == n - 1) {
            if (fin[start] >= l[start][finish] && fin[start] <= h[start][finish]) {
                fin[finish] += fin[start];
                int c = fin[start] == 0 ? 0 : a[start][finish] + fin[start] * fin[start];
                cost += c;
                brute(start + 1, start + 2);
                cost -= c;
                fin[finish] -= fin[start];
            }
            if (start != 0) {
                return;
            }
        }
        int border = Math.min(Math.min(h[start][finish], fin[start]), minFlow);
        for (int flow = l[start][finish]; flow <= border; ++flow) {
            fin[start] -= flow;
            fin[finish] += flow;
            int c = flow == 0 ? 0 : a[start][finish] + flow * flow;
            cost += c;
            brute(start, finish + 1);
            cost -= c;
            fin[start] += flow;
            fin[finish] -= flow;
        }
    }

    public void solve() throws IOException {
        n = readInt();
        l = new int[n][n];
        h = new int[n][n];
        a = new int[n][n];
        int m = n * (n - 1) >> 1;
        for (int i = 0; i < m; ++i) {
            int s = readInt() - 1;
            int f = readInt() - 1;
            l[s][f] = readInt();
            h[s][f] = readInt();
            a[s][f] = readInt();
        }
        fin = new int[n];
        fin[0] = Integer.MAX_VALUE;
        brute(0, 1);
        out.println(minFlow == Integer.MAX_VALUE ? "-1 -1" : (minFlow + " " + maxCost));
    }

}
