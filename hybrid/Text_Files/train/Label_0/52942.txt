import java.util.*;
import java.util.stream.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int mod = (int)1e9 + 7;
        String s = sc.next();
        for (int i = 0; i < s.length(); i++) {
            if ((i % 2 == 0 && s.charAt(i) == 'L') || (i % 2 != 0 && s.charAt(i) == 'R')) {
                System.out.println("No");
                System.exit(0);
            }
        }
        System.out.println("Yes");
    }

}
