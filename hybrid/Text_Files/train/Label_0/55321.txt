
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        new Main().go();
    }
    
    Scanner scan;
    PrintWriter print;
    
    void go() {
        try {
            //scan = new Scanner(new File("in.txt"));
            scan = new Scanner(System.in);
            print = new PrintWriter(System.out);
            for(; scan.hasNext();) {
                long a, b, c;
                a = scan.nextLong();
                b = scan.nextLong();
                c = scan.nextLong();
                long res = calc(a, b, c);
                long r = calc(b, a, c);
                if(r < res) res = r;
                r = calc(c, a, b);
                if(r < res) res = r;
                print.println(res);
            }
        } 
        /*catch (FileNotFoundException ex) {
            ex.printStackTrace();
        } */
        finally {
            print.close();
        }       
    }

    private long calc(long a, long b, long c) {
        long d = Math.min(b, c);
        a += d;
        b -= d;
        c -= d;
        if(b == 0) {
            b = c;
            c = 0;
        }
        if((b & 1) == 1) return d + a + b - 1;
        else if(a > 0) return d + b;
        else return d + a + b - 1;
    }
    
}
