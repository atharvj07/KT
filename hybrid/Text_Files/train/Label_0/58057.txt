
import java.util.*;

public class Main {
    static Scanner input = new Scanner(System.in);

    static public void solve() {
        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();
        input.close();

        int max = a;
        String ans = "A";
        if (b > max) {
            max = b;
            ans = "B";
        }
        if (c > max) {
            max = c;
            ans = "C";
        }
        System.out.println(ans);
    }

    public static void main(String[] args) {
        solve();
    }
}
