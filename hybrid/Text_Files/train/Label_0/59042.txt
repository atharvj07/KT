import java.util.*;
public class Substr {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int x=sc.nextInt();
        if(n%2==0 || x%2==0)
            System.out.println("No");
        else{
            for(int i=1;i<n;i++)
                x=sc.nextInt();
            if(x%2==0)
                System.out.println("No");
            else
                System.out.println("Yes");
                
        }
    }
}