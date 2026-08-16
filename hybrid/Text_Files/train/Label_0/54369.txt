import java.util.Scanner;


public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=Integer.parseInt(sc.nextLine());
        for(int i=0;i<n;i++){
            String[] str= sc.nextLine().split(" ");
            double[] d = new double[6];
            for(int j=0;j<6;j++){
                d[j]=Double.parseDouble(str[j]);
            }
            double dist = Math.sqrt((d[0]-d[3])*(d[0]-d[3])+(d[1]-d[4])*(d[1]-d[4]));
            double big = d[2]+d[5];
            int ans=0;
            if(dist>big){
                ans=0;
            }else{
            
                if(d[2]>d[5]+dist){
                    ans=2;
                }else if(d[5]>d[2]+dist){
                    ans=-2;
                }else{
                    ans=1;
                }
                 
            }
            System.out.println(ans);
        }
    }
}