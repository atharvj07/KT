import java.io.*;
import java.util.*;
import java.math.*;

import static java.lang.Math.*;

public class Main implements Runnable {
    
    void prettyPrint(String[] tokens) {
        for (int j = 0; j < tokens.length; j++) {
            if (j > 0) {
                out.print(":");
            }
            for (int k = 0; k < 4 - tokens[j].length(); k++) {
                out.print('0');
            }
            out.print(tokens[j]);
        }
    }
    
    void solve() throws Exception {
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            String str = in.readLine();
            if (str.equals("::")) {
                out.println("0000:0000:0000:0000:0000:0000:0000:0000");
            } else if (str.startsWith("::")) {
                String[] tokens = str.substring(2).split(":");
                for (int j = 0; j < 8 - tokens.length; j++) {
                    out.print("0000:");
                }
                prettyPrint(tokens);
                out.println();
            } else if (str.endsWith("::")) {
                String[] tokens = str.substring(0, str.length() - 2).split(":");
                prettyPrint(tokens);
                for (int j = 0; j < 8 - tokens.length; j++) {
                    out.print(":0000");
                }
                out.println();
            } else if (str.contains("::")) {
                String[] parts = str.split("::");
                String[] tokens1 = parts[0].split(":"), tokens2 = parts[1].split(":");
                prettyPrint(tokens1);
                out.print(":");
                for (int j = 0; j < 8 - tokens1.length - tokens2.length; j++) {
                    out.print("0000:");
                }
                prettyPrint(tokens2);
                out.println();
            } else {
                String[] tokens = str.split(":");
                prettyPrint(tokens);
                out.println();
            }
        }
    }

    BufferedReader in;
    PrintWriter out;
    FastScanner sc;

    static Throwable uncaught;

    @Override
    public void run() {
        try {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(System.out);
            sc = new FastScanner(in);
            solve();
        } catch (Throwable t) {
            Main.uncaught = t;
        } finally {
            out.close();
        }
    }

    public static void main(String[] args) throws Throwable {
        Thread t = new Thread(null, new Main(), "", 128 * 1024 * 1024);
        t.start();
        t.join();
        if (uncaught != null) {
            throw uncaught;
        }
    }

}

class FastScanner {

    BufferedReader reader;
    StringTokenizer strTok;

    public FastScanner(BufferedReader reader) {
        this.reader = reader;
    }

    public String nextToken() throws IOException {
        while (strTok == null || !strTok.hasMoreTokens()) {
            strTok = new StringTokenizer(reader.readLine());
        }
        return strTok.nextToken();
    }

    public int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    public long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }

    public double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }

}