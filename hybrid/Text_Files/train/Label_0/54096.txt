import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        while(true){
            int d=s.nextInt();
            int w=s.nextInt();
            if(d==0&&w==0) break;
            int depth[][]=new int[d][w];
            for(int i=0;i<d;i++){
                for(int j=0;j<w;j++){
                    depth[i][j]=s.nextInt();
                }
            }
            int max=0;
            
            for(int starti=1;starti<d-1;starti++){
                for(int startj=1;startj<w-1;startj++){
                    for(int endi=starti;endi<d-1;endi++){
                        for(int endj=startj;endj<w-1;endj++){
                            int ddd=dd(starti,startj,endi,endj,depth);
                            if(ddd>max) max=ddd;
                        }
                    }
                }
            }
            System.out.println(max);
        }
    }
    public static int dd(int starti,int startj,int endi,int endj,int[][] depth){
        int max=0;
        int min=depth[starti-1][startj-1];
        for(int i=starti;i<=endi;i++){
            for(int j=startj;j<=endj;j++){
                if(max<depth[i][j]) max=depth[i][j];
            }
        }
        for(int j=startj-1;j<=endj+1;j++){
            if(min>depth[starti-1][j]) min=depth[starti-1][j];
            if(min>depth[endi+1][j]) min=depth[endi+1][j];
        }
        for(int i=starti;i<=endi;i++){
            if(min>depth[i][startj-1]) min=depth[i][startj-1];
            if(min>depth[i][endj+1]) min=depth[i][endj+1];
        }
        //System.out.println(max+" "+min);
        if(max>=min) return 0;
        else{
            int sum=0;
            for(int i=starti;i<=endi;i++){
                for(int j=startj;j<=endj;j++){
                    sum+=(min-depth[i][j]);
                }
            }
            return sum;
        }
    }
}
