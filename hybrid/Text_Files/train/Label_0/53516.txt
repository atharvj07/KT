import java.io.*;
import java.util.*;


/**
 * AIZU ONLINE JUDGE
 * 2522
 *  2020/5/6
 */
public class Main {

    boolean main() throws IOException {

        Scanner sc = new Scanner(systemin);

        String s = sc.nextLine();
        
        boolean valid = false;
        
        if (s.length() < 6) {
            valid = false;
        }
        else {
            boolean num = false;
            boolean small = false;
            boolean big = false;
            for(int i = 0; i < s.length(); i++) {
                int c = s.charAt(i);
                if ('0' <= c && c <= '9') {
                    num = true;
                }
                else if ('a' <= c && c <= 'z') {
                    small = true;
                }
                else if ('A' <= c && c <= 'Z') {
                    big = true;
                }
            }
            if (num && small && big)
                valid = true;
        }
        
        result.printf("%s\n", valid ? "VALID" : "INVALID");

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


