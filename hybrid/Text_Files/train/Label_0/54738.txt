import java.util.Arrays;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] A=new int [N][N];
        int ans=0;

        // 全部一旦情報なしに初期化
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                A[i][j] = -1;
            }
        }

        for(int i=0;i<N;i++){
            int ansnum=sc.nextInt();
            for(int j=0;j<ansnum;j++){
                int x=sc.nextInt();
                int y=sc.nextInt();
                A[i][x-1]=y;
            }
        }

        for(int i=0;i<(1<<N);i++){      // i = 1010
            boolean ok=true;
            for(int j=0;j<N;j++){       // j = 2
                if((i&(1<<j))==0){
                    continue;
                }
                // j番目の人は正直者なので, その人の意見を聞きます
                for(int k=0;k<N;k++){
                    if(A[j][k]==-1){
                        continue;
                    }
                    if(A[j][k]!= (((i&(1<<k)) == 0) ? 0 : 1)){
                        ok=false;
                    }
                }
                if(ok==false){
                    break;//このiは間違い！
                }
            }
            if(ok==false){
                continue;
            }
            int karians=0;
            for(int l=0;l<N;l++){
                if((i&(1<<l))!=0){
                    karians++;
                }
            }
            if(ans<karians){
                ans=karians;
            }
        }
        System.out.println(ans);
	}

}
