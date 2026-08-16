import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.PrintStream;
import java.util.Scanner;
import java.util.TreeSet;

public class CF_1190C {
    static int[] vals;
    static int k;

    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedInputStream(System.in));
        PrintStream out = new PrintStream(new BufferedOutputStream(System.out));

        int n = in.nextInt();
        k = in.nextInt();

        vals = new int[n];
        String s = in.next();
        for (int i = 0; i < n; i++) vals[i] = s.charAt(i) - '0';

        if (solve1(0) || solve1(1)) {
            out.println("tokitsukaze");
        } else if (solve2(0) && solve2(1)) {
            out.println("quailty");
        }else{
            out.println("once again");
        }


        out.close();
        in.close();
    }

    static boolean solve1(int x) {
        TreeSet<Integer> pos = new TreeSet<>();

        for (int i = 0; i < vals.length; i++) {
            if (vals[i] == x) pos.add(i);
        }



        return pos.isEmpty() || pos.last() - pos.first() < k;
    }

    static boolean solve2(int x) {
        TreeSet<Integer> pos = new TreeSet<>();

        for (int i = 0; i < vals.length; i++) {
            if (vals[i] == x) pos.add(i);
        }

        for (int i = 0; i < k; i++) {
            if (vals[i] == x) pos.remove(i);
        }

        if (pos.first() - pos.last() >= k) return false;
        for (int i = 0; i < vals.length - k; i++) {
            if (vals[i] == x) pos.add(i);
            if (vals[i + k] == x) pos.remove(i + k);

            if (!pos.isEmpty() && pos.last() - pos.first() >= k) return false;
        }
        return true;
    }
}
