import java.util.*;
import java.io.*;
public class D {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        long a = s.nextLong(),b = s.nextLong(),x1 = s.nextLong(),y1 = s.nextLong(),x2 = s.nextLong(),y2 = s.nextLong();
        long aInt1 = rd(x1+y1,2*a);
        long aInt2 = rd(x2+y2,2*a);
        long aCross = Math.abs(aInt2 - aInt1);
        long bInt1 = rd(x1-y1,2*b);
        long bInt2 = rd(x2-y2,2*b);
        long bCross = Math.abs(bInt2 - bInt1);
        //System.out.printf("%d,%d:%d / %d,%d:%d%n",aInt1,aInt2,aCross,bInt1,bInt2,bCross);
        System.out.println(Math.max(aCross, bCross));
    }
    public static long rd(long a, long b) {
        if (a < 0) return (a/b)-1;
        else return a/b;
    }
}
