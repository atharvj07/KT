import org.w3c.dom.ls.LSOutput;

import java.util.*;
import java.lang.*;

public class Main {
    static final int INF = 1000 * 1000 * 1000;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int a = in.nextInt();
        int b = in.nextInt();

        if (a == b) {
            System.out.println(a + "0 " + a + "1\n");
        }
        else if (a == b - 1){
            System.out.println(a + "9 " + b + "0\n");
        }
        else if (b == 1 && a == 9) {
            System.out.println("9 10\n");
        }
        else {
            System.out.println(-1);
        }
    }
}




