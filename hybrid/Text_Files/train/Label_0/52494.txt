

import java.io.*;
import java.util.*;


/**
 * AIZU ONLINE JUDGE
 * 3107
 *  2020/5/1
 */
public class Main {




    boolean main() throws IOException {

        Scanner sc = new Scanner(systemin);

        int N = sc.nextInt();
        int M = sc.nextInt();
        sc.nextLine();

        String[] s = new String[N];

        int cnt = 0;
        for(int i = 0; i < N; i++) {
            s[i] = sc.nextLine();
            log.printf("%s\n", s[i]);
        }
        for(int i = 0; i < N; i++) {
            String t = sc.nextLine();
            log.printf("%s\n", t);
            for(int j = 0; j < M; j++) {
                if (s[i].charAt(j) != t.charAt(j)) {
                    cnt++;
                }
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


