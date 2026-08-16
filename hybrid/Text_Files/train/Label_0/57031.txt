import java.util.Arrays;
import java.util.Scanner;

public class C {

    public static void main(String cd[]){
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        nodE a[]=new nodE[n];
        for(int i=0;i<n;i++){
            a[i]=new nodE(in.nextInt(),i+1);
        }
        Arrays.sort(a);
        System.out.println(n-n/2);
        for(int i=0;i<n;i+=2){
            System.out.print(a[i].pos+" ");
        }
        System.out.println();
        System.out.println(n/2);
        for(int i=1;i<n;i+=2){
            System.out.print(a[i].pos+" ");
        }
        System.out.println();
    }
}
class nodE implements Comparable<nodE>{
    int val;
    int pos;
    nodE(int val,int pos){
        this.val=val;
        this.pos=pos;
        
    }
    @Override
    public int compareTo(nodE o) {
        // TODO Auto-generated method stub
        return this.val-o.val;
    }
    
    
}