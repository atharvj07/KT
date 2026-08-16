import java.io.IOException;
import java.util.Scanner;

import static java.lang.Math.min;

public class Main {
    static Scanner in = new Scanner(System.in);
    
    public static void main(String[] args) throws IOException {
        int a = nextInt();
        int b = nextInt();
        int c = nextInt();
        int d = nextInt();
        int e = nextInt();
        System.out.println(min(a, min(b, min(c / 2, min(d / 7, e / 4)))));
    }
    
    static int nextInt() throws IOException {
        return in.nextInt();
    }
}
