import java.util.*;
public class Main {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        System.out.println(GCD(Math.max(x,y),Math.min(x,y)));
    }
    public static int GCD(int a,int b){
        if(b==0) return a;
        else return GCD(b,a%b);
    }
}
