import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author alecs6k
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        codeforces1 solver = new codeforces1();
        solver.solve(1, in, out);
        out.close();
    }

    static class codeforces1 {
        public void solve(int testNumber, Scanner leer, PrintWriter out) {
            int n = leer.nextInt();
            String cad = leer.next();
            int p1 = 0, p2 = 0;
            boolean t = false;
            for (int i = 0; i < n - 1; i++) {
                char a = cad.charAt(i);
                char b = cad.charAt(i + 1);
                if (b < a) {
                    p1 = i;
                    p2 = i + 1;
                    t = true;
                    //out.println(a+" "+b);
                    break;
                }
            }
            p1++;
            p2++;
            if (t) {
                out.println("YES");
                out.println(p1 + " " + p2);
            } else {
                out.println("NO");
            }
        }

    }
}

