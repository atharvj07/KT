import java.util.*;

public class Main {

    static int MOD = 1000000007;
    public static void main(String[] args) {


        Scanner sc = new Scanner(System.in);
        int d=sc.nextInt(),g=sc.nextInt();
        int[] p = new int[d];
        int[] c = new int[d];
        int ans=Integer.MAX_VALUE;

        for(int i=0;i<d;i++) {
            p[i] = sc.nextInt();
            c[i] = sc.nextInt();
        }

        for(int i=0;i<Math.pow(2,d);i++){
            int temp = i;
            int point=0;
            int problems=0;
            boolean[] bit = new boolean[d];
            for(int j=0;j<d;j++){
                bit[j]=temp%2==1;
                temp = temp>>1;
            }
            for(int j=0;j<d;j++){
                if(bit[j]){
                    point+=c[j]+p[j]*100*(j+1);
                    problems+=p[j];
                }
            }
            if(point<g){
                int k;
                for(int j=d-1;j>=0;j--){
                    if(!bit[j]){
                        int dif=g-point;
                        if(dif%(100*(j+1))==0)k=dif/(100*(j+1));
                        else k=dif/(100*(j+1))+1;
                        problems+=k;
                        point+=k*100*(j+1);
                        if(k>p[j]){
                            problems=Integer.MAX_VALUE;
                        }
                        break;
                    }
                }

            }

            ans = Math.min(ans,problems);

        }
        System.out.println(ans);




    }

}
