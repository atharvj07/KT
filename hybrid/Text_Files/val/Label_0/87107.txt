
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    static HashMap<Integer, Integer> Sum = new HashMap<Integer, Integer>();

    public static void add(int x, int cost) {
        while (x > 0) {
            if (Sum.containsKey(x))
                Sum.put(x, Sum.get(x) + cost);
            else
                Sum.put(x, cost);
            x /= 2;
        }
    }

    public static int getSum(int x) {
        if (Sum.containsKey(x))
            return Sum.get(x);
        return 0;
    }

    public static double get(int index, double max) {
        if (!Sum.containsKey(index))
            return max;
        double way1 = getSum(index) - getSum(2 * index);
        way1 = Math.max(way1, max);
        if (way1 <= getSum(2 * index))
            way1 = get(2 * index, way1);
        double way2 = getSum(index) - getSum(2 * index + 1);
        way2 = Math.max(way2, max);
        if (way2 <= getSum(2 * index + 1))
            way2 = get(2 * index + 1, way2);
        return (way1 + way2) * 1.0 / 2;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] S = in.readLine().split(" ");
        int n = Integer.parseInt(S[1]);
        for (int i = 0; i < n; i++) {
            S = in.readLine().split(" ");
            if (S[0].equals("decay"))
                System.out.println(get(1, 0));
            else
                add(Integer.parseInt(S[1]), Integer.parseInt(S[2]));
        }
    }
}
