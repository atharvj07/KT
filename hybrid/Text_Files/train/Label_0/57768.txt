
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.lang.Integer;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeSet;
import java.util.Vector;
import java.util.logging.Level;
import java.util.logging.Logger;


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author toghru
 */
public class Main {

    public static int[] a;
    public static int solve(int l, int r) {
        int ans = r - l + 1;
        if(ans == 0) return 0;
        int min = Integer.MAX_VALUE;
        for(int i = l; i <= r; i++) {
            if(a[i] == 0) {
                return Math.min(ans, solve(l, i - 1) + solve(i + 1, r));
            }
            if(a[i] < min) min = a[i];
        }
        for(int i = l; i <= r; i++) a[i] -= min;
        return Math.min(ans, solve(l, r) + min);
    }
    public static void main(String[] args) throws InterruptedException, IOException {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        PrintWriter out = new PrintWriter(outputStream);
        InputReader in = new InputReader(inputStream);

        int n = in.nextInt();
        
        a = new int[n];
        for(int i = 0; i < n; i++) {
            a[i] = in.nextInt();
        }
        
        out.println(solve(0, n - 1));
        out.close();
    }

    static class InputReader {

        BufferedReader reader;
        StringTokenizer tokenizer;

        public InputReader(InputStream inputStream) {
            reader = new BufferedReader(new InputStreamReader(inputStream), 32624);
            tokenizer = null;
        }
        // suigns dasndasdas

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException ex) {
                    Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        private long nextLong() {
            return Long.parseLong(next());
        }

        private BigInteger nextBigInteger() {
            return new BigInteger(next());
        }
    }

}
