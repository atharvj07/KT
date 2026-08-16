import java.util.*;
public class CF496D {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        int n=s.length();
        int arr[]=new int[n];
        for(int i=0;i<n;i++)
            arr[i]=Integer.parseInt(String.valueOf(s.charAt(i)));
        int i=0,sum=0,ans=0,p=0;
        while(i<n){
            if(arr[i]%3==0){
                sum=0;
                ans++;
                p=i+1;
            }
            else{
                sum+=arr[i];
                if(sum%3==0){
                ans++;
                p=i+1;
                sum=0;
                }
                else{
                    int t=sum;
                    int k=p;
                    while(k<i){
                        t=t-arr[k];
                        if(t%3==0){
                            ans++;
                            sum=0;
                            p=i+1;
                            break;
                            
                        }
                        k++;
                    }
                }
            }
            i++;
        }
        System.out.println(ans);
    }
}