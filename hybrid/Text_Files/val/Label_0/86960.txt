

import java.util.Arrays;
import java.util.Scanner;

public class WaterMelon {
    static Scanner sc = new Scanner(System.in);
    static int[] mem;
    
    public static void main(String[] args) {
        String[] line = sc.nextLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int k = Integer.parseInt(line[1]);
        int l = Integer.parseInt(line[2]);
        int c = Integer.parseInt(line[3]);
        int d = Integer.parseInt(line[4]);
        int p = Integer.parseInt(line[5]);
        int nl = Integer.parseInt(line[6]);
        int np = Integer.parseInt(line[7]);
        
        int slicesT = c*d;
        int milliT = k*l;
        int count = 0;
        while (slicesT >= n && milliT >= n*nl && p >= n*np) {
            slicesT -= n;
            milliT -= n*nl;
            p -= n*np;
            count++;
        }
        
        System.out.println(count);
    }
    

}
