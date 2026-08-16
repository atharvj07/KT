import java.util.*;

public class Main {
    public static void main(String args[]) {
        solve1091();
    }

    public static void solve1091() {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            int a = sc.nextInt();
            int l = sc.nextInt();
            int x = sc.nextInt();
            double nitouhen = menseki(a, calcHeight(l, a));
            double yoyuu = menseki(l, calcHeight(0.5 * (l + x), l));
            System.out.println(nitouhen + 2 * yoyuu);
        }
    }

    public static double menseki(double teihen, double takasa) {
        return 0.5 * teihen * takasa;
    }

    public static double calcHeight(double syahen, double ippen) {
        return Math.sqrt(syahen * syahen - 0.5 * ippen * 0.5 * ippen);
    }
}


