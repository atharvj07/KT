import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

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
        TaskB solver = new TaskB();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskB {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            String s = in.next();
            int n = s.length();
            int count = 0;
            int[] letters = new int[26];
            for (int i = 0; i < n; ++i) {
                letters[s.charAt(i) - 'a']++;
            }
            for (int i = 0; i < 26; ++i) {
                if (letters[i] % 2 == 1) ++count;
            }
            if (count <= 1 || count % 2 != 0) out.print("First");
            else out.print("Second");
        }

    }
}

