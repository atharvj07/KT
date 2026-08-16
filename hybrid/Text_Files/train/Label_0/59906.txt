

import java.util.Arrays;
import java.util.Scanner;

public class A {
    public static boolean between(int x, int st, int end) {
        return x <= Math.max(st,end) && x >= Math.min(st,end);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        if (x == 0 && y == 0) {
            System.out.println(0);
            return;
        }
        int level = Math.max(Math.abs(x), Math.abs(y));
        int res = (level - 1) * 4;
//      System.out.println(res);
        int[] X = new int[5];
        int[] Y = new int[5];
        X[0] = level;
        Y[0] = -(level - 1);
        X[1] = level;
        Y[1] = level;
        X[2] = -level;
        Y[2] = level;
        X[3] =-level;
        Y[3] = -level;
        X[4] = level;
        Y[4] = -level;
//      System.out.println(Arrays.toString(X));
//      System.out.println(Arrays.toString(Y));
        for (int i = 0; i < 4; i++) {
            if(X[i]==x&&Y[i]==y){
                System.out.println(res+i);
                return;
            }
            if (between(x, X[i], X[i + 1]) && between(y, Y[i], Y[i + 1])) {
                System.out.println(res + i+1);
                return;
            }
        }
    }
}
