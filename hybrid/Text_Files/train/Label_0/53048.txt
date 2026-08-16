import java.util.*;
public class Main {
    static double[][] nums;
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        nums=new double[n][2];
        nums[0][0]=sc.nextDouble();
        nums[0][1]=(10.0-sc.nextDouble())/10.0;
        for(int i=1;i<n;i++){
            nums[i][0]=sc.nextInt();
            nums[i][1]=nums[i-1][1]*(10-sc.nextInt())/10.0;
        }
        int q=sc.nextInt();
        int li;
        int ri;
        for(int i=0;i<q;i++){
            li=sc.nextInt();
            ri=sc.nextInt();
            System.out.println((double)((nibu(ri)==-1?1:nums[nibu(ri)][1])/(nibu(li)==-1?1:nums[nibu(li)][1])*1000000000));
        }
    }
    static int nibu(int q){//にぶたんでnums[i][1]<q<nums[i+1][1]になるiを見つける
        int ans=nums.length/2;
        int toadd=nums.length/2;
        while(true){
            if(nums[ans][0]<q){
                ans+=Math.max(1, toadd/=2);
            }else{
                ans-=Math.max(1, toadd/=2);
            }
            if(ans<0||ans>=nums.length-1||(nums[ans][0]<q&&nums[ans+1][0]>q))break;
        }
        return ans;
    }
    
}
