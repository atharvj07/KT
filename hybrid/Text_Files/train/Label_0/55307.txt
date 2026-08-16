import java.io.PrintWriter;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in); PrintWriter out = new PrintWriter(System.out)) {
            int r = in.nextInt(), s = in.nextInt(), p = in.nextInt();
            int[] d = new int[p];
            for (int i = 0; i < p; i++) {
                int y = in.nextInt(), x = in.nextInt();
                d[i] = (r - y + 1) + (x <= s ? s - x + 1 : x - s);
            }
            Arrays.sort(d);
            //System.out.println(Arrays.toString(d));

            for (int i = 1; i < p; i++) {
                d[i] = Math.max(d[i], d[i - 1] + 1);
            }
            out.println(d[p - 1]);
        }
    }
}

