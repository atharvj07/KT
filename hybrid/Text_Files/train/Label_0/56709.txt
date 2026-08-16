import java.util.*;
import static java.lang.System.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        int ans = 0;
        for(int i=1; i<=n; i++){
            ans += (n-1)/i;
        }
        out.println(ans);

    }
}
