import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.List;
import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        ABCGene solver = new ABCGene();
        solver.solve(1, in, out);
        out.close();
    }

    static class ABCGene {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            String S = in.next();
            List<Character> list = new ArrayList<>();
            String ss = S;
            while (S.length() > 3) {
                StringBuilder sb = new StringBuilder();
                char c = 'B';
                if (S.startsWith("ABC")) {
                    c = 'A';
                } else if (S.endsWith("ABC")) {
                    c = 'C';
                }
                for (int i = 0; i < S.length(); i++) {
                    if (i + 2 < S.length() && S.charAt(i) == 'A' && S.charAt(i + 1) == 'B' && S.charAt(i + 2) == 'C') {
                        sb.append(c);
                        i = i + 2;
                    } else {
                        sb.append(S.charAt(i));
                    }
                }
                if (S.equals(sb.toString())) {
                    break;
                }
                list.add(c);
                S = sb.toString();
            }
            if (S.equals("ABC")) {
                Collections.reverse(list);
                for (char key : list) {
                    StringBuilder sb = new StringBuilder();
                    for (char c : S.toCharArray()) {
                        if (c == key) {
                            sb.append("ABC");
                        } else {
                            sb.append(c);
                        }
                    }
                    S = sb.toString();
                }
                out.println(S.equals(ss) ? "Yes" : "No");
            } else {
                out.println("No");
            }
        }

    }
}


