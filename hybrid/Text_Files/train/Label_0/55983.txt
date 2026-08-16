import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int m=sc.nextInt();
        int n=sc.nextInt();
        int[] nums=new int[n];
        for(int i=0;i<n;i++)nums[i]=sc.nextInt();
        int count1=0;
        int count2=0;
        int ans=0;
        if(m==2){
            for(int i=0;i<n;i++){
                if(i%2==0&&nums[i]==1||i%2==1&&nums[i]==2)count1++;
                else count2++;
            }
            System.out.println(Math.min(count1,count2));
        }else{
            for(int i=0;i<n-1;i++){
                if(nums[i]==nums[i+1]){
                    nums[i+1]=-1;
                    ans++;
                }
            }
            System.out.println(ans);
        }
    }
    
}
