
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    void run() {
        Scanner sc = new Scanner(System.in);
        LinkedList<Character> l = new LinkedList<>();
        boolean isR = false;
        String s = sc.next();
        int q = sc.nextInt();

        for (char c : s.toCharArray()) {
            l.addLast(c);
        }

        for (int i = 0; i < q; i++) {
            int t = sc.nextInt();
            if (t == 1) {
                isR = !isR;
            } else {
                boolean isF = sc.nextInt() == 1;
                char c = sc.next().charAt(0);
                if (isF ^ isR) {
                    l.addFirst(c);
                } else {
                    l.addLast(c);
                }
            }
        }

        PrintWriter out = new PrintWriter(System.out);

        if (isR) {
            Collections.reverse(l);
        }

        for (char c : l) {
            out.print(c);
        }

        out.println();
        out.flush();
    }

    void debug(Object... os) {
        System.err.println(Arrays.deepToString(os));
    }

    public static void main(String[] args) {
        new Main().run();
    }

}
