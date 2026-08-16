import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int a = Integer.parseInt(sc.next());
            map.merge(a, 1, Integer::sum);
        }
        int ans = map.keySet().size();
        if (ans % 2 == 0) {
            System.out.println(ans - 1);
        } else {
            System.out.println(ans);
        }
    }
}