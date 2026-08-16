import java.util.Scanner;
import java.lang.Math;

public class main{
    public static void main(String []args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        n = Math.abs(n);

        int step=0,sum=0;

        while(sum<n || ((sum-n)%2==1)){
            step++;
            sum+=step;
        }
        if(n==0){
            System.out.println('0');
        }else System.out.println(step);
    }
}
   