
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        int n = in.nextInt();

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                Num a = new Num(n, 0, i);
                Num b = new Num(n, 0, j);

                out.print(a.mul(b));
                out.print(" ");
            }
            out.println();
        }

        out.flush();
    }

    private static class Num {

        int osn;
        int first;
        int second;

        public Num(int o, int f, int s) {
            osn = o;
            first = f;
            second = s;
        }

        public String mul(Num a) {
            Integer ansSecond = second * a.second;
            Integer ansFirst = ansSecond / osn;
            ansSecond %= osn;
            String ans;
            if (ansFirst == 0) {
                ans = ansSecond.toString();
            } else {
                ans = ansFirst.toString() + ansSecond.toString();
            }
            return ans;
        }
    }
}
