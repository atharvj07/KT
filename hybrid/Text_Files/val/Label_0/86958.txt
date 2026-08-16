import java.util.*;
import java.io.*;

public class B {

    public static void main(String[] args) throws Exception {
        BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
        String input;
        StringTokenizer tok;
        int x1, x2, x3, y1, y2, y3;
        input = bi.readLine();
        tok = new StringTokenizer(input);
        x1 = Integer.parseInt(tok.nextToken());
        y1 = Integer.parseInt(tok.nextToken());
        input = bi.readLine();
        tok = new StringTokenizer(input);
        x2 = Integer.parseInt(tok.nextToken());
        y2 = Integer.parseInt(tok.nextToken());
        input = bi.readLine();
        tok = new StringTokenizer(input);
        x3 = Integer.parseInt(tok.nextToken());
        y3 = Integer.parseInt(tok.nextToken());
        solve(x1, y1, x2, y2, x3, y3);
    }

    static void solve(int x1, int y1, int x2, int y2, int x3, int y3) {
        System.out.println(3); // Always ??
        // Consider 1 as centre.
        // Sides 1-2 and 1-3.
        // Next point is 2 + (1-3) or equivalently 3 + (1-2)
        int x4 = x2 + x3 - x1;
        int y4 = y2 + y3 - y1;
        System.out.println(x4 + " " + y4);
        // Consider 2 as centre.
        // Sides 2-3 and 1-3.
        // Next point is 3 + (2-1) or equivalently 1 + (2-3)
        int x5 = x3 + x1 - x2;
        int y5 = y3 + y1 - y2;
        System.out.println(x5 + " " + y5);
        // Similarly with 3 as centre.
        int x6 = x2 + x1 - x3;
        int y6 = y2 + y1 - y3;
        System.out.println(x6 + " " + y6);
        
    }
}
