

import java.io.*;
import java.util.*;


/**
 * AIZU ONLINE JUDGE
 * 3126
 *  2020/5/1
 */
public class Main {


    boolean main() throws IOException {

        Scanner sc = new Scanner(systemin);

        int N = sc.nextInt();
        sc.nextLine();

        int cnt = 0;
        for(int i = 0; i < N; i++) {
            String s = sc.nextLine();
            if (s.equals("E869120")) {
                cnt++;
            }
        }
        System.out.printf("%d\n", cnt);

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


