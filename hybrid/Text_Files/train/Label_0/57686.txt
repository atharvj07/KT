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
        Jfen solver = new Jfen();
        try {
            int testNumber = 1;
            while (true)
                solver.solve(testNumber++, in, out);
        } catch (UnknownError e) {
            out.close();
        }
    }

    static class Jfen {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            String S = in.next();
            if (S.equals("#")) throw new UnknownError();
            int a, b, c, d;
            a = in.nextInt() - 1;
            b = in.nextInt() - 1;
            c = in.nextInt() - 1;
            d = in.nextInt() - 1;
            String[] Ss = S.split("/");
            StringBuilder[] board = new StringBuilder[Ss.length];
            for (int i = 0; i < Ss.length; i++) {
                board[i] = new StringBuilder();
                for (int j = 0; j < Ss[i].length(); j++) {
                    final char C = Ss[i].charAt(j);
                    if (Character.isDigit(C)) {
                        for (int k = 0; k < C - '0'; k++) {
                            board[i].append('.');
                        }
                    } else {
                        board[i].append(C);
                    }
                }
            }
            final char cbuf = board[a].charAt(b);
            board[a].setCharAt(b, board[c].charAt(d));
            board[c].setCharAt(d, cbuf);
            StringBuilder ans = new StringBuilder();
            for (int i = 0; i < board.length; i++) {
                int cnt = 0;
                for (int j = 0; j < board[i].length(); j++) {
                    if (board[i].charAt(j) == 'b') {
                        if (cnt != 0) {
                            ans.append(cnt);
                        }
                        cnt = 0;
                        ans.append('b');
                    } else {
                        cnt++;
                        if (j + 1 == board[i].length()) {
                            ans.append(cnt);
                            cnt = 0;
                        }
                    }
                    if (i + 1 != board.length && j + 1 == board[i].length()) {
                        ans.append('/');
                    }
                }
            }
            out.println(ans);
        }

    }
}