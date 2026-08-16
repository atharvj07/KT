 import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
         int c=0, t,n=sc.nextInt(),x=sc.nextInt(),y=sc.nextInt();
         String s=sc.next();
         for(t=0;t<y;t++){
             n--;
             if(s.charAt(n)!='0')c++;
         }n--;
         if(s.charAt(n)!='1')c++;
         for(t=y+1;t<x;t++){
             n--;
             if(s.charAt(n)!='0')c++;
         }
         System.out.print(c);
    }
}