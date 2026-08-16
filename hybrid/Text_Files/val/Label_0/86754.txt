import java.io.PrintWriter;
import java.util.Scanner;
import java.util.TreeSet;
import java.util.Vector;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        int m = in.nextInt();
        boolean exist = false;

        Vector<TreeSet<Integer>> v = new Vector<TreeSet<Integer>>();

        for (int i = 0; i <= 4; i++) {
            v.add(new TreeSet<Integer>());
        }

        for (int i = 0; i < m; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            v.elementAt(a - 1).add(b - 1);
            v.elementAt(b - 1).add(a - 1);
        }

        for (int i = 0; i <= 4; i++) {
            for (int j = i + 1; j <= 4; j++) {
                for (int k = j + 1; k <= 4; k++) {
                    if (v.elementAt(i).contains(j) && v.elementAt(i).contains(k) && v.elementAt(j).contains(k)) {
                        exist = true;
                        break;
                    }
                }
            }
        }

        for (int i = 0; i <= 4; i++) {
            for (int j = i + 1; j <= 4; j++) {
                for (int k = j + 1; k <= 4; k++) {
                    if (!v.elementAt(i).contains(j) && !v.elementAt(i).contains(k) && !v.elementAt(j).contains(k)) {
                        exist = true;
                        break;
                    }
                }
            }
        }

        out.print(exist ? "WIN" : "FAIL");

        out.close();
    }
}
