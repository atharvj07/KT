import java.math.BigInteger;
import java.util.*;

import static java.lang.Math.abs;
import static java.lang.Math.exp;
import static java.lang.Math.floor;

public class Main {
    static Scanner scanner = new Scanner(System.in);
    static long  sum[]=new long[100000];

    public static void main(String[] args) {
        int n = scanner.nextInt(),o1=0,o0=0;
        scanner.nextLine();
        String temp=scanner.nextLine();
        for (int i=0;i<n;i++){
            if (temp.charAt(i)=='0'){
                o0++;
            }else {
                o1++;
            }
        }
        System.out.println(Math.abs(o0-o1));
    }

}