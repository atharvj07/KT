import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class FoxDividingChees {
    static int n,m,res;
    static void check(int p){
        int u = 0;int v = 0;
        while(n%p==0){u++;n/=p;}
        while(m%p==0){v++;m/=p;}
        res+= Math.abs(u-v);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        res = 0;
        check(3);
        check(5);
        check(2);
        if(n==m) System.out.println(res);
        else System.out.println(-1);


    }
}