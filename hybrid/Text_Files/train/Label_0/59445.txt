import java.io.*;
import java.util.Scanner;

public class test {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        long a, ab, y, g, b, res  = 0;
        a = in.nextLong();
        ab = in.nextLong();
        y = in.nextLong();
        g = in.nextLong();
        b = in.nextLong();
        
        y *= 2;
        b *= 3;
        
        if (y > a) {
            y -= a;
            res += y;
            a = 0;
        } else {
            a -= y;
        }
        
        if (b > ab) {
            b -= ab;
            res += b;
            ab = 0;
        } else {
            ab -= b;
        }
        
        if (g > a) {
            res += g - a;
            a = 0;
        } else {
            a -= g;
        }
        
        if (g > ab) {
            res += g - ab;
            ab = 0;
        } else {
            ab -= g;
        }
        System.out.println(res);
    }
}