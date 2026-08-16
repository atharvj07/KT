

import java.io.*;
import java.util.*;


/**
 * AIZU ONLINE JUDGE
 * 3130
 *  2020/5/3
 */
public class Main {


    boolean main() throws IOException {

        Scanner sc = new Scanner(systemin);

        long N = sc.nextLong();
        int A = sc.nextInt();
        int B = sc.nextInt();

        N = N % 12;
        for(int i = 0; i < N; i++) {
            if (i % 2 == 0) {
                A = A - B;
            }
            else {
                B = A + B;
            }
        }
        System.out.printf("%d %d\n", A, B);

        sc.close();
        return false;
    }



    PrintStream log;
    PrintStream result = System.out;
    BufferedReader systemin;

    static Main instance = new Main();

    Main() {
        systemin = new BufferedReader(new InputStreamReader(System.in));
        log = new PrintStream(new OutputStream() { public void write(int b) {} } );
    }

    public static void main(String[] args) throws IOException {

        instance.main();

        instance.systemin.close();
    }


}


