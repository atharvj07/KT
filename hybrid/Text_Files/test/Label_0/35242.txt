

import java.io.*;
import java.util.*;


/**
 * AIZU ONLINE JUDGE
 * 3127 Gag
 *  2020/5/1
 */
public class Main {


    boolean main() throws IOException {

        Scanner sc = new Scanner(systemin);

        int N = sc.nextInt();

        long sum = 0;
        for(int i = 0; i < N; i++) {
            int v = sc.nextInt();
            sum += v - i - 1;
        }
        System.out.printf("%d\n", sum);

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


