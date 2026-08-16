import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;
 
public class Main {
 
    void solve() throws IOException {
        int d = ni();
        int[] c = new int[26];
        for (int i = 0; i < 26; i++) {
            c[i] = ni();
        }
        int[][] s = new int[d][26];
        for (int i = 0; i < d; i++) {
            for (int j = 0; j < 26; j++) {
                s[i][j] = ni();
            }
        }
        int[] t = new int[d];
        for (int i = 0; i < t.length; i++) {
            t[i] = ni()-1;
        }
        
        int score = 0;
        int[] last = new int[26];
        for (int i = 1; i <= d; i++) {
            score += s[i-1][t[i-1]];
            int mi = 0;
            last[t[i-1]] = i;
            for (int j = 0; j < 26; j++) {
                mi += c[j]*(i-last[j]);
            }
            score -= mi;
            out.println(score);
        }
    }

 
    String ns() throws IOException {
        while (!tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine(), " ");
        }
        return tok.nextToken();
    }
 
    int ni() throws IOException {
        return Integer.parseInt(ns());
    }
 
    long nl() throws IOException {
        return Long.parseLong(ns());
    }
 
    double nd() throws IOException {
        return Double.parseDouble(ns());
    }
 
    String[] nsa(int n) throws IOException {
        String[] res = new String[n];
        for (int i = 0; i < n; i++) {
            res[i] = ns();
        }
        return res;
    }
 
    int[] nia(int n) throws IOException {
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = ni();
        }
        return res;
    }
 
    long[] nla(int n) throws IOException {
        long[] res = new long[n];
        for (int i = 0; i < n; i++) {
            res[i] = nl();
        }
        return res;
    }
 
    static BufferedReader in;
    static PrintWriter out;
    static StringTokenizer tok;
 
    public static void main(String[] args) throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        tok = new StringTokenizer("");
        Main main = new Main();
        main.solve();
        out.close();
    }
}