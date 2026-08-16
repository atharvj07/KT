import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        int[] dish = new int[Integer.parseInt(sc.next())];
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(sc.next());
            for (int j = 0; j < num; j++) {
                dish[Integer.parseInt(sc.next()) - 1]++;
            }
        }
        int cnt = 0;
        for (int tmp : dish) {
            if (tmp == n) cnt++;
        }
        System.out.println(cnt);
    }
}
