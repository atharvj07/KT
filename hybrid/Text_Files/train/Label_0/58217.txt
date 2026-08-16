import java.util.*;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
        int[] arr = new int[n];
        int max=0,min=0,start=0,end=0,temp=0,tmp=0;
        
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
            if(arr[i]==1){
                min=i;
            } else if(arr[i]==n){
                max=i;
            }
        }
        
        
        if(min>max){
            start=min;
            end=n-1-max;
        } else {
            start=max;
            end=n-1-min;
        }
        
        if(start>end){
            temp=start;
        } else{
            temp=end;
        }
        System.out.print(temp);
    }
}