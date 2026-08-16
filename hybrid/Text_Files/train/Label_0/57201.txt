import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner cin=new Scanner(System.in);
        int n=cin.nextInt();
        int ans=0;
        while(n!=0){
            if(n%8==1) ans++;
            n/=8;
        }
        System.out.printf("%d",ans);
        return;
    }
}