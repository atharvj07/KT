import java.util.*;

public class Example {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int a = in.nextInt();
        int b = in.nextInt();
        int ans = Math.min(n - a, b + 1);

        System.out.println(ans);
    }
}