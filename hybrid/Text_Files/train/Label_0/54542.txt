
import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

public class C {

    int INF = 1 << 28;
    //long INF = 1L << 62;
    double EPS = 1e-10;

    void run() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt();
        if( n < k || (k == 1 && n > 1) ) {
            System.out.println(-1);
            return;
        }
        if( n == 1 && k == 1) {
            System.out.println("a");
            return;
        }
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<n-k+2;i++) {
            sb.append((i%2==0? 'a': 'b'));
        }
        for(int i=0;i<k-2;i++) sb.append((char)(i+'c'));
        System.out.println(sb.toString());
    }

    void debug(Object... os) {
        System.err.println(Arrays.deepToString(os));
    }

    public static void main(String[] args) {
        new C().run();
    }
}


