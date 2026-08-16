import java.util.*;
public class cfCheeseboard {

    static int f1(int n){
        if(n==1){
            return 1;
        }
        int x= (n%2==0) ? (n-1) : n;
        return f1(n-1)+x;
    }




    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        int b=0,w=0;
        for(int i=0;i<n;i++){
            String s=sc.next();
            String im=sc.next();
            if(im.charAt(0)=='s'){
                w++;
            }
            if(im.charAt(0)=='h'){
                b++;
            }

        }
        int c= Math.max(w,b);
        int arr[]=new int[100];
        for(int i=1;i<n+1;i++) {
            int xx=f1(i);

            if(c<=xx){
                if(w==b &&( n%2==1 || n==2)){
                    System.out.println(i+1);
                    break;
                }
            System.out.println(i);
            break;
        }}
    }
}
