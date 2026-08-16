import java.io.*;
import java.util.*;
public class puzzle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-->0){
            int n = sc.nextInt(),m = sc.nextInt();
            if(n==1)
                System.out.println("yes");
            else if(n==2 && m<=n)
                System.out.println("yes");
            else if(n<=100000 && m==1)
                System.out.println("yes");
            else if(n==1 && m<=100000)
                System.out.println("yes");
            else
                System.out.println("no");
        }
       
    }
}