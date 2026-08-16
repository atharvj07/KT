import java.io.*;
import java.lang.reflect.Array;
import java.util.*;
import java.util.logging.StreamHandler;

public class A2 {
    static Scanner in; static int next() throws Exception {return in.nextInt();};
//  static StreamTokenizer in; static int next() throws Exception {in.nextToken(); return (int) in.nval;}
//  static BufferedReader in;
    static PrintWriter out;

    public static void main(String[] args) throws Exception {
        in = new Scanner(System.in);
//      in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
//      in = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);

        int n = next(), m = next(), sumkill = 0;
        String s[] = new String[n];
        int x[] = new int[n];
        for (int i = 0;i < n;i++) s[i] = in.next();
        for (int i = 0;i < n;i++) {
            if (s[i].charAt(0) == '+') x[i] = Integer.parseInt(s[i].substring(1));
            else x[i] = -Integer.parseInt(s[i].substring(1));
        }
        int pos[] = new int[n],
            neg[] = new int[n],
            res[] = new int[n],
            truth[] = new int[n],
            lie[] = new int[n],
            kill[] = new int[n],
            notkill[] = new int[n];

        for (int i = 0;i < n;i++) {
            pos[i] = 0;
            neg[i] = 0;
            res[i] = 0;
            truth[i] = 0;
            lie[i] = 0;
        }
        int sump = 0, sumn = 0;
        for (int i = 0;i < n;i++) {
            if (x[i] > 0) {
                sump++;
                pos[x[i]-1] += 1;
            }
            else {
                sumn++;
                neg[-1-x[i]] += 1;
            }
        }
        for (int i = 0;i < n;i++) {
            res[i] = pos[i]+sumn - neg[i];
            if (res[i] == m) {
                kill[i]++;
                sumkill++;
            } else notkill[i]++;
        }
    //    for (int i = 0;i < n;i++) out.println(kill[i] + " " + notkill[i]);

        for (int i = 0;i < n;i++) {
            if (x[i] > 0) {
                if (kill[x[i]-1] > 0 && notkill[x[i]-1] == 0 && sumkill == kill[x[i]-1]) out.println("Truth");
                else if (kill[x[i]-1] == 0 && notkill[x[i]-1] > 0) out.println("Lie");
                else out.println("Not defined");
            }
            else {
                if (kill[-x[i]-1] > 0 && notkill[-x[i]-1] == 0 && sumkill == kill[-x[i]-1] ) out.println("Lie");
                else if (kill[-x[i]-1] == 0 && notkill[-x[i]-1] > 0) out.println("Truth");
                else out.println("Not defined");
            }
        }

        out.println();
        out.close();
    }
}