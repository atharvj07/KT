
import java.util.Scanner;

public class Mafia {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n=in.nextInt();
        //int[] a=new int[n];
        long sum=0,max=0;
        for(int i=0;i<n;i++){
            int x=in.nextInt();
            sum+=x;
            max=Math.max(max, x);
        }

        long ans=0;
        if(sum%(n-1)==0){
             ans=sum/(n-1);
        }else{
             ans=sum/(n-1)+1;
        }
        ans=Math.max(max, ans);
        System.out.println(ans);



    }
}
