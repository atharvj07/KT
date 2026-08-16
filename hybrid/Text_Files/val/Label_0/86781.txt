import java.util.Scanner;

public class prob1177b {
    public static void main(String[] args){

        Scanner sc=new Scanner(System.in);
        long k,c,n,d;
        c=1;
        d=9;
        n=1;
        k= sc.nextLong();
        while(k>(c*d)) {
            k-=(c*d);
            n*=10;
            d*=10;
            c++;
        }
        n+=(k-1)/c;
        char[] num = String.valueOf(n).toCharArray();
        System.out.println(num[(int)((k-1)%c)]);
    }

}